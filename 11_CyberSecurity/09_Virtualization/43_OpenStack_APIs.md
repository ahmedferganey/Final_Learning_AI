# 43. OpenStack APIs

> Phase 9 — Virtualization

OpenStack is fundamentally an **API-driven cloud platform**.

Horizon and the `openstack` CLI are clients. They ultimately communicate with the same service APIs that your own automation can consume.

The key architecture is:

```text
Application / CLI / Terraform / SDK
             |
             | HTTPS
             v
          Keystone
      Authentication
             |
             | Token + Service Catalog
             v
   +---------+----------+----------+----------+
   |                    |          |          |
 Nova API          Neutron API  Cinder API  Glance API
 Compute            Network       Volume      Image
   |                    |          |          |
   +--------------------+----------+----------+
                        |
                  Other APIs
        Heat / Octavia / Barbican /
        Swift / Manila / Ironic /
        Designate / Placement
```

A raw REST workflow usually looks like:

```text
Credentials
   ↓
POST /v3/auth/tokens
   ↓
X-Subject-Token
   ↓
Read Service Catalog
   ↓
Choose Endpoint
   ↓
Send X-Auth-Token
   ↓
Call Service API
   ↓
HTTP Status + JSON + Request ID
```

A production application should usually let `openstacksdk` and `keystoneauth` handle authentication, catalog discovery, sessions, retries, and endpoint selection rather than manually implementing the entire protocol. Raw `curl` remains essential because it teaches what the SDK is doing.

**Reference baseline:** OpenStack **2026.1 Gazpacho** API documentation.

The teaching pattern is:

```text
API Concept
   ↓
HTTP Request
   ↓
JSON Body
   ↓
Response
   ↓
SDK Equivalent
   ↓
Error Handling
   ↓
Automation Pattern
```

---

## 1. Topic Title

**OpenStack APIs**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain REST and HTTP in the context of OpenStack.
- Explain endpoint discovery, service catalogs, regions, and endpoint interfaces.
- Authenticate directly with Keystone v3.
- Explain `X-Subject-Token` versus `X-Auth-Token`.
- Explain project, domain, system, and unscoped/scoped authentication concepts.
- Explain application credentials and why they are preferable to embedding user passwords in automation.
- Explain token expiration and secure token handling.
- Explain major API versions versus microversions.
- Discover API versions and supported microversion ranges.
- Use Nova's `OpenStack-API-Version: compute ...` model.
- Use Cinder's `OpenStack-API-Version: volume ...` model.
- Explain request IDs and cross-service tracing.
- Understand JSON request/response bodies.
- Understand GET, POST, PUT, PATCH, DELETE, idempotency, and asynchronous cloud operations.
- Understand HTTP status codes used by OpenStack.
- Use `curl` safely.
- Use environment variables without leaking secrets into scripts/logs.
- Use `clouds.yaml`.
- Use OpenStackClient debug output to learn API behavior.
- Use Python `requests` for raw calls.
- Use `keystoneauth1` sessions/adapters.
- Use `openstacksdk` connections and service proxies.
- Create/list/show/delete Nova servers.
- Work with flavors, key pairs, server actions, metadata, and server groups.
- Explain Nova microversions.
- Create/list/update/delete Neutron networks, subnets, ports, routers, security groups, and floating IPs.
- Create/list/update/delete Cinder volumes, snapshots, backups, and attachments conceptually.
- Upload/download/list Glance images.
- Work with Swift accounts, containers, and objects.
- Use Heat stack APIs.
- Use Octavia load-balancer APIs conceptually.
- Use Barbican secret APIs securely.
- Use Manila shared-filesystem APIs conceptually.
- Use Ironic bare-metal APIs and its microversion model conceptually.
- Use Designate DNS APIs conceptually.
- Understand Placement API resources and why ordinary tenant applications rarely call Placement directly.
- Implement pagination.
- Implement timeouts, retries, backoff, and safe polling.
- Distinguish synchronous HTTP success from asynchronous resource completion.
- Handle 400, 401, 403, 404, 409, 413, 429, 500, 503, and timeout failures.
- Write idempotent cloud automation.
- Avoid duplicate resource creation.
- Use tags/metadata for ownership.
- Design cleanup/rollback logic.
- Write API unit/integration tests.
- Protect credentials, tokens, TLS, and logs.
- Build a small OpenStack automation service using Python.

---

## 3. Prerequisites

Required:

- 41. OpenStack Fundamentals
- 42. OpenStack Deployment and Operation
- HTTP basics
- JSON
- Python fundamentals
- Linux shell
- basic networking

Recommended environment:

```text
OpenStack cloud
   |
clouds.yaml
   |
Python virtual environment
```

Install tools:

```bash
python3 -m venv ~/venvs/openstack-api
source ~/venvs/openstack-api/bin/activate

pip install -U pip
pip install \
  python-openstackclient \
  openstacksdk \
  keystoneauth1 \
  requests
```

Do not put real production passwords or tokens in course notes, screenshots, Git repositories, terminal recordings, or CI logs.

---

## 4. Core Concepts Explanation

# Part 1 — OpenStack Is API First

The CLI and Horizon are clients of service APIs.

```text
openstack server create
       ↓
Nova REST API

openstack network create
       ↓
Neutron REST API
```

Learning the APIs explains both user automation and the behavior of higher-level tools.

# Part 2 — REST Resource Model

REST APIs expose resources through URLs.

```text
/servers
/networks
/volumes
/images
```

Operations use HTTP methods to read or change those resources.

# Part 3 — HTTP Methods

Common semantics:

```text
GET     read
POST    create/action
PUT     replace/update depending on API
PATCH   partial update
DELETE  remove
```

Do not assume every OpenStack service uses identical update semantics; read the service API contract.

# Part 4 — HTTP Request Structure

A request contains:

```text
Method
URL
Headers
Body
```

Example:

```http
GET /v2.1/servers HTTP/1.1
Host: compute.example
X-Auth-Token: ...
Accept: application/json
```

# Part 5 — HTTP Response Structure

Response contains:

```text
Status code
Headers
Body
```

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-OpenStack-Request-ID: req-...

{"servers": [...]}
```

# Part 6 — JSON

OpenStack APIs commonly exchange JSON.

```json
{
  "server": {
    "name": "web01",
    "flavorRef": "FLAVOR_ID"
  }
}
```

Your program must validate both HTTP status and expected JSON structure.

# Part 7 — HTTPS and TLS

Production API calls should use trusted HTTPS.

Bad lab shortcut:

```bash
curl -k ...
```

`-k` disables certificate verification. Use it only in a disposable lab; production clients should trust the correct CA and verify endpoint identity.

# Part 8 — Authentication vs Authorization

Authentication:

```text
Who are you?
```

Authorization:

```text
Are you allowed to perform this operation?
```

This maps directly to common errors:

```text
401 → authentication
403 → authorization
```

# Part 9 — Keystone

Keystone provides identity, token issuance, and the service catalog.

```text
Credentials
   ↓
Keystone
   ↓
Token + Catalog
```

Other services validate the token before serving protected requests.

# Part 10 — Keystone v3 Token Endpoint

Authentication uses:

```text
POST /v3/auth/tokens
```

A successful response is normally:

```text
201 Created
```

and the issued token is returned in the `X-Subject-Token` response header.

# Part 11 — Password Authentication Body

Conceptual project-scoped body:

```json
{
  "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "api-user",
          "domain": {"name": "Default"},
          "password": "REDACTED"
        }
      }
    },
    "scope": {
      "project": {
        "name": "demo",
        "domain": {"name": "Default"}
      }
    }
  }
}
```

# Part 12 — Raw Keystone `curl`

Example lab pattern:

```bash
curl -si   -X POST   -H 'Content-Type: application/json'   -d @auth.json   https://identity.example/v3/auth/tokens
```

Inspect the response headers for `X-Subject-Token`.

# Part 13 — `X-Subject-Token`

For Keystone v3 token creation, the token value is returned in:

```text
X-Subject-Token
```

The JSON body contains token metadata and catalog information, but the credential itself is in the response header.

# Part 14 — `X-Auth-Token`

When calling protected OpenStack services, send the issued token using:

```http
X-Auth-Token: <TOKEN>
```

Keystone therefore uses:

```text
X-Subject-Token → token being issued/inspected
X-Auth-Token    → credential authenticating a request
```

# Part 15 — Token Expiration

Tokens expire.

Automation should:

```text
authenticate through SDK/session
cache token temporarily
refresh when required
never assume token is permanent
```

Do not build long-running systems around a copied shell token.

# Part 16 — Unscoped Token

An unscoped token identifies the user but is not bound to a project/domain/system scope.

Most resource APIs require a scoped token because authorization depends on project and role assignments.

# Part 17 — Project Scope

Project-scoped token says:

```text
user X
acting in project Y
with roles Z
```

Most tenant operations—servers, networks, volumes—use project scope.

# Part 18 — Domain Scope

Domain scope is used for domain-level identity administration where policy allows it.

It is not the ordinary scope for launching a VM in a tenant project.

# Part 19 — System Scope

Some administrative APIs support system-scoped authorization.

This separates cloud-wide administration from project administration.

Always use the narrowest scope required.

# Part 20 — Application Credentials

Application credentials let automation authenticate without embedding the user's primary password.

```text
User
  ↓ creates
Application Credential
  ↓
Automation
```

They can be scoped/restricted and revoked independently.

# Part 21 — Why Application Credentials Matter

If a CI system stores a user's password, compromise affects every role and future password usage.

An application credential creates a separate revocable identity secret with narrower intent.

# Part 22 — Service Catalog

The token includes a service catalog.

It tells clients:

```text
service type
service name
region
interface
endpoint URL
```

Clients should discover endpoints from the catalog rather than hard-code every API URL.

# Part 23 — Service Type

Examples:

```text
identity
compute
network
image
volumev3
object-store
orchestration
load-balancer
key-manager
shared-file-system
baremetal
dns
placement
```

The exact catalog depends on the cloud.

# Part 24 — Endpoint Interfaces

Keystone catalog endpoints can be exposed as:

```text
public
internal
admin
```

A client chooses an interface according to network location and use case.

# Part 25 — Region

A cloud may expose the same service in multiple regions.

```text
RegionOne
RegionTwo
```

Automation should explicitly select the intended region instead of assuming only one exists.

# Part 26 — Catalog Inspection

CLI:

```bash
openstack catalog list
openstack catalog show compute
openstack endpoint list
```

This is often the first diagnostic when a client calls the wrong URL.

# Part 27 — Major API Version

Major versions are often represented in endpoint paths.

Examples:

```text
Keystone /v3
Nova     /v2.1
Cinder   /v3
```

A major version identifies a discrete API endpoint family.

# Part 28 — Microversions

Some services evolve within a major API using microversions.

Concept:

```text
Compute API v2.1
   |
   +-- microversion 2.x
```

Microversions let clients opt into newer behavior without breaking older clients.

# Part 29 — Nova Microversion Header

Nova accepts the service-specific header and, for modern microversions, the generic form.

Example:

```http
OpenStack-API-Version: compute 2.27
```

Older compatible form:

```http
X-OpenStack-Nova-API-Version: 2.27
```

# Part 30 — Cinder Microversion Header

Cinder v3 uses:

```http
OpenStack-API-Version: volume 3.x
```

If no microversion is specified, Cinder uses its minimum compatible behavior for the v3 API.

# Part 31 — Version Discovery

Clients can query service roots to discover supported API versions and, for microversioned services, minimum/maximum microversions.

Do not blindly request `latest` in production automation if behavior changes could matter.

# Part 32 — Keystoneauth Discovery

`keystoneauth1` can discover:

```text
service endpoint
major API version
minimum microversion
maximum microversion
```

This is safer than manually parsing every service URL.

# Part 33 — Request IDs

OpenStack responses commonly include request identifiers such as:

```text
X-OpenStack-Request-ID: req-...
```

Record them when reporting an error because operators can correlate the same request across service logs.

# Part 34 — Global Request ID Concept

Nova supports a caller-supplied global request ID in supported microversions.

This allows one upstream transaction to be correlated through multiple OpenStack calls.

Use a valid `req-<UUID>` form when the API supports it.

# Part 35 — HTTP 200

`200 OK` generally means the requested synchronous read/update operation completed successfully.

Still validate the response body; an application should not assume all required fields exist.

# Part 36 — HTTP 201

`201 Created` indicates successful resource/token creation in APIs that use this code.

Keystone token creation is a key example.

# Part 37 — HTTP 202

`202 Accepted` means the API accepted an asynchronous request, not that the cloud resource has finished changing.

Example mental model:

```text
POST server
→ 202
→ server BUILD
→ later ACTIVE or ERROR
```

# Part 38 — HTTP 204

`204 No Content` commonly indicates successful deletion/update without response body.

Do not attempt to parse JSON unconditionally after every successful API call.

# Part 39 — HTTP 400

`400 Bad Request` often indicates malformed JSON, invalid argument, unsupported value, or microversion mismatch.

Validate your request schema before retrying.

# Part 40 — HTTP 401

`401 Unauthorized` suggests missing/invalid/expired authentication.

Check:

```text
token
auth URL
credential
scope
time
```

# Part 41 — HTTP 403

`403 Forbidden` means the request identity is known but policy/role/scope does not permit the operation.

Changing the password will not fix RBAC.

# Part 42 — HTTP 404

`404 Not Found` may mean:

```text
resource ID does not exist
wrong project visibility
wrong endpoint/path
wrong API version
```

Do not assume "server down."

# Part 43 — HTTP 409

`409 Conflict` often indicates current resource state conflicts with requested action.

Examples:

```text
delete attached resource
resize during another task
duplicate/conflicting state
```

# Part 44 — HTTP 413

`413` can indicate request/entity too large or quota/request-limit conditions depending on service.

Check both HTTP context and OpenStack error body.

# Part 45 — HTTP 429

`429 Too Many Requests` indicates throttling/rate limiting when implemented by the endpoint/proxy.

Use backoff; do not hammer the API more aggressively.

# Part 46 — HTTP 500

`500 Internal Server Error` is server-side failure.

Record:

```text
request ID
endpoint
method
time
body
```

Then correlate server logs.

# Part 47 — HTTP 503

`503 Service Unavailable` indicates service or dependency is temporarily unavailable.

Retry may be appropriate, but only with bounded backoff and idempotency awareness.

# Part 48 — Timeouts

Every production API call should have a timeout.

Without one:

```text
dead endpoint
→ thread/process waits indefinitely
```

Use separate connect/read timeout policy where libraries support it.

# Part 49 — Retry

Retry transient errors such as selected 5xx/network failures.

Do **not** retry every 4xx because an invalid request will remain invalid.

# Part 50 — Exponential Backoff

Example delay progression:

```text
1s
2s
4s
8s
```

Add jitter in distributed systems to avoid many clients retrying simultaneously.

# Part 51 — Idempotency

An idempotent operation can be repeated without unintended extra effect.

`GET` is naturally idempotent. Resource creation with `POST` often is not.

Automation must guard against duplicate creates after ambiguous timeouts.

# Part 52 — Duplicate Create Problem

Scenario:

```text
POST create server
   ↓
server created
   ↓
client times out before receiving response
   ↓
client retries POST
   ↓
second server created
```

Mitigate using deterministic names/tags, reconciliation, and post-timeout discovery.

# Part 53 — Asynchronous Operations

Many cloud changes are asynchronous.

```text
API accepted
   ↓
worker/scheduler performs action
   ↓
resource state changes
```

Clients should poll resource state rather than equating HTTP success with completion.

# Part 54 — Polling

Good polling:

```text
sleep between requests
bounded timeout
terminal success states
terminal failure states
```

Bad:

```python
while True:
    get_status()  # no sleep
```

# Part 55 — Pagination

Large list APIs may paginate.

A client must follow:

```text
limit
marker
next link
```

or SDK pagination helpers.

Never assume one response contains every server in a large cloud.

# Part 56 — Filtering

Prefer server-side filters where available.

```text
GET only ACTIVE servers
```

is more efficient than downloading 100,000 records and filtering locally.

# Part 57 — Sorting

APIs may support sort parameters.

Do not rely on implicit order; explicitly sort when application correctness depends on order.

# Part 58 — Resource UUIDs

OpenStack resources generally use UUID identifiers.

Names are often not globally unique.

Automation should retain IDs:

```text
server_id
network_id
volume_id
```

# Part 59 — Names vs IDs

CLI convenience may resolve a name.

Raw API usually expects an ID.

If two networks share a name, name-based automation becomes ambiguous.

# Part 60 — Tags and Metadata

Use metadata/tags for ownership and reconciliation.

Example:

```text
managed-by=inventory-service
environment=prod
request-id=abc123
```

This helps safe cleanup and drift detection.

# Part 61 — `curl` Safely

Use environment variables rather than typing secrets repeatedly:

```bash
export OS_TOKEN='...'

curl   -H "X-Auth-Token: $OS_TOKEN"   "$COMPUTE_ENDPOINT/servers"
```

Remember shell history/process environments can still expose secrets; SDK credential stores are safer.

# Part 62 — OpenStackClient Debug

Run:

```bash
openstack --debug server list
```

This reveals:

```text
authentication
endpoint discovery
HTTP method
URL
headers
response
```

Redact tokens/passwords before sharing debug logs.

# Part 63 — `clouds.yaml`

Centralize cloud configuration:

```yaml
clouds:
  lab:
    auth:
      auth_url: https://identity.example/v3
      application_credential_id: ...
      application_credential_secret: ...
    region_name: RegionOne
```

Protect file permissions.

# Part 64 — Environment Variables

Legacy scripts may use:

```text
OS_AUTH_URL
OS_USERNAME
OS_PASSWORD
OS_PROJECT_NAME
OS_USER_DOMAIN_NAME
OS_PROJECT_DOMAIN_NAME
```

Avoid committing shell files containing real passwords.

# Part 65 — Python `requests`

Raw REST example:

```python
import requests

r = requests.get(
    url,
    headers={"X-Auth-Token": token},
    timeout=10,
)
r.raise_for_status()
data = r.json()
```

This teaches HTTP mechanics but leaves authentication/catalog handling to you.

# Part 66 — `raise_for_status()`

Always handle failed status codes.

```python
response.raise_for_status()
```

Then catch and enrich the error with request ID and response body without leaking secrets.

# Part 67 — `keystoneauth1` Authentication Plugin

`keystoneauth1` can create authentication plugins for password, token, application credential, and other supported methods.

The plugin obtains/refreshes credentials; your application does not manually copy tokens around.

# Part 68 — `keystoneauth1.session.Session`

A session centralizes:

```text
auth
TLS
requests
endpoint discovery
microversion support
```

Concept:

```python
from keystoneauth1 import session

sess = session.Session(auth=auth)
```

# Part 69 — Endpoint Filtering

Keystoneauth session can choose endpoint based on:

```text
service_type
interface
region_name
major version
```

This prevents hard-coded service URLs.

# Part 70 — Keystoneauth Adapter

An Adapter mounts a Session onto a service.

```python
adapter = Adapter(
    session=sess,
    service_type="compute",
    interface="internal",
    region_name="RegionOne",
)
```

Then requests can use service-relative paths.

# Part 71 — Microversion with Session

Keystoneauth can send requested microversion per call.

Concept:

```python
resp = session.get(
    path,
    microversion="3.15",
    endpoint_filter={"service_type": "volume"},
)
```

This keeps version logic explicit.

# Part 72 — `openstacksdk`

OpenStackSDK provides high-level Python objects and service proxies.

```python
import openstack

conn = openstack.connect(cloud="lab")
```

This is generally preferred over raw `requests` for application automation.

# Part 73 — Connection Object

`Connection` exposes services:

```python
conn.compute
conn.network
conn.block_storage
conn.image
conn.object_store
conn.orchestration
```

Exact proxies depend on installed SDK and cloud services.

# Part 74 — List Servers with SDK

```python
for server in conn.compute.servers():
    print(server.id, server.name, server.status)
```

SDK handles pagination and endpoint/auth behavior.

# Part 75 — Find a Resource

Example:

```python
network = conn.network.find_network(
    "private",
    ignore_missing=False,
)
```

For production automation, prefer IDs or enforce uniqueness.

# Part 76 — Create Resource and Wait

Pattern:

```python
server = conn.compute.create_server(...)
server = conn.compute.wait_for_server(server)
```

The SDK provides wait helpers for asynchronous state transitions.

# Part 77 — Delete and Wait

For cleanup, delete and verify disappearance when correctness requires it.

A returned delete response does not always mean every backend resource is instantly gone.

# Part 78 — Nova API

Compute API handles:

```text
servers
flavors
key pairs
server groups
actions
metadata
interfaces
console
migrations
```

Nova's major API is v2.1 with microversion evolution.

# Part 79 — List Nova Servers Raw

Concept:

```bash
curl   -H "X-Auth-Token: $OS_TOKEN"   "$COMPUTE/v2.1/$PROJECT_ID/servers"
```

Many deployments/catalogs include project-specific paths; use discovered endpoint/version conventions for your cloud.

# Part 80 — Create Server Request

Conceptual body:

```json
{
  "server": {
    "name": "web01",
    "imageRef": "IMAGE_ID",
    "flavorRef": "FLAVOR_ID",
    "networks": [
      {"uuid": "NETWORK_ID"}
    ]
  }
}
```

After the API accepts it, poll until `ACTIVE` or `ERROR`.

# Part 81 — Server Actions

Nova exposes actions through a server action endpoint.

Conceptual operations:

```text
reboot
resize
rebuild
shelve
unshelve
create image
rescue
```

Each action has state constraints.

# Part 82 — Reboot Action

Conceptual JSON:

```json
{
  "reboot": {
    "type": "SOFT"
  }
}
```

A soft reboot requests graceful guest behavior; a hard reboot is more disruptive.

# Part 83 — Server Metadata

Metadata is useful for automation ownership.

Concept:

```json
{
  "metadata": {
    "owner": "platform-team",
    "environment": "prod"
  }
}
```

# Part 84 — Server Groups

Server groups express placement policy such as affinity/anti-affinity where supported.

Automation should create the group first and provide its scheduler hint during server creation.

# Part 85 — Nova Microversion Discovery

Before using a feature that requires a newer microversion:

```text
discover min/max
choose required version
send header
```

Do not assume every cloud runs the same maximum microversion.

# Part 86 — Nova Request ID

Record:

```text
X-OpenStack-Request-ID
```

for failed create/migrate/resize operations. Operators can trace the same request in Nova logs.

# Part 87 — Neutron API

Networking API manages:

```text
networks
subnets
ports
routers
floating IPs
security groups
trunks
QoS
```

Networking resources are highly interconnected.

# Part 88 — Create Network

Conceptual body:

```json
{
  "network": {
    "name": "app-net",
    "admin_state_up": true
  }
}
```

# Part 89 — Create Subnet

Concept:

```json
{
  "subnet": {
    "network_id": "NETWORK_ID",
    "ip_version": 4,
    "cidr": "192.168.50.0/24",
    "name": "app-subnet"
  }
}
```

Validate overlap and address-management policy.

# Part 90 — Neutron Port

A port represents network attachment.

Important fields can include:

```text
network_id
fixed_ips
device_id
device_owner
status
security groups
binding information
```

A server vNIC maps to a Neutron port.

# Part 91 — Router API

Routers connect subnets and external networks.

Automation sequence:

```text
create router
set external gateway
add subnet interface
```

Rollback should reverse this dependency order.

# Part 92 — Floating IP API

Floating IP is a resource mapping external address to a port/fixed IP.

Your application should not assume association is instantly reachable; physical routing and security must also be valid.

# Part 93 — Security Group API

Security-group rules are stateful policy resources.

Avoid automation that repeatedly adds identical rules without first reconciling existing state.

# Part 94 — Cinder API

Block Storage v3 manages:

```text
volumes
snapshots
backups
types
attachments
services
```

It uses microversions through the `volume` API-version header.

# Part 95 — List Volumes

Concept:

```bash
curl   -H "X-Auth-Token: $OS_TOKEN"   -H "OpenStack-API-Version: volume 3.x"   "$VOLUME_ENDPOINT/volumes/detail"
```

Use a version actually supported by the endpoint.

# Part 96 — Create Volume

Conceptual JSON:

```json
{
  "volume": {
    "size": 20,
    "name": "db-data"
  }
}
```

Creation is asynchronous; poll until `available` or `error`.

# Part 97 — Cinder Snapshot

Snapshot represents point-in-time volume state.

Creation requires appropriate volume state/flags and backend support.

Poll snapshot state instead of assuming POST completion means usable snapshot.

# Part 98 — Cinder Backup

Backup APIs create independent backup resources according to configured backend.

Do not confuse Cinder snapshot and backup: they have different durability/failure-domain goals.

# Part 99 — Volume Attachments

Modern volume attachment flows involve Nova and Cinder.

If automating directly, understand attachment lifecycle and microversion requirements; ordinary applications should usually let Nova/SDK manage server-volume attachment.

# Part 100 — Glance API

Image service manages:

```text
image metadata
image data upload/download
visibility
properties
members
```

Image metadata and binary upload are separate API concerns.

# Part 101 — Create Image Metadata

Conceptually:

```json
{
  "name": "ubuntu-base",
  "disk_format": "qcow2",
  "container_format": "bare",
  "visibility": "private"
}
```

Then upload image data to the created image resource.

# Part 102 — Image Upload

Binary image data uses an upload endpoint and content type appropriate to the API.

Large uploads require:

```text
timeouts
streaming
checksums/integrity
backend capacity
```

# Part 103 — Image Download

For large images, stream to disk rather than loading the whole image into RAM.

Verify integrity using available hash/checksum metadata.

# Part 104 — Swift Object API

Swift models:

```text
Account
  ↓
Container
  ↓
Object
```

Unlike Cinder, objects are accessed over HTTP rather than attached as VM block devices.

# Part 105 — Create Swift Container

Concept:

```http
PUT /v1/AUTH_project/backups
X-Auth-Token: ...
```

A container is similar to a bucket namespace.

# Part 106 — Upload Swift Object

Concept:

```http
PUT /v1/AUTH_project/backups/report.json
```

The request body is the object data.

Use streaming for large files.

# Part 107 — Swift Metadata

HTTP headers can store object/container metadata.

Avoid placing sensitive secrets in metadata merely because the object body is encrypted.

# Part 108 — Heat API

Heat manages stacks from templates.

Resources:

```text
stacks
resources
events
software deployments
```

Stack creation is asynchronous and should be monitored through stack status/events.

# Part 109 — Heat Stack Create

Concept:

```text
POST stack
  template
  parameters
  environment
```

Poll:

```text
CREATE_IN_PROGRESS
→ CREATE_COMPLETE
or CREATE_FAILED
```

# Part 110 — Heat Events

When a stack fails, inspect resource events.

A Heat error may simply wrap a Nova/Neutron/Cinder failure. Follow the nested request/resource chain.

# Part 111 — Octavia API

Load-balancer resources commonly include:

```text
load balancer
listener
pool
member
health monitor
```

Provisioning is asynchronous and has both operating and provisioning status.

# Part 112 — Octavia Resource Dependency

Correct order:

```text
load balancer
 ↓
listener
 ↓
pool
 ↓
members
 ↓
health monitor
```

Deletion often needs the reverse dependency order.

# Part 113 — Barbican API

Barbican stores secrets.

Never print secret payloads into application logs.

Use separate permissions for:

```text
secret metadata
secret payload
container
ACL
```

# Part 114 — Secret Creation

Conceptual request contains secret metadata and possibly payload depending on API workflow.

Use TLS and restrict automation identities because secret-service access is inherently sensitive.

# Part 115 — Manila API

Shared File Systems API manages:

```text
shares
share networks
share types
access rules
snapshots
```

A share is a network filesystem resource, not a Cinder block volume.

# Part 116 — Manila Access Rules

After creating a share, clients may need an access rule:

```text
IP
user
certificate
```

depending on protocol/backend.

Security depends on both OpenStack access rule and network reachability.

# Part 117 — Ironic API

Ironic manages physical nodes.

Resources include:

```text
nodes
ports
port groups
drivers
allocations
```

Bare-metal changes can affect real physical hardware, so API automation must be especially guarded.

# Part 118 — Ironic Microversion

Ironic supports its own API-version header model.

Clients should request a supported version rather than depending on very old default behavior.

# Part 119 — Designate API

DNS API manages:

```text
zones
recordsets
pools/backends administratively
```

Deleting a zone can have immediate external service impact.

# Part 120 — Create DNS Recordset Concept

Example logical resource:

```text
Zone: example.internal.
Record: api.example.internal.
Type: A
Value: 10.10.10.250
```

Automation should respect TTL and eventual DNS propagation.

# Part 121 — Placement API

Placement manages:

```text
resource providers
inventories
traits
allocations
allocation candidates
```

It primarily serves schedulers/operators rather than ordinary tenant application workflows.

# Part 122 — Why Not Call Placement for Normal VM Create?

Nova owns the scheduling workflow.

If an application separately allocates Placement resources without Nova coordination, cloud state can become inconsistent.

Use Nova unless building a component explicitly designed for Placement integration.

# Part 123 — CLI vs SDK vs Raw REST

Use:

```text
CLI
  operator/manual scripting

SDK
  application automation

Raw REST
  learning/debugging/special integration
```

Do not write hundreds of lines of custom authentication code when a maintained SDK already solves it.

# Part 124 — SDK Resource Objects

SDK objects wrap JSON resources.

Example:

```python
server.id
server.name
server.status
```

Do not assume every field is loaded; SDKs may lazily fetch detail or vary with microversion.

# Part 125 — SDK Exceptions

Catch meaningful SDK/HTTP exceptions and convert them into application-specific errors.

Log:

```text
operation
resource ID
request ID
status
```

but not token/password/secret payload.

# Part 126 — Connection Pooling

Reuse HTTP sessions/connections.

Bad:

```text
new TCP/TLS/auth session for every call
```

Better:

```text
long-lived authenticated SDK session
```

This reduces latency and control-plane load.

# Part 127 — Timeout Policy

Define:

```text
connect timeout
read timeout
overall operation timeout
```

A server create may need 5 minutes even though each API request should have a 10-second network timeout.

# Part 128 — Operation Timeout vs HTTP Timeout

These are different:

```text
HTTP timeout:
one request did not answer

Operation timeout:
resource never reached desired state
```

Handle both separately.

# Part 129 — Retryable vs Non-Retryable

Potentially retry:

```text
connection reset
503
selected 500
429
```

Usually do not retry unchanged:

```text
400
401 with invalid permanent credential
403
404 for required missing resource
```

# Part 130 — Conflict Handling

A 409 may be temporary because another asynchronous task is running.

Example:

```text
server resize in progress
→ reboot request conflicts
```

Wait for resource state rather than retrying immediately.

# Part 131 — Reconciliation Loop

Declarative automation should compare desired vs actual state.

```text
Desired:
network app-net exists

Actual:
missing
   ↓
create

Actual:
exists correctly
   ↓
no change
```

This is safer than blindly executing create every run.

# Part 132 — Idempotent Resource Creation

Pattern:

```python
resource = find_resource(name)
if resource is None:
    resource = create_resource()
```

Then validate configuration, not just existence.

# Part 133 — Drift Detection

A resource may exist but differ:

```text
desired CIDR 192.168.10.0/24
actual CIDR 192.168.20.0/24
```

Decide:

```text
update
replace
fail safely
```

Never silently assume name match means configuration match.

# Part 134 — Transactional Thinking Across APIs

OpenStack operations span multiple services but HTTP does not provide one distributed transaction.

Example:

```text
network created
server create fails
```

Your automation must decide whether to retain or clean the network.

# Part 135 — Compensating Actions

A Saga-style workflow uses rollback/compensation.

```text
create network
create subnet
create server
server fails
   ↓
delete subnet
delete network
```

Only delete resources that your workflow owns.

# Part 136 — Ownership Tags

Mark automation-created resources:

```text
managed-by=my-service
workflow-id=...
expires-at=...
```

This prevents cleanup code from deleting manually managed production resources.

# Part 137 — Cleanup Safety

Before deleting:

```text
verify project
verify ID
verify ownership tag
verify dependency
verify current state
```

Never implement `delete everything with prefix test-` as the only safeguard.

# Part 138 — Concurrency

Two automation workers may try to create the same resource simultaneously.

Mitigations:

```text
locking
unique deterministic identifiers
recheck after conflict
database uniqueness
```

# Part 139 — Rate Limits and Thundering Herd

If 10,000 agents poll every second:

```text
API overloaded
```

Use:

```text
event-driven callbacks where possible
adaptive polling
jitter
batching
```

# Part 140 — Caching Catalog/Discovery

Endpoint discovery does not need to run from scratch for every request.

Keystoneauth sessions cache discovery metadata, reducing unnecessary calls.

# Part 141 — API Security — Least Privilege

Give automation only the roles/scope it needs.

A monitoring service that only lists servers should not receive cloud-admin permissions.

# Part 142 — API Security — Application Credentials

Prefer application credentials for automation where supported.

Rotate/revoke independently without changing a human user's password.

# Part 143 — API Security — Token Logging

Never log:

```text
X-Auth-Token
X-Subject-Token
application credential secret
Barbican payload
password
```

Use redaction middleware.

# Part 144 — API Security — TLS Verification

Certificate verification protects against endpoint impersonation.

Production code should provide the CA bundle/trust store instead of `verify=False`.

# Part 145 — API Security — Secrets at Rest

Store API credentials in:

```text
secret manager
encrypted CI variables
protected credential file
workload identity system
```

not source code.

# Part 146 — API Security — Scope

A credential can be correctly authenticated and still dangerously over-scoped.

Review:

```text
project
domain/system scope
roles
service permissions
```

# Part 147 — Audit and Correlation

Log:

```text
caller
operation
resource
project
request ID
result
latency
```

This supports incident response without exposing credentials.

# Part 148 — API Testing Pyramid

Test at multiple levels:

```text
unit tests
  mock HTTP/SDK

integration tests
  real test project

end-to-end tests
  create/use/delete actual resources
```

# Part 149 — Mocking

Unit tests can mock SDK calls:

```python
fake_compute.create_server.assert_called_once()
```

Do not claim this proves the real cloud is compatible.

# Part 150 — Integration Test Project

Use a dedicated test project with quotas and cleanup.

Never run destructive API test suites against production tenant projects accidentally.

# Part 151 — Contract Tests

Validate assumptions such as:

```text
required service exists
minimum microversion available
image/flavor present
network features enabled
```

Fail early if the cloud cannot satisfy your application contract.

# Part 152 — Microversion Contract

If your software requires a Nova feature introduced in microversion X:

```text
discover max
if max < X:
    fail with clear compatibility message
```

Do not make the call and hope.

# Part 153 — Multi-Cloud Portability

Different OpenStack clouds vary in:

```text
regions
flavors
images
networks
extensions
microversions
policies
```

Avoid hard-coding provider-specific resource IDs.

# Part 154 — Capabilities Discovery

Before using optional features, inspect service availability and API extensions/capabilities.

Your automation should degrade gracefully when a cloud lacks an optional service.

# Part 155 — Service Unavailable Strategy

If Cinder is unavailable but your workflow can use ephemeral disks:

```text
fallback only if business requirements permit
```

Do not silently downgrade durability.

# Part 156 — Observability Metrics

Track:

```text
API latency
success rate
status codes
retry count
token refresh
operation completion time
request IDs
resource error rate
```

# Part 157 — API Latency vs Cloud Operation Latency

A Nova POST may return in 200 ms while the server needs 60 seconds to become ACTIVE.

Measure both:

```text
API request latency
resource provisioning latency
```

# Part 158 — SLOs

Example:

```text
99.9% API request success
95% VM creation < 120s
```

Define SLOs from user/business requirements, not arbitrary numbers.

# Part 159 — Circuit Breaker Concept

If an API is persistently failing:

```text
stop flooding it
fail fast temporarily
probe recovery
resume gradually
```

This protects both client and cloud.

# Part 160 — Bulk Operations

Large automation should batch and pace operations.

Launching 5,000 VMs simultaneously can overload schedulers, images, storage, DHCP, and compute even if quota allows it.

# Part 161 — CLI Debug as API Learning Tool

For any CLI command:

```bash
openstack --debug ...
```

observe the real REST call, then reproduce it with `curl` or SDK.

This is one of the fastest ways to learn OpenStack API behavior.

# Part 162 — API Documentation Reading Strategy

For an endpoint, identify:

```text
method/path
required role/policy
microversion
request schema
response schema
status codes
errors
asynchronous state
```

Do not copy a JSON example without reading its version requirements.

# Part 163 — Deprecated APIs

Avoid new automation against deprecated endpoints.

Use the current API index and current endpoints rather than blog posts targeting obsolete OpenStack releases.

# Part 164 — SDK Versioning

Pin/test your `openstacksdk` dependency.

A cloud upgrade and SDK upgrade are separate events; test their compatibility independently.

# Part 165 — API Error Wrapper

A production client should return a useful internal error:

```text
Operation: create server
HTTP: 409
Request-ID: req-...
Cloud: prod
Resource: web01
Message: server currently locked by resize task
```

without leaking token/body secrets.

# Part 166 — Safe Python Retry Example

Concept:

```python
for attempt in range(max_attempts):
    try:
        return call()
    except RetryableError:
        sleep(backoff(attempt))
raise OperationFailed()
```

Classify the exception before retrying.

# Part 167 — Server Provisioning Workflow

A robust workflow:

```text
find image/flavor/network
validate quota/capability
create server
record ID immediately
poll
if ACTIVE → success
if ERROR → capture fault/request ID
if timeout → inspect server by ID before retry/create
```

# Part 168 — Network Provisioning Workflow

```text
find/create network
find/create subnet
find/create router
attach subnet
configure gateway
create security groups
validate connectivity
```

Each resource should be tagged/owned for cleanup.

# Part 169 — Volume Provisioning Workflow

```text
create volume
wait available
attach
wait in-use
verify server attachment
```

On failure, determine whether the volume is safe to delete or must be preserved for investigation.

# Part 170 — Final API Engineering Mental Model

Do not think:

```text
"I called the API, therefore the cloud did it."
```

Think:

```text
I authenticated
discovered the right endpoint/version
submitted an operation
received a request ID
tracked asynchronous state
handled partial failure
verified final resource
recorded ownership
protected credentials
```

That is production-grade OpenStack API engineering.

---

# Enhanced Deep-Study Layer — OpenStack API Engineering

This layer preserves the uploaded API course and expands it into production-oriented cloud API engineering.

```text
Secure Auth → Discovery → Version Contract → Request → Request ID
→ Async State → Retry/Reconcile → Final Verification → Audit
```

The uploaded source uses **OpenStack 2026.1 “Gazpacho”** API documentation as its reference baseline. Exact schemas, maximum microversions, extensions, and policy rules must be discovered from the target cloud.


## Advanced Deep Dive 1 — API-first architecture

### Concept

Horizon, CLI, Terraform, SDKs, and custom apps all consume OpenStack service APIs.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server list
openstack --debug network list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **API-first architecture**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 2 — HTTP request anatomy

### Concept

Method, URL, headers, body, TLS, and timeout together define the request contract.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -v -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP request anatomy**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 3 — HTTP response anatomy

### Concept

Status, headers, body, and request ID must all be inspected.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP response anatomy**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 4 — Keystone v3 token exchange

### Concept

POST /v3/auth/tokens returns the credential in X-Subject-Token and token metadata/catalog in the body.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si -X POST -H 'Content-Type: application/json' -d @auth.json "$IDENTITY/v3/auth/tokens"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Keystone v3 token exchange**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 5 — X-Subject-Token versus X-Auth-Token

### Concept

X-Subject-Token identifies the issued/inspected token; X-Auth-Token authenticates protected service requests.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **X-Subject-Token versus X-Auth-Token**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 6 — Project, domain, and system scopes

### Concept

Authorization is evaluated in a scope; tenant operations normally use project scope while administrative operations may use domain/system scope.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack token issue
openstack role assignment list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Project, domain, and system scopes**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 7 — Application credentials

### Concept

Application credentials give automation a revocable scoped secret instead of a human password.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack application credential list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Application credentials**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 8 — Service catalog discovery

### Concept

Clients should discover service endpoints by service type, region, and interface rather than hard-code URLs.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack catalog list
openstack endpoint list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Service catalog discovery**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 9 — Regions and endpoint interfaces

### Concept

The same service may expose public/internal/admin-style endpoints in multiple regions.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack catalog show compute
openstack endpoint list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Regions and endpoint interfaces**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 10 — Major API versions

### Concept

Major versions select endpoint families such as Keystone v3, Nova v2.1, and Cinder v3.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug token issue
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Major API versions**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 11 — Microversions

### Concept

Microversions let Nova/Cinder/Ironic evolve behavior within a compatible major API.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Microversions**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 12 — Nova microversion header

### Concept

Nova can use OpenStack-API-Version: compute <version>.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -H "OpenStack-API-Version: compute 2.XX" -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova microversion header**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 13 — Cinder microversion header

### Concept

Cinder v3 can use OpenStack-API-Version: volume <version>.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -H "OpenStack-API-Version: volume 3.XX" -H "X-Auth-Token: $OS_TOKEN" "$VOLUME_ENDPOINT/volumes/detail"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Cinder microversion header**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 14 — Version discovery

### Concept

Production clients should discover supported ranges and fail clearly if required microversions are unavailable.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Version discovery**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 15 — Request IDs

### Concept

X-OpenStack-Request-ID gives operators a correlation key across service logs.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server create ...
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Request IDs**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 16 — Global correlation IDs

### Concept

A platform service should keep its own workflow/trace ID alongside each OpenStack request ID.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
import uuid
print('req-'+str(uuid.uuid4()))
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Global correlation IDs**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 17 — HTTP 200 and body validation

### Concept

A 200 still requires schema/content validation.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 200 and body validation**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 18 — HTTP 201

### Concept

201 indicates creation for APIs such as Keystone token issuance.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si -X POST -H 'Content-Type: application/json' -d @auth.json "$IDENTITY/v3/auth/tokens"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 201**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 19 — HTTP 202 and async work

### Concept

202 means accepted, not complete; resource state must be polled.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 202 and async work**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 20 — HTTP 204

### Concept

204 is success without a response body and clients must not blindly parse JSON.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si -X DELETE -H "X-Auth-Token: $OS_TOKEN" <resource-url>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 204**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 21 — HTTP 400

### Concept

400 normally means invalid request syntax/schema/value or version semantics.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug <bad-command> 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 400**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 22 — HTTP 401

### Concept

401 normally points to missing/invalid/expired authentication.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack token issue
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 401**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 23 — HTTP 403

### Concept

403 means the identity is known but policy/role/scope denies the action.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack role assignment list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 403**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 24 — HTTP 404

### Concept

404 can mean missing resource, wrong endpoint/path/version, wrong scope, or hidden resource.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack endpoint list
openstack catalog list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 404**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 25 — HTTP 409

### Concept

409 commonly represents resource state or dependency conflicts.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server show <id>
openstack volume show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 409**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 26 — HTTP 413

### Concept

413 may indicate request/entity size or request-limit conditions depending on service.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug image create ...
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 413**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 27 — HTTP 429

### Concept

429 indicates throttling/rate limiting where implemented and should trigger backpressure.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si <endpoint>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 429**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 28 — HTTP 500

### Concept

500 is server-side failure; capture time, request ID, endpoint, method, and safe response body.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 500**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 29 — HTTP 503

### Concept

503 indicates temporary service/dependency unavailability; retries require bounded backoff and idempotency awareness.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **HTTP 503**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 30 — Connect, read, and operation timeouts

### Concept

Network request timeouts and overall resource-operation timeouts are distinct.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
import requests
print('requests.get(url, timeout=(3, 15))')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Connect, read, and operation timeouts**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 31 — Retry classification

### Concept

Retry only transient failures and network exceptions, not every 4xx.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print({429,500,502,503,504})
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Retry classification**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 32 — Exponential backoff

### Concept

Retry delay should grow with attempts.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
for i in range(5): print(2**i)
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Exponential backoff**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 33 — Jitter

### Concept

Randomized retry delays prevent synchronized thundering herds.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
import random
print([round((2**i)*random.uniform(.5,1.5),2) for i in range(5)])
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Jitter**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 34 — Idempotency

### Concept

Repeated operations should not create unintended additional effects.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list --name web01
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Idempotency**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 35 — Duplicate create after timeout

### Concept

A POST may succeed before the response is lost, so reconcile actual state before retrying.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list --name web01
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Duplicate create after timeout**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 36 — Asynchronous polling

### Concept

Poll with sleep, terminal success/failure states, and a hard deadline.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Asynchronous polling**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 37 — Pagination

### Concept

Large result sets require following markers/next links or SDK generators.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Pagination**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 38 — Server-side filtering

### Concept

Use supported API filters to reduce transfer and control-plane load.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list --status ACTIVE
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Server-side filtering**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 39 — Explicit sorting

### Concept

Never rely on implicit API list order when correctness depends on ordering.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Explicit sorting**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 40 — UUIDs versus names

### Concept

Names may be duplicated; automation should persist UUIDs.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server show <uuid>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **UUIDs versus names**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 41 — Ownership tags and metadata

### Concept

managed-by, workflow-id, owner, environment, and expiry fields support reconciliation and safe cleanup.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server set <id> --property managed-by=my-service
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Ownership tags and metadata**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 42 — curl safety

### Concept

Raw curl is excellent for learning/debugging but token handling, TLS, and shell history require care.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl --cacert ca.pem -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **curl safety**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 43 — OpenStackClient debug

### Concept

--debug reveals auth, catalog discovery, endpoint URL, HTTP method, headers, response, and request ID.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **OpenStackClient debug**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 44 — clouds.yaml

### Concept

Named cloud configuration should hold auth and endpoint-selection settings with strict file permissions.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
chmod 600 ~/.config/openstack/clouds.yaml
export OS_CLOUD=lab
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **clouds.yaml**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 45 — Python requests

### Concept

Raw requests teaches HTTP mechanics but leaves auth/catalog/version handling to application code.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
import requests
print('requests.get(url, headers=headers, timeout=10)')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Python requests**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 46 — raise_for_status and safe errors

### Concept

HTTP failures should become structured application errors enriched with request IDs without leaking tokens.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
import requests
print('response.raise_for_status()')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **raise_for_status and safe errors**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 47 — keystoneauth authentication plugins

### Concept

keystoneauth1 implements password, token, application credential, and other auth methods.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
from keystoneauth1 import loading
print(loading.get_available_plugin_names())
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **keystoneauth authentication plugins**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 48 — keystoneauth Session

### Concept

A Session centralizes auth, TLS, token refresh, and request behavior.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('Session(auth=auth, timeout=10)')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **keystoneauth Session**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 49 — Keystoneauth Adapter

### Concept

An Adapter binds a Session to a service type, interface, region, and version context.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('Adapter(session=sess, service_type="compute", region_name="RegionOne")')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Keystoneauth Adapter**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 50 — openstacksdk Connection

### Concept

Connection exposes service proxies and handles common auth/discovery/pagination operations.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
import openstack
print('conn = openstack.connect(cloud="lab")')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **openstacksdk Connection**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 51 — SDK resource objects

### Concept

SDK objects wrap JSON resources and expose properties such as id, name, and status.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('for server in conn.compute.servers(): print(server.id, server.status)')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **SDK resource objects**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 52 — SDK exceptions

### Concept

Applications should normalize SDK/HTTP exceptions into safe domain errors.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('operation, resource_id, status, request_id, retryable')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **SDK exceptions**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 53 — Connection pooling

### Concept

Reuse authenticated sessions/connections to reduce TLS handshakes, Keystone calls, and endpoint discovery load.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('Create Connection once and reuse it')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Connection pooling**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 54 — Nova server list/show

### Concept

Nova server resources are asynchronous compute objects with IDs, states, metadata, addresses, and faults.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list
openstack server show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova server list/show**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 55 — Nova server create

### Concept

Robust create resolves image/flavor/network, submits, records ID, waits, and handles ERROR/timeout.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server create web01 --image <image> --flavor <flavor> --network <network>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova server create**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 56 — Nova server actions

### Concept

Reboot/resize/rebuild/shelve/rescue have state constraints and can return conflicts.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server reboot <id>
openstack server show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova server actions**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 57 — Nova metadata

### Concept

Metadata supports ownership and application automation but is not a secret store.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server set <id> --property owner=platform --property environment=prod
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova metadata**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 58 — Nova server groups

### Concept

Affinity/anti-affinity policy can be expressed through server groups and scheduler hints.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server group list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova server groups**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 59 — Nova microversion contract

### Concept

Software should verify required Nova feature version before serving requests.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Nova microversion contract**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 60 — Neutron networks/subnets

### Concept

Network APIs are dependency-oriented and should persist created UUIDs.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack network list
openstack subnet list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Neutron networks/subnets**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 61 — Neutron ports

### Concept

Ports contain fixed IP, MAC, device ownership, SGs, and binding state and are central to network troubleshooting.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack port show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Neutron ports**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 62 — Neutron routers

### Concept

Router creation, external gateway, and subnet interface attachment are separate resources/actions.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack router show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Neutron routers**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 63 — Floating IP API

### Concept

API association must be followed by real connectivity validation.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack floating ip show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Floating IP API**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 64 — Security group API

### Concept

Firewall automation should reconcile desired rules instead of blindly adding duplicates.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack security group rule list <sg>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Security group API**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 65 — Cinder volume create

### Concept

Volume creation is async and should poll to available or error.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack volume create --size 10 data01
openstack volume show data01
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Cinder volume create**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 66 — Cinder snapshot

### Concept

Snapshot creation is async and backend/state dependent.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack volume snapshot create --volume <vol> snap1
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Cinder snapshot**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 67 — Cinder backup

### Concept

Backup resources have different durability goals from snapshots.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack volume backup create <vol> 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Cinder backup**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 68 — Cinder attachment lifecycle

### Concept

Create→available→attach→in-use→detach→available→delete should be modeled explicitly.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server add volume <server> <volume>
openstack volume show <volume>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Cinder attachment lifecycle**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 69 — Glance metadata and upload

### Concept

Image metadata creation and binary upload are separate concerns and large transfers should be streamed/integrity checked.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack image show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Glance metadata and upload**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 70 — Glance download

### Concept

Large image downloads should stream to disk and verify available checksums/hashes.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack image save --file image.bin <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Glance download**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 71 — Swift account/container/object

### Concept

Object storage APIs use HTTP objects and namespaces rather than block devices.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack container list 2>/dev/null || true
openstack object list <container> 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Swift account/container/object**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 72 — Heat stack lifecycle

### Concept

Stack creation is async and nested resource events reveal downstream Nova/Neutron/Cinder failures.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack stack show <stack> 2>/dev/null || true
openstack stack event list <stack> 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Heat stack lifecycle**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 73 — Octavia API

### Concept

Load balancer provisioning status and operating status are separate and both must be validated.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack loadbalancer show <lb> 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Octavia API**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 74 — Barbican API security

### Concept

Secret payloads, tokens, and app credential secrets must never be logged.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack secret list 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Barbican API security**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 75 — Manila API

### Concept

Share resources, share networks, types, access rules, and protocol/network reachability form one file-service workflow.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack share list 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Manila API**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 76 — Ironic API guardrails

### Concept

Bare-metal actions can affect real physical servers and BMCs, so destructive automation needs stronger ownership and approval checks.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack baremetal node list 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Ironic API guardrails**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 77 — Designate API and DNS propagation

### Concept

API success does not imply every resolver sees the new record immediately due to authoritative sync and TTL caching.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack zone list 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Designate API and DNS propagation**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 78 — Placement API boundaries

### Concept

Ordinary VM applications should use Nova rather than manipulate Placement allocations directly.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack resource provider list 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Placement API boundaries**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 79 — Reconciliation loop

### Concept

Desired versus actual state is safer than one-shot create scripts.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack network show app-net 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Reconciliation loop**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 80 — Drift detection

### Concept

An existing name may have wrong CIDR, project, MTU, tags, or policy and should not be treated as correct automatically.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack network show <id>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Drift detection**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 81 — Saga and compensating actions

### Concept

Multi-service workflows are not one database transaction and need explicit compensation for partial success.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack network list
openstack subnet list
openstack server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Saga and compensating actions**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 82 — Cleanup dependency order

### Concept

Delete children/attachments before parent resources and prove ownership first.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack port list
openstack router list
openstack network list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Cleanup dependency order**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 83 — Concurrency control

### Concept

Two workers can race on read-then-create and require locks, deterministic identifiers, or conflict-aware reconciliation.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list --name <deterministic-name>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Concurrency control**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 84 — Rate limiting and backpressure

### Concept

429/high latency should reduce client concurrency and trigger bounded jittered backoff.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl -si <endpoint>
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Rate limiting and backpressure**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 85 — Circuit breaker

### Concept

Persistent service failure should stop repeated calls temporarily and probe recovery rather than flood the API.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('CLOSED -> OPEN -> HALF_OPEN -> CLOSED')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Circuit breaker**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 86 — Bulk operation safety

### Concept

Large creates/deletes should be batched, paced, checkpointed, and ownership validated.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack server list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Bulk operation safety**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 87 — Token redaction

### Concept

Bearer tokens and app credential secrets must be stripped from logs and support bundles.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print({'x-auth-token','x-subject-token','authorization'})
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Token redaction**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 88 — TLS verification

### Concept

Production clients should trust the cloud CA and prohibit verify=False/curl -k modes.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
curl --cacert ca.pem https://api.example/v3
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **TLS verification**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 89 — Secrets at rest

### Concept

Credentials belong in a secret manager/protected CI store or restricted file, not source code.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
chmod 600 ~/.config/openstack/clouds.yaml
git grep -nE 'OS_TOKEN|password|application_credential_secret' || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Secrets at rest**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 90 — Audit logging

### Concept

Log caller, project, operation, resource ID, request ID, status, latency, and outcome—without secrets.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print('caller project operation resource_id request_id status latency')
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Audit logging**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 91 — API latency versus operation latency

### Concept

A fast POST can start a slow provisioning workflow; both metrics need separate SLOs.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack --debug server create ...
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **API latency versus operation latency**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 92 — Testing pyramid

### Concept

Use mocks for logic, a dedicated project for integration, and controlled E2E workflows for real compatibility.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
pytest -q
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Testing pyramid**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 93 — Contract tests

### Concept

Validate service presence, region/interface, required images/flavors/networks, and minimum microversions at startup.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack catalog list
openstack image list
openstack flavor list
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Contract tests**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 94 — SDK version pinning

### Concept

Cloud release and openstacksdk release evolve independently and should be tested as separate dependencies.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python -m pip show openstacksdk
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **SDK version pinning**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 95 — Multi-cloud portability

### Concept

Clouds differ in regions, resources, extensions, policies, and microversion support; code should discover and configure these differences.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
openstack catalog list
openstack extension list 2>/dev/null || true
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **Multi-cloud portability**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


## Advanced Deep Dive 96 — API error object design

### Concept

A platform should convert backend errors into stable safe internal errors with request IDs and retryability.

Production API engineering requires more than knowing an endpoint path. For every operation, the client must reason about authentication, endpoint discovery, API version, request semantics, asynchronous completion, retries, partial failure, final resource verification, and security.

### Protocol / Mental Model

```text
Application
   |
Auth / Session
   |
Keystone token + catalog
   |
Service endpoint + version
   |
HTTP request
   |
HTTP response + request ID
   |
Asynchronous cloud work
   |
Final resource state
   |
Verification / reconciliation
```

### Commands / Code

```bash
python - <<'PY'
print({'operation':'server_create','status':409,'request_id':'req-...','retryable':False})
PY
```

### Expected Result

A successful client records the exact resource UUID, service/region, final state, and request ID where available. It distinguishes HTTP success from resource completion and refuses to silently ignore incompatible API versions or authorization failures.

### Why It Works

OpenStack APIs are distributed contracts. A request can be accepted by one service and fail later in a scheduler, worker, network backend, image store, volume backend, or compute node. Robust clients therefore need state machines and reconciliation, not only HTTP calls.

### Production Pattern

For **API error object design**, a production application should:

```text
validate capability
→ submit bounded request
→ record resource/request IDs
→ wait for terminal state
→ classify failures
→ reconcile after ambiguity
→ compensate only owned resources
→ emit safe observability
```

### Troubleshooting Workflow

```text
Client symptom
  ↓
Auth method and token scope
  ↓
Service catalog: type / region / interface
  ↓
Major version / microversion
  ↓
Method / URL / headers / JSON
  ↓
HTTP status / body / request ID
  ↓
Resource state
  ↓
Safe retry? Reconcile? Compensate?
  ↓
Verify final cloud and application state
```

### Security Requirements

- Never log tokens, passwords, app-credential secrets, private keys, or Barbican payloads.
- Use trusted TLS.
- Prefer scoped machine credentials.
- Limit retries and concurrency.
- Validate project and ownership before delete.
- Keep integration tests in isolated projects.
- Treat Ironic and other destructive administrative APIs as higher risk.

### Best Practices

- Persist UUIDs.
- Use SDK/auth libraries for normal production code.
- Use raw REST for learning/debugging/special integrations.
- Request the minimum microversion needed.
- Make operations idempotent through reconciliation.
- Use exponential backoff + jitter.
- Implement operation deadlines.
- Structure errors around status + request ID + resource ID.
- Test failure paths, not only happy paths.

---


# Enhanced OpenStack API Engineering Labs

## Enhanced Lab 1 — API-first architecture

**Objective:** implement or diagnose **API-first architecture** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server list
openstack --debug network list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 2 — HTTP request anatomy

**Objective:** implement or diagnose **HTTP request anatomy** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -v -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 3 — HTTP response anatomy

**Objective:** implement or diagnose **HTTP response anatomy** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 4 — Keystone v3 token exchange

**Objective:** implement or diagnose **Keystone v3 token exchange** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si -X POST -H 'Content-Type: application/json' -d @auth.json "$IDENTITY/v3/auth/tokens"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 5 — X-Subject-Token versus X-Auth-Token

**Objective:** implement or diagnose **X-Subject-Token versus X-Auth-Token** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 6 — Project, domain, and system scopes

**Objective:** implement or diagnose **Project, domain, and system scopes** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack token issue
openstack role assignment list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 7 — Application credentials

**Objective:** implement or diagnose **Application credentials** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack application credential list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 8 — Service catalog discovery

**Objective:** implement or diagnose **Service catalog discovery** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack catalog list
openstack endpoint list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 9 — Regions and endpoint interfaces

**Objective:** implement or diagnose **Regions and endpoint interfaces** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack catalog show compute
openstack endpoint list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 10 — Major API versions

**Objective:** implement or diagnose **Major API versions** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug token issue
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 11 — Microversions

**Objective:** implement or diagnose **Microversions** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 12 — Nova microversion header

**Objective:** implement or diagnose **Nova microversion header** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -H "OpenStack-API-Version: compute 2.XX" -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 13 — Cinder microversion header

**Objective:** implement or diagnose **Cinder microversion header** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -H "OpenStack-API-Version: volume 3.XX" -H "X-Auth-Token: $OS_TOKEN" "$VOLUME_ENDPOINT/volumes/detail"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 14 — Version discovery

**Objective:** implement or diagnose **Version discovery** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 15 — Request IDs

**Objective:** implement or diagnose **Request IDs** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server create ...
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 16 — Global correlation IDs

**Objective:** implement or diagnose **Global correlation IDs** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
import uuid
print('req-'+str(uuid.uuid4()))
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 17 — HTTP 200 and body validation

**Objective:** implement or diagnose **HTTP 200 and body validation** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 18 — HTTP 201

**Objective:** implement or diagnose **HTTP 201** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si -X POST -H 'Content-Type: application/json' -d @auth.json "$IDENTITY/v3/auth/tokens"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 19 — HTTP 202 and async work

**Objective:** implement or diagnose **HTTP 202 and async work** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 20 — HTTP 204

**Objective:** implement or diagnose **HTTP 204** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si -X DELETE -H "X-Auth-Token: $OS_TOKEN" <resource-url>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 21 — HTTP 400

**Objective:** implement or diagnose **HTTP 400** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug <bad-command> 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 22 — HTTP 401

**Objective:** implement or diagnose **HTTP 401** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack token issue
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 23 — HTTP 403

**Objective:** implement or diagnose **HTTP 403** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack role assignment list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 24 — HTTP 404

**Objective:** implement or diagnose **HTTP 404** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack endpoint list
openstack catalog list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 25 — HTTP 409

**Objective:** implement or diagnose **HTTP 409** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server show <id>
openstack volume show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 26 — HTTP 413

**Objective:** implement or diagnose **HTTP 413** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug image create ...
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 27 — HTTP 429

**Objective:** implement or diagnose **HTTP 429** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si <endpoint>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 28 — HTTP 500

**Objective:** implement or diagnose **HTTP 500** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 29 — HTTP 503

**Objective:** implement or diagnose **HTTP 503** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 30 — Connect, read, and operation timeouts

**Objective:** implement or diagnose **Connect, read, and operation timeouts** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
import requests
print('requests.get(url, timeout=(3, 15))')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 31 — Retry classification

**Objective:** implement or diagnose **Retry classification** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print({429,500,502,503,504})
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 32 — Exponential backoff

**Objective:** implement or diagnose **Exponential backoff** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
for i in range(5): print(2**i)
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 33 — Jitter

**Objective:** implement or diagnose **Jitter** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
import random
print([round((2**i)*random.uniform(.5,1.5),2) for i in range(5)])
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 34 — Idempotency

**Objective:** implement or diagnose **Idempotency** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list --name web01
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 35 — Duplicate create after timeout

**Objective:** implement or diagnose **Duplicate create after timeout** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list --name web01
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 36 — Asynchronous polling

**Objective:** implement or diagnose **Asynchronous polling** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 37 — Pagination

**Objective:** implement or diagnose **Pagination** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 38 — Server-side filtering

**Objective:** implement or diagnose **Server-side filtering** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list --status ACTIVE
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 39 — Explicit sorting

**Objective:** implement or diagnose **Explicit sorting** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 40 — UUIDs versus names

**Objective:** implement or diagnose **UUIDs versus names** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server show <uuid>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 41 — Ownership tags and metadata

**Objective:** implement or diagnose **Ownership tags and metadata** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server set <id> --property managed-by=my-service
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 42 — curl safety

**Objective:** implement or diagnose **curl safety** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl --cacert ca.pem -H "X-Auth-Token: $OS_TOKEN" "$COMPUTE_ENDPOINT/servers"
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 43 — OpenStackClient debug

**Objective:** implement or diagnose **OpenStackClient debug** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 44 — clouds.yaml

**Objective:** implement or diagnose **clouds.yaml** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
chmod 600 ~/.config/openstack/clouds.yaml
export OS_CLOUD=lab
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 45 — Python requests

**Objective:** implement or diagnose **Python requests** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
import requests
print('requests.get(url, headers=headers, timeout=10)')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 46 — raise_for_status and safe errors

**Objective:** implement or diagnose **raise_for_status and safe errors** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
import requests
print('response.raise_for_status()')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 47 — keystoneauth authentication plugins

**Objective:** implement or diagnose **keystoneauth authentication plugins** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
from keystoneauth1 import loading
print(loading.get_available_plugin_names())
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 48 — keystoneauth Session

**Objective:** implement or diagnose **keystoneauth Session** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('Session(auth=auth, timeout=10)')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 49 — Keystoneauth Adapter

**Objective:** implement or diagnose **Keystoneauth Adapter** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('Adapter(session=sess, service_type="compute", region_name="RegionOne")')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 50 — openstacksdk Connection

**Objective:** implement or diagnose **openstacksdk Connection** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
import openstack
print('conn = openstack.connect(cloud="lab")')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 51 — SDK resource objects

**Objective:** implement or diagnose **SDK resource objects** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('for server in conn.compute.servers(): print(server.id, server.status)')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 52 — SDK exceptions

**Objective:** implement or diagnose **SDK exceptions** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('operation, resource_id, status, request_id, retryable')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 53 — Connection pooling

**Objective:** implement or diagnose **Connection pooling** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('Create Connection once and reuse it')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 54 — Nova server list/show

**Objective:** implement or diagnose **Nova server list/show** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list
openstack server show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 55 — Nova server create

**Objective:** implement or diagnose **Nova server create** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server create web01 --image <image> --flavor <flavor> --network <network>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 56 — Nova server actions

**Objective:** implement or diagnose **Nova server actions** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server reboot <id>
openstack server show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 57 — Nova metadata

**Objective:** implement or diagnose **Nova metadata** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server set <id> --property owner=platform --property environment=prod
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 58 — Nova server groups

**Objective:** implement or diagnose **Nova server groups** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server group list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 59 — Nova microversion contract

**Objective:** implement or diagnose **Nova microversion contract** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 60 — Neutron networks/subnets

**Objective:** implement or diagnose **Neutron networks/subnets** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack network list
openstack subnet list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 61 — Neutron ports

**Objective:** implement or diagnose **Neutron ports** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack port show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 62 — Neutron routers

**Objective:** implement or diagnose **Neutron routers** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack router show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 63 — Floating IP API

**Objective:** implement or diagnose **Floating IP API** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack floating ip show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 64 — Security group API

**Objective:** implement or diagnose **Security group API** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack security group rule list <sg>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 65 — Cinder volume create

**Objective:** implement or diagnose **Cinder volume create** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack volume create --size 10 data01
openstack volume show data01
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 66 — Cinder snapshot

**Objective:** implement or diagnose **Cinder snapshot** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack volume snapshot create --volume <vol> snap1
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 67 — Cinder backup

**Objective:** implement or diagnose **Cinder backup** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack volume backup create <vol> 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 68 — Cinder attachment lifecycle

**Objective:** implement or diagnose **Cinder attachment lifecycle** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server add volume <server> <volume>
openstack volume show <volume>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 69 — Glance metadata and upload

**Objective:** implement or diagnose **Glance metadata and upload** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack image show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 70 — Glance download

**Objective:** implement or diagnose **Glance download** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack image save --file image.bin <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 71 — Swift account/container/object

**Objective:** implement or diagnose **Swift account/container/object** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack container list 2>/dev/null || true
openstack object list <container> 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 72 — Heat stack lifecycle

**Objective:** implement or diagnose **Heat stack lifecycle** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack stack show <stack> 2>/dev/null || true
openstack stack event list <stack> 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 73 — Octavia API

**Objective:** implement or diagnose **Octavia API** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack loadbalancer show <lb> 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 74 — Barbican API security

**Objective:** implement or diagnose **Barbican API security** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack secret list 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 75 — Manila API

**Objective:** implement or diagnose **Manila API** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack share list 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 76 — Ironic API guardrails

**Objective:** implement or diagnose **Ironic API guardrails** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack baremetal node list 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 77 — Designate API and DNS propagation

**Objective:** implement or diagnose **Designate API and DNS propagation** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack zone list 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 78 — Placement API boundaries

**Objective:** implement or diagnose **Placement API boundaries** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack resource provider list 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 79 — Reconciliation loop

**Objective:** implement or diagnose **Reconciliation loop** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack network show app-net 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 80 — Drift detection

**Objective:** implement or diagnose **Drift detection** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack network show <id>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 81 — Saga and compensating actions

**Objective:** implement or diagnose **Saga and compensating actions** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack network list
openstack subnet list
openstack server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 82 — Cleanup dependency order

**Objective:** implement or diagnose **Cleanup dependency order** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack port list
openstack router list
openstack network list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 83 — Concurrency control

**Objective:** implement or diagnose **Concurrency control** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list --name <deterministic-name>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 84 — Rate limiting and backpressure

**Objective:** implement or diagnose **Rate limiting and backpressure** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl -si <endpoint>
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 85 — Circuit breaker

**Objective:** implement or diagnose **Circuit breaker** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('CLOSED -> OPEN -> HALF_OPEN -> CLOSED')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 86 — Bulk operation safety

**Objective:** implement or diagnose **Bulk operation safety** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack server list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 87 — Token redaction

**Objective:** implement or diagnose **Token redaction** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print({'x-auth-token','x-subject-token','authorization'})
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 88 — TLS verification

**Objective:** implement or diagnose **TLS verification** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
curl --cacert ca.pem https://api.example/v3
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 89 — Secrets at rest

**Objective:** implement or diagnose **Secrets at rest** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
chmod 600 ~/.config/openstack/clouds.yaml
git grep -nE 'OS_TOKEN|password|application_credential_secret' || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 90 — Audit logging

**Objective:** implement or diagnose **Audit logging** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print('caller project operation resource_id request_id status latency')
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 91 — API latency versus operation latency

**Objective:** implement or diagnose **API latency versus operation latency** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack --debug server create ...
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 92 — Testing pyramid

**Objective:** implement or diagnose **Testing pyramid** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
pytest -q
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 93 — Contract tests

**Objective:** implement or diagnose **Contract tests** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack catalog list
openstack image list
openstack flavor list
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 94 — SDK version pinning

**Objective:** implement or diagnose **SDK version pinning** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python -m pip show openstacksdk
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 95 — Multi-cloud portability

**Objective:** implement or diagnose **Multi-cloud portability** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
openstack catalog list
openstack extension list 2>/dev/null || true
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---

## Enhanced Lab 96 — API error object design

**Objective:** implement or diagnose **API error object design** using a disposable OpenStack test project.

### Procedure
1. Confirm `OS_CLOUD`, project, region, endpoint interface, and authentication method.
2. Capture the expected HTTP/API contract and resource state machine.
3. Run the command/code below.
4. Record the exact UUID and `X-OpenStack-Request-ID` if available.
5. Validate HTTP status and JSON/SDK response.
6. If asynchronous, poll to success/failure with a bounded timeout.
7. Run the same workflow twice and check idempotency where relevant.
8. Inject one safe failure such as invalid role, unsupported version, timeout simulation, or state conflict.
9. Decide whether retry, reconciliation, or compensation is correct.
10. Redact credentials before saving any debug output.

```bash
python - <<'PY'
print({'operation':'server_create','status':409,'request_id':'req-...','retryable':False})
PY
```

**Safety:** never run destructive tests in production projects; never print real tokens or secret payloads; verify resource ownership before cleanup.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Inspect the Service Catalog

```bash
export OS_CLOUD=lab
openstack catalog list
openstack endpoint list
```

Create a table:

```text
Service
Type
Region
Public URL
Internal URL
```

### Lab 2 — Get a Keystone Token with Raw REST

Create `auth.json` with a disposable lab credential.

```bash
curl -si \
  -X POST \
  -H 'Content-Type: application/json' \
  -d @auth.json \
  "$IDENTITY/v3/auth/tokens"
```

Find:

```text
X-Subject-Token
```

### Lab 3 — Use Token Against an API

```bash
export OS_TOKEN='REDACTED'

curl \
  -H "X-Auth-Token: $OS_TOKEN" \
  "$COMPUTE_ENDPOINT/servers"
```

Explain the difference between token issuance and token usage.

### Lab 4 — Parse Catalog JSON

Save the Keystone response body.

Use Python:

```python
import json

with open("token.json") as f:
    data = json.load(f)

for service in data["token"]["catalog"]:
    print(service["type"])
```

### Lab 5 — HTTP Status Lab

Generate controlled cases:

```text
bad password → 401
unauthorized action → 403
missing resource → 404
invalid JSON → 400
```

Record the response body and request ID.

### Lab 6 — Nova Version Discovery

Inspect Nova version endpoint and identify supported microversion range.

Send one request with a specific `OpenStack-API-Version: compute ...` header.

### Lab 7 — Cinder Microversion

Call a Cinder v3 endpoint with a supported:

```http
OpenStack-API-Version: volume <version>
```

Compare response with minimum/default behavior if a visible field differs.

### Lab 8 — OpenStackClient Debug

```bash
openstack --debug server list
```

Redact secrets and identify:

```text
Keystone call
catalog discovery
Nova URL
request headers
response status
request ID
```

### Lab 9 — Python `requests`

Write:

```python
requests.get(
    endpoint,
    headers={"X-Auth-Token": token},
    timeout=10,
)
```

Handle non-2xx status and print request ID safely.

### Lab 10 — Keystoneauth Session

Build an authenticated session.

Use endpoint discovery instead of hard-coding Nova URL.

### Lab 11 — OpenStackSDK

```python
import openstack

conn = openstack.connect(cloud="lab")

for server in conn.compute.servers():
    print(server.id, server.name)
```

### Lab 12 — SDK Create Server

Using a disposable test project:

1. resolve image;
2. resolve flavor;
3. resolve network;
4. create VM;
5. wait for ACTIVE;
6. capture ID;
7. delete VM.

### Lab 13 — Timeout and Reconciliation

Simulate a client timeout after create.

Before retrying, search for the server by stored ID/name/tag.

Explain how this prevents duplicate resources.

### Lab 14 — Neutron API

Create:

```text
network
subnet
router
```

with SDK or raw REST.

Record every resource ID.

### Lab 15 — Floating IP Automation

Create a floating IP and associate it with a disposable server.

Validate both API state and actual reachability.

### Lab 16 — Security Group Automation

Create a security group with one narrow SSH rule.

Re-run your script and prove it does not create duplicate rules.

### Lab 17 — Cinder API

Create a volume, wait for `available`, attach it, wait for `in-use`, detach, then delete.

### Lab 18 — Glance API

Create image metadata, upload a small image, show it, download it, and verify checksum/hash metadata where available.

### Lab 19 — Swift API

Create a container, upload:

```text
hello.txt
```

download it, compare checksum, delete object and container.

### Lab 20 — Heat API

Create a simple stack from a template.

Poll:

```text
CREATE_IN_PROGRESS
CREATE_COMPLETE
```

On failure, inspect stack events.

### Lab 21 — Barbican Security Exercise

Create a lab secret using an approved method.

Verify that your application logs never print the secret payload or auth token.

Delete the disposable secret afterward.

### Lab 22 — Pagination

Create enough disposable resources or mock API pages to demonstrate:

```text
limit
marker/next
```

Write a function that returns all pages safely.

### Lab 23 — Retry with Backoff

Implement:

```text
max attempts
exponential delay
jitter
retryable status list
```

Do not retry 400/403 blindly.

### Lab 24 — Async Poller

Write reusable Python:

```python
wait_for_status(
    getter,
    success={"ACTIVE"},
    failure={"ERROR"},
    timeout=300,
    interval=5,
)
```

### Lab 25 — Request-ID Logging

For every HTTP/API failure, log:

```text
method
service
resource
HTTP status
request ID
```

and redact secrets.

### Lab 26 — Application Credential

Create a lab application credential with the minimum required role/scope.

Configure `clouds.yaml` to use it instead of the user's password.

Revoke it and verify automation fails cleanly.

### Lab 27 — Reconciliation Controller

Write a small script whose desired state is:

```text
network app-net exists
subnet app-subnet exists
security group app-sg exists
```

Run it twice. The second run should make no duplicate resources.

### Lab 28 — Compensating Rollback

Workflow:

```text
create network
create subnet
simulate server create failure
```

Delete only the resources owned by that workflow.

### Lab 29 — API Compatibility Check

At startup, verify:

```text
required services present
required region present
Nova microversion sufficient
Cinder microversion sufficient if used
```

Exit with a clear message if incompatible.

### Lab 30 — API Troubleshooting Challenge

Analyze:

1. expired token.
2. 403 due to missing role.
3. wrong region.
4. wrong endpoint interface.
5. unsupported microversion.
6. 400 JSON validation error.
7. 409 state conflict.
8. 429 throttling.
9. 503 service unavailable.
10. client timeout after successful create.
11. duplicate resource.
12. server remains BUILD.
13. volume remains creating.
14. network port DOWN.
15. Heat stack CREATE_FAILED.

For each document:

```text
Request
Status
Request ID
Resource State
Root Cause
Safe Retry?
Correction
Verification
```

---

## 6. Mini Project

# Mini Project — OpenStack Infrastructure Automation Service

Build a Python application that creates an isolated application environment.

Desired architecture:

```text
Project
  |
  +-- Network
  |    |
  |    +-- Subnet
  |    +-- Router
  |
  +-- Security Group
  |
  +-- Server
  |    |
  |    +-- Floating IP
  |
  +-- Cinder Volume
```

## Requirements

Use:

```text
openstacksdk
clouds.yaml
application credential
structured logging
request IDs
timeouts
retry/backoff
resource ownership tags
cleanup
```

## Application Workflow

```text
validate cloud capabilities
   ↓
reconcile network
   ↓
reconcile subnet
   ↓
reconcile router
   ↓
reconcile security group
   ↓
create/reconcile server
   ↓
wait ACTIVE
   ↓
create/reconcile volume
   ↓
attach
   ↓
associate floating IP
   ↓
health check
```

## Failure Workflow

```text
operation fails
   ↓
capture HTTP status/request ID
   ↓
determine whether request may have succeeded
   ↓
query actual cloud state
   ↓
retry or compensate
```

## Project Structure

```text
openstack-automation/
├── README.md
├── pyproject.toml
├── config/
│   └── clouds.example.yaml
├── src/
│   ├── connection.py
│   ├── compute.py
│   ├── network.py
│   ├── storage.py
│   ├── retry.py
│   ├── waiters.py
│   ├── reconcile.py
│   └── logging_utils.py
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
    ├── API_COMPATIBILITY.md
    ├── SECURITY.md
    └── TROUBLESHOOTING.md
```

## Required Tests

```text
second run is idempotent
401 handling
403 handling
timeout after create
409 handling
server ERROR
volume error
cleanup after partial failure
unsupported microversion
```

---


# Expanded Capstone — Production-Grade OpenStack Automation Service

Build a Python application that reconciles:

```text
Project
  |
  +-- app-net
  |    +-- app-subnet
  |    +-- router
  |
  +-- app-security-group
  |
  +-- web01
  |    +-- floating IP
  |
  +-- data01 Cinder volume
```

Required structure:

```text
openstack-automation/
├── pyproject.toml
├── README.md
├── config/
│   └── clouds.example.yaml
├── src/cloudapp/
│   ├── connection.py
│   ├── capabilities.py
│   ├── compute.py
│   ├── network.py
│   ├── storage.py
│   ├── waiters.py
│   ├── retry.py
│   ├── circuit_breaker.py
│   ├── reconcile.py
│   ├── cleanup.py
│   ├── errors.py
│   └── observability.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
└── docs/
    ├── SECURITY.md
    ├── API_COMPATIBILITY.md
    ├── FAILURE_MODEL.md
    └── RUNBOOK.md
```

Mandatory behavior:

```text
authenticate with application credential
discover service endpoints
validate region/interface
validate Nova/Cinder microversions
resolve image/flavor/network by UUID
reconcile network/subnet/router/SG
create/reconcile server
record server UUID immediately
wait ACTIVE or ERROR
create/reconcile volume
attach and wait in-use
allocate/associate floating IP
perform application health check
```

Required failure tests:

```text
401
403
404 wrong scope
409 conflict
429 throttling
503 outage
HTTP timeout after successful POST
duplicate concurrent create
server ERROR
volume error
port DOWN
unsupported microversion
cleanup after partial failure
```

Required observability:

```text
workflow_id
cloud
region
project
operation
resource_type
resource_id
OpenStack request_id
HTTP status
retry_count
API latency
operation latency
final state
```

Never log:

```text
X-Auth-Token
X-Subject-Token
password
application_credential_secret
private key
Barbican payload
```


## 7. Recommended Resources

This Markdown is designed to be self-contained for learning. For exact schemas, status codes, and microversion-specific fields, consult the API reference for the exact OpenStack release.

Relevant official 2026.1 API families include:

```text
Identity — Keystone
Compute — Nova
Networking — Neutron
Block Storage — Cinder
Image — Glance
Object Storage — Swift
Orchestration — Heat
Load Balancer — Octavia
Key Manager — Barbican
Shared File Systems — Manila
Bare Metal — Ironic
DNS — Designate
Placement
```

Supporting client documentation:

```text
OpenStack API Quick Start
openstacksdk
keystoneauth1
OpenStackClient
```

---

## 8. Certification Relevance

Relevant to:

```text
Cloud Backend Engineer
OpenStack Engineer
Platform Engineer
DevOps Engineer
SRE
Infrastructure Automation Engineer
Cloud Application Developer
```

It also prepares directly for later courses in:

```text
Terraform
Infrastructure as Code
CI/CD
Backend APIs
Cloud-Native Development
DevSecOps
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Hard-code every API endpoint.  
  **Best practice:** use Keystone service catalog and SDK discovery.

- **Mistake:** Log tokens.  
  **Best practice:** redact auth headers and secret payloads.

- **Mistake:** Store human user password in automation.  
  **Best practice:** use application credentials or approved workload secrets.

- **Mistake:** Use `verify=False` in production.  
  **Best practice:** install/trust the cloud CA.

- **Mistake:** Assume HTTP 202 means resource is ready.  
  **Best practice:** poll final resource state.

- **Mistake:** Retry every failed request.  
  **Best practice:** classify transient vs permanent errors.

- **Mistake:** Retry a POST after timeout without checking state.  
  **Best practice:** reconcile before creating again.

- **Mistake:** Use resource names as globally unique IDs.  
  **Best practice:** persist UUIDs and ownership metadata.

- **Mistake:** Ignore microversions.  
  **Best practice:** discover support and request the minimum version your feature needs.

- **Mistake:** Assume one list response contains everything.  
  **Best practice:** implement pagination.

- **Mistake:** Delete resources by name prefix only.  
  **Best practice:** validate project, ID, ownership tags, and dependencies.

- **Mistake:** Treat OpenStack multi-service workflow as one database transaction.  
  **Best practice:** implement compensating rollback/reconciliation.

- **Mistake:** Run integration tests in production projects.  
  **Best practice:** isolate test projects and quotas.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the first API called in most authenticated OpenStack workflows?

**Short answer:** Keystone Identity API to obtain authentication scope/token and service catalog.

### Q2. Where is a Keystone v3 token returned?

**Short answer:** In the `X-Subject-Token` response header.

### Q3. How is a token sent to other services?

**Short answer:** With the `X-Auth-Token` request header.

### Q4. What is a service catalog?

**Short answer:** Keystone-provided registry of service endpoints, regions, and interfaces.

### Q5. Public vs internal endpoint?

**Short answer:** Different network exposure/interface choices for the same service.

### Q6. Major version vs microversion?

**Short answer:** Major version selects an API endpoint family; microversion selects behavior/features within a compatible major version.

### Q7. Nova generic microversion header?

**Short answer:** `OpenStack-API-Version: compute <version>`.

### Q8. Cinder microversion header?

**Short answer:** `OpenStack-API-Version: volume <version>`.

### Q9. What is `X-OpenStack-Request-ID` useful for?

**Short answer:** Correlating an API request with service logs and troubleshooting.

### Q10. What does HTTP 202 mean?

**Short answer:** Request accepted for asynchronous processing; final resource state is not yet guaranteed.

### Q11. 401 vs 403?

**Short answer:** 401 authentication failed; 403 authenticated identity lacks authorization.

### Q12. What is idempotency?

**Short answer:** Repeating an operation does not create unintended additional effects.

### Q13. Why can retrying POST after timeout be dangerous?

**Short answer:** The first request may have succeeded, causing duplicate resources.

### Q14. What should you do after an ambiguous timeout?

**Short answer:** Reconcile actual cloud state before retrying creation.

### Q15. Why use application credentials?

**Short answer:** They provide revocable automation credentials without storing a user's primary password.

### Q16. Why use `openstacksdk`?

**Short answer:** It handles authentication, discovery, resources, pagination, and service-specific APIs at a higher level.

### Q17. What does keystoneauth Session solve?

**Short answer:** Authentication, endpoint discovery, request sessions, and microversion-related service access.

### Q18. Why implement pagination?

**Short answer:** Large API result sets may be split across multiple responses.

### Q19. Why is a `200` response not enough for data correctness?

**Short answer:** The application must still validate the returned JSON/schema/content it expects.

### Q20. What is a compensating action?

**Short answer:** A cleanup/reversal operation used when part of a multi-service workflow succeeds and a later step fails.

### Q21. Why tag automation resources?

**Short answer:** To identify ownership, reconcile desired state, and perform safe cleanup.

### Q22. What is the correct model for asynchronous VM creation?

**Short answer:** Submit create, record ID/request ID, poll until ACTIVE or ERROR, then verify.

### Q23. Why should clients discover microversion support?

**Short answer:** Different clouds may expose different maximum versions/features.

### Q24. Why shouldn't normal applications directly allocate Placement resources?

**Short answer:** Nova owns compute scheduling/allocation consistency.

### Q25. What is the core production API-engineering mindset?

**Short answer:** Authenticate securely, discover capabilities, send a versioned request, trace it with request IDs, handle asynchronous/partial failure, reconcile state, and verify final outcome.

---

# Expanded Self-Assessment Bank

### Q1. What makes OpenStack API-first?
**Answer:** CLI, Horizon, SDKs, and automation all consume service APIs.

### Q2. Where is Keystone v3 token returned?
**Answer:** X-Subject-Token response header.

### Q3. How is token sent to services?
**Answer:** X-Auth-Token request header.

### Q4. Why does scope matter?
**Answer:** Roles are evaluated in project/domain/system context.

### Q5. Why use application credentials?
**Answer:** Scoped revocable automation secrets separate from human passwords.

### Q6. What does service catalog provide?
**Answer:** Service types, regions, endpoint interfaces, and URLs.

### Q7. Why not hard-code endpoints?
**Answer:** They differ by cloud/region/interface and can change.

### Q8. Major version vs microversion?
**Answer:** API family vs feature behavior within the family.

### Q9. Why not use latest microversion blindly?
**Answer:** Target cloud may not support it and behavior can change.

### Q10. Why capture request IDs?
**Answer:** To correlate client failures with distributed service logs.

### Q11. What does HTTP 202 mean?
**Answer:** Accepted for asynchronous processing, not complete.

### Q12. HTTP timeout vs operation timeout?
**Answer:** One HTTP call timeout versus total resource transition deadline.

### Q13. What is retry classification?
**Answer:** Deciding which failures are transient and safe to retry.

### Q14. Why not retry 403?
**Answer:** Authorization will not improve by repetition.

### Q15. What is exponential backoff?
**Answer:** Increasing delay between retries.

### Q16. Why add jitter?
**Answer:** Avoid synchronized retry storms.

### Q17. What is idempotency?
**Answer:** Repeated execution does not create unintended extra effects.

### Q18. Why is retrying POST after timeout dangerous?
**Answer:** First create may have succeeded, producing duplicates.

### Q19. What should happen after ambiguous timeout?
**Answer:** Reconcile cloud state before another create.

### Q20. What is a reconciliation loop?
**Answer:** Compare desired vs actual and make minimum safe change.

### Q21. Why detect drift?
**Answer:** A resource can exist but not match required configuration.

### Q22. Why store UUIDs?
**Answer:** Names are not reliably unique.

### Q23. Why tag owned resources?
**Answer:** Safe cleanup, audit, and reconciliation.

### Q24. What is Saga compensation?
**Answer:** Cleanup/reversal of completed steps after partial multi-service failure.

### Q25. Why does cleanup need dependency order?
**Answer:** Children/attachments can block parent deletion.

### Q26. Why is concurrency control necessary?
**Answer:** Two workers can race and duplicate resources.

### Q27. Why is pagination necessary?
**Answer:** A single list response may be incomplete.

### Q28. Why use server-side filters?
**Answer:** Reduce data transfer and API load.

### Q29. What does keystoneauth Session solve?
**Answer:** Authentication, TLS, token refresh, discovery, and HTTP session behavior.

### Q30. What is an Adapter?
**Answer:** Session bound to a service/region/interface/version context.

### Q31. Why use openstacksdk?
**Answer:** High-level service proxies, resource objects, pagination, and waiters.

### Q32. What should robust server-create workflow do?
**Answer:** Resolve dependencies, create, store ID, wait, handle ERROR/timeout, reconcile.

### Q33. Why can server action return 409?
**Answer:** Resource is in a conflicting state/task.

### Q34. What is a microversion contract?
**Answer:** Fail early when required service version is unsupported.

### Q35. Why reconcile security-group rules?
**Answer:** Avoid duplicate or drifting firewall policy.

### Q36. Why verify floating IP with actual traffic?
**Answer:** API state does not prove data-plane reachability.

### Q37. What is the Cinder attachment lifecycle?
**Answer:** available→attach→in-use→detach→available.

### Q38. Why stream Glance/Swift data?
**Answer:** Avoid huge memory use and support integrity checks.

### Q39. How should Heat be monitored?
**Answer:** Poll stack status and inspect nested resource events.

### Q40. Why does Octavia have provisioning and operating status?
**Answer:** Configuration state and runtime member health differ.

### Q41. Why must Barbican payloads not be logged?
**Answer:** They are secrets.

### Q42. Why should normal apps not manipulate Placement?
**Answer:** Nova owns allocation consistency.

### Q43. Why reuse HTTP sessions?
**Answer:** Reduce auth/TLS/discovery overhead.

### Q44. What is backpressure?
**Answer:** Reduce client request rate when service is throttled/overloaded.

### Q45. What is a circuit breaker?
**Answer:** Temporarily stop repeated calls to a persistently failing dependency.

### Q46. API latency vs operation latency?
**Answer:** HTTP response time versus end-to-end resource completion.

### Q47. What is the testing pyramid?
**Answer:** Unit, integration in isolated project, then controlled E2E.

### Q48. What is a contract test?
**Answer:** Startup validation of services, resource references, and API versions.

### Q49. Why pin SDK version?
**Answer:** SDK behavior evolves independently of cloud release.

### Q50. Why redact tokens?
**Answer:** They are bearer credentials.

### Q51. Why forbid verify=False in production?
**Answer:** It removes endpoint identity verification.

### Q52. Where should secrets live?
**Answer:** Secret manager, protected CI variables, workload identity, or locked credential file.

### Q53. Why pace bulk operations?
**Answer:** Avoid overwhelming APIs, schedulers, image, network, DB/MQ, and storage.

### Q54. 401 vs 403?
**Answer:** Authentication vs authorization.

### Q55. What can 404 mean?
**Answer:** Missing resource, wrong endpoint/version/region/scope, or hidden resource.

### Q56. What does 409 usually mean?
**Answer:** Current state or dependency conflict.

### Q57. What should happen on 429?
**Answer:** Apply bounded backoff/jitter and reduce concurrency.

### Q58. How should 503 be handled?
**Answer:** Bounded retry only when semantics are safe, with reconciliation for ambiguous writes.

### Q59. What is the core API engineering mindset?
**Answer:** Secure auth, discovery, versioning, request tracing, async state, reconciliation, compensation, verification.


## Completion Checklist

- [ ] I understand REST/HTTP/JSON.
- [ ] I can authenticate against Keystone v3.
- [ ] I understand `X-Subject-Token` and `X-Auth-Token`.
- [ ] I understand scopes and application credentials.
- [ ] I understand service catalog/regions/interfaces.
- [ ] I understand major versions and microversions.
- [ ] I understand request IDs.
- [ ] I can interpret common HTTP status codes.
- [ ] I can use `curl` safely.
- [ ] I can use `clouds.yaml`.
- [ ] I can use `openstack --debug`.
- [ ] I can use Python `requests`.
- [ ] I understand keystoneauth sessions/adapters.
- [ ] I can use openstacksdk.
- [ ] I understand Nova APIs.
- [ ] I understand Neutron APIs.
- [ ] I understand Cinder APIs.
- [ ] I understand Glance/Swift/Heat APIs.
- [ ] I understand Octavia/Barbican/Manila/Ironic/Designate concepts.
- [ ] I can implement polling, pagination, timeout, and retry.
- [ ] I can build idempotent reconciliation.
- [ ] I understand partial-failure compensation.
- [ ] I understand secure credential/token handling.
- [ ] I can design API tests and compatibility checks.
- [ ] I completed all 30 labs.
- [ ] I completed the OpenStack Infrastructure Automation Service project.
