# 15. Web Fundamentals

> Phase 3 — Web Foundations

This module connects the browser work from the previous two modules to the underlying web architecture. You will study what happens when a user enters a URL, how names are resolved, how connections are established, how HTTP requests and responses are structured, how cookies and caching work, how HTTPS protects transport, and where browser security boundaries fit.

This is a critical bridge to later Networking, Backend/API Development, Cloud Architecture, Application Security, API Security, and Web Penetration Testing.

## 1. Topic Title

**Web Fundamentals**

## 2. Learning Objectives

By the end of this module, you should be able to:

- Explain the client-server architecture of the web.
- Break a URL into scheme, authority/host, port, path, query, and fragment.
- Describe the role of DNS in resolving domain names.
- Explain the high-level relationship among IP, TCP/QUIC, TLS, and HTTP.
- Read and reason about HTTP request and response messages.
- Use common HTTP methods and status-code classes correctly.
- Explain important HTTP headers.
- Explain cookies, sessions, caching, redirects, content negotiation, and compression.
- Explain HTTPS and the role of certificates at a high level.
- Understand origins, CORS, CSP, and secure-cookie concepts at a foundation level.
- Use browser DevTools and command-line tools such as `curl` to inspect web traffic.

## 3. Prerequisites

Complete:

- 13. HTML5 and CSS3.
- 14. Client-Side Technologies.
- Phase 1 Computer Networks Fundamentals is strongly recommended.

You do not need advanced routing, switching, TLS cryptography, or backend-framework knowledge yet. Those will be covered later in the curriculum.

## 4. Core Concepts Explanation


### 4.1 Client-Server Architecture

The web commonly follows a client-server model.

A **client** initiates a request. In normal browsing, the client is a web browser.

A **server** listens for requests and returns responses. The server might be:

- A reverse proxy.
- A web server.
- An application server.
- A serverless function.
- An API gateway.
- A CDN edge node.
- A cloud load balancer forwarding traffic to another component.

Simple conceptual flow:

```text
Browser
   |
   | HTTP request
   v
Web/Application Server
   |
   | Database query / internal service calls
   v
Database / Other Services
   |
   v
Server builds response
   |
   | HTTP response
   v
Browser
```

The browser cannot safely be trusted to enforce business rules. A user controls their own client and can modify or replace browser-generated requests. Authorization and critical validation therefore belong on trusted server-side systems.
### 4.2 What Happens When You Enter a URL

Suppose you enter:

```text
https://portal.example.com/status?region=eu#database
```

A simplified flow is:

1. Browser parses the URL.
2. Browser determines whether it already has useful cached information.
3. The domain name is resolved to an IP address, normally using DNS.
4. The browser establishes transport connectivity to the server.
5. For HTTPS, TLS is negotiated and the server presents a certificate.
6. The browser sends an HTTP request.
7. The server processes the request.
8. The server returns an HTTP response.
9. The browser processes headers and body.
10. If the body is HTML, the browser parses it.
11. Referenced CSS, JavaScript, fonts, and images may trigger additional requests.
12. Browser rendering and JavaScript execution continue.
13. The fragment `#database` is normally handled by the browser and is not included as part of the HTTP request target sent to the server in the same way the path/query are.

Real browsers perform many optimizations and can use HTTP/2 or HTTP/3, cached connections, service workers, preload hints, CDNs, and more, but this sequence is the essential mental model.
### 4.3 URL Anatomy

Example:

```text
https://user@example.com:8443/api/servers?env=prod&limit=20#results
```

Conceptual components:

```text
scheme:   https
host:     example.com
port:     8443
path:     /api/servers
query:    env=prod&limit=20
fragment: results
```

Do not assume query strings are secret. URLs can appear in browser history, logs, analytics, proxies, screenshots, and referrer-related contexts. Sensitive credentials should not be placed casually in URLs.
### 4.4 Domain Names and DNS

Humans prefer names such as:

```text
portal.example.com
```

Networks route using IP addresses. DNS provides a distributed naming system that can map names to records.

Common record types you will encounter:

- `A` — IPv4 address.
- `AAAA` — IPv6 address.
- `CNAME` — canonical-name alias.
- `MX` — mail-exchange destination.
- `TXT` — arbitrary text used for many purposes.
- `NS` — authoritative name servers.

A web request may involve DNS resolvers, caches, authoritative servers, and TTL-based caching.

Example command-line investigation:
```bash
nslookup example.com
```
or on many systems:

```bash
dig example.com
```
Phase 4 will go deeper into networking. For now, understand DNS as the naming layer that normally resolves a host name before a connection is made.
### 4.5 HTTP as an Application-Layer Protocol

HTTP defines semantics for requests and responses. It is an application-layer protocol.

A simplified HTTP/1.1 request might look like:
```http
GET /api/servers?env=prod HTTP/1.1
Host: api.example.com
Accept: application/json
User-Agent: ExampleClient/1.0
```
A simplified response:
```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store

{"servers":[{"name":"web-01","status":"healthy"}]}
```
Conceptually, requests contain:

- Method.
- Request target.
- Protocol-version/framing information depending on HTTP version.
- Headers.
- Optional body.

Responses contain:

- Status.
- Headers.
- Optional body.

HTTP/2 and HTTP/3 use different wire framing than HTTP/1.1, so do not assume the text examples above are the literal on-the-wire representation of all modern HTTP traffic. The method/status/header semantics remain essential.
### 4.6 HTTP Methods

Common methods:

**GET**  
Retrieve a representation/resource.

```http
GET /servers/123
```

**POST**  
Submit data for processing or create a subordinate resource depending on API design.

```http
POST /maintenance-requests
```

**PUT**  
Often used to replace or create a resource at a known URI.

```http
PUT /servers/123/config
```

**PATCH**  
Apply a partial modification.

```http
PATCH /servers/123
```

**DELETE**  
Request deletion.

```http
DELETE /servers/123
```

**HEAD**  
Similar to GET semantics but response omits the representation body.

**OPTIONS**  
Requests communication options; browsers also use OPTIONS in some CORS preflight flows.

Method names have semantics. A GET should not be designed to perform destructive state changes just because a browser can send it easily.
### 4.7 Safe and Idempotent Methods

Two useful HTTP concepts:

**Safe method**  
Intended to be read-only from the client's requested semantics. GET and HEAD are examples.

**Idempotent method**  
Repeating the same request should have the same intended effect as making it once. PUT and DELETE are defined as idempotent in their semantics, although implementation details and logging/side effects still require care.

POST is not generally assumed idempotent.

These properties matter for retries, caching, API design, proxies, and distributed systems.
### 4.8 HTTP Status Codes

Status codes are grouped:

- `1xx` — informational.
- `2xx` — successful.
- `3xx` — redirection.
- `4xx` — client-side/request-related errors.
- `5xx` — server-side errors.

Important examples:

**200 OK**  
Request succeeded.

**201 Created**  
A resource was created.

**204 No Content**  
Request succeeded and no response body is needed.

**301 Moved Permanently** / **308 Permanent Redirect**  
Permanent redirection semantics, with important method-preservation distinctions depending on code.

**302 Found** / **307 Temporary Redirect**  
Temporary redirection semantics, again with method-handling differences.

**304 Not Modified**  
Used in conditional cache validation.

**400 Bad Request**  
Malformed or invalid request.

**401 Unauthorized**  
Despite the name, usually means authentication is required or credentials are invalid/missing.

**403 Forbidden**  
Server understood the request but refuses access.

**404 Not Found**  
Target resource was not found or is intentionally not disclosed.

**409 Conflict**  
Request conflicts with current resource state.

**422 Unprocessable Content**  
Often used when syntax is valid but semantic validation fails.

**429 Too Many Requests**  
Rate limit or request-throttling condition.

**500 Internal Server Error**  
Generic unexpected server failure.

**502 Bad Gateway**  
A gateway/proxy received an invalid response from an upstream.

**503 Service Unavailable**  
Service currently unable to handle the request.

**504 Gateway Timeout**  
Gateway/proxy timed out waiting for an upstream.
### 4.9 Important Request Headers

```http
Host: api.example.com
Accept: application/json
Authorization: Bearer <token>
Content-Type: application/json
User-Agent: ExampleClient/1.0
If-None-Match: "abc123"
Origin: https://portal.example.com
```
Important distinctions:

**`Accept`** describes response media types the client can accept.

**`Content-Type`** describes the media type of the body being sent.

**`Authorization`** carries credentials according to an authentication scheme.

**`Origin`** identifies the request origin in relevant browser contexts and is important to CORS behavior.

Headers are part of the protocol; they are not automatically trusted just because a browser usually creates them.
### 4.10 Important Response Headers

```http
Content-Type: application/json; charset=utf-8
Content-Length: 248
Cache-Control: no-store
ETag: "abc123"
Location: /resources/123
Set-Cookie: session=...; Secure; HttpOnly; SameSite=Lax
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=31536000
```
Headers can control:

- Content interpretation.
- Caching.
- Redirect locations.
- Cookies.
- Browser security policies.
- CORS behavior.
- Transport expectations.
### 4.11 Content Types / MIME Types

Examples:

```text
text/html
text/css
application/javascript
application/json
image/png
image/svg+xml
application/pdf
```

The `Content-Type` header tells the recipient how to interpret the body.

For a JSON API:
```http
Content-Type: application/json
```
Sending the wrong content type can break clients or produce security-relevant ambiguity in poorly configured systems.
### 4.12 Request Bodies and HTML Forms

Traditional form submission often uses:

```text
application/x-www-form-urlencoded
```

File uploads commonly use:

```text
multipart/form-data
```

JSON APIs commonly use:

```text
application/json
```

Example JSON body:
```json
{
  "hostname": "web-01",
  "environment": "production"
}
```
The server must validate the body regardless of what the browser form allowed.
### 4.13 Cookies and Sessions

HTTP itself does not automatically maintain application login state between unrelated requests. Cookies are one mechanism that allows state identifiers to be carried across requests.

A common session model:

1. User authenticates.
2. Server creates a server-side session record.
3. Server generates an unpredictable session identifier.
4. Server sends that identifier in a cookie.
5. Browser sends the cookie on eligible later requests.
6. Server maps the identifier back to session state.

Conceptual response:
```http
Set-Cookie: session_id=random-value; Secure; HttpOnly; SameSite=Lax
```
Later request:

```http
Cookie: session_id=random-value
```
The cookie should not contain sensitive raw credentials simply because cookies can carry data. Session architecture must consider confidentiality, integrity, expiration, rotation, revocation, CSRF-related behavior, and XSS exposure.
### 4.14 Cookie Attributes

**Secure**  
Cookie is sent only over secure transport contexts.

**HttpOnly**  
JavaScript cannot read the cookie through normal document-cookie APIs.

**SameSite**  
Controls some cross-site cookie sending. Values include `Strict`, `Lax`, and `None` with associated browser rules.

**Path**  
Limits eligible request paths.

**Domain**  
Controls host/domain scoping.

**Expires / Max-Age**  
Controls persistence.

These attributes reduce risk but do not replace correct session design.
### 4.15 Authentication vs Authorization

**Authentication** asks:

> Who are you?

**Authorization** asks:

> What are you allowed to do?

A request can be authenticated but unauthorized.

Example:

```text
User Ahmed is successfully authenticated.
Ahmed requests DELETE /admin/users/42.
The server checks Ahmed's permissions.
If Ahmed lacks admin permission, the server denies the action.
```

The frontend may hide an admin button, but that is not authorization. A user can manually send the request. The server must enforce access control independently.
### 4.16 Redirects

A server can tell a client to request another URL:
```http
HTTP/1.1 302 Found
Location: /login
```
Browsers commonly follow redirects automatically.

Redirects are used for:

- HTTP-to-HTTPS migration.
- Login flows.
- Canonical URLs.
- Moved resources.
- Application routing.

Security note: applications should avoid open-redirect behavior where untrusted input can cause redirection to arbitrary external destinations without adequate validation.
### 4.17 Caching

Caching reduces latency and server load by reusing previous responses.

`Cache-Control` is a key response header.

Examples:
```http
Cache-Control: public, max-age=3600
```
```http
Cache-Control: no-store
```
`no-store` tells caches not to store the response.

Validation can use entity tags:
```http
ETag: "version-123"
```
Later request:

```http
If-None-Match: "version-123"
```
If unchanged:

```http
HTTP/1.1 304 Not Modified
```
Caching sensitive data incorrectly can expose information on shared devices or intermediary systems. Cache policy must reflect data sensitivity and application requirements.
### 4.18 Content Negotiation

Clients can express preferred representations.

Example:
```http
Accept: application/json
Accept-Language: en
Accept-Encoding: gzip, br
```
Servers can use these preferences to choose a representation, language, or compression encoding.

The exact negotiation behavior depends on server/application configuration.
### 4.19 Compression

HTTP responses can be compressed to reduce transferred bytes.

Client:
```http
Accept-Encoding: gzip, br
```
Server may respond:

```http
Content-Encoding: br
```
Compression improves performance, but infrastructure should avoid blindly compressing every content type; some formats are already compressed, and security/performance implications can vary.
### 4.20 HTTP/1.1, HTTP/2, and HTTP/3 — Foundation View

You do not need protocol-engineering depth yet.

**HTTP/1.1**
- Text-oriented message syntax.
- Persistent connections are supported.
- Multiple concurrent resource loads often require connection-management strategies.

**HTTP/2**
- Binary framing.
- Multiplexes multiple streams over a connection.
- Header compression.
- Retains HTTP method/status/header semantics.

**HTTP/3**
- Uses QUIC rather than TCP as its transport foundation.
- Designed to improve behavior under loss and connection changes.
- Retains HTTP semantics with different transport/framing characteristics.

Do not say "HTTP/2 makes websites secure." Security comes from the HTTPS/TLS deployment and application security design, not from version number alone.
### 4.21 TCP, QUIC, and Ports — High-Level Context

Traditional HTTPS commonly uses TCP underneath TLS and HTTP/1.1 or HTTP/2.

HTTP/3 uses QUIC, which runs over UDP.

Default conventional ports:

- HTTP: TCP port 80.
- HTTPS: TCP port 443.
- HTTP/3 commonly uses UDP port 443.

A port identifies an endpoint at the transport layer. A URL can specify a non-default port explicitly:
```text
https://example.com:8443/
```
Phase 4 Networking will explain ports, TCP, UDP, addressing, routing, switching, and packet flow in much more depth.
### 4.22 HTTPS and TLS

HTTPS is HTTP protected by TLS.

TLS aims to provide:

- Confidentiality — observers should not be able to read protected application data in transit.
- Integrity — modification should be detectable.
- Authentication of the server identity through certificates and trust validation in normal public-web use.

Simplified sequence:

```text
Browser                     Server
   |                           |
   |---- connection ---------->|
   |                           |
   |<--- TLS handshake ------->|
   |   certificate checked     |
   |   keys established        |
   |                           |
   |==== encrypted HTTP ======>|
   |<=== encrypted HTTP =======|
```

HTTPS does **not** mean the website itself is trustworthy or free of vulnerabilities. It protects the transport connection according to TLS/security assumptions.
### 4.23 Certificates — Foundation View

A server certificate binds a public key to names and other certificate information, signed through a certificate chain.

Browsers validate properties such as:

- Whether the certificate is currently valid.
- Whether the requested hostname is covered.
- Whether the chain leads to a trusted root under browser/OS trust rules.
- Whether signatures and policy constraints validate.

You will study PKI and security concepts in greater depth later.
### 4.24 Reverse Proxies and Load Balancers

A browser may not connect directly to the application process.

Common architecture:
```text
Internet
   |
   v
CDN / WAF
   |
   v
Load Balancer / Reverse Proxy
   |
   +----> App Server 1
   |
   +----> App Server 2
   |
   +----> App Server 3
```
A reverse proxy receives client requests and forwards them to upstream services.

A load balancer distributes traffic across multiple healthy backends.

These components can terminate TLS, add headers, enforce routing, cache responses, apply WAF rules, and perform health checks depending on configuration.
### 4.25 Forward Proxy vs Reverse Proxy

**Forward proxy**

Represents or intermediates the client side.

```text
Client -> Forward Proxy -> Internet Servers
```

**Reverse proxy**

Represents or fronts server-side applications.

```text
Clients -> Reverse Proxy -> Backend Servers
```

The direction of representation is the key distinction.
### 4.26 CDN — Content Delivery Network

A CDN places edge infrastructure near users and can cache or proxy content.

Potential benefits:

- Lower latency.
- Reduced origin load.
- DDoS absorption capabilities depending on provider/service.
- TLS termination.
- Static asset delivery.
- Edge routing.

A CDN does not automatically make an application secure. Origin security, access control, cache policy, and configuration still matter.
### 4.27 Same-Origin Policy and CORS in the Web Architecture

Recall the browser origin concept:

```text
scheme + host + port
```

Example:

```text
https://portal.example.com
```

and:

```text
https://api.example.com
```

are different origins because the hosts differ.

The same-origin policy restricts scripts from one origin from freely reading another origin's protected data.

CORS allows the server to explicitly permit certain cross-origin access through HTTP response headers.

Example:
```http
Access-Control-Allow-Origin: https://portal.example.com
```
Do not "fix CORS" by automatically allowing all origins without understanding whether credentials, private data, or write operations are involved.
### 4.28 Preflight Requests

For some cross-origin requests, the browser first sends an `OPTIONS` request to determine whether the server permits the requested method/headers.

Simplified:
```http
OPTIONS /api/servers HTTP/1.1
Origin: https://portal.example.com
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type
```
Possible response:

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://portal.example.com
Access-Control-Allow-Methods: GET, PATCH
Access-Control-Allow-Headers: Content-Type
```
If policy permits, the browser can proceed with the actual request.

A preflight is a browser security mechanism, not a replacement for server authentication/authorization.
### 4.29 Content Security Policy — Foundation

Content Security Policy (CSP) is a browser-enforced defense that can restrict which content sources a page may load or execute.

Example:
```http
Content-Security-Policy: default-src 'self'; img-src 'self' https:; object-src 'none'
```
CSP can reduce the impact of some injection vulnerabilities and restrict unexpected content loading. It is defense in depth, not a substitute for output encoding, safe DOM APIs, and secure application design.
### 4.30 Basic Web Security Model

At this stage, understand the categories without performing offensive exploitation:

**Input validation**  
Server validates data type, format, length, range, and business rules.

**Output handling / encoding**  
Data is placed into HTML/JavaScript/URL contexts safely.

**Authentication**  
Establishes identity.

**Authorization**  
Enforces permitted actions.

**Session management**  
Protects authenticated state.

**Transport security**  
HTTPS protects data in transit.

**Browser isolation**  
Same-origin policy and related mechanisms reduce cross-site access.

**Security headers**  
Headers such as CSP and HSTS influence browser security behavior.

**Logging and monitoring**  
Security-relevant events should be observable.

Later phases will cover vulnerabilities such as XSS, injection, access-control failures, SSRF, CSRF-related risks, and other web attack classes in controlled and ethical contexts.
### 4.31 Using `curl` to Inspect HTTP

```bash
curl -i https://example.com/
```
`-i` includes response headers.

Headers only:
```bash
curl -I https://example.com/
```
Verbose connection information:

```bash
curl -v https://example.com/
```
Send an Accept header:

```bash
curl -H "Accept: application/json" https://example.com/api/status
```
POST JSON to your own local/test endpoint:

```bash
curl   -X POST   -H "Content-Type: application/json"   -d '{"hostname":"web-01"}'   http://localhost:8000/api/servers
```
Use these commands only against systems you own, administer, or are explicitly authorized to test.
### 4.32 Browser Network Panel

Open Developer Tools → Network and reload a page.

For each request identify:

- URL.
- Method.
- Status.
- Request headers.
- Response headers.
- Request payload.
- Response body.
- Content type.
- Timing.
- Cache behavior.
- Initiator.

This single exercise connects HTML, JavaScript, HTTP, DNS/connection behavior, caching, CORS, and server responses.


# Enhanced Deep-Dive — Web Architecture, DNS, HTTP, TLS, Caching, Proxies, Browser Security, and Request Troubleshooting

The original module already establishes the correct bridge from HTML/CSS/JavaScript into DNS, HTTP, TLS, caching, cookies, reverse proxies, CDNs, CORS, CSP, `curl`, and browser Developer Tools. This enhanced version preserves all original material and expands it into a self-contained web-protocol foundation for later networking, backend/API engineering, cloud architecture, DevOps, application security, API security, and web penetration testing.

The main end-to-end mental model is:

```text
User enters URL
      ↓
Browser parses URL
      ↓
Cache / service worker checks
      ↓
DNS resolution
      ↓
IP destination selected
      ↓
Transport connection
├─ TCP for HTTP/1.1 or HTTP/2
└─ QUIC/UDP for HTTP/3
      ↓
TLS handshake for HTTPS
      ↓
HTTP request
      ↓
Edge / CDN / WAF / Load Balancer / Reverse Proxy
      ↓
Application
      ↓
Cache / Database / Internal Services
      ↓
HTTP response
      ↓
Browser security checks
      ↓
Cache processing
      ↓
HTML/CSS/JS processing
      ↓
DOM / rendering / JavaScript
```

A debugging model used throughout this course is:

```text
URL correct?
    ↓
DNS works?
    ↓
Transport reachable?
    ↓
TLS succeeds?
    ↓
HTTP request correct?
    ↓
Proxy/upstream reachable?
    ↓
Application response correct?
    ↓
Browser policy allows access?
    ↓
Client parses response correctly?
```

A security model is:

```text
Browser is user-controlled
        ↓
Never trust request fields merely because
"a browser normally sends them"
        ↓
Server authenticates
        ↓
Server authorizes
        ↓
Server validates
        ↓
Server returns safe content/policies
```


### Deep Dive — Web Architecture as Layered Systems

A web request crosses multiple layers. HTTP is only one layer.

At a high level:
- URL identifies the target and request context.
- DNS translates names to records such as IP addresses.
- IP provides addressing/routing.
- TCP or QUIC provides transport.
- TLS protects HTTPS transport.
- HTTP defines application request/response semantics.
- The application implements business behavior.

#### Diagram / Mental Model

```text
Application meaning
     HTTP
      ↓
     TLS
      ↓
 TCP / QUIC
      ↓
      IP
      ↓
 Link / local network
```

#### Why It Matters

When a web request fails, knowing the layer tells you which tool and hypothesis to use.



### Deep Dive — URL Syntax Beyond the Basic Parts

A URL is a structured identifier, not just a string.

Important components include:
- scheme
- authority
- optional user-information syntax
- host
- optional port
- path
- query
- fragment

The fragment is normally interpreted by the client and is not sent to the HTTP server as part of the request target.

#### Diagram / Mental Model

```text
https://user@example.com:8443/api/servers?env=prod#results
|---|  |---------------------| |----------| |------| |-----|
scheme        authority           path       query   fragment

authority:
user@example.com:8443
     host = example.com
     port = 8443
```

#### Why It Matters

URL parsing is relevant to routing, CORS origins, redirects, proxies, logging, and security validation.



### Deep Dive — Percent-Encoding / URL Encoding

URLs cannot represent every character literally in every component. Percent-encoding represents a byte as `%HH`.

For example, a space in a query parameter is commonly encoded rather than inserted literally.

Do not manually concatenate raw user text into a URL. Use URL-building APIs.

#### Diagram / Mental Model

```text
user text:
web server

query value:
web%20server
```

#### CLI Example

```bash
python - <<'PY'
from urllib.parse import urlencode
print(urlencode({"query": "web server", "env": "prod"}))
PY
```

#### Expected Behavior / Output

```text
query=web+server&env=prod
```

#### Why It Matters

Correct encoding prevents malformed URLs and ambiguous parameter boundaries.



### Deep Dive — Path vs Query vs Fragment

Use the URL components according to their semantics.

- Path generally identifies hierarchical resource location.
- Query modifies or parameterizes the request.
- Fragment identifies a client-side section/state within the representation.

#### Diagram / Mental Model

```text
/servers/123?view=full#metrics
|----------| |-------| |-----|
   path       query    fragment
```

#### Why It Matters

This helps API design and prevents placing sensitive data in inappropriate URL components.



### Deep Dive — Origin vs Site vs Host

These terms are related but not identical.

For browser-origin rules, an origin is broadly:
- scheme
- host
- port

`https://app.example.com` and `https://api.example.com` are different origins even though they share a parent domain.

#### Diagram / Mental Model

```text
https://app.example.com:443
scheme = https
host   = app.example.com
port   = 443

origin = combination of all three
```

#### Why It Matters

Origin reasoning is essential for CORS, same-origin policy, storage, and browser isolation.



### Deep Dive — DNS Resolution Path

DNS resolution can involve several components:
- browser cache
- operating-system resolver cache
- configured recursive resolver
- root servers
- TLD servers
- authoritative name servers

In practice, caching often means not every lookup reaches every layer.

#### Diagram / Mental Model

```text
Browser
  ↓ cache miss
OS resolver
  ↓
Recursive DNS resolver
  ↓
Root
  ↓
TLD (.com)
  ↓
Authoritative server
  ↓
A / AAAA / other record
```

#### Why It Matters

DNS failures can occur before any HTTP request exists.



### Deep Dive — Recursive vs Authoritative DNS Roles

A recursive resolver performs lookup work on behalf of a client. An authoritative server provides answers for zones it is responsible for.

These roles are different.

#### Diagram / Mental Model

```text
Client
  ↓ asks
Recursive Resolver
  ↓ asks hierarchy
Authoritative DNS
  ↓ answer
Recursive Resolver
  ↓ cached answer
Client
```

#### Why It Matters

Understanding resolver roles helps interpret DNS troubleshooting output.



### Deep Dive — DNS Record Types for Web Systems

Important records include:
- A → IPv4 address
- AAAA → IPv6 address
- CNAME → alias to another DNS name
- NS → authoritative name server
- TXT → text metadata
- MX → mail routing
- SOA → zone metadata
- CAA → certificate-authority authorization policy

#### CLI Example

```bash
dig example.com A
dig example.com AAAA
dig example.com NS
dig example.com TXT
```

#### Why It Matters

Web infrastructure often uses several record types together.



### Deep Dive — TTL and DNS Caching

DNS records are cached for a time determined by TTL and resolver behavior.

Changing a DNS record does not mean every client immediately observes the new answer.

#### Diagram / Mental Model

```text
Authoritative record changes
        ↓
old cached answers still valid
        ↓
TTL expires
        ↓
resolver refreshes
```

#### Why It Matters

This explains migration/rollout delay and why different clients can temporarily see different destinations.



### Deep Dive — Negative DNS Caching Awareness

DNS resolvers may cache negative answers such as 'name does not exist' for a period.

Creating a previously missing name may therefore not become visible to every resolver instantly.

#### Why It Matters

Not all DNS-cache problems involve old positive addresses.



### Deep Dive — DNS CNAME Chaining Awareness

A hostname can resolve through one or more aliases before reaching address records.

Example:
`www.example.test` → CNAME → `edge.vendor.test` → A/AAAA.

#### Diagram / Mental Model

```text
www.example.test
      ↓ CNAME
edge.vendor.test
      ↓
A / AAAA
```

#### Why It Matters

CDNs and cloud services commonly use aliases.



### Deep Dive — Host Header and Virtual Hosting

One IP address can host multiple websites. HTTP identifies the intended host using the Host header in HTTP/1.1 semantics and equivalent authority information in newer versions.

The server/reverse proxy can route requests based on host.

#### Diagram / Mental Model

```text
203.0.113.10
├─ portal.example.com
├─ api.example.com
└─ docs.example.com
```

#### HTTP Example

```http
GET / HTTP/1.1
Host: portal.example.com
```

#### Why It Matters

DNS resolving several names to one IP does not mean they are the same website or origin.



### Deep Dive — TCP Connection Foundation for HTTP/1.1 and HTTP/2

Traditional HTTP/1.1 and HTTP/2 commonly use TCP.

TCP provides an ordered reliable byte stream. Before application data flows, endpoints establish a connection.

#### Diagram / Mental Model

```text
Client                     Server
  | ---- SYN -------------> |
  | <--- SYN/ACK ---------- |
  | ---- ACK -------------> |
  |                         |
  | ==== byte stream =====> |
```

#### Why It Matters

Connection failures, resets, retransmission, and latency can affect HTTP even when application code is correct.



### Deep Dive — TCP Connection Reuse

Opening a new transport connection for every resource is expensive. Modern HTTP clients reuse connections where protocol rules permit.

Connection reuse reduces repeated handshake latency.

#### Diagram / Mental Model

```text
Without reuse:
request 1 → new TCP/TLS
request 2 → new TCP/TLS
request 3 → new TCP/TLS

With reuse:
one connection
├─ request 1
├─ request 2
└─ request 3
```

#### Why It Matters

Connection behavior affects latency and load.



### Deep Dive — QUIC and HTTP/3 Foundation

HTTP/3 uses QUIC over UDP rather than TCP.

QUIC includes transport-security integration and stream multiplexing behavior designed to improve several limitations of TCP-based HTTP stacks.

#### Diagram / Mental Model

```text
HTTP/1.1 or HTTP/2
HTTP
 ↓
TLS
 ↓
TCP
 ↓
IP

HTTP/3
HTTP/3
 ↓
QUIC
 ↓
UDP
 ↓
IP
```

#### Why It Matters

HTTP semantics remain recognizable even though the transport/framing changes.



### Deep Dive — TLS Handshake Mental Model

For HTTPS, TLS establishes protected transport before application HTTP data is exchanged.

At a high level:
- negotiate protocol parameters
- server presents certificate information
- client validates identity/trust
- key agreement establishes session keys
- encrypted application traffic begins

#### Diagram / Mental Model

```text
Client                      Server
  | --- ClientHello -------> |
  | <--- ServerHello ------- |
  | <--- Certificate ------- |
  | ... key agreement ...    |
  | === encrypted HTTP ====> |
```

#### Why It Matters

A TLS failure happens before the application can return a normal HTTP response.



### Deep Dive — SNI Awareness

During modern TLS connection setup, the client can indicate the hostname it wants using Server Name Indication (SNI).

This allows multiple HTTPS sites to share an IP address while presenting the correct certificate.

#### Diagram / Mental Model

```text
Client → IP 203.0.113.10
        SNI=portal.example.com
              ↓
Server chooses portal certificate
```

#### Why It Matters

Virtual hosting exists at both TLS and HTTP routing layers.



### Deep Dive — ALPN Awareness

Application-Layer Protocol Negotiation allows TLS peers to agree on the application protocol, such as HTTP/1.1 or HTTP/2, during connection setup.

#### Diagram / Mental Model

```text
TLS handshake
   ↓
ALPN proposals
"h2", "http/1.1"
   ↓
selected protocol
```

#### Why It Matters

A single HTTPS endpoint can support multiple HTTP versions.



### Deep Dive — Certificate Name Validation

A browser checks that the certificate covers the hostname being requested.

A valid certificate for one hostname is not automatically valid for another.

#### Diagram / Mental Model

```text
Requested:
https://api.example.com

Certificate names must cover:
api.example.com
(or appropriate wildcard rules)
```

#### Why It Matters

Hostname mismatch is a TLS identity problem, not an HTTP 404.



### Deep Dive — Certificate Chain of Trust

Server certificates are commonly validated through a chain leading to a root trusted by the client platform/browser.

Conceptually:
leaf/server certificate → intermediate CA → root CA.

#### Diagram / Mental Model

```text
api.example.com certificate
        ↓ signed by
Intermediate CA
        ↓ signed by
Trusted Root CA
```

#### Why It Matters

Trust depends on successful validation of the chain and policy, not simply 'certificate exists'.



### Deep Dive — TLS Does Not Validate Application Safety

HTTPS protects transport confidentiality/integrity and server identity under the TLS trust model.

It does not guarantee:
- server code has no vulnerabilities
- page content is truthful
- authorization is correct
- downloaded files are safe

#### Why It Matters

The padlock is not an application-security certification.



### Deep Dive — HTTP Message Semantics vs Wire Framing

HTTP/1.1 text examples are ideal for learning request/response semantics. HTTP/2 and HTTP/3 use binary framing.

Methods, status codes, header fields, and representation semantics remain core concepts across versions.

#### Diagram / Mental Model

```text
HTTP semantics:
GET /status
status = 200
content-type = application/json

Wire framing:
HTTP/1.1 → textual message framing
HTTP/2   → binary frames/streams
HTTP/3   → QUIC-based streams
```

#### Why It Matters

Do not assume a packet capture of HTTP/2 looks like an HTTP/1.1 text block.



### Deep Dive — Request Target Forms Awareness

Most browser requests use an origin-form request target such as `/path?query`.

Proxies and special methods can use other request-target forms. You do not need proxy-protocol depth yet, but avoid assuming every HTTP request line is always identical.

#### HTTP Example

```http
GET /api/status?env=prod HTTP/1.1
Host: api.example.com
```

#### Why It Matters

HTTP syntax and semantics have more detail than the basic examples show.



### Deep Dive — Method Semantics: GET

GET requests retrieve a current representation of a resource according to server semantics.

GET is defined as safe: the client is not asking for a state-changing operation.

#### HTTP Example

```http
GET /api/servers/123 HTTP/1.1
Host: api.example.com
Accept: application/json
```

#### Why It Matters

Caching, prefetching, crawlers, and retries assume method semantics.



### Deep Dive — Method Semantics: POST

POST submits a representation to a resource for processing. The server decides what the submission means.

POST is not generally assumed idempotent.

#### HTTP Example

```http
POST /maintenance-requests HTTP/1.1
Host: portal.example.com
Content-Type: application/json

{"asset":"web-01","reason":"patching"}
```

#### Why It Matters

Retries of non-idempotent operations require deliberate duplicate-prevention design.



### Deep Dive — Method Semantics: PUT vs PATCH

PUT generally represents creating/replacing the state of a target resource. PATCH applies a partial modification according to the patch document semantics.

Do not use the method name as decoration; define what repeated requests mean.

#### Diagram / Mental Model

```text
PUT /servers/123
→ replacement representation

PATCH /servers/123
→ partial modification instructions
```

#### Why It Matters

Idempotency, validation, and API client behavior depend on clear semantics.



### Deep Dive — DELETE Semantics and Idempotency

DELETE requests removal of the association/resource according to server semantics.

Repeating DELETE is still idempotent in intended effect even if the second response differs because the resource is already absent.

#### Why It Matters

Idempotency is about intended server state, not identical response bytes.



### Deep Dive — HEAD

HEAD has semantics similar to GET but the server does not send the representation body.

It is useful for metadata checks where supported correctly.

#### HTTP Example

```http
HEAD /large-report.pdf HTTP/1.1
Host: files.example.com
```

#### Why It Matters

Clients can inspect metadata such as content type/length without downloading the full representation.



### Deep Dive — OPTIONS

OPTIONS asks about communication options for a resource/server. Browsers also use OPTIONS automatically in some CORS preflight flows.

#### HTTP Example

```http
OPTIONS /api/servers HTTP/1.1
Origin: https://portal.example.com
Access-Control-Request-Method: PATCH
```

#### Why It Matters

A preflight request is browser protocol behavior, not necessarily a request your frontend code explicitly issued.



### Deep Dive — Safe vs Idempotent vs Cacheable

These terms are different.

- Safe → client asks only for retrieval/read-like semantics.
- Idempotent → repeating the request has the same intended effect.
- Cacheable → response may be reused according to HTTP caching rules.

A method can be idempotent without being safe.

#### Diagram / Mental Model

```text
GET
safe + idempotent
often cacheable

PUT
idempotent
not safe

POST
not generally idempotent
can be cacheable only under specific semantics/policies
```

#### Why It Matters

Distributed systems, proxies, retries, and caches use these distinctions.



### Deep Dive — Status Code Design: 200 vs 201 vs 204

Use response codes to communicate the actual result.

- 200: successful response with representation/result.
- 201: resource created; often paired with Location.
- 204: success with no response body.

#### HTTP Example

```http
HTTP/1.1 201 Created
Location: /maintenance-requests/482
Content-Type: application/json

{"id":482,"status":"scheduled"}
```

#### Why It Matters

Clients should not infer meaning only from body text.



### Deep Dive — 401 vs 403

401 commonly means valid authentication is absent or insufficient for identifying the request. 403 means the server understood the identity/request but refuses authorization.

The word 'Unauthorized' in the 401 reason phrase is historically confusing.

#### Diagram / Mental Model

```text
No/invalid authentication
→ 401

Authenticated but not allowed
→ 403
```

#### Why It Matters

Accurate status semantics improve API behavior and security logging.



### Deep Dive — 404 as Non-Disclosure

A server may return 404 even when a resource conceptually exists if revealing existence would leak information.

Therefore, 404 means the target is not available as a found resource to this request; it does not always prove the backend has no corresponding record.

#### Why It Matters

Security-sensitive applications sometimes avoid user-enumeration leakage.



### Deep Dive — 409 Conflict

409 communicates that the request conflicts with the current state of the target.

Examples:
- version conflict
- duplicate unique identifier
- invalid state transition

#### HTTP Example

```http
HTTP/1.1 409 Conflict
Content-Type: application/json

{"error":"deployment already in progress"}
```

#### Why It Matters

It distinguishes resource-state conflict from malformed syntax.



### Deep Dive — 422 Unprocessable Content

422 is often used when the request body syntax/media parsing succeeded but semantic validation failed.

Example: a valid JSON object with an invalid business value.

#### HTTP Example

```http
HTTP/1.1 422 Unprocessable Content
Content-Type: application/json

{"field":"replicas","error":"must be between 1 and 20"}
```

#### Why It Matters

Validation errors should be machine-readable enough for clients to respond usefully.



### Deep Dive — 429 Too Many Requests

429 indicates request rate limiting/throttling. A response may include Retry-After or other application-specific rate-limit metadata.

#### HTTP Example

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
```

#### Why It Matters

Clients should back off instead of immediately generating more load.



### Deep Dive — 502, 503, and 504

These codes frequently appear in proxied/cloud environments.

- 502: gateway/proxy got an invalid/unusable upstream response.
- 503: service unavailable.
- 504: gateway timed out waiting for upstream.

#### Diagram / Mental Model

```text
Client
 ↓
Reverse Proxy
 ↓
App

App malformed/connection issue → 502
Service intentionally unavailable → 503
Proxy waits too long → 504
```

#### Why It Matters

These often indicate different failure locations than a direct application 500.



### Deep Dive — Headers Are Metadata, Not Automatically Trusted

HTTP headers can be generated by browsers, proxies, clients, gateways, or attackers using custom clients.

A backend must not trust identity/authorization-related headers unless they come through an authenticated trusted infrastructure path with correct sanitization.

#### Why It Matters

Headers are protocol input, not proof of legitimacy.



### Deep Dive — Content-Type and Media Types

Content-Type tells the recipient how to interpret the message body.

Examples:
- text/html
- text/css
- application/json
- image/png
- application/pdf

For textual formats, charset parameters can matter.

#### HTTP Example

```http
Content-Type: application/json; charset=utf-8
```

#### Why It Matters

Incorrect media types can break parsers and security expectations.



### Deep Dive — Accept and Representation Negotiation

Accept describes response media types the client is willing to receive.

A server may support multiple representations of the same resource.

#### HTTP Example

```http
GET /report/42 HTTP/1.1
Host: reports.example.com
Accept: application/json
```

#### Why It Matters

Content negotiation separates resource identity from one fixed representation format.



### Deep Dive — Accept-Language and Localization

Clients can express language preferences using Accept-Language. Servers may choose a localized representation.

Caches may need to distinguish responses that vary by language.

#### HTTP Example

```http
Accept-Language: en-US,en;q=0.9,ar;q=0.8
```

#### Why It Matters

Content negotiation interacts with caching through the Vary response header.



### Deep Dive — Content-Encoding and Compression

Content-Encoding describes transformation of the representation payload, commonly compression.

The client advertises supported encodings through Accept-Encoding.

#### HTTP Example

```http
Accept-Encoding: gzip, br

HTTP/1.1 200 OK
Content-Encoding: br
```

#### Why It Matters

Compression reduces transfer size but must be chosen appropriately.



### Deep Dive — Transfer-Encoding vs Content-Length Awareness

HTTP/1.1 message framing may use Content-Length or transfer coding such as chunked transfer encoding.

Newer HTTP versions use different framing, so do not generalize HTTP/1.1 wire rules to all versions.

#### Why It Matters

Message framing bugs can be security-sensitive, but deep protocol exploitation belongs later in controlled security modules.



### Deep Dive — Content-Disposition Awareness

Content-Disposition can suggest whether content should be displayed inline or downloaded and can carry a filename.

The browser may still apply its own handling rules.

#### HTTP Example

```http
Content-Disposition: attachment; filename="report.pdf"
```

#### Why It Matters

Useful for download endpoints and user-generated reports.



### Deep Dive — Location Header

Location identifies a target URI in redirects and is also commonly included after successful creation.

#### HTTP Example

```http
HTTP/1.1 302 Found
Location: /login
```

#### Why It Matters

Redirect behavior is controlled by both status code and Location.



### Deep Dive — Referer Header Awareness

The Referer header can communicate the referring page URL according to browser policy.

Referrer-Policy can reduce what is sent.

#### Why It Matters

URLs can leak through referrer behavior, reinforcing why secrets should not be placed casually in query strings.



### Deep Dive — User-Agent and Client Hints Awareness

User-Agent historically identifies client software. Modern browsers also have Client Hints mechanisms for certain metadata.

Servers should avoid using user-agent strings as a strong security trust signal.

#### Why It Matters

Client metadata can be spoofed and changes over time.



### Deep Dive — Cookies as HTTP State

Cookies are HTTP-associated state managed by the user agent.

A cookie can be set by a response and later attached automatically to eligible requests according to cookie rules.

#### Diagram / Mental Model

```text
Response
Set-Cookie: session=abc
       ↓
Browser cookie store
       ↓
Matching future request
Cookie: session=abc
```

#### Why It Matters

This automatic request behavior is central to sessions and CSRF-related considerations.



### Deep Dive — Session Identifier Model

A common server-side session stores the important state on the server and gives the browser an unpredictable session identifier.

The identifier is a reference, not the user's password.

#### Diagram / Mental Model

```text
Browser cookie:
session_id=RANDOM

       ↓ request

Server session store:
RANDOM → user_id=42, roles=[operator], expiry=...
```

#### Why It Matters

Session identifiers must be protected because possession can represent authenticated state.



### Deep Dive — Cookie Domain and Host Scope

The Domain attribute changes which hosts are eligible to receive the cookie under cookie rules. Leaving Domain unset commonly creates a host-only cookie.

Broader domain scope can increase exposure.

#### Why It Matters

Use the narrowest cookie scope that satisfies the application.



### Deep Dive — Cookie Path Scope

Path limits which URL paths are eligible for sending a cookie.

Path is useful for scoping but should not be treated as a strong authorization boundary.

#### Why It Matters

Cookie delivery rules do not replace server-side access control.



### Deep Dive — Secure Cookie Attribute

Secure limits cookie transmission to secure contexts/HTTPS according to browser rules.

It helps prevent cookie transmission over plain HTTP.

#### Why It Matters

Secure should be a normal expectation for authentication cookies on HTTPS applications.



### Deep Dive — HttpOnly Cookie Attribute

HttpOnly prevents JavaScript from reading a cookie through normal document-cookie APIs.

It reduces direct cookie theft through many XSS scenarios, but XSS can still perform actions in the victim's browser.

#### Why It Matters

HttpOnly reduces exposure but does not make XSS harmless.



### Deep Dive — SameSite Cookie Attribute

SameSite influences when cookies are sent in cross-site contexts.

Values include Strict, Lax, and None with browser-specific rules/requirements.

#### Why It Matters

SameSite is an important CSRF-related defense layer, not a substitute for understanding application session flows.



### Deep Dive — Cookie Expiration and Session Lifetime

Cookies can be session-scoped or persistent through Max-Age/Expires.

Application session lifetime should also be enforced server-side rather than trusting only the client cookie expiration.

#### Why It Matters

Server-side expiry/revocation is required for reliable session control.



### Deep Dive — Session Rotation

Applications commonly rotate a session identifier after authentication or privilege changes to reduce fixation-related risk.

The high-level concept is:
old identifier → invalidated/replaced → new identifier.

#### Diagram / Mental Model

```text
anonymous session ID A
      ↓ login
server creates/rotates
      ↓
authenticated session ID B
```

#### Why It Matters

Session identity should evolve safely across trust-state changes.



### Deep Dive — Redirect Status Codes: 301/302/303/307/308

Redirect codes differ in permanence and method-handling semantics.

At foundation level:
- 301/308 → permanent
- 302/307 → temporary
- 303 → retrieve result using GET semantics in common workflows
- 307/308 explicitly preserve method/body semantics

#### Why It Matters

Choosing redirect codes intentionally prevents unexpected POST/GET behavior.



### Deep Dive — Open Redirect Risk

An application becomes an open redirect when untrusted input can choose an arbitrary redirect destination.

Use known internal route identifiers or allowlists rather than blindly trusting a `next` parameter.

#### Diagram / Mental Model

```text
/login?next=<untrusted>
         ↓
validate
  ├─ known internal path → redirect
  └─ external/unexpected → reject/default
```

#### Why It Matters

Redirect destinations are security-sensitive input.



### Deep Dive — HTTP Caching Mental Model

Caching has two broad questions:
1. May this response be stored/reused?
2. If stored, is it still fresh or must it be revalidated?

Cache-Control directives, validators, and intermediary behavior answer these questions.

#### Diagram / Mental Model

```text
request
 ↓
cache entry?
 ├─ no → origin
 └─ yes
     ↓ fresh?
     ├─ yes → reuse
     └─ no → conditional validation
```

#### Why It Matters

Caching is a protocol behavior, not simply 'browser keeps a copy'.



### Deep Dive — `Cache-Control: no-store` vs `no-cache`

These directives are commonly confused.

- `no-store` says caches should not store the response.
- `no-cache` permits storage but requires validation before reuse.

The name `no-cache` does not literally mean 'never store'.

#### Why It Matters

Sensitive response handling often needs `no-store`, while revalidation workflows can use `no-cache`.



### Deep Dive — `max-age` and Freshness

`max-age` defines how long a response can be considered fresh in seconds under caching rules.

A fresh response can often be reused without contacting the origin.

#### HTTP Example

```http
Cache-Control: public, max-age=3600
```

#### Why It Matters

Long-lived static assets benefit from intentional freshness policies.



### Deep Dive — ETag Validation

An ETag is a validator representing a version of a representation.

A later request can send If-None-Match. If unchanged, the server can return 304 without retransmitting the full representation.

#### HTTP Example

```http
If-None-Match: "version-123"

HTTP/1.1 304 Not Modified
ETag: "version-123"
```

#### Why It Matters

Conditional validation saves bandwidth while preserving freshness.



### Deep Dive — Last-Modified and If-Modified-Since

Last-Modified provides a timestamp validator. Clients can send If-Modified-Since for conditional validation.

ETags can provide more precise version identity depending on implementation.

#### HTTP Example

```http
Last-Modified: Wed, 19 Aug 2026 07:00:00 GMT
```

#### Why It Matters

Different validators fit different resource/versioning strategies.



### Deep Dive — `Vary` Header

Vary tells caches which request-header fields affect representation selection.

For example, if content changes by Accept-Encoding or Accept-Language, caches may need separate variants.

#### HTTP Example

```http
Vary: Accept-Encoding, Accept-Language
```

#### Why It Matters

Incorrect Vary behavior can serve the wrong representation to clients.



### Deep Dive — Private vs Public Caching

`private` restricts reuse to private/user-specific caches, while `public` permits shared-cache use when otherwise allowed.

Sensitive authenticated data needs careful cache policy.

#### Why It Matters

Shared intermediary caches introduce privacy considerations.



### Deep Dive — Cache Busting with Content Hashes

Static assets can be given filenames containing a content hash.

When content changes, the URL changes; unchanged assets can use long freshness lifetimes.

#### Diagram / Mental Model

```text
app.83af2c.css
app.4e2d11.js
```

#### Why It Matters

This separates content versioning from forced short cache lifetimes.



### Deep Dive — Reverse Proxy

A reverse proxy accepts client traffic on behalf of backend services and forwards requests upstream.

It may perform TLS termination, routing, header management, compression, caching, authentication integration, or WAF-related controls depending on configuration.

#### Diagram / Mental Model

```text
Client
  ↓
Reverse Proxy
  ├─ /api → app
  ├─ /static → asset server
  └─ /auth → auth service
```

#### Why It Matters

Many 'server errors' actually originate at proxy/upstream boundaries.



### Deep Dive — Forward Proxy

A forward proxy represents clients when reaching external destinations.

The proxy may enforce policy, logging, filtering, caching, or egress control.

#### Diagram / Mental Model

```text
Internal client
    ↓
Forward Proxy
    ↓
Internet
```

#### Why It Matters

Forward and reverse proxies represent opposite sides of the communication.



### Deep Dive — Load Balancing

A load balancer distributes traffic across healthy targets.

Common conceptual algorithms include:
- round robin
- least connections
- weighted strategies
- hash/stickiness strategies

#### Diagram / Mental Model

```text
Client
  ↓
Load Balancer
 ├─ App 1
 ├─ App 2
 └─ App 3
```

#### Why It Matters

Horizontal scaling usually adds routing and health-state decisions.



### Deep Dive — Health Checks

Load balancers/proxies often determine backend availability using health checks.

A health endpoint should reflect the intended readiness semantics and avoid expensive/unreliable work.

#### HTTP Example

```http
GET /health HTTP/1.1

HTTP/1.1 200 OK
Content-Type: application/json

{"status":"ok"}
```

#### Why It Matters

Liveness and readiness are different concepts in larger systems.



### Deep Dive — Sticky Sessions Awareness

Some load balancers attempt to keep a client mapped to the same backend.

This can simplify stateful legacy applications but creates scaling/failover trade-offs.

#### Diagram / Mental Model

```text
Client A → App 1
Client A → App 1
Client B → App 2
```

#### Why It Matters

Stateless application design generally reduces dependence on stickiness.



### Deep Dive — CDN Request Path

A CDN edge can answer from cache or forward to the origin.

The edge may also terminate TLS and apply security/routing controls depending on provider configuration.

#### Diagram / Mental Model

```text
User
 ↓
CDN Edge
 ├─ cache HIT → response
 └─ cache MISS
       ↓
      Origin
```

#### Why It Matters

CDN behavior must be included when troubleshooting cache, headers, TLS, or stale content.



### Deep Dive — Origin Server Protection Awareness

When a CDN/WAF fronts an application, the origin should not automatically remain broadly reachable in ways that bypass expected controls.

Network restrictions and authentication between layers may be appropriate depending on architecture.

#### Why It Matters

A security control in front of an origin is weaker if clients can trivially bypass it.



### Deep Dive — Gateway Header Trust and `X-Forwarded-*` Awareness

Reverse proxies may add headers such as X-Forwarded-For, X-Forwarded-Proto, or standardized Forwarded information.

Applications should trust these only from known proxy paths with correct sanitization.

#### Why It Matters

If arbitrary clients can supply trusted proxy headers directly, logs and security decisions can be spoofed.



### Deep Dive — Same-Origin Policy

The browser same-origin policy restricts scripts from freely reading data from different origins.

It is a browser-side isolation boundary, not a network firewall.

#### Diagram / Mental Model

```text
https://portal.example.com
        ↓ JS fetch
https://api.example.com
different origin
        ↓
browser applies cross-origin rules
```

#### Why It Matters

The network request and JavaScript's ability to read the response are separate questions.



### Deep Dive — CORS Response Headers

CORS lets a server tell browsers which origins may access responses in supported scenarios.

Important headers can include:
- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Credentials
- Access-Control-Expose-Headers

#### HTTP Example

```http
Access-Control-Allow-Origin: https://portal.example.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type
```

#### Why It Matters

CORS is browser-enforced response-access policy, not backend authorization.



### Deep Dive — CORS Preflight

For some cross-origin requests, the browser sends an OPTIONS preflight describing the intended origin, method, and non-simple headers.

The server responds with policy. If permitted, the browser proceeds with the actual request.

#### Diagram / Mental Model

```text
Browser
  ↓ OPTIONS preflight
Server
  ↓ CORS permission
Browser
  ↓ actual PATCH/POST/etc
```

#### Why It Matters

Seeing an OPTIONS request in DevTools does not necessarily mean application JavaScript explicitly sent it.



### Deep Dive — Credentialed CORS Awareness

Credentialed cross-origin requests have additional constraints.

Allowing credentials broadly while reflecting arbitrary origins is dangerous. CORS policy should name the origins the application actually trusts.

#### Why It Matters

Credentials, cookies, cross-origin access, and server authorization must be designed together.



### Deep Dive — CSRF vs CORS

CSRF and CORS address different issues.

CORS:
- whether browser JavaScript may read certain cross-origin responses.

CSRF:
- unwanted state-changing requests sent using ambient browser credentials.

One does not automatically solve the other.

#### Diagram / Mental Model

```text
CORS question:
"May this origin's JS read the response?"

CSRF question:
"Can another site cause the browser to send an unwanted authenticated action?"
```

#### Why It Matters

Security troubleshooting often fails when these mechanisms are conflated.



### Deep Dive — Content Security Policy

CSP is an HTTP response policy that restricts classes of content loading/execution.

Examples include script, image, frame, object, and connection sources.

#### HTTP Example

```http
Content-Security-Policy:
  default-src 'self';
  img-src 'self' https:;
  object-src 'none'
```

#### Why It Matters

CSP reduces attack surface/impact but does not replace safe output handling or server security.



### Deep Dive — HSTS

HTTP Strict Transport Security tells supporting browsers to use HTTPS for the host for a period once policy has been learned according to browser rules.

#### HTTP Example

```http
Strict-Transport-Security:
  max-age=31536000; includeSubDomains
```

#### Why It Matters

HSTS reduces downgrade/accidental HTTP exposure after policy establishment.

#### Common Problems / Troubleshooting

Deploy carefully, especially with includeSubDomains/preload-related decisions, because the policy can affect many hosts.



### Deep Dive — X-Content-Type-Options Awareness

`X-Content-Type-Options: nosniff` tells browsers not to perform certain MIME-sniffing behavior.

Correct Content-Type headers remain necessary.

#### HTTP Example

```http
X-Content-Type-Options: nosniff
```

#### Why It Matters

Content interpretation is a security boundary.



### Deep Dive — Referrer-Policy Awareness

Referrer-Policy controls how much referrer information the browser includes when navigating or fetching resources.

#### HTTP Example

```http
Referrer-Policy: strict-origin-when-cross-origin
```

#### Why It Matters

This can reduce URL-information leakage.



### Deep Dive — Permissions-Policy Awareness

Permissions-Policy can restrict selected browser capabilities for a page and embedded contexts.

It is relevant to features such as camera, microphone, geolocation, and others.

#### Why It Matters

Browser capability access should be intentionally scoped.



### Deep Dive — Authentication vs Authorization

Authentication establishes identity. Authorization decides whether that identity may perform an action.

A request can be:
- unauthenticated
- authenticated but forbidden
- authenticated and allowed

#### Diagram / Mental Model

```text
credentials/session
     ↓
authentication
     ↓ identity
authorization policy
     ↓
allow / deny
```

#### Why It Matters

Frontend visibility never replaces server authorization.



### Deep Dive — Bearer Token Awareness

Some APIs use bearer tokens in Authorization headers.

Possession of a bearer token is sufficient for whoever presents it under the token's rules, so tokens must be protected and scoped.

#### HTTP Example

```http
Authorization: Bearer <token>
```

#### Why It Matters

The browser-storage/session architecture determines exposure and transport behavior.



### Deep Dive — Basic Authentication Awareness

HTTP Basic authentication encodes username/password-like credentials into the Authorization header.

It must be protected by HTTPS because base64 encoding is not encryption.

#### Why It Matters

Encoding is not confidentiality.



### Deep Dive — Rate Limiting

Servers/gateways may limit requests per identity, IP, API key, route, or another dimension.

Rate limiting protects capacity and can reduce abuse but does not replace authentication/authorization.

#### HTTP Example

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 10
```

#### Why It Matters

Clients should understand backoff/retry semantics.



### Deep Dive — Idempotency Keys Awareness

For operations such as payment/order creation where clients may retry a POST after network uncertainty, an idempotency key can let the server recognize a repeated logical operation.

This is application-level design built on top of HTTP semantics.

#### HTTP Example

```http
Idempotency-Key: 96a7b...
```

#### Why It Matters

Network failure can leave the client unsure whether a server processed a request.



### Deep Dive — Timeout Layers

A single web request may have several timeout layers:
- browser/client
- CDN
- load balancer
- reverse proxy
- application
- database/internal service

The smallest effective timeout can terminate the request.

#### Diagram / Mental Model

```text
Client timeout 30s
  ↓
Proxy timeout 15s
  ↓
App timeout 20s
  ↓
DB timeout 5s

DB may fail first.
```

#### Why It Matters

504-style problems require tracing the whole request path.



### Deep Dive — Retries and Retry Storms Awareness

Retries can improve resilience for transient failures but can amplify load when many clients retry simultaneously.

Use:
- bounded retries
- backoff
- jitter
- idempotency-aware behavior

#### Diagram / Mental Model

```text
service slows
   ↓
clients timeout
   ↓
all retry immediately
   ↓
more load
   ↓
service worsens
```

#### Why It Matters

HTTP client behavior affects distributed-system stability.



### Deep Dive — Observability: Request IDs / Correlation IDs

A request identifier can be propagated across proxy/application logs so one transaction can be traced through several components.

Do not accept a client-supplied request ID blindly as authoritative without normalization/trust rules.

#### Diagram / Mental Model

```text
Browser
 request-id=abc
   ↓
Gateway log abc
   ↓
App log abc
   ↓
DB/service trace abc
```

#### Why It Matters

Correlation dramatically improves troubleshooting.



### Deep Dive — Access Logs

Web servers/proxies commonly log request metadata such as:
- timestamp
- method
- path
- status
- bytes
- latency
- user agent
- client/proxy address data

Sensitive fields should be excluded/redacted.

#### Why It Matters

Logs are both an operations asset and a potential sensitive-data sink.



### Deep Dive — Do Not Log Secrets

URLs, headers, and request bodies can contain secrets or personal data.

Avoid logging:
- passwords
- session identifiers
- bearer tokens
- full sensitive request bodies
- secrets in query strings

#### Why It Matters

Security failures often happen through observability systems, not only application databases.



### Deep Dive — `curl` Core Inspection

`curl` is one of the best tools for learning and troubleshooting HTTP.

Useful options:
- `-i` include response headers
- `-I` HEAD request
- `-v` verbose protocol/connection details
- `-L` follow redirects
- `-H` add request headers
- `-d` request body
- `--data-binary` preserve body bytes more literally

#### CLI Example

```bash
curl -i http://localhost:8000/
curl -I http://localhost:8000/
curl -v http://localhost:8000/
curl -L http://localhost:8000/redirect
```

#### Why It Matters

Use against your own/local/test endpoints for controlled experimentation.



### Deep Dive — `curl` JSON Request

For a local JSON endpoint, send explicit Content-Type and inspect status/headers/body.

#### CLI Example

```bash
curl -i   -X POST   -H 'Content-Type: application/json'   -H 'Accept: application/json'   --data '{"hostname":"web-01"}'   http://localhost:8000/echo
```

#### Why It Matters

This separates frontend behavior from backend/protocol behavior during debugging.



### Deep Dive — `curl -w` Timing Metrics

`curl` can print timing metrics, helping distinguish DNS, connect, TLS, first-byte, and total-time delays.

#### CLI Example

```bash
curl -sS -o /dev/null   -w 'dns=%{time_namelookup}
connect=%{time_connect}
starttransfer=%{time_starttransfer}
total=%{time_total}
'   https://example.com/
```

#### Why It Matters

Latency is not one number; different phases can dominate.



### Deep Dive — `curl --resolve` Awareness

For authorized/local troubleshooting, `--resolve` can map a hostname and port to a chosen IP while preserving the hostname in TLS/HTTP handling.

This is useful when testing a server before DNS cutover.

#### CLI Example

```bash
curl --resolve portal.example.test:443:127.0.0.1   https://portal.example.test/
```

#### Why It Matters

It separates DNS selection from application/TLS hostname behavior.

#### Common Problems / Troubleshooting

Use only with systems you control or are authorized to test.



### Deep Dive — `openssl s_client` Awareness

OpenSSL can inspect TLS connection/certificate information at a low level.

This is useful for learning certificates and SNI, but browser validation policy and OpenSSL behavior are not identical in every detail.

#### CLI Example

```bash
openssl s_client   -connect example.com:443   -servername example.com
```

#### Why It Matters

It helps distinguish TLS handshake/certificate issues from HTTP issues.



### Deep Dive — Browser DevTools Network Waterfall

A Network waterfall visually shows:
- request start time
- queueing
- connection
- request sent
- waiting/TTFB
- download

The exact labels differ by browser, but the phases expose where time is spent.

#### Diagram / Mental Model

```text
HTML   [DNS][TCP][TLS][wait][download]
CSS              [wait][download]
JS               [wait][download]
IMG                    [wait][download]
```

#### Why It Matters

Page-load performance is a dependency graph, not a single request.



### Deep Dive — TTFB Awareness

Time To First Byte measures elapsed time until the first response byte is received.

It can include:
- network latency
- connection/TLS setup
- proxy delay
- application processing
- database/internal calls

#### Why It Matters

High TTFB does not automatically mean 'the backend code is slow'; investigate the path.



### Deep Dive — Browser Cache vs Memory/Disk Cache

Browsers may serve resources from memory or disk caches depending on resource state and browser implementation.

DevTools can show cache source, but behavior varies by browser/version and navigation type.

#### Why It Matters

Always inspect actual request details rather than relying on assumptions.



### Deep Dive — Service Worker Interception Awareness

A service worker can intercept fetches and return cached/generated responses.

This means a browser request may not always reach the network/origin.

#### Diagram / Mental Model

```text
page fetch
   ↓
service worker
  ├─ return cache response
  └─ fetch network
```

#### Why It Matters

When DevTools behavior seems inconsistent, check service-worker state.



### Deep Dive — WebSocket vs HTTP Request/Response

Traditional HTTP follows discrete request/response exchanges. WebSocket upgrades to a long-lived bidirectional channel.

Use WebSocket only when continuous two-way communication is actually needed.

#### Diagram / Mental Model

```text
HTTP:
request → response
request → response

WebSocket:
client ⇄ server
persistent messages
```

#### Why It Matters

Different communication patterns have different scaling, proxy, timeout, and security implications.



### Deep Dive — SSE vs WebSocket

Server-Sent Events provide one-way server-to-client streaming over HTTP. WebSocket supports bidirectional messaging.

Choose based on communication requirements rather than popularity.

#### Diagram / Mental Model

```text
SSE:
Server ─────→ Browser

WebSocket:
Server ⇄ Browser
```

#### Why It Matters

Real-time design begins with message direction and lifecycle requirements.



### Deep Dive — REST Awareness

REST is an architectural style, not simply 'JSON over HTTP'.

At this stage, focus on:
- resources
- representations
- uniform HTTP semantics
- stateless request interactions
- meaningful methods/statuses

#### Why It Matters

A later API course will go deeper; this prevents reducing REST to URL naming conventions.



### Deep Dive — API Versioning Awareness

APIs can evolve through compatible changes or explicit versioning approaches such as URL, header, or media-type strategies.

Versioning cannot replace disciplined backward compatibility.

#### Diagram / Mental Model

```text
/api/v1/assets

or negotiated header/media strategy
```

#### Why It Matters

Clients and servers evolve independently.



### Deep Dive — Pagination Awareness

Large collections should not always be returned in one response.

Common strategies include:
- page/offset
- cursor/token

Cursor-style designs often behave better with changing large datasets.

#### HTTP Example

```http
GET /api/assets?limit=50&cursor=abc123
```

#### Why It Matters

Pagination affects caching, consistency, latency, and API design.



### Deep Dive — HTTP Range Requests Awareness

Range requests let clients request part of a representation when servers support them.

They are useful for large downloads and media.

#### HTTP Example

```http
Range: bytes=0-999
```

#### Why It Matters

Partial content behavior is another example of HTTP metadata controlling representation transfer.



### Deep Dive — Conditional Updates with ETags Awareness

ETags can also support optimistic concurrency. A client can update only if the resource version still matches.

Conceptually, `If-Match` says: apply this request only if the current representation validator matches.

#### HTTP Example

```http
PATCH /api/assets/42 HTTP/1.1
If-Match: "v7"
```

#### Why It Matters

This prevents silently overwriting another actor's newer update.



### Deep Dive — Browser Security Boundary Summary

At browser level, several mechanisms work together:
- same-origin policy
- CORS
- cookies and SameSite
- CSP
- HSTS
- secure content types
- referrer policy
- permissions policy

None of them replaces server authentication, authorization, validation, or safe output handling.

#### Diagram / Mental Model

```text
Browser security controls
        +
Server security controls
        +
TLS transport
        +
Application logic
        ↓
Defense in depth
```

#### Why It Matters

Web security is a system of layers.



### Deep Dive — Structured Troubleshooting: DNS Failure

Symptoms:
- browser reports host not found/name resolution error
- `curl` cannot resolve host
- no HTTP status is available

Tools:
- `nslookup`
- `dig`
- OS resolver checks

Do not troubleshoot HTTP headers before DNS succeeds.

#### CLI Example

```bash
nslookup example.com
dig example.com A
```

#### Why It Matters

Start at the lowest failing layer.



### Deep Dive — Structured Troubleshooting: TLS Failure

Symptoms:
- certificate warning
- handshake failure
- hostname mismatch
- expired/not-yet-valid certificate

Tools:
- browser certificate/security UI
- `curl -v`
- `openssl s_client`

The application may never receive a normal HTTP request.

#### Why It Matters

TLS failure is distinct from HTTP 4xx/5xx responses.



### Deep Dive — Structured Troubleshooting: HTTP 404

A 404 proves the request reached an HTTP-speaking endpoint that decided the target was not found/disclosed.

Check:
- final URL after redirects
- host
- path
- proxy route
- application route
- case/path normalization

#### Why It Matters

Do not confuse DNS success with correct application routing.



### Deep Dive — Structured Troubleshooting: 502/504

For a gateway response:
- client reached proxy
- proxy had trouble with upstream response/timeout

Investigate:
- upstream DNS
- upstream port
- application health
- connection refusal
- proxy timeout
- backend latency

#### Diagram / Mental Model

```text
Client ✓
  ↓
Gateway ✓
  ↓
Upstream ✗
```

#### Why It Matters

The response code points to the failing relationship.



### Deep Dive — Structured Troubleshooting: CORS Error

A browser CORS failure does not necessarily mean the network request failed.

Inspect Network:
- was a preflight sent?
- what status came back?
- what Access-Control-* headers were present?
- did credentials change requirements?
- is the requested origin exactly permitted?

Then verify server auth independently.

#### Why It Matters

Browser JavaScript access can fail even when the server responded.



### Deep Dive — Structured Troubleshooting: Wrong Content Type

If a browser expects JSON but receives HTML, common causes include:
- reverse proxy error page
- authentication redirect to login
- wrong route
- fallback HTML response
- server misconfiguration

Inspect status, final URL, and Content-Type before parsing.

#### Diagram / Mental Model

```text
Frontend expects JSON
     ↓
response is text/html
     ↓
JSON.parse fails
```

#### Why It Matters

The parsing error is often only the final symptom.



### Deep Dive — Structured Troubleshooting: Stale Content

Possible causes include:
- browser cache
- CDN cache
- service worker cache
- proxy cache
- DNS still pointing to old deployment
- old backend instance
- application-level cache

Inspect response headers and request path before clearing everything blindly.

#### Why It Matters

Caching exists at multiple layers.



### Deep Dive — Local Python HTTP Lab Server

A small local server can help demonstrate methods, headers, redirects, cookies, cache controls, and error responses without requiring a backend framework.

This is educational infrastructure for your own machine only.

#### Python Example

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, payload, headers=None):
        body = json.dumps(payload).encode()

        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8",
        )
        self.send_header(
            "Content-Length",
            str(len(body)),
        )

        for name, value in (headers or {}).items():
            self.send_header(name, value)

        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/status":
            self.send_json(
                200,
                {"status": "healthy"},
                {"Cache-Control": "no-store"},
            )
            return

        if self.path == "/redirect":
            self.send_response(302)
            self.send_header("Location", "/status")
            self.end_headers()
            return

        if self.path == "/error":
            self.send_json(
                500,
                {"error": "synthetic lab failure"},
            )
            return

        self.send_json(
            404,
            {"error": "not found"},
        )

server = HTTPServer(
    ("127.0.0.1", 8000),
    Handler,
)

print("http://127.0.0.1:8000")
server.serve_forever()
```

#### Why It Matters

A controlled local target lets you experiment safely with HTTP semantics.



### Deep Dive — Local Request Flow Walkthrough

For `http://127.0.0.1:8000/status`, DNS is not needed because the URL already contains the loopback IP.

The simplified flow is:
browser/curl → TCP loopback connection → HTTP GET → Python handler → HTTP response.

#### Diagram / Mental Model

```text
curl/browser
    ↓
127.0.0.1:8000
    ↓
Python HTTPServer
    ↓
Handler.do_GET()
    ↓
200 JSON
```

#### Why It Matters

This isolates HTTP learning from DNS/TLS complexity.



### Deep Dive — End-to-End Request Dependency Graph

A modern page can trigger dozens of dependent requests.

The initial HTML may discover CSS/JS. CSS can discover fonts/images. JavaScript can call APIs. Each request can have DNS/connection/TLS/cache behavior.

#### Diagram / Mental Model

```text
HTML
├─ CSS
│  ├─ font
│  └─ background image
├─ JS
│  └─ API
└─ image
```

#### Why It Matters

Page loading is a dependency graph, not a single waterfall line.



### Deep Dive — Final Web-Fundamentals Engineering Model

The web is best understood as a chain of independent but interacting layers.

A professional can explain:
- what component acts at each layer
- what observable evidence proves progress/failure
- which security boundary applies
- which caching/proxy behavior can alter the path

#### Diagram / Mental Model

```text
URL
 ↓
DNS
 ↓
Transport
 ↓
TLS
 ↓
HTTP
 ↓
Proxy/CDN
 ↓
Application
 ↓
Storage/services
 ↓
HTTP response
 ↓
Browser policy/cache
 ↓
Frontend
```

#### Why It Matters

This model is the bridge into Phase 4 networking and later backend/cloud/security phases.



## 5. Hands-on Lab / Practical Exercises


### Lab 1 — Trace a Page Load

Use a simple page you created yourself.

1. Start a local web server.
2. Open Developer Tools → Network.
3. Clear the request list.
4. Reload the page.
5. Identify the initial HTML request.
6. Identify CSS, JavaScript, and image requests.
7. Record method, status, content type, and transferred size.
8. Disable cache in Developer Tools and reload.
9. Re-enable caching and compare behavior.
10. Explain the dependency chain.

Create a report table:

| Resource | Method | Status | Content-Type | Purpose |
|---|---|---:|---|---|
| `/` | GET | 200 | text/html | Main document |
| `/styles.css` | GET | 200 | text/css | Presentation |
| `/app.js` | GET | 200 | application/javascript | Behavior |
### Lab 2 — Inspect HTTP with `curl`

Run against your own local web server or a public site that permits normal browsing.

Tasks:

1. Fetch headers.
2. Fetch body.
3. Use verbose mode.
4. Send a custom `Accept` header.
5. Compare HTTP and HTTPS URLs if the service supports both.
6. Identify redirects.
7. Record `Content-Type`.
8. Record caching headers.
9. Identify cookies if present.
10. Explain which information belongs to request vs response.

Do not send disruptive traffic or attempt authentication bypasses.
### Lab 3 — Build a Local Client/Server Demonstration

Use a simple local server already available to you, such as a Python development server or a tiny test application.

Create:

```text
browser -> localhost server -> JSON response
```

Requirements:

1. Browser page contains a Load Status button.
2. JavaScript calls a local `/status` endpoint.
3. Endpoint returns JSON.
4. Network panel shows request/response.
5. UI renders the returned text safely.
6. Temporarily return a 500 response and observe client handling.
7. Temporarily return malformed JSON and observe parsing failure.
8. Document what happened at each layer.

If you have not yet learned backend frameworks, use a supplied/test server rather than turning this phase into backend development.
### Lab 4 — DNS and URL Analysis

Choose three well-known domains.

For each:

1. Break the URL into components.
2. Resolve the hostname using `nslookup` or `dig`.
3. Record A/AAAA information if present.
4. Open the page and inspect the Network panel.
5. Identify whether redirects occur.
6. Inspect certificate information using the browser's connection/security UI.
7. Record the final origin.
8. Explain whether subdomains are the same origin.

Do not infer organizational network architecture solely from public DNS records; record only what the tools actually show.


## Enhanced Hands-on Labs

### Enhanced Lab 1 — URL Anatomy

Break 20 URLs into scheme, authority, host, port, path, query, and fragment.

### Enhanced Lab 2 — URL Encoding

Encode/decode query parameters containing spaces, ampersands, Arabic text, and slashes using a URL library.

### Enhanced Lab 3 — Origin Classification

Classify 20 URL pairs as same-origin or cross-origin.

### Enhanced Lab 4 — DNS Resolution

Use nslookup/dig on three domains and distinguish recursive-answer output from authoritative concepts.

### Enhanced Lab 5 — DNS Record Types

Inspect A, AAAA, NS, CNAME/TXT where available and explain each record's purpose.

### Enhanced Lab 6 — TTL

Record TTL values for a test domain at different times and explain cache countdown behavior.

### Enhanced Lab 7 — CNAME Chain

Find or create a controlled alias chain and draw resolution.

### Enhanced Lab 8 — Virtual Hosting

Run two local virtual-host style services conceptually or inspect Host header behavior with a local server.

### Enhanced Lab 9 — TCP Mental Trace

Draw SYN/SYN-ACK/ACK then place HTTP after connection establishment.

### Enhanced Lab 10 — Connection Reuse

Use browser Network or curl verbose output to observe/reason about reused vs new connections.

### Enhanced Lab 11 — TLS Inspection

Use browser certificate UI on a normal public site and record hostname, issuer chain, validity period without extracting secrets.

### Enhanced Lab 12 — OpenSSL TLS

Use openssl s_client against a normal public site and identify certificate/SNI-related output.

### Enhanced Lab 13 — HTTP Request Read

Annotate method, request target, headers, blank line, body in ten request examples.

### Enhanced Lab 14 — HTTP Response Read

Annotate status line, headers, body in ten responses.

### Enhanced Lab 15 — GET Semantics

Create/read a local GET endpoint and explain why it should not mutate server state.

### Enhanced Lab 16 — POST Semantics

Create a local POST example and document duplicate-retry risk.

### Enhanced Lab 17 — PUT vs PATCH

Write sample API requests for replacement vs partial update.

### Enhanced Lab 18 — HEAD

Use curl -I and compare metadata with GET.

### Enhanced Lab 19 — OPTIONS

Inspect a controlled OPTIONS response.

### Enhanced Lab 20 — Safe/Idempotent

Classify GET/HEAD/POST/PUT/PATCH/DELETE by safe/idempotent expectations.

### Enhanced Lab 21 — 2xx Statuses

Create sample 200, 201, and 204 responses and explain use cases.

### Enhanced Lab 22 — 401 vs 403

Write three auth scenarios and select the appropriate status.

### Enhanced Lab 23 — 404 Non-Disclosure

Explain a scenario where a system intentionally returns 404 instead of revealing resource existence.

### Enhanced Lab 24 — 409

Model a duplicate deployment/state-conflict response.

### Enhanced Lab 25 — 422

Model semantic validation errors for a valid JSON body.

### Enhanced Lab 26 — 429

Simulate a local rate-limit response with Retry-After.

### Enhanced Lab 27 — 502/503/504

Map each code to a proxy/backend failure scenario.

### Enhanced Lab 28 — Content-Type

Serve JSON with correct and incorrect Content-Type and observe client behavior.

### Enhanced Lab 29 — Accept

Send different Accept headers to a controlled endpoint and inspect response.

### Enhanced Lab 30 — Accept-Language

Design a localization negotiation example and include Vary reasoning.

### Enhanced Lab 31 — Compression

Inspect Accept-Encoding and Content-Encoding on a normal public response.

### Enhanced Lab 32 — Content-Disposition

Create a local download response with attachment filename.

### Enhanced Lab 33 — Location

Build a local redirect and follow it with/without curl -L.

### Enhanced Lab 34 — Referer Awareness

Inspect browser referrer behavior using only local/test pages and explain policy effects.

### Enhanced Lab 35 — Cookie Set/Send

Use a local server/browser to observe Set-Cookie then Cookie on later eligible request.

### Enhanced Lab 36 — Cookie Scope

Experiment conceptually/locally with Path and host scope.

### Enhanced Lab 37 — Cookie Security

Document Secure/HttpOnly/SameSite for an authentication-cookie design.

### Enhanced Lab 38 — Session Model

Draw browser session ID → server-side session record mapping.

### Enhanced Lab 39 — Session Rotation

Document the before-login and after-login identifier lifecycle.

### Enhanced Lab 40 — Redirect Codes

Compare 302/303/307 behavior conceptually with POST in a controlled local lab.

### Enhanced Lab 41 — Open Redirect Defense

Validate a local `next` path using an allowlist.

### Enhanced Lab 42 — Cache Freshness

Serve a local response with max-age and observe cache reuse.

### Enhanced Lab 43 — no-store vs no-cache

Compare these directives using DevTools.

### Enhanced Lab 44 — ETag

Implement or simulate ETag/If-None-Match/304 locally.

### Enhanced Lab 45 — Last-Modified

Observe conditional validation with timestamp-based validator if available.

### Enhanced Lab 46 — Vary

Explain why two Accept-Language variants must not share one cache representation.

### Enhanced Lab 47 — Private/Public Cache

Design cache policies for static CSS, public docs, user dashboard, and banking-like account response.

### Enhanced Lab 48 — Asset Hashing

Rename a static asset with a content hash and explain long-term caching.

### Enhanced Lab 49 — Reverse Proxy Map

Draw browser→reverse proxy→three upstream services and annotate responsibilities.

### Enhanced Lab 50 — Load Balancer

Design a simple health-check and traffic-distribution scenario.

### Enhanced Lab 51 — Sticky Session

Explain failure/scaling trade-offs of backend stickiness.

### Enhanced Lab 52 — CDN Hit/Miss

Trace edge cache hit and miss paths.

### Enhanced Lab 53 — Forwarded Headers

List which proxy headers an app may trust only from known infrastructure.

### Enhanced Lab 54 — CORS Simple Case

Inspect a controlled cross-origin GET and required response header.

### Enhanced Lab 55 — CORS Preflight

Inspect OPTIONS + actual request in a local/test setup.

### Enhanced Lab 56 — CORS Credentials

Explain why wildcard origin and credentials require careful policy.

### Enhanced Lab 57 — CORS vs CSRF

Build a comparison table with threat, browser behavior, and defense.

### Enhanced Lab 58 — CSP

Design a restrictive conceptual CSP for a simple self-hosted app.

### Enhanced Lab 59 — HSTS

Explain HSTS lifecycle and why deployment requires care.

### Enhanced Lab 60 — Security Headers

Inspect CSP/HSTS/Referrer-Policy/nosniff on a normal public site and explain purpose only.

### Enhanced Lab 61 — Bearer Token

Construct a dummy local Authorization header and explain why possession matters.

### Enhanced Lab 62 — Basic Auth

Explain why HTTPS is mandatory despite base64 encoding.

### Enhanced Lab 63 — Rate Limit

Design client backoff behavior after 429.

### Enhanced Lab 64 — Idempotency Key

Design a synthetic order-create retry flow using a client-generated idempotency key.

### Enhanced Lab 65 — Timeout Layers

Draw client/CDN/proxy/app/database timeout values and identify which fires first.

### Enhanced Lab 66 — Retry Storm

Simulate on paper how immediate retries increase load; propose exponential backoff+jitter.

### Enhanced Lab 67 — Correlation ID

Add a synthetic request ID through local client/server logs.

### Enhanced Lab 68 — Access Log

Design a safe access-log schema excluding secrets.

### Enhanced Lab 69 — curl Headers

Use curl -i/-I/-v on local/test endpoints.

### Enhanced Lab 70 — curl Redirect

Use curl with and without -L and document each response.

### Enhanced Lab 71 — curl JSON

POST JSON to the local lab server and inspect request/response.

### Enhanced Lab 72 — curl Timing

Use curl -w and explain DNS/connect/start-transfer/total.

### Enhanced Lab 73 — curl Resolve

Use --resolve only in a controlled/local setup and explain how it bypasses DNS selection.

### Enhanced Lab 74 — DevTools Waterfall

Record one page-load waterfall and explain dependency order.

### Enhanced Lab 75 — TTFB

Identify three different causes of high TTFB.

### Enhanced Lab 76 — Service Worker Awareness

Inspect whether a controlled app has an active service worker and explain how it can intercept requests.

### Enhanced Lab 77 — WebSocket vs SSE

Choose appropriate transport for bidirectional chat vs one-way status feed.

### Enhanced Lab 78 — REST Awareness

Review one local API and identify resources, representations, methods, and status semantics.

### Enhanced Lab 79 — API Versioning

Design a backward-compatible evolution example before adding explicit v2.

### Enhanced Lab 80 — Pagination

Compare offset and cursor pagination for a changing 1M-row asset dataset.

### Enhanced Lab 81 — Range Requests

Inspect a normal large/static file's range support if available.

### Enhanced Lab 82 — Optimistic Concurrency

Design If-Match/ETag update conflict behavior.

### Enhanced Lab 83 — DNS Failure Runbook

Create a troubleshooting runbook from browser error to resolver checks.

### Enhanced Lab 84 — TLS Failure Runbook

Create a runbook for certificate mismatch/expiry/chain problems.

### Enhanced Lab 85 — 404 Runbook

Trace URL→proxy route→application route.

### Enhanced Lab 86 — 502/504 Runbook

Trace gateway→upstream DNS/port/health/timeout.

### Enhanced Lab 87 — CORS Runbook

Trace Origin→preflight→response headers→credential rules.

### Enhanced Lab 88 — Wrong Content-Type

Create a frontend expecting JSON but receiving HTML and diagnose using Network panel.

### Enhanced Lab 89 — Stale Content

Create a cache-layer checklist: browser/CDN/service worker/proxy/app.

### Enhanced Lab 90 — Local Python Server

Run the safe local Python HTTP server from the course and test /status, /redirect, /error, and 404.

### Enhanced Lab 91 — Capstone

Complete the expanded Web Request Observatory and WEB_REQUEST_FLOW.md.


## 6. Mini Project

### Mini Project — Web Request Observatory

Create a small educational project that demonstrates how browser requests work.

**Part A — Frontend**

Build a page with:

- URL input for a **predefined allowlist of safe local/test endpoints**.
- Method selector for GET and POST.
- JSON body input for POST.
- Send button.
- Response-status area.
- Response-header area.
- Response-body area.
- Error display.

**Part B — Local test service**

Use a simple local server that exposes:

- `GET /status`
- `GET /servers`
- `POST /echo`
- `GET /redirect`
- `GET /cache-demo`
- `GET /error`

**Part C — Analysis**

For each endpoint, document:

- Request method.
- Request headers.
- Request body.
- Status code.
- Response headers.
- Response body.
- Cache behavior.
- Redirect behavior.
- Whether cookies are used.
- Whether cross-origin rules affect the request.

**Security restriction**

Keep the observatory restricted to endpoints you own or deliberately set up for the lab. Do not turn it into an unrestricted request-forwarding tool.

**Deliverable**

Write `WEB_REQUEST_FLOW.md` explaining one request from URL entry all the way through DNS/connection/TLS/HTTP/browser processing at the level covered in this module.


### Expanded Capstone — Web Request Observatory + Local Protocol Lab

Build a complete educational request observatory restricted to local/test endpoints you own.

```text
web-request-observatory/
├── README.md
├── WEB_REQUEST_FLOW.md
├── TROUBLESHOOTING_RUNBOOK.md
├── SECURITY_NOTES.md
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── server/
│   └── lab_server.py
├── fixtures/
│   ├── assets.json
│   └── report.txt
└── docs/
    ├── http-methods.md
    ├── status-codes.md
    ├── caching.md
    ├── cookies-sessions.md
    ├── cors-csrf.md
    ├── tls.md
    └── proxy-cdn.md
```

## Local endpoints

Implement these on `127.0.0.1` only:

```text
GET  /status
GET  /servers
POST /echo
GET  /redirect
GET  /cache-demo
GET  /etag-demo
GET  /set-cookie
GET  /show-cookie
GET  /error
GET  /slow
GET  /download
OPTIONS /cors-demo
```

Keep the project local. Do not make it an unrestricted proxy or arbitrary URL fetcher.

## Frontend request allowlist

The browser UI can only call predefined local endpoints.

Example:

```javascript
const allowedEndpoints = new Set([
    "/status",
    "/servers",
    "/echo",
    "/redirect",
    "/cache-demo",
    "/etag-demo",
    "/error"
]);
```

The UI must display:

```text
request URL
method
request headers (safe subset)
request body
response status
response headers
response body
elapsed time
cache indication when observable
error type
```

## HTTP Analysis Matrix

For each endpoint, record:

```text
Method
Safe?
Idempotent?
Request body?
Status
Content-Type
Cache-Control
ETag?
Location?
Set-Cookie?
CORS?
Expected retry behavior?
```

## Request flow document

`WEB_REQUEST_FLOW.md` must explain one HTTPS request conceptually:

```text
URL parsing
   ↓
DNS cache/resolution
   ↓
IP selection
   ↓
TCP or QUIC
   ↓
TLS certificate / protocol negotiation
   ↓
HTTP request
   ↓
CDN/proxy/load balancer possibilities
   ↓
application processing
   ↓
HTTP response
   ↓
browser cache
   ↓
CORS/CSP/cookie rules
   ↓
frontend parsing/rendering
```

## Caching experiment

Implement:
- one `max-age` response
- one `no-store` response
- one ETag validator

Observe:

```text
initial request
fresh reuse
conditional request
304 response
```

## Cookie experiment

Use only dummy local session-like values.

Demonstrate conceptually:

```text
Set-Cookie
   ↓
browser cookie store
   ↓
eligible request
   ↓
Cookie header
```

Document Secure/HttpOnly/SameSite even if the plain local HTTP lab cannot demonstrate all production behavior correctly.

Do not use real authentication credentials.

## Redirect experiment

Implement:

```text
/redirect
  ↓ 302
/status
```

Use both browser DevTools and:

```bash
curl -i http://127.0.0.1:8000/redirect
curl -i -L http://127.0.0.1:8000/redirect
```

Explain why the outputs differ.

## Failure experiment

Produce synthetic:

```text
400
404
409
422
429
500
503
```

For each:
- identify which layer generated it
- state whether retry is sensible
- state what user-facing message should look like
- state what operators should log

## Proxy architecture exercise

Draw this architecture:

```text
Internet
   ↓
CDN/WAF
   ↓
Load Balancer
   ↓
Reverse Proxy
   ├─ /api → Application
   ├─ /static → Static assets
   └─ /auth → Identity service
```

Annotate:

```text
DNS
TLS termination
request ID
cache
rate limit
authentication integration
upstream timeout
health check
```

## Security document

`SECURITY_NOTES.md` must explain:

```text
browser is untrusted
server validation
server authorization
HTTPS is transport security, not app security
query-string leakage
session-id protection
Secure / HttpOnly / SameSite
CORS is not authorization
CORS != CSRF
CSP is defense in depth
HSTS
no secrets in logs
trusted-proxy header boundary
open redirect prevention
cache policy for sensitive data
```

## Troubleshooting runbook

Include decision trees for:

```text
DNS failure
connection refused
TLS certificate error
404
401/403
429
500
502
503
504
CORS error
invalid JSON
wrong Content-Type
stale cached content
redirect loop
```

Example structure:

```text
Browser cannot load page
        ↓
Can DNS resolve?
 ├─ no → resolver/DNS path
 └─ yes
      ↓
Can transport connect?
 ├─ no → IP/port/firewall/service
 └─ yes
      ↓
Does TLS succeed?
 ├─ no → certificate/SNI/chain/time
 └─ yes
      ↓
What HTTP status?
      ↓
route to HTTP/app/proxy runbook
```

## Final success criterion

You should be able to look at a failed browser request and answer:

```text
1. What URL did the client actually request?
2. What origin is involved?
3. Did DNS succeed?
4. Which transport/protocol is used?
5. Did TLS succeed?
6. Which HTTP method was sent?
7. What status came back?
8. Which proxy/application layer likely generated it?
9. Did caching alter behavior?
10. Did browser security policy block JavaScript access?
11. What evidence proves each conclusion?
```


## 7. Recommended Resources

- MDN Web Docs — HTTP overview and guides.
- MDN Web Docs — HTTP methods, status codes, and headers.
- MDN Web Docs — CORS.
- MDN Web Docs — cookies and web security concepts.
- RFC 9110 — HTTP Semantics.
- RFC 9112 — HTTP/1.1.
- RFC 9113 — HTTP/2.
- RFC 9114 — HTTP/3.
- curl official documentation.
- Browser Developer Tools Network documentation.
- Cloudflare Learning Center can be useful for approachable explanations of DNS, TLS, CDN, and HTTP concepts, but verify protocol details against standards/official documentation when precision matters.

## 8. Certification Relevance

Web fundamentals support many later certification and job domains even when not directly tested as a standalone section:

**Cloud**
- Load balancers
- CDNs
- DNS
- TLS certificates
- API gateways
- HTTP health checks

**DevOps**
- Reverse proxies
- CI/CD deployment verification
- Service health endpoints
- Web-server configuration

**Cybersecurity**
- Browser security model
- Cookies/sessions
- HTTP headers
- CORS
- TLS
- Application-security controls
- Web logs

**Backend engineering**
- API methods
- Status codes
- content types
- caching
- authentication/authorization boundaries

## 9. Common Mistakes & Best Practices

- **Mistake:** Saying HTTPS means a website is safe.  
  **Best practice:** HTTPS protects transport; application security is separate.

- **Mistake:** Treating 401 and 403 as identical.  
  **Best practice:** Understand authentication-related vs access-forbidden semantics.

- **Mistake:** Putting secrets in query strings.  
  **Best practice:** Remember URLs are widely logged and exposed.

- **Mistake:** Using GET for destructive state changes.  
  **Best practice:** Follow HTTP method semantics.

- **Mistake:** Treating CORS as server-side authorization.  
  **Best practice:** Enforce authentication and authorization independently.

- **Mistake:** Assuming frontend-hidden buttons enforce permissions.  
  **Best practice:** Server must check permissions for every protected operation.

- **Mistake:** Returning detailed stack traces to users.  
  **Best practice:** Log detailed diagnostics server-side and return safe client messages.

- **Mistake:** Caching sensitive responses without thought.  
  **Best practice:** Select cache controls according to data sensitivity.

- **Mistake:** Ignoring redirects during debugging.  
  **Best practice:** Inspect the full redirect chain.

- **Mistake:** Confusing DNS with HTTP.  
  **Best practice:** DNS resolves names; HTTP carries application requests after connectivity is established.


### Additional Web-Fundamentals Mistakes & Best Practices

- **Mistake:** Treating URL, DNS, TCP, TLS, and HTTP as one layer.
  - **Best practice:** Identify exactly which layer failed.
- **Mistake:** Assuming DNS changes are instantly visible everywhere.
  - **Best practice:** account for TTL/caches.
- **Mistake:** Assuming one IP means one website.
  - **Best practice:** understand SNI and Host-based virtual hosting.
- **Mistake:** Calling every encrypted website safe.
  - **Best practice:** TLS protects transport, not application correctness.
- **Mistake:** Treating idempotent as 'same response every time'.
  - **Best practice:** reason about intended resulting state.
- **Mistake:** Treating `no-cache` as 'do not store'.
  - **Best practice:** distinguish no-cache from no-store.
- **Mistake:** Trusting headers because browsers normally generate them.
  - **Best practice:** only trust identity/proxy headers through controlled infrastructure.
- **Mistake:** Broadening cookie Domain unnecessarily.
  - **Best practice:** scope cookies as narrowly as possible.
- **Mistake:** Treating Path as authorization.
  - **Best practice:** enforce server-side authorization.
- **Mistake:** Treating HttpOnly as full XSS protection.
  - **Best practice:** XSS can still perform actions as the user.
- **Mistake:** Following redirects without inspecting the chain.
  - **Best practice:** inspect every status and Location.
- **Mistake:** Treating a 502 as an application 500.
  - **Best practice:** inspect gateway-to-upstream communication.
- **Mistake:** Treating CORS as authentication or CSRF defense.
  - **Best practice:** separate the security mechanisms.
- **Mistake:** Logging Authorization/Cookie headers.
  - **Best practice:** redact/drop sensitive fields.
- **Mistake:** Clearing every cache during troubleshooting.
  - **Best practice:** identify which cache layer is stale.
- **Mistake:** Retrying every failure immediately.
  - **Best practice:** retry only transient/idempotent-safe scenarios with backoff/jitter.


## 10. Self-Assessment Questions (with short answers)

1. **What is client-server architecture?**  
   A model where clients initiate requests to services provided by servers.

2. **What is the purpose of DNS?**  
   To resolve names and provide other naming records used by networked applications.

3. **What does HTTP define?**  
   Application-level request/response semantics and associated metadata.

4. **What is the default port conventionally associated with HTTP?**  
   TCP 80.

5. **What is the default port conventionally associated with HTTPS?**  
   TCP 443; HTTP/3 commonly uses QUIC over UDP 443.

6. **What does GET normally mean?**  
   Retrieve a representation/resource using safe semantics.

7. **What is POST commonly used for?**  
   Submitting data for processing or creating resources depending on API design.

8. **What does 201 mean?**  
   Created.

9. **What does 401 commonly indicate?**  
   Authentication is required or invalid/missing.

10. **What does 403 mean?**  
    Access is forbidden despite the request being understood.

11. **What does 404 mean?**  
    Resource not found or not disclosed.

12. **What does 500 mean?**  
    Internal server error.

13. **What does `Content-Type` describe?**  
    The media type of the message body.

14. **What does `Accept` describe?**  
    The response media types the client prefers/can accept.

15. **What is a cookie?**  
    Small HTTP state data that can be stored by a user agent and sent with eligible requests.

16. **What is a server-side session?**  
    Application state associated with a client/session identifier, often referenced through a cookie.

17. **What does `HttpOnly` do?**  
    Prevents JavaScript from reading the cookie through normal document cookie APIs.

18. **What does `Secure` do?**  
    Restricts cookie transmission to secure transport contexts.

19. **What is CORS?**  
    A browser/HTTP mechanism for controlled cross-origin response access.

20. **What is HTTPS?**  
    HTTP protected by TLS.

21. **What does a reverse proxy do?**  
    Accepts client traffic and forwards it to backend servers/services.

22. **What does a load balancer do?**  
    Distributes traffic across multiple backend targets.

23. **What does a CDN do?**  
    Delivers/proxies content through distributed edge infrastructure, often reducing latency and origin load.

24. **What does cache validation with ETag enable?**  
    The client/cache can ask whether a stored representation is still current.

25. **Why is frontend validation insufficient for security?**  
    The client is controlled by the user and requests can be altered or sent directly.

## Integrated Request Walkthrough

Assume a user clicks **Refresh Status** on:

```text
https://portal.example.com/dashboard
```

JavaScript executes:

```javascript
const response = await fetch(
    "https://api.example.com/status",
    {
        headers: {
            "Accept": "application/json"
        }
    }
);
```

Walkthrough:

1. The browser identifies a cross-origin request because `portal.example.com` and `api.example.com` are different origins.
2. It resolves `api.example.com` using DNS if necessary.
3. It establishes/reuses network connectivity.
4. Because the URL uses HTTPS, TLS protects the connection.
5. Browser sends an HTTP GET request.
6. Request includes an `Origin` header in the relevant cross-origin context.
7. API checks authentication/authorization as required.
8. API returns JSON with an HTTP status and headers.
9. To allow the portal origin to read the response, the server must provide appropriate CORS headers.
10. Browser applies its CORS rules.
11. If allowed, JavaScript receives access to the response.
12. JavaScript checks `response.ok`.
13. JavaScript parses JSON.
14. JavaScript updates the DOM using safe text/element operations.
15. Browser renders the updated status.

This one sequence connects nearly the entire Phase 3 curriculum.


## Extended Self-Assessment

### Extended Q1. What layers usually exist below HTTP?

**Answer:** DNS for naming, IP for routing, TCP/QUIC transport, and TLS for HTTPS.

### Extended Q2. Is a URL fragment sent like the query to the server?

**Answer:** Normally no; it is client-side fragment state.

### Extended Q3. What is percent-encoding?

**Answer:** Representing URL bytes as %HH sequences.

### Extended Q4. What is an origin?

**Answer:** Broadly scheme + host + port.

### Extended Q5. Recursive vs authoritative DNS?

**Answer:** Recursive resolves on behalf of clients; authoritative answers for zones it serves.

### Extended Q6. Why do DNS changes propagate gradually?

**Answer:** Caches retain answers until TTL/policy expiry.

### Extended Q7. What does Host enable?

**Answer:** HTTP virtual hosting/routing for multiple names on one address.

### Extended Q8. What does SNI enable?

**Answer:** TLS hostname indication so a shared IP can present the right certificate.

### Extended Q9. What is ALPN?

**Answer:** TLS negotiation mechanism for application protocols such as h2/http1.1.

### Extended Q10. What must certificate name validation match?

**Answer:** The requested hostname must be covered by certificate identity rules.

### Extended Q11. HTTP semantics vs framing?

**Answer:** Methods/status/headers are semantics; versions differ in wire framing.

### Extended Q12. Safe method meaning?

**Answer:** Client requests read-only semantics.

### Extended Q13. Idempotent meaning?

**Answer:** Repeated request has same intended effect on server state.

### Extended Q14. GET safe/idempotent?

**Answer:** Yes by HTTP semantics.

### Extended Q15. POST generally idempotent?

**Answer:** No.

### Extended Q16. PUT generally idempotent?

**Answer:** Yes.

### Extended Q17. 201 means?

**Answer:** Resource created.

### Extended Q18. 204 means?

**Answer:** Success with no representation body.

### Extended Q19. 401 vs 403?

**Answer:** Authentication missing/invalid vs authenticated/understood but forbidden.

### Extended Q20. 409 means?

**Answer:** Conflict with current resource state.

### Extended Q21. 422 means?

**Answer:** Syntax/content parsed but semantic validation failed.

### Extended Q22. 429 means?

**Answer:** Too many requests/rate limiting.

### Extended Q23. 502 vs 504?

**Answer:** Bad upstream response vs upstream timeout at a gateway.

### Extended Q24. What does Content-Type describe?

**Answer:** Media type of message body.

### Extended Q25. What does Accept describe?

**Answer:** Response media types preferred by the client.

### Extended Q26. What does Vary do?

**Answer:** Tells caches which request headers affect representation selection.

### Extended Q27. no-store vs no-cache?

**Answer:** No-store forbids storage; no-cache permits storage but requires validation before reuse.

### Extended Q28. What is an ETag?

**Answer:** Representation validator/version identifier used for conditional requests.

### Extended Q29. What is a reverse proxy?

**Answer:** Server-side intermediary forwarding client requests to upstream services.

### Extended Q30. What is a forward proxy?

**Answer:** Client-side intermediary used to reach external services.

### Extended Q31. What is a CDN hit?

**Answer:** Edge serves from cache without fetching origin for that request.

### Extended Q32. Why protect origin behind a CDN/WAF?

**Answer:** Avoid bypassing front-door controls where architecture expects them.

### Extended Q33. What is Same-Origin Policy?

**Answer:** Browser isolation restricting cross-origin data access.

### Extended Q34. What is CORS?

**Answer:** Browser/HTTP mechanism allowing controlled cross-origin response access.

### Extended Q35. What is a preflight?

**Answer:** Browser OPTIONS permission check for certain cross-origin requests.

### Extended Q36. CORS vs CSRF?

**Answer:** Response-read policy vs unwanted authenticated state-changing request threat.

### Extended Q37. What does HttpOnly do?

**Answer:** Prevents normal JS access to a cookie.

### Extended Q38. What does Secure do?

**Answer:** Restricts cookie transmission to secure contexts.

### Extended Q39. What does SameSite influence?

**Answer:** Cross-site cookie sending behavior.

### Extended Q40. Why rotate session IDs after login?

**Answer:** Reduce fixation-related risk and separate trust state.

### Extended Q41. What is HSTS?

**Answer:** Browser policy requiring HTTPS for a host after policy is learned.

### Extended Q42. What does CSP do?

**Answer:** Restricts classes of browser content loading/execution.

### Extended Q43. Why are forwarded headers dangerous?

**Answer:** If trusted from arbitrary clients they can spoof addresses/protocol/identity context.

### Extended Q44. What is TTFB?

**Answer:** Time until first response byte; includes network and server-side delays.

### Extended Q45. What is an idempotency key?

**Answer:** Application key used to recognize repeated logical non-idempotent operations.

### Extended Q46. Why use correlation IDs?

**Answer:** Trace one request across multiple services/logs.

### Extended Q47. Why not log Authorization/Cookie?

**Answer:** They can contain credentials/session secrets.

### Extended Q48. What is `curl -L`?

**Answer:** Follow HTTP redirects.

### Extended Q49. What does `curl -w` help measure?

**Answer:** Timing metrics such as DNS/connect/start-transfer/total.

### Extended Q50. What should you troubleshoot first when hostname cannot resolve?

**Answer:** DNS/resolver layer, not HTTP.

### Extended Q51. What does a browser CORS error prove?

**Answer:** Browser access policy failed; network/server response may still have occurred.

### Extended Q52. What can cause JSON parse errors besides bad API code?

**Answer:** HTML error/login/proxy pages returned with wrong content type or route.

### Extended Q53. Why can content stay stale?

**Answer:** Caches/service workers/CDN/proxy/app or old DNS/backend path.

### Extended Q54. What is service-worker request interception?

**Answer:** A service worker can answer/modify fetch flow before network.

### Extended Q55. HTTP vs WebSocket?

**Answer:** Discrete request/response vs long-lived bidirectional channel.

### Extended Q56. SSE direction?

**Answer:** Server-to-browser one-way event stream.

### Extended Q57. REST is simply JSON?

**Answer:** No; it is an architectural style using resource/representation/uniform-interface ideas.

### Extended Q58. Why paginate?

**Answer:** Bound response size/latency and handle large collections.

### Extended Q59. What does If-Match support?

**Answer:** Conditional update/optimistic concurrency based on a validator.

### Extended Q60. Final debugging rule?

**Answer:** Identify the lowest failing layer and prove each step with observable evidence.


## Completion Checklist

- [ ] I can explain what happens after entering a URL.
- [ ] I can decompose a URL accurately.
- [ ] I can explain DNS at a foundation level.
- [ ] I can read basic HTTP request and response messages.
- [ ] I understand common methods and status codes.
- [ ] I can explain cookies and sessions.
- [ ] I understand caching and redirects.
- [ ] I can explain HTTPS/TLS at a foundation level.
- [ ] I can explain same-origin policy and CORS at a foundation level.
- [ ] I can inspect requests using curl and browser Developer Tools.
- [ ] I completed all labs and the mini project.


## Enhanced Completion Checklist

- [ ] I can decompose URLs and reason about origins.
- [ ] I understand DNS resolution, record types, recursive/authoritative roles, TTL, and caching.
- [ ] I understand how TCP and QUIC relate to HTTP versions.
- [ ] I can explain TLS handshake, SNI, ALPN, certificate name validation, and trust chain at foundation level.
- [ ] I can read HTTP requests/responses and distinguish semantics from wire framing.
- [ ] I understand safe/idempotent/cacheable method properties.
- [ ] I can choose and interpret major 2xx/3xx/4xx/5xx status codes.
- [ ] I understand Content-Type, Accept, Content-Encoding, Location, Vary, and other important headers.
- [ ] I understand cookies, server-side sessions, scope, Secure, HttpOnly, SameSite, expiry, and rotation.
- [ ] I can explain redirect behavior and open-redirect risk.
- [ ] I understand freshness, no-store/no-cache, ETag, 304, Last-Modified, Vary, and asset hashing.
- [ ] I understand forward/reverse proxies, load balancers, health checks, stickiness, CDNs, and trusted forwarded-header boundaries.
- [ ] I understand SOP, CORS, preflight, credentialed CORS, CSRF distinction, CSP, HSTS, and security-header concepts.
- [ ] I understand authentication vs authorization, bearer/basic auth awareness, rate limits, and idempotency-key concepts.
- [ ] I understand timeout/retry/backoff/jitter/correlation-ID concepts.
- [ ] I can inspect requests with curl, browser Network tools, and basic TLS tools.
- [ ] I can troubleshoot DNS, TLS, 404, 502/504, CORS, wrong content type, redirects, and stale caches systematically.
- [ ] I understand WebSocket/SSE/service-worker request-path concepts.
- [ ] I understand REST, API versioning, pagination, range, and optimistic-concurrency awareness.
- [ ] I completed the enhanced labs.
- [ ] I completed the expanded Web Request Observatory.
