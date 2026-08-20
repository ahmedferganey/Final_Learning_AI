# 24. Linux Web Server Administration

> Phase 5 — Linux System Administration

This course moves from general Linux administration into the operation of production-style web infrastructure.

The objective is not only to install Apache or NGINX. A web server administrator must understand the entire request path:

```text
Client
  ↓
DNS
  ↓
IP routing
  ↓
TCP
  ↓
TLS
  ↓
Host firewall
  ↓
Web server / reverse proxy
  ↓
Application or static content
  ↓
Filesystem / upstream service
```

On current Red Hat Enterprise Linux 10, Red Hat documents Apache HTTP Server, NGINX, TLS, NGINX reverse proxy and HTTP load balancing, and Squid caching proxy use cases. This module concentrates mainly on Apache and NGINX because those concepts transfer directly into DevOps, containers, Kubernetes ingress, cloud load balancing, application security, and SRE work.

---

## 1. Topic Title

**Linux Web Server Administration**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain web-server, application-server, reverse-proxy, load-balancer, and forward/caching-proxy roles.
- Install, configure, validate, start, secure, monitor, and troubleshoot Apache HTTP Server.
- Build name-based virtual hosts with independent document roots and logs.
- Coordinate Apache configuration with Linux permissions, SELinux, firewalld, DNS, and TCP sockets.
- Configure HTTPS/TLS using certificates and private keys.
- Install and configure NGINX as a static-content server.
- Configure NGINX server blocks, TLS, reverse proxying, and basic HTTP load balancing.
- Explain forwarding headers, upstream routing, timeouts, 502 vs 504 failures, and proxy trust boundaries.
- Read access/error logs and investigate common HTTP status codes.
- Apply least privilege, patching, configuration validation, backup, monitoring, and safe change-management practices.
- Build and troubleshoot a multi-node web tier.

---

## 3. Prerequisites

Required:

- 20. Linux Essentials
- 21. Red Hat System Administration I
- 22. Red Hat System Administration II
- Phase 3 — Web Fundamentals
- Phase 4 — Networking

You should already understand:

```text
DNS
IPv4/IPv6
TCP/80
TCP/443
HTTP methods
HTTP status codes
systemd
DNF/RPM
SELinux
firewalld
Linux ownership/permissions
curl
dig
ss
journalctl
```

Recommended lab:

```text
proxy01.lab.example  192.168.56.20
web01.lab.example    192.168.56.21
web02.lab.example    192.168.56.22
client.lab.example   192.168.56.30
```

Two VMs are sufficient for the first labs. Three or four VMs make reverse-proxy and load-balancing behavior much easier to understand.

---

## 4. Core Concepts Explanation

# Part 1 — Web Infrastructure Architecture

### 1. Web Server

A web server receives HTTP requests and returns HTTP responses.

Typical software:

```text
Apache HTTP Server -> httpd
NGINX              -> nginx
```

Static-content flow:

```text
Client
  |
  | GET /index.html
  v
Web Server
  |
  | read
  v
/var/www/.../index.html
  |
  v
HTTP 200 + body
```

A web server does not have to read a local file. It can also proxy the request to another service.

### 2. Application Server

An application server executes application logic.

Examples:

```text
FastAPI / Uvicorn / Gunicorn
Node.js
Java / Spring
PHP-FPM
.NET
```

Common architecture:

```text
Internet
   ↓
NGINX / Apache
   ↓
Application server
127.0.0.1:8000
   ↓
Database / API
```

The reverse proxy can handle TLS, public-facing sockets, static files, request routing, and logging while the application focuses on business logic.

### 3. Reverse Proxy

A reverse proxy represents backend servers to clients.

```text
Client
  ↓
NGINX
  ↓
Backend application
```

Common purposes:

- TLS termination
- virtual-host routing
- path routing
- hiding backend addresses
- load balancing
- standardized logging
- connection buffering
- centralized security controls

### 4. Forward Proxy vs Reverse Proxy

```text
Forward proxy:
Client -> Proxy -> Internet

Reverse proxy:
Internet -> Proxy -> Servers
```

The forward proxy represents the client side.

The reverse proxy represents the server side.

### 5. Load Balancer

A load balancer distributes traffic across multiple backend servers.

```text
                    +--> web01
Client -> NGINX ----+
                    +--> web02
```

Possible load-balancing layers:

```text
Layer 4 -> TCP/UDP
Layer 7 -> HTTP-aware
```

NGINX can act as an HTTP reverse proxy and load balancer.

### 6. Caching Proxy

A caching proxy saves reusable responses.

Benefits:

- reduced latency
- reduced upstream traffic
- reduced origin load

Risks:

- serving stale data
- caching private data
- incorrect cache keys
- inconsistent authentication/session behavior

Squid is a common Linux caching proxy.

---

# Part 2 — HTTP from the Administrator's View

### 7. URL to Request

Example:

```text
https://app.example.com/orders?id=42
```

Breakdown:

```text
scheme = https
host   = app.example.com
path   = /orders
query  = id=42
```

Simplified request path:

```text
DNS
 ↓
IP address
 ↓
TCP connection
 ↓
TLS handshake
 ↓
HTTP request
 ↓
web-server routing
 ↓
content or proxy
```

### 8. Request Example

```http
GET /health HTTP/1.1
Host: app.example.com
User-Agent: curl/8.x
Accept: */*
```

### 9. Response Example

```http
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 3

OK
```

### 10. Important Status Codes

```text
200  OK
201  Created
301  Permanent redirect
302  Temporary redirect
307  Temporary redirect preserving method semantics
308  Permanent redirect preserving method semantics
400  Bad request
401  Authentication required/failed
403  Forbidden
404  Not found
408  Request timeout
413  Request body too large
429  Too many requests
500  Internal server error
502  Bad gateway
503  Service unavailable
504  Gateway timeout
```

A reverse-proxy administrator must understand the difference between 502 and 504.

**502 Bad Gateway**

The proxy could not use the upstream response successfully. Possible examples:

- connection refused
- upstream closed unexpectedly
- wrong upstream protocol
- invalid upstream response

**504 Gateway Timeout**

The proxy waited too long for the upstream.

Do not guess. Read the proxy error log and test the upstream directly.

---

# Part 3 — Apache HTTP Server Installation

### 11. Install Apache

```bash
sudo dnf install httpd

rpm -q httpd

sudo systemctl enable --now httpd

systemctl status httpd
ss -tlnp | grep ':80'
```

These checks answer separate questions:

```text
rpm -q              package installed?
systemctl status     service running?
ss                   socket listening?
```

### 12. RHEL Apache Configuration Layout

Important locations:

```text
/etc/httpd/conf/httpd.conf
/etc/httpd/conf.d/
/etc/httpd/conf.modules.d/
```

Conceptual layout:

```text
/etc/httpd/
├── conf/
│   └── httpd.conf
├── conf.d/
└── conf.modules.d/
```

Use focused configuration files under `conf.d` where appropriate instead of turning the primary configuration into an unstructured file.

### 13. Validate Before Restart

```bash
sudo apachectl configtest
```

Expected successful result:

```text
Syntax OK
```

Then apply:

```bash
sudo systemctl reload httpd
```

Verify:

```bash
systemctl status httpd
journalctl -u httpd --since "10 minutes ago"
```

The operating pattern is:

```text
edit
 ↓
syntax validation
 ↓
reload/restart
 ↓
runtime verification
 ↓
log verification
```

---

# Part 4 — Apache Static Content

### 14. Default Static Page

```bash
echo '<h1>web01</h1>' | sudo tee /var/www/html/index.html

curl http://127.0.0.1/
curl -I http://127.0.0.1/
```

### 15. Understand File Access

Inspect:

```bash
namei -l /var/www/html/index.html
ls -ld /var /var/www /var/www/html
ls -l /var/www/html/index.html
ls -Z /var/www/html/index.html
```

Apache needs:

- Unix permission to traverse directories
- Unix permission to read the file
- SELinux policy to permit the access

Do not solve this using:

```text
chmod 777
```

### 16. Custom Document Root

Create:

```bash
sudo mkdir -p /srv/example
echo '<h1>Example Site</h1>' | sudo tee /srv/example/index.html
```

Apply persistent SELinux context policy:

```bash
sudo semanage fcontext \
  -a \
  -t httpd_sys_content_t \
  '/srv/example(/.*)?'

sudo restorecon -Rv /srv/example
```

Verify:

```bash
ls -Zd /srv/example
ls -Z /srv/example/index.html
```

---

# Part 5 — Apache Virtual Hosts

### 17. Name-based Hosting

One IP can serve multiple domain names.

```text
192.168.56.21
    |
    +-- www.alpha.lab
    |
    +-- www.beta.lab
```

HTTP requests contain a `Host` header.

Apache uses this to select the matching name-based virtual host.

### 18. Alpha Virtual Host

Example `/etc/httpd/conf.d/alpha.conf`:

```apache
<VirtualHost *:80>
    ServerName www.alpha.lab

    DocumentRoot /srv/www/alpha

    ErrorLog  /var/log/httpd/alpha-error.log
    CustomLog /var/log/httpd/alpha-access.log combined

    <Directory /srv/www/alpha>
        Require all granted
        AllowOverride None
        Options -Indexes
    </Directory>
</VirtualHost>
```

### 19. Beta Virtual Host

```apache
<VirtualHost *:80>
    ServerName www.beta.lab

    DocumentRoot /srv/www/beta

    ErrorLog  /var/log/httpd/beta-error.log
    CustomLog /var/log/httpd/beta-access.log combined

    <Directory /srv/www/beta>
        Require all granted
        AllowOverride None
        Options -Indexes
    </Directory>
</VirtualHost>
```

### 20. Prepare Content

```bash
sudo mkdir -p /srv/www/{alpha,beta}

echo '<h1>Alpha</h1>' | sudo tee /srv/www/alpha/index.html
echo '<h1>Beta</h1>'  | sudo tee /srv/www/beta/index.html

sudo semanage fcontext \
  -a \
  -t httpd_sys_content_t \
  '/srv/www(/.*)?'

sudo restorecon -Rv /srv/www
```

### 21. Lab Name Resolution

For a simple lab:

```text
192.168.56.21 www.alpha.lab www.beta.lab
```

In real infrastructure, use DNS records.

### 22. Test Virtual-host Selection

```bash
curl -H 'Host: www.alpha.lab' http://192.168.56.21/

curl -H 'Host: www.beta.lab' http://192.168.56.21/
```

Validate before applying:

```bash
sudo apachectl configtest
sudo systemctl reload httpd
```

---

# Part 6 — Apache Directory Access and Modules

### 23. Directory Blocks

```apache
<Directory /srv/www/alpha>
    Require all granted
    AllowOverride None
    Options -Indexes
</Directory>
```

`Options -Indexes` prevents directory-list rendering when no index file exists.

Directory listing should be explicitly justified, not left enabled accidentally.

### 24. Apache Modules

List:

```bash
httpd -M | sort
```

Selected examples:

```bash
httpd -M | grep ssl
httpd -M | grep proxy
httpd -M | grep headers
```

Modules add capabilities such as:

- TLS
- reverse proxying
- authentication
- response headers
- compression

Minimize unused functionality.

### 25. `.htaccess`

`.htaccess` allows configuration inside content directories when `AllowOverride` permits it.

Central configuration is normally easier to:

- audit
- version control
- validate
- troubleshoot

Use `.htaccess` only when delegated per-directory configuration is a real requirement.

---

# Part 7 — Apache Logging

### 26. Default Logs

```bash
sudo tail -f /var/log/httpd/access_log
sudo tail -f /var/log/httpd/error_log
```

Also:

```bash
journalctl -u httpd
```

### 27. Access Log Interpretation

Example:

```text
192.168.56.30 - - [17/Aug/2026:12:00:00 +0300] \
"GET /index.html HTTP/1.1" 200 1234 "-" "curl/8.x"
```

Possible fields:

- client IP
- timestamp
- request method/path/version
- status
- bytes
- referrer
- user agent

A user-agent string is client-provided data and is not trusted identity.

### 28. Simple Status Analysis

```bash
awk '{print $9}' /var/log/httpd/access_log \
  | sort \
  | uniq -c \
  | sort -nr
```

This can show counts such as:

```text
120 200
 15 404
  3 500
```

---

# Part 8 — firewalld

### 29. Permit HTTP and HTTPS

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

Verify:

```bash
sudo firewall-cmd --list-services
```

### 30. Layered Verification

```bash
systemctl is-active httpd
ss -tlnp | grep -E ':80|:443'
sudo firewall-cmd --list-all
curl -I http://127.0.0.1/
```

Remember:

```text
firewall open
≠
service listening

service listening
≠
remote route exists
```

---

# Part 9 — SELinux and Apache/NGINX

### 31. Inspect Context

```bash
ls -Zd /var/www/html
ls -Z /var/www/html
```

### 32. Correct Persistent Label

```bash
sudo semanage fcontext \
  -a \
  -t httpd_sys_content_t \
  '/srv/www(/.*)?'

sudo restorecon -Rv /srv/www
```

### 33. Diagnose Denials

```bash
sudo ausearch -m AVC -ts recent
journalctl | grep -i avc
```

Troubleshooting order:

```text
Unix permissions
 ↓
SELinux label
 ↓
SELinux Boolean/policy
 ↓
application config
```

Do not start by disabling SELinux.

### 34. Reverse Proxy Network Connections

Inspect:

```bash
getsebool httpd_can_network_connect
```

If the web-server SELinux domain must connect to a backend network service, a supported SELinux Boolean/policy adjustment may be necessary.

Do not enable Booleans without understanding what capability they grant.

---

# Part 10 — TLS and HTTPS

### 35. Why TLS Exists

TLS provides:

- confidentiality
- integrity
- certificate-based authentication

HTTPS:

```text
HTTP
inside
TLS
```

TLS does **not** fix insecure application authorization, injection, XSS, or other application vulnerabilities.

### 36. Certificate vs Private Key

```text
Private key:
secret

Certificate:
public information
public key
identity names
issuer/signature information
```

Protect the private key.

### 37. Lab Certificate

```bash
sudo openssl req \
  -x509 \
  -newkey rsa:3072 \
  -nodes \
  -days 30 \
  -keyout /etc/pki/tls/private/alpha.key \
  -out /etc/pki/tls/certs/alpha.crt \
  -subj '/CN=www.alpha.lab'
```

This is appropriate for a controlled lab.

Production public services should use an appropriate trusted certificate-authority workflow.

### 38. Apache HTTPS Virtual Host

```apache
<VirtualHost *:443>
    ServerName www.alpha.lab

    DocumentRoot /srv/www/alpha

    SSLEngine on
    SSLCertificateFile /etc/pki/tls/certs/alpha.crt
    SSLCertificateKeyFile /etc/pki/tls/private/alpha.key

    <Directory /srv/www/alpha>
        Require all granted
    </Directory>
</VirtualHost>
```

Validate:

```bash
sudo apachectl configtest
sudo systemctl reload httpd
```

### 39. TLS Verification

```bash
openssl s_client \
  -connect www.alpha.lab:443 \
  -servername www.alpha.lab
```

Lab-only test:

```bash
curl -vk https://www.alpha.lab/
```

`-k` disables normal TLS certificate verification.

Do not make certificate-verification bypass a production habit.

### 40. HTTP to HTTPS Redirect

```apache
<VirtualHost *:80>
    ServerName www.alpha.lab
    Redirect permanent / https://www.alpha.lab/
</VirtualHost>
```

Test:

```bash
curl -I http://www.alpha.lab/
```

---

# Part 11 — NGINX Installation

### 41. Install

```bash
sudo dnf install nginx
sudo systemctl enable --now nginx
```

Verify:

```bash
rpm -q nginx
systemctl status nginx
ss -tlnp | grep ':80'
```

### 42. Important Locations

Typical RHEL locations include:

```text
/etc/nginx/nginx.conf
/etc/nginx/conf.d/
/usr/share/nginx/html/
```

### 43. Configuration Test

```bash
sudo nginx -t
```

Then:

```bash
sudo systemctl reload nginx
journalctl -u nginx --since "10 minutes ago"
```

---

# Part 12 — NGINX Server Blocks

### 44. Static Site

```nginx
server {
    listen 80;
    server_name www.alpha.lab;

    root /srv/www/alpha;
    index index.html;

    access_log /var/log/nginx/alpha-access.log;
    error_log  /var/log/nginx/alpha-error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Validate:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Test:

```bash
curl -H 'Host: www.alpha.lab' http://192.168.56.20/
```

---

# Part 13 — NGINX Reverse Proxy

### 45. Local Upstream

Assume an application listens on:

```text
127.0.0.1:8000
```

NGINX:

```nginx
server {
    listen 80;
    server_name api.lab.example;

    location / {
        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 46. Request Flow

```text
Client
192.168.56.30
      |
      v
NGINX
192.168.56.20:80
      |
      v
Application
127.0.0.1:8000
```

### 47. Forwarded Headers

Common:

```text
Host
X-Real-IP
X-Forwarded-For
X-Forwarded-Proto
```

Trust-boundary warning:

A backend should trust forwarding headers only from known trusted proxies. If clients can directly reach the backend and the app blindly trusts those headers, clients may forge them.

### 48. Diagnose Upstream

```bash
curl -v http://127.0.0.1:8000/health

ss -tlnp | grep ':8000'

sudo nginx -t

journalctl -u nginx

tail -f /var/log/nginx/error.log
```

For 502, ask:

```text
Is upstream running?
Correct IP?
Correct port?
Correct protocol?
DNS resolves?
SELinux permits proxy connect?
Remote firewall permits it?
```

---

# Part 14 — NGINX Load Balancing

### 49. Upstream Group

```nginx
upstream app_backend {
    server 192.168.56.21:8080;
    server 192.168.56.22:8080;
}

server {
    listen 80;
    server_name app.lab.example;

    location / {
        proxy_pass http://app_backend;

        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 50. Backend Test

Make web01 return:

```text
response from web01
```

Make web02 return:

```text
response from web02
```

Then:

```bash
for i in {1..10}; do
    curl -s http://app.lab.example/
done
```

Observe backend distribution.

### 51. Weighted Upstream

```nginx
upstream app_backend {
    server 192.168.56.21:8080 weight=3;
    server 192.168.56.22:8080 weight=1;
}
```

This expresses relative distribution preference.

It is not a guarantee that every four sequential requests produce an exact 3:1 visible pattern.

---

# Part 15 — NGINX HTTPS Reverse Proxy

### 52. TLS Termination

```nginx
server {
    listen 443 ssl;
    server_name app.lab.example;

    ssl_certificate     /etc/pki/tls/certs/app.crt;
    ssl_certificate_key /etc/pki/tls/private/app.key;

    location / {
        proxy_pass http://app_backend;

        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}
```

Flow:

```text
Client
  |
 HTTPS
  |
NGINX
  |
HTTP on private network
  |
Backend
```

Whether the proxy-to-backend connection should also use TLS depends on trust boundaries and architecture.

---

# Part 16 — Apache Reverse Proxy

### 53. Apache Proxy Example

Required proxy modules must be loaded.

Inspect:

```bash
httpd -M | grep proxy
```

Example:

```apache
<VirtualHost *:80>
    ServerName api.lab.example

    ProxyPreserveHost On

    ProxyPass        / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

Validate:

```bash
sudo apachectl configtest
```

Apache and NGINX can both serve as reverse proxies. Choose based on architecture, support standards, modules, operational skill, and measured requirements.

---

# Part 17 — Authentication Fundamentals

### 54. Basic Authentication

Basic authentication is only encoding, not encryption.

Use it only over TLS.

Lab password file:

```bash
sudo dnf install httpd-tools
sudo htpasswd -c /etc/httpd/.htpasswd labuser
```

Apache example:

```apache
<Location "/private">
    AuthType Basic
    AuthName "Private Lab"
    AuthUserFile /etc/httpd/.htpasswd
    Require valid-user
</Location>
```

Test:

```bash
curl -I https://www.alpha.lab/private/
curl -u labuser https://www.alpha.lab/private/
```

Enterprise identity may instead use:

- Kerberos/GSSAPI
- OIDC
- SAML through an identity-aware proxy/application
- LDAP-integrated systems

Authentication architecture should be selected deliberately.

---

# Part 18 — Processes, Sockets, and Bind Addresses

### 55. Listening Addresses

```bash
ss -tlnp | grep -E ':80|:443|:8000'
```

Examples:

```text
0.0.0.0:80
```

means all IPv4 local interfaces.

```text
127.0.0.1:8000
```

means loopback only.

A backend bound to loopback can be reached by a local proxy but not directly from the network.

### 56. Port Collision

Only one process can normally bind a specific IP/port tuple at a time.

If Apache already owns:

```text
0.0.0.0:80
```

NGINX cannot also bind that same tuple.

Check:

```bash
sudo ss -tlnp | grep ':80'
```

---

# Part 19 — Timeouts and Limits

### 57. Proxy Timeout

Too short:

```text
valid slow requests fail
```

Too long:

```text
dead/slow upstreams consume resources longer
```

Use measured application behavior.

### 58. Upload/Request Size

Web servers can restrict request-body size.

Coordinate:

```text
web-server limit
application limit
API contract
client expectation
```

Otherwise one layer might reject a request unexpectedly.

---

# Part 20 — Performance Fundamentals

### 59. Static vs Dynamic Content

Common split:

```text
NGINX
├── /static/ -> files
└── /api/    -> upstream application
```

### 60. Keep-alive

Persistent HTTP connections reduce repeated setup overhead.

Monitor:

- connection count
- worker/thread usage
- idle timeout
- upstream connection behavior

### 61. Compression

Compression can reduce bandwidth for text-like content.

Do not blindly compress everything:

- JPEG/MP4/ZIP are already compressed
- CPU cost matters
- sensitive compression scenarios may have security implications

### 62. Authorized Load Testing

Only load-test systems you own or are explicitly authorized to test.

Small local lab example if ApacheBench is installed:

```bash
ab -n 20 -c 2 http://127.0.0.1/
```

Start small.

Do not run high concurrency against shared or production environments without approval.

---

# Part 21 — Security Hardening

### 63. Patch Management

```bash
sudo dnf check-update
dnf info httpd
dnf info nginx
```

Supported and patched software is the foundation.

### 64. Minimize Attack Surface

Inspect:

```bash
ss -tulpen
systemctl --type=service --state=running
sudo firewall-cmd --list-all
```

Disable services/features you do not require.

### 65. Private-key Protection

```bash
sudo chown root:root /etc/pki/tls/private/app.key
sudo chmod 600 /etc/pki/tls/private/app.key
```

Never commit private keys to ordinary application repositories.

### 66. Writable Areas

Separate:

```text
configuration
read-only application/static content
uploads
cache/temp
logs
private secrets
```

Do not make the complete web tree writable by the web process.

### 67. Security Headers

Common browser-oriented controls:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
Referrer-Policy
```

Do not copy a complex CSP from another application. A correct CSP must reflect the actual application's script, style, frame, image, font, and API requirements.

---

# Part 22 — Troubleshooting Methodology

### 68. Troubleshoot by Layer

```text
1. process
2. socket
3. SELinux/firewall
4. local HTTP
5. DNS/routing
6. remote HTTP
7. proxy upstream
8. application
```

### 69. Apache Fails to Start

```bash
sudo apachectl configtest

systemctl status httpd

journalctl -u httpd -b

ss -tlnp | grep -E ':80|:443'
```

Common causes:

- syntax error
- duplicate listener
- wrong certificate/key path
- missing module
- permission/SELinux issue

### 70. NGINX Fails to Start

```bash
sudo nginx -t

systemctl status nginx

journalctl -u nginx -b
```

### 71. Local Works, Remote Fails

```bash
curl -I http://127.0.0.1/

ip -br address
ip route

sudo firewall-cmd --list-all
```

Likely areas:

- service bound to loopback only
- host firewall
- upstream network firewall
- wrong route
- wrong DNS record

### 72. DNS Failure

```bash
dig app.lab.example
getent hosts app.lab.example
```

Never rewrite web-server configuration to solve a DNS problem.

### 73. TLS Failure

```bash
openssl s_client \
  -connect app.lab.example:443 \
  -servername app.lab.example \
  -showcerts
```

Inspect:

- certificate names
- validity dates
- chain
- issuer
- server-name selection
- client trust

### 74. Proxy 502

Test upstream directly:

```bash
curl -v http://192.168.56.21:8080/health
```

Then proxy logs.

### 75. Proxy 504

Investigate:

- slow application
- network delay
- overloaded backend
- deadlock
- timeout too aggressive
- external dependency

---

# Part 23 — Change Management and Configuration Backup

### 76. Backup Before Major Changes

```bash
sudo cp -a /etc/httpd \
  /root/httpd-config-backup-$(date +%F)

sudo cp -a /etc/nginx \
  /root/nginx-config-backup-$(date +%F)
```

For production, prefer:

```text
Git / configuration management
review
automated syntax validation
controlled deployment
```

### 77. Change Workflow

```text
requirement
 ↓
review current state
 ↓
backup/version control
 ↓
edit
 ↓
syntax test
 ↓
reload
 ↓
local test
 ↓
remote test
 ↓
logs/metrics
 ↓
document
```

---

# Part 24 — Apache vs NGINX

A simplified comparison:

```text
Apache
- mature modular HTTP server
- rich authentication/module ecosystem
- reverse proxy capability
- per-directory configuration available

NGINX
- event-driven server
- strong reverse-proxy use
- HTTP load balancing
- common cloud/container edge component
```

Avoid simplistic conclusions such as:

```text
NGINX is always faster
Apache is obsolete
```

Actual choice depends on:

- feature requirements
- support standards
- operations knowledge
- application architecture
- deployment platform
- benchmarked workload

---


# Enhanced Deep-Study Layer — Production Linux Web Infrastructure

The original course content is preserved below. This enhanced layer adds deeper web-server internals, request-routing mechanics, TLS reasoning, Apache and NGINX configuration behavior, reverse-proxy trust boundaries, observability, performance, security hardening, troubleshooting decision trees, and multi-node labs.

The operational model throughout this course is:

```text
Client
  ↓
Name resolution
  ↓
Route
  ↓
TCP connection
  ↓
TLS / SNI / certificate validation
  ↓
HTTP parsing
  ↓
Virtual host / server block selection
  ↓
Location / directory / route selection
  ↓
Static file OR upstream application
  ↓
Response generation
  ↓
Logging / metrics
```

A production incident should be debugged in the same order. Do not edit Apache or NGINX configuration before proving that the failing layer actually belongs to the web server.

---

## Enhanced Deep Dive 1 — Web Server vs Reverse Proxy vs Application Server

These roles are commonly combined, but conceptually they are different.

```text
Web server
→ terminates HTTP and can serve files

Reverse proxy
→ receives requests on behalf of backend services

Application server
→ executes business logic

Load balancer
→ distributes traffic among multiple backends
```

Example:

```text
Browser
   ↓ HTTPS
NGINX
   ├── /static/* → local files
   └── /api/*    → FastAPI/Uvicorn
                       ↓
                    PostgreSQL
```

Why separate roles?

```text
TLS policy can be centralized
backend can bind to loopback/private network
static files can avoid application runtime
logging/routing becomes standardized
```

---

## Enhanced Deep Dive 2 — Complete HTTP Request Path

A user entering:

```text
https://app.example.com/orders/42
```

does not immediately contact the application.

```text
URL
 ↓
DNS lookup
 ↓
IP route lookup
 ↓
TCP three-way handshake
 ↓
TLS handshake
 ↓
HTTP request
 ↓
virtual host selection
 ↓
path/location routing
 ↓
static content or upstream
 ↓
response
```

Useful tools at each layer:

```text
DNS       → dig, getent
route     → ip route get
TCP       → ss, nc/ncat in authorized lab
TLS       → openssl s_client
HTTP      → curl -v
process   → systemctl, ps
logs      → journalctl, access/error logs
```

---

## Enhanced Deep Dive 3 — HTTP Message Anatomy

Request:

```http
GET /api/health?verbose=1 HTTP/1.1
Host: api.lab.example
User-Agent: curl/8.x
Accept: application/json
Connection: keep-alive
```

Structure:

```text
request line
headers
blank line
optional request body
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 15

{"status":"ok"}
```

The administrator must distinguish:

```text
transport succeeded
HTTP parser succeeded
application returned an error
```

A TCP connection can be successful while HTTP returns 500.

---

## Enhanced Deep Dive 4 — HTTP Methods and Administrative Meaning

Common methods:

```text
GET      retrieve
HEAD     headers without response body
POST     submit/create/action
PUT      replace/update
PATCH    partial update
DELETE   delete
OPTIONS  capability/CORS-related discovery
```

Test safely:

```bash
curl -I http://127.0.0.1/
curl -X OPTIONS -i http://127.0.0.1/
```

A web administrator should know which methods the application requires.

Security controls that globally disable methods can break applications.

---

## Enhanced Deep Dive 5 — HTTP Status Code Families

```text
1xx informational
2xx success
3xx redirect
4xx client/request/auth/access issue
5xx server/proxy/application issue
```

Important troubleshooting map:

```text
401 → authentication challenge/failure
403 → server understood request but denies access
404 → selected server/location cannot find target
413 → request body exceeds configured limit
429 → rate limiting/resource policy
500 → local web/app failure
502 → bad/unusable upstream response
503 → service unavailable
504 → upstream response timeout
```

Do not treat every 5xx as "NGINX is broken."

---

## Enhanced Deep Dive 6 — 502 vs 504

### 502

Common path:

```text
NGINX
  ↓ connect upstream
connection refused / reset / invalid response
  ↓
502
```

Examples:

```text
backend process down
wrong IP
wrong port
HTTP proxying to HTTPS backend incorrectly
backend crashes while responding
SELinux blocks connection
```

### 504

```text
NGINX
  ↓ upstream request accepted
wait
wait
wait
timeout
  ↓
504
```

Possible causes:

```text
slow database
deadlock
external API delay
backend overload
proxy timeout too short
network latency
```

Troubleshooting:

```bash
curl -v http://backend:8000/health
ss -tlnp
journalctl -u nginx
tail -n 100 /var/log/nginx/error.log
```

---

## Enhanced Deep Dive 7 — HTTP/1.1 Persistent Connections

HTTP/1.1 commonly reuses TCP connections.

Without keep-alive:

```text
request
→ TCP connect
→ response
→ close
→ next request creates new TCP
```

With persistent connections:

```text
TCP connection
├── request 1
├── request 2
├── request 3
└── close later
```

Benefits:

```text
less handshake overhead
lower latency
less connection churn
```

Costs:

```text
idle sockets consume resources
timeouts must be tuned
```

---

## Enhanced Deep Dive 8 — HTTP/2 and HTTP/3 Awareness

Modern environments can use:

```text
HTTP/2
→ multiplexed streams over one TCP connection

HTTP/3
→ HTTP over QUIC/UDP
```

You do not need to memorize all wire details at this stage, but understand:

```text
same URL/application
different transport behavior
different debugging implications
```

A reverse proxy may terminate HTTP/2 from clients while using HTTP/1.1 to the upstream.

---

## Enhanced Deep Dive 9 — DNS and Virtual Hosting

Name-based hosting depends on the requested hostname.

DNS:

```text
www.alpha.lab
www.beta.lab
       ↓
same IP
```

HTTP:

```text
Host: www.alpha.lab
```

or:

```text
Host: www.beta.lab
```

The web server chooses different site configuration.

Test without DNS:

```bash
curl \
  -H 'Host: www.alpha.lab' \
  http://192.168.56.21/
```

DNS only maps name to address. It does not decide which virtual host Apache serves.

---

## Enhanced Deep Dive 10 — TLS SNI and HTTPS Virtual Hosting

With HTTPS, the server often needs to choose a certificate before normal HTTP headers are available.

SNI carries the requested server name during TLS negotiation.

Model:

```text
Client
  ↓ TCP/443
TLS ClientHello
  └── SNI=www.alpha.lab
        ↓
server selects certificate/TLS vhost
        ↓
TLS established
        ↓
HTTP Host header
```

Inspect:

```bash
openssl s_client \
  -connect 192.168.56.21:443 \
  -servername www.alpha.lab
```

Without correct SNI, the server may present the default certificate.

---

## Enhanced Deep Dive 11 — Certificate Chain

A certificate is usually validated through a chain:

```text
server certificate
      ↓ signed by
intermediate CA
      ↓ signed by
root CA trusted by client
```

A server may need to provide intermediate certificates.

Common TLS failures:

```text
hostname mismatch
expired certificate
not-yet-valid certificate
missing intermediate
unknown CA
wrong certificate selected
private key mismatch
```

Inspect:

```bash
openssl s_client \
  -connect app.example.com:443 \
  -servername app.example.com \
  -showcerts
```

---

## Enhanced Deep Dive 12 — Certificate Names: SAN, Not Just CN

Modern certificate validation uses Subject Alternative Names.

Concept:

```text
Certificate:
SAN:
  DNS:app.example.com
  DNS:www.example.com
```

A certificate for:

```text
app.example.com
```

does not automatically validate:

```text
api.example.com
```

unless included appropriately.

Production certificates should be issued according to organizational PKI/CA policy.

---

## Enhanced Deep Dive 13 — Private Key Protection

The private key proves server possession of the certificate identity.

Protect:

```bash
sudo chown root:root /etc/pki/tls/private/app.key
sudo chmod 600 /etc/pki/tls/private/app.key
```

Threat model:

```text
private key stolen
    ↓
attacker may impersonate service
depending on certificate/PKI context
```

Do not:

```text
commit key to Git
email key
place key in world-readable web root
copy key into container image layer carelessly
```

---

## Enhanced Deep Dive 14 — Apache Process Architecture and MPM Awareness

Apache uses a Multi-Processing Module (MPM) that determines worker/process/thread behavior.

Common concepts include:

```text
prefork
worker
event
```

Exact defaults depend on platform/build.

Inspect:

```bash
httpd -V | grep -i 'Server MPM'
httpd -M | sort
```

Why it matters:

```text
concurrency model
thread/process count
module compatibility
memory use
keep-alive behavior
```

Do not tune worker counts before measuring workload and memory.

---

## Enhanced Deep Dive 15 — Apache Configuration Merge Model

Apache configuration can come from:

```text
main config
conf.d includes
VirtualHost blocks
Directory blocks
Location blocks
Files blocks
optional .htaccess
```

Simplified:

```text
global directives
      +
virtual host
      +
directory/location context
      ↓
effective request configuration
```

A directive valid globally may behave differently inside a virtual host or directory context.

Use official module/directive documentation for context rules.

---

## Enhanced Deep Dive 16 — Apache Include Layout

A maintainable layout might be:

```text
/etc/httpd/
├── conf/httpd.conf
├── conf.d/
│   ├── 10-security.conf
│   ├── 20-alpha.conf
│   ├── 30-api-proxy.conf
│   └── 40-tls.conf
└── conf.modules.d/
```

Benefits:

```text
smaller change scope
easier review
clear ownership
easier rollback
```

Validate all files together:

```bash
apachectl configtest
```

---

## Enhanced Deep Dive 17 — Apache Virtual Host Selection

Name-based selection depends on:

```text
listener/address
port
Host header / server name
configuration ordering/default
```

Inspect parsed virtual hosts:

```bash
apachectl -S
```

This is one of the most useful commands for:

```text
wrong site served
unexpected default vhost
duplicate ServerName
port mismatch
```

---

## Enhanced Deep Dive 18 — `ServerName` vs `ServerAlias`

Example:

```apache
ServerName www.alpha.lab
ServerAlias alpha.lab alpha.internal.lab
```

`ServerName` is the canonical primary name for that vhost.

`ServerAlias` adds alternate names.

If DNS points a new name to the server but the name is absent from the intended vhost, Apache can select another/default vhost.

---

## Enhanced Deep Dive 19 — Apache `<Directory>` vs `<Location>`

These match different things.

```text
<Directory>
→ filesystem path

<Location>
→ URL path
```

Example:

```apache
<Directory /srv/www/private>
    Require all denied
</Directory>
```

versus:

```apache
<Location /health>
    Require all granted
</Location>
```

Do not confuse URL paths with filesystem paths when access control is involved.

---

## Enhanced Deep Dive 20 — DocumentRoot Access: DAC + SELinux

Apache reading:

```text
/srv/www/alpha/index.html
```

requires multiple layers.

```text
Parent-directory execute permissions
    AND
file read permission
    AND
SELinux policy/label
```

Inspect:

```bash
namei -l /srv/www/alpha/index.html
ls -Z /srv/www/alpha/index.html
getenforce
```

Persistent SELinux mapping:

```bash
sudo semanage fcontext \
  -a \
  -t httpd_sys_content_t \
  '/srv/www(/.*)?'

sudo restorecon -Rv /srv/www
```

Never use `chmod 777` as a SELinux workaround.

---

## Enhanced Deep Dive 21 — Read-Only vs Writable Web Content

Separate:

```text
static/read-only content
uploads
cache
runtime sockets
logs
configuration
secrets
```

Architecture:

```text
/srv/app/static
→ read-only to web process

/srv/app/uploads
→ writable only if application requires

/etc/app
→ root-managed configuration

/var/log/app
→ controlled logging
```

If the web process can write its own executable/static application tree, exploitation impact can increase.

Least privilege applies to filesystem layout.

---

## Enhanced Deep Dive 22 — Apache Modules as Attack Surface

Inspect:

```bash
httpd -M | sort
```

Modules add capabilities:

```text
proxy
ssl
headers
auth
rewrite
status
compression
```

Unused modules:

```text
increase complexity
increase exposed behavior
increase patch surface
```

Do not disable modules blindly. First confirm application dependency.

---

## Enhanced Deep Dive 23 — `.htaccess` Trade-offs

`.htaccess` allows directory-level delegated configuration when `AllowOverride` permits it.

Advantages:

```text
application team can manage directory policy without global config access
```

Costs:

```text
harder centralized auditing
additional per-request filesystem checks in some designs
configuration fragmented inside content tree
```

For centrally managed servers, explicit global/vhost configuration is often easier to control.

---

## Enhanced Deep Dive 24 — Apache Logging Deep Dive

Access log can capture:

```text
client address
request line
status
bytes
referrer
user agent
request time if configured
forwarded address if trusted
```

Error log captures server/module errors.

Useful analysis:

```bash
awk '{print $9}' /var/log/httpd/access_log |
sort |
uniq -c |
sort -nr
```

Top requested paths:

```bash
awk '{print $7}' /var/log/httpd/access_log |
sort |
uniq -c |
sort -nr |
head
```

Do not treat user agent as authenticated identity.

---

## Enhanced Deep Dive 25 — Log Rotation and Open Files

Web logs can grow quickly.

Use system log rotation mechanisms rather than deleting current files.

Inspect:

```bash
ls /etc/logrotate.d | grep -E 'httpd|nginx'
```

Deleted-but-open problem:

```text
rm access.log
   ↓
directory entry gone
   ↓
httpd still holds fd open
   ↓
disk blocks remain allocated
```

Inspect:

```bash
sudo lsof +L1
```

---

## Enhanced Deep Dive 26 — NGINX Master and Worker Model

Simplified NGINX architecture:

```text
master process
   ├── reads config
   ├── opens/manages lifecycle
   └── controls workers
        ├── worker 1
        ├── worker 2
        └── ...
```

Inspect:

```bash
ps -ef | grep '[n]ginx'
nginx -V
```

Workers handle network events using an event-driven model.

Do not assume this automatically means NGINX is always faster than Apache for every workload.

---

## Enhanced Deep Dive 27 — NGINX Configuration Hierarchy

Typical:

```text
main context
  ↓
events
  ↓
http
  ↓
server
  ↓
location
```

Example:

```nginx
http {
    server {
        listen 80;
        server_name app.lab;

        location /api/ {
            proxy_pass http://backend;
        }
    }
}
```

Directives are valid only in specific contexts.

Always run:

```bash
nginx -t
```

before reload.

---

## Enhanced Deep Dive 28 — NGINX Server Selection

Selection uses:

```text
listen address/port
server_name
default server behavior
```

If the hostname does not match an intended server block, NGINX may use the default server for that listener.

Inspect full effective configuration:

```bash
nginx -T
```

This prints included files too.

Be careful: output can include sensitive configuration paths/content.

---

## Enhanced Deep Dive 29 — NGINX `location` Matching Awareness

Location matching can use:

```text
prefix
exact
regular expression
named locations
```

Example:

```nginx
location = /health {
    return 200 "OK\n";
}

location /static/ {
    root /srv/site;
}
```

More complex regex/prefix precedence can surprise administrators.

Keep routing simple unless requirements demand complexity.

---

## Enhanced Deep Dive 30 — `root` vs `alias` in NGINX

These are not interchangeable.

Conceptually:

```nginx
location /images/ {
    root /srv/site;
}
```

maps:

```text
/images/logo.png
→ /srv/site/images/logo.png
```

Whereas `alias` replaces the matched prefix with a different filesystem path.

Misunderstanding this causes many 404s.

Test every mapping with:

```bash
nginx -t
curl -v http://127.0.0.1/images/logo.png
```

---

## Enhanced Deep Dive 31 — `try_files`

Example:

```nginx
location / {
    try_files $uri $uri/ =404;
}
```

Concept:

```text
requested URI
   ↓
existing file?
   ↓ no
existing directory?
   ↓ no
return 404
```

For single-page apps, deployments often use a different final fallback such as `/index.html`; that decision belongs to application architecture.

---

## Enhanced Deep Dive 32 — `proxy_pass` URI Semantics

This is a common NGINX confusion.

These can behave differently:

```nginx
location /api/ {
    proxy_pass http://backend;
}
```

and:

```nginx
location /api/ {
    proxy_pass http://backend/;
}
```

The trailing URI slash can change which part of the original path is replaced.

Always test concrete URLs:

```text
/api/users
/api/health
```

against expected upstream paths.

Do not deploy proxy path rewrites by intuition alone.

---

## Enhanced Deep Dive 33 — Forwarded Headers and Trust Boundaries

Common headers:

```text
Host
X-Real-IP
X-Forwarded-For
X-Forwarded-Proto
```

Flow:

```text
Client IP 203.0.113.10
      ↓
Proxy 192.0.2.10
      ↓
Backend
X-Forwarded-For: 203.0.113.10
```

Security issue:

If backend is directly reachable by clients and blindly trusts:

```http
X-Forwarded-For: 127.0.0.1
```

the client may forge identity/address assumptions.

Rule:

```text
trust forwarding headers
ONLY
from known trusted proxy hops
```

---

## Enhanced Deep Dive 34 — Upstream Address Selection

Backend can bind:

```text
127.0.0.1:8000
→ local proxy only

0.0.0.0:8000
→ all IPv4 interfaces

192.168.56.21:8000
→ selected interface
```

Inspect:

```bash
ss -tlnp | grep ':8000'
```

Binding is part of security architecture.

A backend that should only be reachable through local NGINX should not necessarily listen publicly.

---

## Enhanced Deep Dive 35 — FastAPI/Uvicorn Example Behind NGINX

Minimal application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

Run in lab:

```bash
uvicorn app:app \
  --host 127.0.0.1 \
  --port 8000
```

NGINX:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8000/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

Verify both layers:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1/api/health
```

---

## Enhanced Deep Dive 36 — Application Process Manager Awareness

A development server is not always the correct production process model.

Production application deployments may use:

```text
Gunicorn
Uvicorn workers
systemd
container runtime
Java service manager
Node.js process manager
```

The reverse proxy and application process lifecycle should be independent.

Example:

```text
NGINX systemd service
     ↓ proxy
app.service systemd unit
     ↓
FastAPI process
```

If backend fails:

```text
NGINX can remain up
but return 502
```

---

## Enhanced Deep Dive 37 — WebSocket Proxying Awareness

WebSockets begin with an HTTP upgrade and become a persistent bidirectional connection.

Simplified:

```text
Client
  ↓ HTTP Upgrade
NGINX
  ↓ forwarded Upgrade
Backend
  ⇄ persistent connection
```

Proxy configuration may require correct upgrade/connection headers depending on server/application.

Do not globally apply WebSocket headers to every location without need.

---

## Enhanced Deep Dive 38 — Reverse Proxy Timeouts

Important categories include:

```text
connect timeout
read timeout
send timeout
client timeout
```

A timeout represents a contract.

Too short:

```text
valid slow operations fail
```

Too long:

```text
broken upstreams hold resources longer
```

Set from measured application behavior and SLOs, not copied defaults.

---

## Enhanced Deep Dive 39 — Request Body Size Limits

Multiple layers can reject uploads:

```text
client
proxy
web server
application framework
application code
object storage/API
```

If NGINX allows 50 MB but application allows 10 MB:

```text
request reaches app
then fails there
```

If NGINX allows only 1 MB:

```text
proxy returns 413 before application
```

Document the intended request-size contract.

---

## Enhanced Deep Dive 40 — Proxy Buffering

Reverse proxies can buffer request/response data.

Benefits:

```text
protect slow clients from tying up upstream connection
smooth I/O behavior
```

Trade-offs:

```text
memory/disk temporary use
streaming latency
large response behavior
```

Streaming APIs and server-sent events may require different buffering choices.

---

## Enhanced Deep Dive 41 — Load Balancing Algorithms

Common concepts:

```text
round robin
weighted round robin
least connections
hash-based/session-aware approaches
```

Selection depends on:

```text
backend capacity
session model
request duration
application state
```

Weighted configuration:

```nginx
upstream app_backend {
    server 192.168.56.21:8080 weight=3;
    server 192.168.56.22:8080 weight=1;
}
```

Weights express preference, not exact sequence guarantees.

---

## Enhanced Deep Dive 42 — Stateless vs Stateful Backends

Stateless web tier:

```text
request 1 → web01
request 2 → web02
```

works if application state is stored externally or encoded appropriately.

Stateful session stored only on web01:

```text
request 1 → web01 login
request 2 → web02 session missing
```

Possible architectural solutions:

```text
shared session store
database
Redis
sticky-session design where justified
application redesign
```

Load balancing cannot fix an application that assumes all requests stay on one process unless architecture supports it.

---

## Enhanced Deep Dive 43 — Passive Health and Failure Behavior

Open-source/proxy health behavior varies by product/version/configuration.

At minimum, understand:

```text
connection failure
timeout
backend marked temporarily unavailable
next backend considered
```

Do not assume "load balancer" automatically performs sophisticated active health checks.

Test actual failure behavior:

```text
backend stop
connection refusal
slow backend
bad HTTP response
```

---

## Enhanced Deep Dive 44 — TLS Termination vs End-to-End TLS

TLS termination:

```text
Client
  ↓ HTTPS
Proxy
  ↓ HTTP
Backend
```

End-to-end:

```text
Client
  ↓ HTTPS
Proxy
  ↓ HTTPS
Backend
```

Decision depends on:

```text
network trust boundary
compliance
service identity
performance
certificate management
zero-trust architecture
```

"Private network" does not automatically mean plaintext is acceptable.

---

## Enhanced Deep Dive 45 — HTTP to HTTPS Redirect

Apache:

```apache
Redirect permanent / https://www.alpha.lab/
```

NGINX:

```nginx
server {
    listen 80;
    server_name app.lab.example;
    return 301 https://$host$request_uri;
}
```

Verify:

```bash
curl -I http://app.lab.example/
```

Check:

```text
status
Location header
host/path correctness
no redirect loop
```

---

## Enhanced Deep Dive 46 — HSTS

HSTS tells supported browsers to prefer HTTPS for a domain after receiving the policy over HTTPS.

Header example:

```text
Strict-Transport-Security: max-age=...
```

Risk:

A bad HSTS rollout can lock browsers into HTTPS while TLS/certificate/service is not ready.

Plan:

```text
TLS stable
all required subdomains understood
short initial max-age
monitor
then increase
```

Do not add `includeSubDomains` or preload-like policy without understanding impact.

---

## Enhanced Deep Dive 47 — Security Headers

Common controls:

```text
Content-Security-Policy
X-Content-Type-Options
Referrer-Policy
Strict-Transport-Security
frame-related policy via CSP/X-Frame-Options in legacy contexts
```

Security headers must match the application.

A copied CSP can break:

```text
JavaScript
stylesheets
fonts
frames
API calls
images
```

Test with browser developer tools and application owners.

---

## Enhanced Deep Dive 48 — Basic Authentication

Basic authentication sends credentials in a reversible encoding within HTTP headers.

Therefore:

```text
Basic auth
must be protected by TLS
```

Lab:

```bash
sudo htpasswd -c /etc/httpd/.htpasswd labuser
```

Never place the password file under the public document root.

Authentication is not authorization architecture by itself.

---

## Enhanced Deep Dive 49 — Reverse Proxy Authentication Architectures

Enterprise deployments may use:

```text
OIDC-aware proxy
SAML gateway
Kerberos/GSSAPI
LDAP-integrated authentication
application-native identity
```

Architecture:

```text
Browser
  ↓
identity-aware proxy
  ↓ authenticated identity headers/tokens
application
```

Critical trust question:

```text
Can clients bypass the proxy and send those identity headers directly?
```

If yes, the trust model is broken unless the app independently verifies them.

---

## Enhanced Deep Dive 50 — PHP-FPM / FastCGI Awareness

Some web stacks separate HTTP server and language runtime:

```text
NGINX
  ↓ FastCGI
PHP-FPM
  ↓
PHP application
```

or:

```text
Apache
  ↓ proxy_fcgi
PHP-FPM
```

Troubleshooting layers:

```text
web server
FastCGI socket/TCP port
PHP-FPM process
filesystem permission
SELinux
application error
```

A 502 can be a dead FastCGI backend just like a dead HTTP backend.

---

## Enhanced Deep Dive 51 — UNIX Domain Sockets vs TCP Upstreams

Applications can communicate locally via:

```text
TCP 127.0.0.1:8000
```

or:

```text
UNIX socket /run/app/app.sock
```

UNIX socket considerations:

```text
filesystem owner/group/mode
parent directory traversal
SELinux label
service startup ordering
socket cleanup
```

TCP loopback considerations:

```text
port ownership
local firewall usually less relevant
SELinux network-connect rules
```

Choose based on operational simplicity and application support.

---

## Enhanced Deep Dive 52 — systemd for Application Services

Example conceptual unit:

```ini
[Unit]
Description=FastAPI application
After=network.target

[Service]
User=appuser
Group=appuser
WorkingDirectory=/srv/app
ExecStart=/srv/app/.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8000
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Workflow:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now app.service

systemctl status app.service
journalctl -u app.service
ss -tlnp | grep ':8000'
```

Do not run production applications manually inside an SSH terminal.

---

## Enhanced Deep Dive 53 — systemd Service Hardening Awareness

systemd can apply service restrictions such as:

```text
NoNewPrivileges
PrivateTmp
ProtectSystem
ProtectHome
CapabilityBoundingSet
RestrictAddressFamilies
```

Not every restriction fits every application.

Hardening workflow:

```text
understand app filesystem/network needs
apply one restriction
test
observe logs
iterate
```

Do not paste a hardened unit profile that prevents required application behavior without understanding why.

---

## Enhanced Deep Dive 54 — SELinux Reverse Proxy Networking

A web process confined by SELinux may not be allowed to make arbitrary outbound connections.

Inspect:

```bash
getsebool httpd_can_network_connect
```

When architecture legitimately requires proxying to a backend, use the supported SELinux policy/Boolean rather than disabling SELinux.

After changing:

```bash
ausearch -m AVC -ts recent
```

if access still fails.

---

## Enhanced Deep Dive 55 — firewalld Web Tier Design

A proxy may need:

```text
client-facing:
80/tcp
443/tcp

backend-facing:
8080/tcp from proxy subnet only
```

Do not expose backend port to all client networks if architecture says only proxy should reach it.

Model:

```text
Internet/client
    ↓ 443
proxy
    ↓ 8080
backend

client ─X→ 8080 backend
```

Host firewall and network firewall should reflect this trust model.

---

## Enhanced Deep Dive 56 — Socket Verification Before Firewall Changes

Always prove:

```text
process exists
socket exists
correct bind address
```

before opening a firewall.

```bash
systemctl status nginx
ss -tlnp | grep ':443'
```

Firewall rule cannot make a process listen.

Likewise:

```text
listener exists
```

does not prove remote path/firewall permits traffic.

---

## Enhanced Deep Dive 57 — Port Collision

Tuple:

```text
IP address
protocol
port
```

Normally one listening service owns a specific tuple unless special socket-sharing mechanisms apply.

If Apache has:

```text
0.0.0.0:80
```

NGINX cannot normally bind the same:

```text
0.0.0.0:80
```

Inspect:

```bash
sudo ss -ltnp | grep ':80'
```

Fix architecture rather than repeatedly restarting both.

---

## Enhanced Deep Dive 58 — TLS Cipher and Protocol Policy Awareness

TLS policy includes:

```text
protocol versions
cipher suites
certificate algorithms
key sizes
client trust
```

On enterprise Linux, system-wide cryptographic policy may affect available protocols/ciphers.

Do not enable obsolete TLS versions merely to make an old client work without assessing security/support requirements.

Test:

```bash
openssl s_client \
  -connect app.lab.example:443 \
  -servername app.lab.example
```

Use approved organizational cryptographic policy as authority.

---

## Enhanced Deep Dive 59 — Certificate Renewal Operations

A certificate deployment is not complete if there is no renewal process.

Lifecycle:

```text
request/issue
  ↓
install
  ↓
validate
  ↓
monitor expiry
  ↓
renew
  ↓
reload service
  ↓
verify new certificate
```

Monitor expiry before outage.

Example inspection:

```bash
openssl x509 \
  -in /etc/pki/tls/certs/app.crt \
  -noout \
  -subject \
  -issuer \
  -dates
```

---

## Enhanced Deep Dive 60 — Access Log as an Operational Dataset

Useful questions:

```text
Which status codes increased?
Which paths produce 404?
Which client addresses generate most requests?
Which requests are largest?
Which user agents dominate?
```

Examples:

```bash
awk '{print $9}' access.log |
sort |
uniq -c |
sort -nr
```

Top paths:

```bash
awk '{print $7}' access.log |
sort |
uniq -c |
sort -nr |
head -20
```

Top client addresses:

```bash
awk '{print $1}' access.log |
sort |
uniq -c |
sort -nr |
head
```

Log formats must be understood before field-based parsing.

---

## Enhanced Deep Dive 61 — Request IDs / Correlation IDs

In multi-tier systems, one request can pass through:

```text
load balancer
NGINX
application
database/API
```

A correlation/request ID helps connect logs.

Model:

```text
request ID = abc123

proxy log:
abc123 /orders 502

app log:
abc123 upstream database timeout
```

If the application already supplies a trace/request ID, propagate it consistently rather than generating conflicting IDs at every layer.

---

## Enhanced Deep Dive 62 — Monitoring Web Infrastructure

Monitor at least:

```text
process state
listener
request rate
latency
status-code rate
5xx rate
upstream errors
TLS expiry
CPU/memory
file descriptor use
disk/log usage
backend health
```

Service "active" is not enough.

Health:

```text
systemd active
AND
port listening
AND
HTTP health endpoint succeeds
AND
dependency health acceptable
```

---

## Enhanced Deep Dive 63 — File Descriptor Limits

Each connection/file consumes descriptors.

Inspect:

```bash
ulimit -n
cat /proc/$(pgrep -o nginx)/limits 2>/dev/null || true
```

Symptoms of exhaustion can include:

```text
too many open files
failed accepts
upstream connection errors
log failures
```

Do not only raise limits. Determine why usage is high and size resources intentionally.

---

## Enhanced Deep Dive 64 — Connection Backlog Awareness

Incoming connections can queue before application acceptance.

Backlog behavior spans:

```text
kernel
listener
web server
upstream app
```

Under overload, symptoms can include:

```text
connection timeout
reset
latency spikes
```

Capacity tuning requires measurement across all tiers, not one `worker_connections` number copied from a blog.

---

## Enhanced Deep Dive 65 — Compression Trade-offs

Compressible content:

```text
HTML
CSS
JavaScript
JSON
text
```

Already compressed:

```text
JPEG
MP4
ZIP
many PDFs
```

Compression uses CPU.

Also, compression of secrets combined with attacker-controlled reflected input can create side-channel risks in some architectures.

Apply content-type and security-aware policy.

---

## Enhanced Deep Dive 66 — Caching Concepts

Cache key may depend on:

```text
scheme
host
path
query
headers
cookies
authorization
```

Incorrect caching can expose private data.

Do not cache authenticated/private responses unless you understand:

```text
Cache-Control
Vary
authorization/session behavior
cache key
purge/invalidation
```

A stale fast response is still wrong.

---

## Enhanced Deep Dive 67 — Rate Limiting and Abuse Controls

Reverse proxies can apply request-rate/concurrency limits.

Use cases:

```text
protect login endpoint
protect expensive API
reduce accidental overload
```

But rate limiting must consider:

```text
trusted proxy address
NAT/shared clients
real client-IP extraction
burst behavior
API contract
```

If all users appear as one proxy IP, an IP-based limiter can block everyone.

---

## Enhanced Deep Dive 68 — Load Testing Safety

Performance testing can become denial of service.

Use only authorized systems.

Start:

```bash
ab -n 20 -c 2 http://127.0.0.1/
```

Then measure:

```text
latency
error rate
CPU
memory
connections
backend saturation
```

Increase gradually.

Never launch large concurrency at production or third-party systems without an approved test plan.

---

## Enhanced Deep Dive 69 — Web Root Ownership Strategy

Bad:

```text
web process owns all application files
```

Better separation:

```text
deployment account/root
→ owns application/static files

web service user
→ read-only where possible

upload/runtime directory
→ only specific writable paths
```

This limits post-exploitation modification ability.

---

## Enhanced Deep Dive 70 — Upload Directory Security

User uploads can be dangerous if a server later executes or interprets them.

Good design:

```text
uploads outside executable code tree
randomized/object identifiers
content-type validation
size limits
malware/content inspection where required
no execute permission
serve with safe content disposition/type
```

Do not let "upload directory writable" become "entire website writable."

---

## Enhanced Deep Dive 71 — Directory Listing

Apache:

```apache
Options -Indexes
```

NGINX:

```nginx
autoindex off;
```

Directory listings can expose:

```text
backup files
internal filenames
temporary artifacts
source archives
```

Enable only if listing is intentionally part of the service.

---

## Enhanced Deep Dive 72 — Configuration Secrets

Examples:

```text
TLS private key
proxy credentials
API tokens
basic-auth files
upstream credentials
```

Do not store secrets in:

```text
world-readable conf
public Git
web document root
container image history
shell history
```

Use appropriate secret-management and permissions.

---

## Enhanced Deep Dive 73 — Backup vs Version Control

Version control protects configuration history.

Backup protects:

```text
configuration
certificates/keys according to policy
application data
logs where required
```

Git is not automatically a secure backup for secrets.

A good recovery package includes:

```text
configs
package/version inventory
certificate issuance process
firewall/SELinux policy
DNS records
application deployment
runbook
```

---

## Enhanced Deep Dive 74 — Safe Web Change Workflow

```text
requirement
   ↓
capture current config
   ↓
edit in version control
   ↓
syntax test
   ↓
local request test
   ↓
reload
   ↓
remote request test
   ↓
TLS/DNS/proxy tests
   ↓
logs/metrics
   ↓
document
```

Apache:

```bash
apachectl configtest
```

NGINX:

```bash
nginx -t
```

Prefer reload when configuration can be reloaded safely and a full restart is not required.

---

## Enhanced Deep Dive 75 — Apache Failure Decision Tree

```text
httpd will not start
   ↓
package installed?
   ↓
apachectl configtest
   ↓
duplicate listener?
   ↓
certificate/key file?
   ↓
permissions/SELinux?
   ↓
module exists?
   ↓
journal
```

Commands:

```bash
rpm -q httpd
apachectl configtest
apachectl -S
httpd -M
ss -ltnp
journalctl -u httpd -b
```

---

## Enhanced Deep Dive 76 — NGINX Failure Decision Tree

```text
nginx will not start
   ↓
nginx -t
   ↓
include file path?
   ↓
duplicate listen?
   ↓
certificate/key?
   ↓
permissions?
   ↓
SELinux?
   ↓
journal/error log
```

Commands:

```bash
nginx -t
nginx -T
ss -ltnp
journalctl -u nginx -b
tail -n 100 /var/log/nginx/error.log
```

---

## Enhanced Deep Dive 77 — Local Works, Remote Fails

If:

```bash
curl http://127.0.0.1/
```

works but remote client fails:

```text
bind address?
host firewall?
network firewall?
route?
DNS?
NAT/load balancer?
```

Check:

```bash
ss -ltnp
ip -br address
ip route
firewall-cmd --list-all
```

Do not change application code first.

---

## Enhanced Deep Dive 78 — Wrong Website Served

Likely layers:

```text
DNS correct?
Host header?
SNI?
default vhost?
server_name/ServerName?
config order?
```

Apache:

```bash
apachectl -S
```

NGINX:

```bash
nginx -T
```

Test explicitly:

```bash
curl -H 'Host: alpha.lab' http://SERVER_IP/
```

For HTTPS:

```bash
curl \
  --resolve alpha.lab:443:SERVER_IP \
  https://alpha.lab/
```

Use valid/trusted lab certificates or appropriate `--cacert`; avoid making `-k` the default.

---

## Enhanced Deep Dive 79 — TLS Works by IP but Hostname Fails

Certificate validation is hostname-based.

Connecting to:

```text
https://192.168.56.20/
```

with a certificate for:

```text
app.lab.example
```

can fail name validation.

Use:

```bash
curl \
  --resolve app.lab.example:443:192.168.56.20 \
  https://app.lab.example/
```

This keeps the intended hostname/SNI while directing to a chosen IP.

---

## Enhanced Deep Dive 80 — Reverse Proxy Failure Matrix

```text
Symptom       Likely investigation
---------------------------------------------------
502           backend down/protocol/SELinux/reset
504           backend slow/timeout/network delay
404           path rewrite/location/upstream route
403           access policy/SELinux/app auth
413           body-size limit
429           rate limit
TLS error     cert/SNI/chain/private key/protocol
wrong client IP forwarded-header trust/config
```

Always test the upstream directly before blaming the proxy.

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Request Path Mapping

For a working site, record:

```text
DNS result
route
TCP listener
TLS details
virtual host
filesystem/upstream
response status
logs
```

## Enhanced Lab 2 — HTTP Message Inspection

Use `curl -v` to inspect request/response headers for:

```text
GET
HEAD
redirect
404
```

## Enhanced Lab 3 — Status Code Matrix

Generate safe examples of:

```text
200
301
401
403
404
413
500
502
504
```

where practical in the lab and document the responsible layer.

## Enhanced Lab 4 — Apache MPM Inspection

Identify active MPM, loaded modules, process tree, and connection behavior.

## Enhanced Lab 5 — Apache Include Design

Split a monolithic lab config into:

```text
security
vhosts
proxy
TLS
```

files under `conf.d`.

## Enhanced Lab 6 — Apache Vhost Selection

Create three vhosts and use `apachectl -S` to explain default selection.

## Enhanced Lab 7 — ServerAlias

Add alternate DNS names and prove Host-header routing.

## Enhanced Lab 8 — Directory vs Location

Create filesystem and URL access-control examples and explain the difference.

## Enhanced Lab 9 — SELinux Document Root

Create `/srv/web/alpha`, label persistently, verify with `restorecon`, test under enforcing mode.

## Enhanced Lab 10 — Writable Upload Area

Create separate read-only static tree and writable upload tree with minimum permissions.

## Enhanced Lab 11 — Apache Log Analysis

Generate traffic and report:

```text
status counts
top paths
top clients
```

## Enhanced Lab 12 — Logrotate

Inspect httpd logrotate policy, rotate synthetic logs, and inspect open descriptors.

## Enhanced Lab 13 — TLS Chain Inspection

Use `openssl s_client` against the lab service and identify leaf/intermediate/root trust concepts.

## Enhanced Lab 14 — SAN Testing

Create lab certificate with appropriate SANs and compare valid hostname vs invalid hostname.

## Enhanced Lab 15 — SNI

Host two TLS names and prove certificate selection with different `-servername` values.

## Enhanced Lab 16 — HTTP→HTTPS Redirect

Configure redirect and verify path/query preservation.

## Enhanced Lab 17 — HSTS Staged Design

Write a rollout plan with short initial max-age, monitoring, and rollback considerations.

## Enhanced Lab 18 — NGINX Master/Workers

Inspect process hierarchy before/after reload.

## Enhanced Lab 19 — NGINX Effective Config

Use `nginx -T` and map includes to server blocks.

## Enhanced Lab 20 — NGINX Location Matching

Build exact and prefix locations, predict behavior, then test.

## Enhanced Lab 21 — root vs alias

Create two filesystem mappings and verify how request paths become filesystem paths.

## Enhanced Lab 22 — try_files

Serve static files and observe 200 vs 404 paths.

## Enhanced Lab 23 — proxy_pass Slash Behavior

Build two locations differing only in trailing slash and document upstream URI results.

## Enhanced Lab 24 — FastAPI Backend

Run a local FastAPI/Uvicorn health endpoint and proxy through NGINX.

## Enhanced Lab 25 — Backend Bind Address

Compare loopback-only and private-interface binding; verify reachability from another VM.

## Enhanced Lab 26 — systemd Application Service

Run the application using a systemd unit rather than an SSH shell.

## Enhanced Lab 27 — WebSocket Awareness

If your test app supports WebSocket, proxy it; otherwise document required upgrade flow.

## Enhanced Lab 28 — 502 Failure

Stop backend, observe 502, correlate NGINX error log and backend state.

## Enhanced Lab 29 — 504 Failure

Create a safe delayed endpoint and a shorter proxy timeout, then observe timeout behavior.

## Enhanced Lab 30 — Request Body Limit

Configure a small lab limit and observe 413 for a larger generated request.

## Enhanced Lab 31 — Forwarded Headers

Return received headers from backend and verify `Host`, `X-Forwarded-For`, and scheme.

## Enhanced Lab 32 — Forged Forwarded Header

In a controlled lab, send a fake `X-Forwarded-For` directly to backend and explain why backend trust policy matters.

## Enhanced Lab 33 — Two-Backend Load Balancing

Return hostname from web01/web02 and observe distribution.

## Enhanced Lab 34 — Weighted Backend

Use 3:1 weighting and collect enough requests to discuss preference vs exact sequence.

## Enhanced Lab 35 — Stateful Session Problem

Simulate session state local to one backend and observe why load balancing can break it.

## Enhanced Lab 36 — Backend Failure

Stop one backend and record client-visible behavior and proxy logs.

## Enhanced Lab 37 — TLS Termination

Use HTTPS client→proxy and HTTP proxy→backend, document trust boundary.

## Enhanced Lab 38 — End-to-End TLS Design

Create a design for HTTPS proxy→backend and list certificate/trust requirements.

## Enhanced Lab 39 — Basic Auth

Protect `/private` over TLS and test 401/valid credentials.

## Enhanced Lab 40 — UNIX Socket Upstream

If supported by test app, proxy via a UNIX socket and troubleshoot mode/SELinux.

## Enhanced Lab 41 — firewalld Segmentation

Allow clients to proxy ports while only proxy subnet reaches backend port.

## Enhanced Lab 42 — SELinux Proxy Boolean

Create a controlled proxy denial if possible and correct it using supported SELinux policy while enforcing remains on.

## Enhanced Lab 43 — Port Collision

Run Apache on 80, attempt NGINX on same tuple, diagnose with `ss`.

## Enhanced Lab 44 — Certificate Expiry Check

Write a script reporting subject/issuer/expiry of lab certificate.

## Enhanced Lab 45 — Request ID

Add or pass a request ID and correlate proxy and backend logs.

## Enhanced Lab 46 — Web Health Monitoring

Create checks for:

```text
systemd
listener
HTTP health
TLS expiry
```

## Enhanced Lab 47 — File Descriptor Observation

Generate modest authorized concurrency and observe NGINX/Apache descriptor counts.

## Enhanced Lab 48 — Compression

Enable compression for text content in a lab and compare headers/size.

## Enhanced Lab 49 — Cache Design

Design a safe cache policy for public static content and explain why authenticated responses should not be cached casually.

## Enhanced Lab 50 — Rate Limit Design

Create a low lab rate limit and observe 429 behavior; explain NAT/client-IP implications.

## Enhanced Lab 51 — Upload Security

Create isolated upload directory and document owner/mode/SELinux/execution policy.

## Enhanced Lab 52 — Security Headers

Add a minimal lab set and test headers. Do not deploy CSP blindly; document required application sources.

## Enhanced Lab 53 — Wrong Vhost Incident

Deliberately misconfigure server name/default selection and solve with Apache/NGINX introspection tools.

## Enhanced Lab 54 — DNS Incident

Point lab name to wrong IP and prove web config is correct while DNS is wrong.

## Enhanced Lab 55 — SNI Incident

Present wrong default certificate and prove the selected SNI name fixes/identifies vhost selection.

## Enhanced Lab 56 — Backend Protocol Mismatch

Proxy HTTP to a TLS-only backend or vice versa in a controlled lab and identify 502/root cause.

## Enhanced Lab 57 — Maintenance Reload

Change harmless config, validate, reload, compare process behavior and client continuity.

## Enhanced Lab 58 — Backup/Restore Config

Archive Apache/NGINX config, change a lab vhost, restore, validate, and reload.

## Enhanced Lab 59 — Security Review

Audit:

```text
listeners
firewall
SELinux
modules
writable directories
private key mode
backend exposure
```

## Enhanced Lab 60 — Broken Web Tier Challenge

Inject at least 15 faults across:

```text
DNS
route
firewall
SELinux
TLS
virtual host
location
upstream
application
logs
permissions
```

For each document:

```text
symptom
layer
evidence
root cause
minimal fix
verification
prevention
```



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Apache Static Site

1. Install `httpd`.
2. Create a static page.
3. Enable and start the service.
4. Allow HTTP through firewalld.
5. Verify local curl.
6. Verify remote curl.
7. Inspect access and error logs.

### Lab 2 — Apache Virtual Hosts

1. Create `www.alpha.lab`.
2. Create `www.beta.lab`.
3. Use different document roots.
4. Use different access/error logs.
5. Add DNS or lab hosts entries.
6. Verify Host-header routing.
7. Break one ServerName and troubleshoot.

### Lab 3 — SELinux Custom Document Root

1. Create `/srv/www/lab`.
2. Configure an Apache virtual host.
3. Inspect initial SELinux labels.
4. Add persistent `semanage fcontext`.
5. Run `restorecon`.
6. Verify with `ls -Z`.
7. Test with curl.
8. Keep SELinux enforcing.

### Lab 4 — Apache TLS

1. Create a controlled lab certificate.
2. Configure HTTPS.
3. Allow HTTPS in firewalld.
4. Validate Apache syntax.
5. Inspect TLS with `openssl s_client`.
6. Redirect HTTP to HTTPS.
7. Explain why `curl -k` is lab-only.

### Lab 5 — NGINX Static Site

1. Install NGINX.
2. Ensure Apache is not using the same socket on the test machine.
3. Create a server block.
4. Use a custom document root.
5. Validate with `nginx -t`.
6. Verify logs and content.

### Lab 6 — Reverse Proxy

1. Run an authorized test app on TCP/8000.
2. Bind it to loopback.
3. Configure NGINX reverse proxy.
4. Set forwarding headers.
5. Test application directly locally.
6. Test through NGINX.
7. Inspect headers and logs.

### Lab 7 — Two-backend Load Balancer

1. Run backend on web01:8080.
2. Run backend on web02:8080.
3. Make each return hostname.
4. Configure NGINX upstream group.
5. Send repeated requests.
6. Stop one backend.
7. Observe failure behavior.
8. Restore backend.

### Lab 8 — Basic Authentication

1. Configure HTTPS first.
2. Create a lab password file.
3. Protect `/private`.
4. Test without credentials.
5. Test with valid credentials.
6. Explain HTTP 401 behavior.
7. Explain why Basic auth must use TLS.

### Lab 9 — Log Analysis

1. Generate successful requests.
2. Generate 404.
3. Generate 403 in a safe configuration.
4. Generate a redirect.
5. Create status-count report with awk.
6. Identify source IP and user agent.

### Lab 10 — Broken Web Tier

Inject one fault at a time:

1. Apache syntax error.
2. NGINX syntax error.
3. wrong SELinux label.
4. closed firewall.
5. wrong DNS address.
6. wrong upstream port.
7. dead backend.
8. certificate name mismatch.

For every fault:

```text
Symptom:
Layer:
Evidence:
Root cause:
Fix:
Verification:
```

---

## 6. Mini Project

# Mini Project — Production-style Linux Web Tier

Build:

```text
                     Client
                        |
                     HTTPS
                        |
                        v
                  proxy01 / NGINX
                     /       \
                    /         \
                   v           v
             web01:8080    web02:8080
```

## DNS

```text
app.lab.example -> proxy01
```

## proxy01 Requirements

- NGINX installed.
- TCP/80 redirects to HTTPS.
- TCP/443 provides TLS.
- Reverse proxy to both backend nodes.
- Forwarded headers configured.
- Separate logs.
- firewalld exposes only required web ports.
- SELinux remains enforcing.
- Configuration passes `nginx -t`.

## Backend Requirements

Each backend:

- returns its hostname,
- listens on TCP/8080,
- is accessible from proxy01,
- is not unnecessarily exposed to the client network,
- has correct SELinux/firewall policy.

## Verification

Use:

```bash
dig app.lab.example
curl -I http://app.lab.example/
curl -vk https://app.lab.example/
openssl s_client -connect app.lab.example:443 -servername app.lab.example
ss -tlnp
journalctl -u nginx
```

## Documentation

Create:

```text
ARCHITECTURE.md
DNS.md
TLS.md
FIREWALL.md
SELINUX.md
NGINX.md
BACKENDS.md
LOGGING.md
TROUBLESHOOTING.md
```

## Failure Tests

1. web01 fails.
2. web02 fails.
3. both fail.
4. NGINX configuration invalid.
5. HTTPS firewall closed.
6. wrong upstream port.
7. wrong DNS record.
8. certificate hostname mismatch.
9. backend firewall blocks proxy.
10. SELinux blocks proxy connectivity.

Document for every incident:

```text
User-visible symptom
HTTP/network symptom
Failed layer
Evidence
Root cause
Correction
Verification
```

---


# Expanded Capstone — Production-Style Multi-Node Web Platform

Build:

```text
                    client01
                       |
                     DNS
                       |
                 app.lab.example
                       |
                    HTTPS
                       |
                    proxy01
                 NGINX :443
                   /      \
                  /        \
          HTTP/8080       HTTP/8080
             /                \
          web01              web02
           |                   |
        app01                app02
```

Optional:

```text
static content → served directly by proxy01
/api/*         → backend pool
```

## proxy01 Requirements

- NGINX enabled and managed by systemd.
- Port 80 redirects to HTTPS.
- Port 443 terminates TLS.
- Certificate SAN matches `app.lab.example`.
- Reverse proxy/load-balancer upstream contains web01 and web02.
- Forwarded headers configured.
- Backend is not exposed to client network except as designed.
- SELinux remains enforcing.
- firewalld exposes only intended ports.
- `nginx -t` succeeds before reload.
- access/error logs separated for the site.
- request/correlation ID strategy documented.
- TLS expiry check included.

## Backend Requirements

Each backend:

```text
systemd-managed application service
bind only to intended address
health endpoint
returns hostname
separate logs
minimum filesystem permissions
```

Example app:

```python
from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def root():
    return {"backend": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "ok"}
```

## Security Requirements

Document:

```text
TLS trust model
private-key permissions
firewall trust boundary
SELinux policy/Boolean
forwarded-header trust boundary
backend bind addresses
writable directories
security headers
rate limiting decision
```

## Observability

Collect:

```text
request count
2xx/3xx/4xx/5xx count
backend distribution
proxy 502/504 count
application health
TLS expiry
disk/log growth
```

## Failure Tests

At least 20:

```text
DNS points wrong IP
client route failure
proxy firewall 443 closed
NGINX syntax error
certificate expired/not yet valid simulation/documented
certificate hostname mismatch
wrong SNI/default certificate
private key unreadable
wrong NGINX server_name
wrong location
proxy_pass trailing-slash path bug
backend process stopped
backend port wrong
backend firewall blocks proxy
SELinux blocks proxy network connect
one backend slow → timeout
both backends down
forwarded-header trust misconfiguration
application returns 500
log filesystem full simulation
```

Measure for each:

```text
user-visible symptom
HTTP status
failed layer
log evidence
root cause
repair
post-fix verification
```

## Documentation

Create:

```text
ARCHITECTURE.md
DNS_AND_ROUTING.md
TLS_AND_CERTIFICATES.md
NGINX_CONFIGURATION.md
BACKEND_SERVICES.md
FIREWALL.md
SELINUX.md
TRUST_BOUNDARIES.md
LOGGING_AND_METRICS.md
PERFORMANCE.md
SECURITY_REVIEW.md
FAILURE_TESTS.md
CHANGE_AND_ROLLBACK.md
```


## 7. Recommended Resources

Prioritize:

- Red Hat Enterprise Linux 10 documentation for deploying web servers and reverse proxies.
- Apache HTTP Server official documentation.
- NGINX official documentation.
- OpenSSL documentation.
- Red Hat SELinux documentation.
- Red Hat firewalld documentation.
- Local manuals and service documentation.

Useful commands:

```bash
man httpd
man apachectl
man nginx
man openssl
```

---

## 8. Certification Relevance

This is not a standalone RHCSA course, but it applies RHCSA/RHCE skills to one of the most important Linux service categories.

It supports later:

- DevOps
- cloud infrastructure
- reverse proxy and load balancing
- containers
- Kubernetes ingress concepts
- application security
- web penetration testing
- SOC troubleshooting
- SRE and production operations

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Opening firewall ports before confirming a service is listening.  
  **Best practice:** Verify package → service → socket → firewall → network.

- **Mistake:** Using `chmod 777` for web content.  
  **Best practice:** Use correct owner/group/mode and SELinux policy.

- **Mistake:** Disabling SELinux.  
  **Best practice:** Diagnose labels, booleans, and AVC denials.

- **Mistake:** Restarting after a config change without testing syntax.  
  **Best practice:** Use `apachectl configtest` or `nginx -t`.

- **Mistake:** Using `curl -k` permanently.  
  **Best practice:** Fix trust, certificate chain, or hostname problems.

- **Mistake:** Trusting `X-Forwarded-For` from any client.  
  **Best practice:** Trust proxy headers only across controlled proxy boundaries.

- **Mistake:** Exposing backend apps publicly by accident.  
  **Best practice:** Bind/firewall backends according to architecture.

- **Mistake:** Treating 502 and 504 as identical.  
  **Best practice:** Test the upstream and read proxy logs.

- **Mistake:** Storing private keys in ordinary Git repositories.  
  **Best practice:** Use approved secret/key management.

- **Mistake:** Load testing without authorization.  
  **Best practice:** Use a dedicated lab or approved test window.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is a web server?

**Short answer:** A service that accepts HTTP requests and returns HTTP responses, often serving files or proxying to applications.

### Q2. What is a reverse proxy?

**Short answer:** A server that receives client requests and forwards them to backend servers.

### Q3. What is the RHEL Apache service called?

**Short answer:** `httpd`.

### Q4. What validates Apache configuration?

**Short answer:** `apachectl configtest`.

### Q5. What validates NGINX configuration?

**Short answer:** `nginx -t`.

### Q6. What HTTP header is central to name-based virtual hosting?

**Short answer:** `Host`.

### Q7. Why might Apache return 403 even when Unix permissions look correct?

**Short answer:** SELinux policy/context may deny access.

### Q8. What firewalld service normally permits port 80?

**Short answer:** `http`.

### Q9. What firewalld service normally permits port 443?

**Short answer:** `https`.

### Q10. What must remain secret in a TLS deployment?

**Short answer:** The private key.

### Q11. What does a 502 usually indicate at a proxy?

**Short answer:** A problem obtaining/using a valid response from the upstream.

### Q12. What does a 504 usually indicate?

**Short answer:** The proxy timed out waiting for the upstream.

### Q13. What does `ss -tlnp` help verify?

**Short answer:** Listening TCP sockets and owning processes.

### Q14. Why set `X-Forwarded-Proto`?

**Short answer:** So an upstream app can know the original client-side scheme when TLS terminates at the proxy.

### Q15. What is the correct web troubleshooting order?

**Short answer:** Process → socket → SELinux/firewall/network → HTTP → proxy upstream → application.

---


# Enhanced Self-Assessment Bank

### Q1. Web server vs application server?
**Answer:** A web server handles HTTP and can serve/proxy content; an application server executes application logic.

### Q2. Reverse proxy?
**Answer:** Server that receives client requests on behalf of backend services.

### Q3. What comes before HTTP over HTTPS?
**Answer:** DNS/routing, TCP, then TLS.

### Q4. What is SNI?
**Answer:** TLS extension carrying the requested server name so the server can select the correct certificate/TLS vhost.

### Q5. What header drives HTTP/1.1 name-based hosting?
**Answer:** `Host`.

### Q6. 502 vs 504?
**Answer:** 502 means bad/unusable upstream response/connection; 504 means upstream response timed out.

### Q7. What does 413 mean?
**Answer:** Request body too large for a configured limit.

### Q8. What does 429 mean?
**Answer:** Too many requests/rate limiting.

### Q9. What does `apachectl -S` show?
**Answer:** Parsed virtual-host configuration and selection details.

### Q10. What does `nginx -T` show?
**Answer:** Effective NGINX configuration including included files.

### Q11. Why validate config before reload?
**Answer:** Prevent a syntax/configuration error from breaking the service.

### Q12. Directory vs Location in Apache?
**Answer:** Filesystem path vs URL-space matching.

### Q13. Why is `chmod 777` wrong for web troubleshooting?
**Answer:** It weakens DAC and does not solve SELinux/architecture problems.

### Q14. What does `restorecon` do?
**Answer:** Applies expected SELinux context from policy mappings.

### Q15. What is `httpd_sys_content_t` conceptually?
**Answer:** Common SELinux type for web-server-readable content in appropriate policy.

### Q16. Why minimize Apache modules?
**Answer:** Reduce unnecessary features, complexity, and attack surface.

### Q17. Why can `.htaccess` be harder to operate?
**Answer:** It fragments configuration into content directories and can complicate auditing/troubleshooting.

### Q18. NGINX master vs worker?
**Answer:** Master manages configuration/lifecycle; workers handle request/event processing.

### Q19. `root` vs `alias` in NGINX?
**Answer:** Root appends URI path to root path; alias replaces matched location path semantics.

### Q20. Why can trailing slash in `proxy_pass` matter?
**Answer:** It can change how the request URI is rewritten before forwarding upstream.

### Q21. Why trust `X-Forwarded-For` only from known proxies?
**Answer:** Clients can forge it if they can reach the backend directly.

### Q22. Loopback-bound backend?
**Answer:** Reachable only locally, useful when local proxy is the only intended client.

### Q23. What does `ss -tlnp` prove?
**Answer:** Which TCP sockets are listening and often owning processes.

### Q24. Does open firewall mean service works?
**Answer:** No.

### Q25. Does active systemd service mean HTTP health is good?
**Answer:** No.

### Q26. TLS termination?
**Answer:** Proxy decrypts client TLS and forwards request onward.

### Q27. End-to-end TLS?
**Answer:** TLS also protects proxy-to-backend connection.

### Q28. What must remain secret in TLS?
**Answer:** Private key.

### Q29. Why SAN matters?
**Answer:** Client hostname validation checks certificate subject alternative names.

### Q30. Why can connecting by IP fail TLS hostname validation?
**Answer:** Certificate may identify a DNS name rather than the IP.

### Q31. What does `curl --resolve` help test?
**Answer:** Force name→IP mapping while preserving hostname/SNI.

### Q32. HSTS risk?
**Answer:** Browsers can be forced to HTTPS, so bad rollout can lock users into broken TLS.

### Q33. Basic auth without TLS safe?
**Answer:** No.

### Q34. Why separate writable uploads from static application files?
**Answer:** Limit web-process write access and code modification risk.

### Q35. Why should backend process be systemd-managed?
**Answer:** Reliable lifecycle, restart policy, logging, boot integration.

### Q36. What is a UNIX socket upstream?
**Answer:** Local IPC endpoint represented by filesystem path rather than TCP port.

### Q37. Why can UNIX socket fail?
**Answer:** Path permissions, parent traversal, SELinux, service startup, socket owner/mode.

### Q38. What is WebSocket?
**Answer:** HTTP-upgraded persistent bidirectional connection.

### Q39. Why tune timeouts from measurements?
**Answer:** Too short breaks valid requests; too long wastes resources on failed/slow upstreams.

### Q40. Why request-size limits must be coordinated?
**Answer:** Different layers can reject the same request at different sizes.

### Q41. Stateless backend?
**Answer:** Request can be handled by any backend without relying on local per-node session state.

### Q42. Why can local sessions break load balancing?
**Answer:** Next request may reach another backend without the session.

### Q43. Weight 3:1 guarantees exact every four requests?
**Answer:** No; it expresses relative preference, not exact visible sequence.

### Q44. What is request correlation ID?
**Answer:** Identifier propagated across tiers to connect logs for one request.

### Q45. Why monitor TLS expiry?
**Answer:** Prevent certificate-expiration outages.

### Q46. What is file-descriptor exhaustion?
**Answer:** Process reaches open-file/socket limit and cannot accept/open more resources.

### Q47. Is low latency enough to judge health?
**Answer:** No; include errors, availability, saturation, and dependencies.

### Q48. Compression equals encryption?
**Answer:** No.

### Q49. Why cache authenticated responses carefully?
**Answer:** Incorrect cache keys/policy can expose private data.

### Q50. Rate limiting by proxy IP can be wrong when?
**Answer:** When many users share one NAT/proxy address or real-client extraction is misconfigured.

### Q51. Why load testing requires authorization?
**Answer:** It can degrade or deny service.

### Q52. Why avoid directory listing?
**Answer:** It can expose files, backups, and internal structure.

### Q53. Best first step for Apache start failure?
**Answer:** `apachectl configtest`.

### Q54. Best first step for NGINX start failure?
**Answer:** `nginx -t`.

### Q55. Local works, remote fails — likely layers?
**Answer:** Bind address, firewall, routing, DNS/network path.

### Q56. Wrong site served — likely layers?
**Answer:** DNS, Host/SNI, default vhost/server block, server name/config order.

### Q57. 502 first upstream test?
**Answer:** Test backend directly from the proxy host.

### Q58. 504 investigation?
**Answer:** Backend latency, overload, network delay, external dependency, timeout policy.

### Q59. What makes a web change complete?
**Answer:** Syntax validation, reload, local/remote tests, logs/metrics, persistence/rollback documentation.

### Q60. Core troubleshooting principle?
**Answer:** Debug the request path layer-by-layer and change only the layer proven to be wrong.


## Completion Checklist

- [ ] I can install and configure Apache.
- [ ] I can create multiple Apache virtual hosts.
- [ ] I can configure custom content with correct SELinux labels.
- [ ] I can configure and inspect TLS in a lab.
- [ ] I can install and configure NGINX.
- [ ] I can build an NGINX reverse proxy.
- [ ] I can build a two-backend load balancer.
- [ ] I can troubleshoot 403, 404, 500, 502, and 504 problems.
- [ ] I can reason across process, socket, DNS, firewall, SELinux, TLS, and upstream layers.
- [ ] I completed all labs and the web-tier mini project.
