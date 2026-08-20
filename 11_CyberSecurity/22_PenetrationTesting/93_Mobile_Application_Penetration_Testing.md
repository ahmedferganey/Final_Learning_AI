# 93. Mobile Application Penetration Testing

> Phase 22 — Penetration Testing

This course is **lab-first, authorization-first, and evidence-driven**. The material is designed for deliberately vulnerable applications, owned devices/emulators, disposable AD domains, or other systems explicitly covered by written authorization.

---

## 1. Topic Title

**Mobile Application Penetration Testing**

---

## 2. Learning Objectives

- Understand Android and iOS application/package structure and platform trust boundaries.
- Use ADB, static decompilation, manifests/plists, and controlled runtime observation on owned apps/devices.
- Assess local storage, logs, clipboard, backups, screenshots, key storage, and crypto use.
- Assess Android components, intents, deep links, WebViews, and IPC exposure.
- Assess iOS URL schemes, entitlements, ATS, Keychain, and file-protection concepts.
- Assess mobile TLS, certificate pinning, OAuth/PKCE, tokens, and backend APIs.
- Use Frida-style dynamic instrumentation only in authorized lab apps.
- Identify client-side trust assumptions that must be enforced on the backend.
- Write platform-specific findings and remediation.
- Retest on the same app/OS/device configuration.

---

## 3. Prerequisites

Required:

```text
90 Ethical Hacking and Security Assessment
Web/API Security Fundamentals
HTTP / TLS
Android/iOS basic user familiarity
Linux command line
Basic Java / Kotlin / Swift awareness is helpful
```

Recommended:

```text
Android Studio emulator
ADB
JADX
apktool
Burp or ZAP
dedicated test device
```

Use only apps/devices you own or are explicitly authorized to test.

---

## 4. Core Concepts Explanation

# Part 1 — Mobile Application Penetration Testing Purpose

### Core Explanation

Mobile application penetration testing evaluates the mobile client, local device storage, platform integration, network behavior, and backend APIs within an authorized scope.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 2 — Mobile Testing Scope

### Core Explanation

Scope should identify Android/iOS package identifiers, app versions, test accounts, backend APIs, devices, environments, and third-party services.

### Diagram / Code / Command Example

```text
Written authorization
   ↓
App package / bundle
   ↓
Test accounts
   ↓
Device / emulator
   ↓
Allowed backend APIs
   ↓
No third-party app/service testing
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 3 — Mobile Rules of Engagement

### Core Explanation

Define whether reverse engineering, dynamic instrumentation, rooted/jailbroken devices, traffic interception, and backend API testing are allowed.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 4 — Test Device

### Core Explanation

Use a dedicated test device, emulator, or simulator rather than a personal device containing real sensitive data.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 5 — Synthetic Accounts

### Core Explanation

Use test users and synthetic records so mobile workflows can be exercised safely.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 6 — Android Application Architecture

### Core Explanation

Android apps contain manifests, DEX code, resources, native libraries, assets, and platform components.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 7 — APK

### Core Explanation

An APK is an Android application package containing executable code, resources, manifest metadata, and signatures.

### Diagram / Code / Command Example

```text
APK
├─ AndroidManifest.xml
├─ classes*.dex
├─ resources.arsc
├─ res/
├─ lib/
└─ META-INF/

Static assessment asks:
permissions?
exported components?
network config?
embedded secrets?
debuggable?
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 8 — AAB Awareness

### Core Explanation

Android App Bundles are publishing artifacts from which device-specific APKs may be generated.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 9 — AndroidManifest.xml

### Core Explanation

The manifest declares package identity, components, permissions, intent filters, SDK requirements, and security-relevant settings.

### Diagram / Code / Command Example

```text
APK
├─ AndroidManifest.xml
├─ classes*.dex
├─ resources.arsc
├─ res/
├─ lib/
└─ META-INF/

Static assessment asks:
permissions?
exported components?
network config?
embedded secrets?
debuggable?
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 10 — Android Permission Model

### Core Explanation

Applications request permissions for protected platform capabilities and should request only what they need.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 11 — Dangerous Permission

### Core Explanation

Some Android permissions require runtime user approval because they expose sensitive capabilities.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 12 — Exported Component

### Core Explanation

Activities, services, receivers, or providers exposed to other apps require deliberate permissions and input validation.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 13 — Activity

### Core Explanation

An Activity represents a user-facing Android component and may be launchable through intents.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 14 — Service

### Core Explanation

Android Services perform background or bound work and should not expose privileged operations unnecessarily.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 15 — Broadcast Receiver

### Core Explanation

Receivers process broadcast intents and need appropriate export/permission controls.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 16 — Content Provider

### Core Explanation

Content providers expose structured data and need correct URI permissions and authorization.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 17 — Intent

### Core Explanation

Intents carry actions, data, categories, extras, and component targets between Android components.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 18 — Intent Filter

### Core Explanation

Intent filters define which implicit intents a component may receive and can unintentionally expose functionality.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 19 — PendingIntent Awareness

### Core Explanation

PendingIntent grants another process the ability to perform an app-defined future action and must be scoped/immutable appropriately.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 20 — Android Deep Link

### Core Explanation

Deep links route external URIs into application components and require strict destination and parameter validation.

### Diagram / Code / Command Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 21 — Android App Link

### Core Explanation

Verified app links bind HTTPS domains to the intended Android application and reduce ambiguous handler selection.

### Diagram / Code / Command Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 22 — Custom URL Scheme

### Core Explanation

Custom schemes can be claimed by multiple apps and should not carry sensitive secrets without additional verification.

### Diagram / Code / Command Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 23 — Android WebView

### Core Explanation

WebViews embed web content and create a browser-to-native trust boundary.

### Diagram / Code / Command Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 24 — WebView JavaScript

### Core Explanation

Enable JavaScript only when needed and avoid loading untrusted content with powerful native capabilities.

### Diagram / Code / Command Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 25 — WebView Native Bridge

### Core Explanation

JavaScript interfaces exposed to WebView content can become high-impact attack surfaces.

### Diagram / Code / Command Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 26 — WebView File Access

### Core Explanation

File/content URL access should be minimized and configured according to application need.

### Diagram / Code / Command Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 27 — WebView Mixed Content

### Core Explanation

Loading HTTP resources inside HTTPS content weakens transport security.

### Diagram / Code / Command Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 28 — Android Network Security Config

### Core Explanation

Android network security configuration can define cleartext policy, custom trust anchors, and certificate pinning behavior.

### Diagram / Code / Command Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 29 — Cleartext Traffic

### Core Explanation

Sensitive application traffic should not use plaintext HTTP across untrusted networks.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 30 — TLS Validation

### Core Explanation

Mobile clients should validate certificate chains and hostnames using supported platform trust mechanisms.

### Diagram / Code / Command Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 31 — Certificate Pinning

### Core Explanation

Pinning can reduce some interception risks but adds certificate lifecycle and failure-management complexity.

### Diagram / Code / Command Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 32 — Android Keystore

### Core Explanation

Android Keystore can protect cryptographic keys and may use hardware-backed storage on supported devices.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 33 — SharedPreferences

### Core Explanation

Preferences are convenient local storage but should not contain plaintext credentials or high-value secrets.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 34 — SQLite Storage

### Core Explanation

Local databases can contain cached sensitive data and need minimization, access protection, and safe backup behavior.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 35 — File Storage

### Core Explanation

Internal, external, cache, and shared storage have different exposure and lifecycle characteristics.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 36 — External Storage Risk

### Core Explanation

Externally accessible storage may be visible to other apps/users depending on platform/version and should not contain secrets.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 37 — Backup Configuration

### Core Explanation

App backup settings can unintentionally copy sensitive local data to backups.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 38 — Clipboard Risk

### Core Explanation

Sensitive tokens or credentials copied to the clipboard may be visible to other apps or users.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 39 — Screenshot Risk

### Core Explanation

Sensitive screens may require platform protections against screenshots or recent-app previews when justified.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 40 — Logcat

### Core Explanation

Application logs should not expose passwords, tokens, session identifiers, personal information, or cryptographic secrets.

### Diagram / Code / Command Example

```bash
# Own lab device
adb logcat -d | tail -n 50
```

Check that tokens, passwords, personal data,
and cryptographic material are not logged.

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 41 — Debuggable Flag

### Core Explanation

Production Android applications should not normally be debuggable.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 42 — Test-Only Components

### Core Explanation

Development activities, test endpoints, debug menus, and mock services should not remain exposed in production builds.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 43 — Hardcoded Secret

### Core Explanation

API keys, passwords, symmetric keys, and private credentials embedded in a mobile binary should be assumed extractable.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 44 — Obfuscation

### Core Explanation

Code obfuscation raises reverse-engineering cost but is not a secret-storage mechanism.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 45 — JADX

### Core Explanation

JADX decompiles Android DEX bytecode into Java-like source for static analysis.

### Diagram / Code / Command Example

```text
APK
  ↓
JADX / apktool
  ↓
manifest + Java/Kotlin-like source + resources
  ↓
identify:
API endpoints
logging
storage
crypto use
WebView settings
exported components
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 46 — apktool Awareness

### Core Explanation

apktool decodes resources and smali-level structure and can help inspect manifests and resources.

### Diagram / Code / Command Example

```text
APK
├─ AndroidManifest.xml
├─ classes*.dex
├─ resources.arsc
├─ res/
├─ lib/
└─ META-INF/

Static assessment asks:
permissions?
exported components?
network config?
embedded secrets?
debuggable?
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 47 — Smali Awareness

### Core Explanation

Smali is an assembly-like representation of Dalvik bytecode useful for understanding low-level Android logic.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 48 — Native Library Awareness

### Core Explanation

JNI/native libraries expand the attack surface and may require native-code analysis for sensitive functions.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 49 — ADB

### Core Explanation

Android Debug Bridge provides authorized device/emulator interaction for installation, shell access, logs, and testing.

### Diagram / Code / Command Example

```bash
# Own emulator/device only
adb devices
adb shell getprop ro.build.version.release
adb shell pm list packages | head
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 50 — ADB Device Enumeration

### Core Explanation

Verify that only intended test devices are connected before running commands.

### Diagram / Code / Command Example

```bash
# Own emulator/device only
adb devices
adb shell getprop ro.build.version.release
adb shell pm list packages | head
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 51 — ADB Shell

### Core Explanation

The device shell helps inspect platform state, files available to the test context, and package information.

### Diagram / Code / Command Example

```bash
# Own emulator/device only
adb devices
adb shell getprop ro.build.version.release
adb shell pm list packages | head
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 52 — Application Data Directory

### Core Explanation

App-private data should not be accessible to unrelated unprivileged apps under normal platform security.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 53 — Rooted Device Awareness

### Core Explanation

Rooting changes device security assumptions and is useful only for dedicated test devices when authorized.

### Diagram / Code / Command Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 54 — Emulator

### Core Explanation

Emulators provide reproducible snapshots and instrumentation for Android security testing.

### Diagram / Code / Command Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 55 — Frida Awareness

### Core Explanation

Frida provides dynamic instrumentation for observing or changing runtime behavior in owned/authorized applications.

### Diagram / Code / Command Example

```text
Own lab app
  ↓
dynamic instrumentation
  ↓
observe method arguments / return values
  ↓
understand runtime behavior
  ↓
remove tooling after test

Use only on apps you own or are explicitly authorized to test.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 56 — Dynamic Instrumentation Boundary

### Core Explanation

Use instrumentation to understand application logic, not to bypass controls on third-party apps without permission.

### Diagram / Code / Command Example

```text
Own lab app
  ↓
dynamic instrumentation
  ↓
observe method arguments / return values
  ↓
understand runtime behavior
  ↓
remove tooling after test

Use only on apps you own or are explicitly authorized to test.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 57 — Runtime Method Observation

### Core Explanation

Observing method inputs/outputs can confirm whether secrets, keys, or authorization decisions exist only on the client.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 58 — Client-Side Trust

### Core Explanation

A hostile user controls their own client; security-critical decisions must be enforced on the server or protected platform boundary.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 59 — Root Detection Awareness

### Core Explanation

Root detection can signal risk but can often be bypassed and should not be the sole control protecting backend authorization.

### Diagram / Code / Command Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 60 — Anti-Tamper Awareness

### Core Explanation

Integrity checks can raise attacker cost but do not replace secure backend design.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 61 — Biometric Authentication

### Core Explanation

Biometrics should unlock a protected local credential or authorize a platform-mediated action rather than serve as a standalone backend identity.

### Diagram / Code / Command Example

```text
Biometric prompt
  ↓
platform authentication result
  ↓
unlock local secret / authorize operation
  ↓
server still enforces account authorization

Biometric UI alone must not become the sole server-side control.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 62 — Biometric Bypass Risk

### Core Explanation

If the app only hides a screen after biometric success while a token remains accessible, the control may be cosmetic.

### Diagram / Code / Command Example

```text
Biometric prompt
  ↓
platform authentication result
  ↓
unlock local secret / authorize operation
  ↓
server still enforces account authorization

Biometric UI alone must not become the sole server-side control.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 63 — Android Cryptography

### Core Explanation

Use platform cryptographic APIs and strong random generation rather than custom algorithms.

### Diagram / Code / Command Example

```text
Key material
  ↓ platform keystore/keychain
  ↓ app asks platform to use key
  ↓ ciphertext/signature
  ↓ key never stored as plaintext app config
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 64 — Random Number Generation

### Core Explanation

Security tokens and keys require cryptographically secure random sources.

### Diagram / Code / Command Example

```text
Key material
  ↓ platform keystore/keychain
  ↓ app asks platform to use key
  ↓ ciphertext/signature
  ↓ key never stored as plaintext app config
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 65 — Key Management

### Core Explanation

Long-lived keys should remain in platform-protected storage or backend systems rather than plaintext app files.

### Diagram / Code / Command Example

```text
Key material
  ↓ platform keystore/keychain
  ↓ app asks platform to use key
  ↓ ciphertext/signature
  ↓ key never stored as plaintext app config
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 66 — Android IPC Security

### Core Explanation

Binder/IPC components should validate callers, permissions, and input.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 67 — Content URI Security

### Core Explanation

Content URIs and temporary grants should expose only intended resources for limited duration.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 68 — FileProvider

### Core Explanation

FileProvider can share files through controlled content URIs instead of exposing raw filesystem paths.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 69 — iOS Application Architecture

### Core Explanation

iOS apps include an executable, Info.plist, entitlements, resources, frameworks, and code signatures.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 70 — IPA

### Core Explanation

An IPA is an iOS application archive containing the app bundle and resources.

### Diagram / Code / Command Example

```text
IPA
  ↓ unzip
Payload/App.app/
  ├─ executable
  ├─ Info.plist
  ├─ frameworks
  └─ resources

Review:
URL schemes
entitlements
ATS
permissions
embedded endpoints
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 71 — Info.plist

### Core Explanation

Info.plist contains bundle metadata, URL schemes, permissions descriptions, networking settings, and configuration.

### Diagram / Code / Command Example

```text
IPA
  ↓ unzip
Payload/App.app/
  ├─ executable
  ├─ Info.plist
  ├─ frameworks
  └─ resources

Review:
URL schemes
entitlements
ATS
permissions
embedded endpoints
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 72 — Entitlements

### Core Explanation

Entitlements grant platform capabilities such as keychain groups, associated domains, push, or app groups.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 73 — ATS

### Core Explanation

App Transport Security encourages secure TLS networking and should not be broadly disabled.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 74 — iOS URL Scheme

### Core Explanation

Custom URL schemes can expose routing logic and require careful validation.

### Diagram / Code / Command Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 75 — Universal Link

### Core Explanation

Universal Links bind approved HTTPS domains to an iOS application.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 76 — iOS Keychain

### Core Explanation

The Keychain stores credentials and cryptographic material with configurable accessibility classes.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 77 — NSUserDefaults Awareness

### Core Explanation

NSUserDefaults is not appropriate for high-value plaintext secrets.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 78 — iOS File Protection

### Core Explanation

Data-protection classes control when encrypted files become accessible relative to device unlock state.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 79 — App Group Storage

### Core Explanation

Shared app-group containers increase the number of processes that may access data and require careful entitlement governance.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 80 — Pasteboard Risk

### Core Explanation

Sensitive clipboard data can leak between apps or remain longer than intended.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 81 — Jailbreak Awareness

### Core Explanation

Jailbroken test devices can expose otherwise protected files and enable instrumentation, changing normal platform assumptions.

### Diagram / Code / Command Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 82 — iOS Simulator

### Core Explanation

The simulator provides convenient testing but does not reproduce every hardware security property of a physical device.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 83 — Static iOS Analysis

### Core Explanation

Inspect Info.plist, entitlements, strings, frameworks, endpoints, and cryptographic usage.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 84 — Dynamic iOS Analysis Awareness

### Core Explanation

Authorized dynamic instrumentation can observe runtime behavior on dedicated test devices.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 85 — Mobile Network Interception

### Core Explanation

Use a controlled proxy on your own device/app to inspect application traffic when policy permits.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 86 — Proxy CA Trust

### Core Explanation

Installing a lab proxy CA changes the device trust environment and should be reverted after testing.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 87 — Certificate Pinning Test

### Core Explanation

Determine whether pinning is implemented and whether its lifecycle/failure behavior matches the threat model.

### Diagram / Code / Command Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 88 — Backend API Scope

### Core Explanation

Mobile application testing commonly requires backend API testing, which must be explicitly included in scope.

### Diagram / Code / Command Example

```text
Written authorization
   ↓
App package / bundle
   ↓
Test accounts
   ↓
Device / emulator
   ↓
Allowed backend APIs
   ↓
No third-party app/service testing
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 89 — Mobile API Authentication

### Core Explanation

Review token issuance, renewal, storage, device binding, logout, and MFA.

### Diagram / Code / Command Example

```text
Mobile App
  ↓
API Gateway / Backend
  ↓
Authentication
  ↓
Object authorization
  ↓
Business logic
  ↓
Data

Mobile UI restrictions never replace backend authorization.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 90 — Mobile API Authorization

### Core Explanation

Server-side object and function authorization must not rely on the mobile UI.

### Diagram / Code / Command Example

```text
Written authorization
   ↓
App package / bundle
   ↓
Test accounts
   ↓
Device / emulator
   ↓
Allowed backend APIs
   ↓
No third-party app/service testing
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 91 — Device Identifier Trust

### Core Explanation

Device identifiers can change or be spoofed and should not be treated as strong identity by themselves.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 92 — Push Notification Security

### Core Explanation

Notifications can expose sensitive content on lock screens and device tokens need protected lifecycle.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 93 — Push Token

### Core Explanation

Push tokens identify app/device delivery channels but should not act as standalone user authentication.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 94 — In-App Browser / Custom Tabs Awareness

### Core Explanation

Authentication flows using browser-based components should preserve origin, redirect, state, and PKCE protections.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 95 — OAuth in Mobile Apps

### Core Explanation

Public mobile clients should use authorization code with PKCE rather than embedded client secrets.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 96 — Redirect URI Handling

### Core Explanation

Mobile OAuth redirects must be tightly bound to the intended app through verified links or robust scheme controls.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 97 — SSO Token Storage

### Core Explanation

SSO tokens are high-value bearer credentials and need secure local handling and revocation.

### Diagram / Code / Command Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 98 — Offline Mode

### Core Explanation

Cached authorization and data in offline mode require expiry and conflict-handling rules.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 99 — Local Data Minimization

### Core Explanation

Store only the data required for offline or performance needs and clear it at appropriate lifecycle points.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 100 — Logout Data Cleanup

### Core Explanation

Logout should remove or invalidate local secrets, cached sensitive data, and server-side sessions as appropriate.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 101 — Multi-Account Switching

### Core Explanation

Switching accounts should not leak cached data, files, notifications, or WebView sessions between users.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 102 — Screen Overlay Awareness

### Core Explanation

Sensitive input flows may need platform protections against overlay or tapjacking risks depending on threat model.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 103 — Keyboard / IME Risk Awareness

### Core Explanation

Highly sensitive input can interact with third-party keyboards; application design should minimize unnecessary secret entry.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 104 — Accessibility Service Risk Awareness

### Core Explanation

Accessibility services have powerful UI visibility and control; apps should not rely solely on client UI secrecy.

### Diagram / Code / Command Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 105 — Mobile Logging to SIEM

### Core Explanation

Important authentication, device-registration, token, and high-risk actions should be visible through backend telemetry.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 106 — Mobile Finding Evidence

### Core Explanation

Record app version, device/emulator, OS version, component, test account, and exact action.

### Diagram / Code / Command Example

```text
Finding:
Platform / app version
Component
Test device/emulator
Steps
Evidence
Security impact
Backend relevance
Remediation
Retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 107 — Mobile Finding Remediation

### Core Explanation

Fix root cause in platform configuration, app code, local storage, or backend authorization as appropriate.

### Diagram / Code / Command Example

```text
Finding:
Platform / app version
Component
Test device/emulator
Steps
Evidence
Security impact
Backend relevance
Remediation
Retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 108 — Mobile Retest

### Core Explanation

Repeat the same static/dynamic/API validation after the fix.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 109 — Mobile Application Penetration Testing Final Mental Model

### Core Explanation

Treat the mobile client as user-controlled, validate platform storage/IPC/network behavior, and enforce real authorization and data protection on trusted backend/platform boundaries.

### Diagram / Code / Command Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Mobile Application Penetration Testing Purpose

### Objective

Practice **Mobile Application Penetration Testing Purpose** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 2 — Mobile Testing Scope

### Objective

Practice **Mobile Testing Scope** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
   ↓
App package / bundle
   ↓
Test accounts
   ↓
Device / emulator
   ↓
Allowed backend APIs
   ↓
No third-party app/service testing
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 3 — Mobile Rules of Engagement

### Objective

Practice **Mobile Rules of Engagement** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 4 — Test Device

### Objective

Practice **Test Device** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 5 — Synthetic Accounts

### Objective

Practice **Synthetic Accounts** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 6 — Android Application Architecture

### Objective

Practice **Android Application Architecture** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 7 — APK

### Objective

Practice **APK** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
APK
├─ AndroidManifest.xml
├─ classes*.dex
├─ resources.arsc
├─ res/
├─ lib/
└─ META-INF/

Static assessment asks:
permissions?
exported components?
network config?
embedded secrets?
debuggable?
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 8 — AAB Awareness

### Objective

Practice **AAB Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 9 — AndroidManifest.xml

### Objective

Practice **AndroidManifest.xml** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
APK
├─ AndroidManifest.xml
├─ classes*.dex
├─ resources.arsc
├─ res/
├─ lib/
└─ META-INF/

Static assessment asks:
permissions?
exported components?
network config?
embedded secrets?
debuggable?
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 10 — Android Permission Model

### Objective

Practice **Android Permission Model** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 11 — Dangerous Permission

### Objective

Practice **Dangerous Permission** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 12 — Exported Component

### Objective

Practice **Exported Component** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 13 — Activity

### Objective

Practice **Activity** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 14 — Service

### Objective

Practice **Service** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 15 — Broadcast Receiver

### Objective

Practice **Broadcast Receiver** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 16 — Content Provider

### Objective

Practice **Content Provider** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 17 — Intent

### Objective

Practice **Intent** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 18 — Intent Filter

### Objective

Practice **Intent Filter** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 19 — PendingIntent Awareness

### Objective

Practice **PendingIntent Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 20 — Android Deep Link

### Objective

Practice **Android Deep Link** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 21 — Android App Link

### Objective

Practice **Android App Link** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 22 — Custom URL Scheme

### Objective

Practice **Custom URL Scheme** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External URI
  ↓
OS dispatcher
  ↓
app route
  ↓
validate scheme / host / path / parameters
  ↓
authenticate / authorize sensitive action
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 23 — Android WebView

### Objective

Practice **Android WebView** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 24 — WebView JavaScript

### Objective

Practice **WebView JavaScript** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 25 — WebView Native Bridge

### Objective

Practice **WebView Native Bridge** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 26 — WebView File Access

### Objective

Practice **WebView File Access** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 27 — WebView Mixed Content

### Objective

Practice **WebView Mixed Content** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Untrusted content
   ↓
WebView
   ↓
JavaScript?
file access?
mixed content?
native bridge?
URL allowlist?

Minimize capabilities and validate navigation.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 28 — Android Network Security Config

### Objective

Practice **Android Network Security Config** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 29 — Cleartext Traffic

### Objective

Practice **Cleartext Traffic** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 30 — TLS Validation

### Objective

Practice **TLS Validation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 31 — Certificate Pinning

### Objective

Practice **Certificate Pinning** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
App
  ↓ TLS
API

Validate:
system trust
hostname
certificate chain
TLS config

Pinning is defense-in-depth and requires lifecycle planning.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 32 — Android Keystore

### Objective

Practice **Android Keystore** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 33 — SharedPreferences

### Objective

Practice **SharedPreferences** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 34 — SQLite Storage

### Objective

Practice **SQLite Storage** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 35 — File Storage

### Objective

Practice **File Storage** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 36 — External Storage Risk

### Objective

Practice **External Storage Risk** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Sensitive data
  ↓
platform secure storage where appropriate
  ↓
access controls
  ↓
device lock / key protection
  ↓
minimal retention

Avoid plaintext tokens in preferences/files/logs.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 37 — Backup Configuration

### Objective

Practice **Backup Configuration** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 38 — Clipboard Risk

### Objective

Practice **Clipboard Risk** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 39 — Screenshot Risk

### Objective

Practice **Screenshot Risk** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 40 — Logcat

### Objective

Practice **Logcat** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```bash
# Own lab device
adb logcat -d | tail -n 50
```

Check that tokens, passwords, personal data,
and cryptographic material are not logged.

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 41 — Debuggable Flag

### Objective

Practice **Debuggable Flag** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 42 — Test-Only Components

### Objective

Practice **Test-Only Components** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 43 — Hardcoded Secret

### Objective

Practice **Hardcoded Secret** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 44 — Obfuscation

### Objective

Practice **Obfuscation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 45 — JADX

### Objective

Practice **JADX** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
APK
  ↓
JADX / apktool
  ↓
manifest + Java/Kotlin-like source + resources
  ↓
identify:
API endpoints
logging
storage
crypto use
WebView settings
exported components
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 46 — apktool Awareness

### Objective

Practice **apktool Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
APK
├─ AndroidManifest.xml
├─ classes*.dex
├─ resources.arsc
├─ res/
├─ lib/
└─ META-INF/

Static assessment asks:
permissions?
exported components?
network config?
embedded secrets?
debuggable?
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 47 — Smali Awareness

### Objective

Practice **Smali Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 48 — Native Library Awareness

### Objective

Practice **Native Library Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 49 — ADB

### Objective

Practice **ADB** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```bash
# Own emulator/device only
adb devices
adb shell getprop ro.build.version.release
adb shell pm list packages | head
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 50 — ADB Device Enumeration

### Objective

Practice **ADB Device Enumeration** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```bash
# Own emulator/device only
adb devices
adb shell getprop ro.build.version.release
adb shell pm list packages | head
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 51 — ADB Shell

### Objective

Practice **ADB Shell** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```bash
# Own emulator/device only
adb devices
adb shell getprop ro.build.version.release
adb shell pm list packages | head
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 52 — Application Data Directory

### Objective

Practice **Application Data Directory** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 53 — Rooted Device Awareness

### Objective

Practice **Rooted Device Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 54 — Emulator

### Objective

Practice **Emulator** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 55 — Frida Awareness

### Objective

Practice **Frida Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Own lab app
  ↓
dynamic instrumentation
  ↓
observe method arguments / return values
  ↓
understand runtime behavior
  ↓
remove tooling after test

Use only on apps you own or are explicitly authorized to test.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 56 — Dynamic Instrumentation Boundary

### Objective

Practice **Dynamic Instrumentation Boundary** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Own lab app
  ↓
dynamic instrumentation
  ↓
observe method arguments / return values
  ↓
understand runtime behavior
  ↓
remove tooling after test

Use only on apps you own or are explicitly authorized to test.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 57 — Runtime Method Observation

### Objective

Practice **Runtime Method Observation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 58 — Client-Side Trust

### Objective

Practice **Client-Side Trust** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 59 — Root Detection Awareness

### Objective

Practice **Root Detection Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Testing environment:
emulator / simulator
or dedicated test device
  ↓
snapshot / reset capability
  ↓
synthetic accounts
  ↓
isolated proxy / logging
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 60 — Anti-Tamper Awareness

### Objective

Practice **Anti-Tamper Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 61 — Biometric Authentication

### Objective

Practice **Biometric Authentication** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Biometric prompt
  ↓
platform authentication result
  ↓
unlock local secret / authorize operation
  ↓
server still enforces account authorization

Biometric UI alone must not become the sole server-side control.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 62 — Biometric Bypass Risk

### Objective

Practice **Biometric Bypass Risk** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Biometric prompt
  ↓
platform authentication result
  ↓
unlock local secret / authorize operation
  ↓
server still enforces account authorization

Biometric UI alone must not become the sole server-side control.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 63 — Android Cryptography

### Objective

Practice **Android Cryptography** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Key material
  ↓ platform keystore/keychain
  ↓ app asks platform to use key
  ↓ ciphertext/signature
  ↓ key never stored as plaintext app config
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 64 — Random Number Generation

### Objective

Practice **Random Number Generation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Key material
  ↓ platform keystore/keychain
  ↓ app asks platform to use key
  ↓ ciphertext/signature
  ↓ key never stored as plaintext app config
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 65 — Key Management

### Objective

Practice **Key Management** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Key material
  ↓ platform keystore/keychain
  ↓ app asks platform to use key
  ↓ ciphertext/signature
  ↓ key never stored as plaintext app config
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 66 — Android IPC Security

### Objective

Practice **Android IPC Security** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 67 — Content URI Security

### Objective

Practice **Content URI Security** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 68 — FileProvider

### Objective

Practice **FileProvider** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
External app
  ↓ explicit / implicit intent
Exported component
  ↓
permission / input validation
  ↓
safe action

Export only components that require external access.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 69 — iOS Application Architecture

### Objective

Practice **iOS Application Architecture** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Static analysis
   ↓
Runtime observation
   ↓
Platform storage / IPC / network
   ↓
Backend/API behavior
   ↓
Minimal proof
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 70 — IPA

### Objective

Practice **IPA** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
IPA
  ↓ unzip
Payload/App.app/
  ├─ executable
  ├─ Info.plist
  ├─ frameworks
  └─ resources

Review:
URL schemes
entitlements
ATS
permissions
embedded endpoints
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## 6. Mini Project

# Mini Project — Mobile App Security Assessment

Use your own small Android test app or an intentionally vulnerable mobile training app. Perform static manifest/code/resource review, inspect local storage/logging, test deep links or exported components, observe network/API behavior through a controlled proxy, review token storage and TLS configuration, and use optional runtime instrumentation only on the lab app. Produce at least eight validated findings or control observations, remediate at least four, and retest.

### Required Deliverables

1. Authorization / lab scope
2. Architecture or trust-boundary diagram
3. Asset / component inventory
4. Test accounts / roles
5. Test plan
6. Evidence repository
7. Validated findings
8. Impact and attack-path explanation
9. Remediation plan
10. Detection / logging observations
11. Cleanup checklist
12. Retest evidence
13. Executive / triage-ready summary
14. Technical appendix

---

## 7. Recommended Resources

- OWASP Mobile Application Security project / MASVS / MASTG — https://mas.owasp.org/
- Android Security Documentation — https://developer.android.com/privacy-and-security/security
- Apple Platform Security — https://support.apple.com/guide/security/welcome/web
- JADX — https://github.com/skylot/jadx
- Frida Documentation — https://frida.re/docs/home/

---

## 8. Certification Relevance

Relevant to mobile application security, Android/iOS security assessment, MASVS/MASTG-oriented learning, application-security consulting, and API security.

Certification objectives and platform versions change over time. Verify current official exam and platform documentation when preparing for certification or production work.

---

## 9. Common Mistakes & Best Practices

### Common Mistakes

- Testing beyond written scope.
- Using real sensitive data when synthetic proof is sufficient.
- Trusting the mobile/web client as an authorization boundary.
- Treating scanner/decompiler/graph output as a confirmed exploit path.
- Running high-impact techniques before validating preconditions.
- Continuing after enough evidence has already been collected.
- Failing to record app/OS/domain versions and test-account context.
- Leaving test accounts, ACL changes, tokens, sessions, instrumentation, or lab artifacts behind.

### Best Practices

- Map trust boundaries before tools.
- Change one variable at a time.
- Prefer low-impact evidence before exploitation.
- Use synthetic identities and data.
- Use disposable lab snapshots.
- Preserve exact requests, commands, object IDs, and timestamps.
- Correlate tests with defensive telemetry.
- Fix the root cause.
- Retest with the original safe proof.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the key lesson from **Mobile Application Penetration Testing Purpose**?

**Short answer:** Mobile application penetration testing evaluates the mobile client, local device storage, platform integration, network behavior, and backend APIs within an authorized scope.

### Q2. What is the key lesson from **Mobile Testing Scope**?

**Short answer:** Scope should identify Android/iOS package identifiers, app versions, test accounts, backend APIs, devices, environments, and third-party services.

### Q3. What is the key lesson from **Mobile Rules of Engagement**?

**Short answer:** Define whether reverse engineering, dynamic instrumentation, rooted/jailbroken devices, traffic interception, and backend API testing are allowed.

### Q4. What is the key lesson from **Test Device**?

**Short answer:** Use a dedicated test device, emulator, or simulator rather than a personal device containing real sensitive data.

### Q5. What is the key lesson from **Synthetic Accounts**?

**Short answer:** Use test users and synthetic records so mobile workflows can be exercised safely.

### Q6. What is the key lesson from **Android Application Architecture**?

**Short answer:** Android apps contain manifests, DEX code, resources, native libraries, assets, and platform components.

### Q7. What is the key lesson from **APK**?

**Short answer:** An APK is an Android application package containing executable code, resources, manifest metadata, and signatures.

### Q8. What is the key lesson from **AAB Awareness**?

**Short answer:** Android App Bundles are publishing artifacts from which device-specific APKs may be generated.

### Q9. What is the key lesson from **AndroidManifest.xml**?

**Short answer:** The manifest declares package identity, components, permissions, intent filters, SDK requirements, and security-relevant settings.

### Q10. What is the key lesson from **Android Permission Model**?

**Short answer:** Applications request permissions for protected platform capabilities and should request only what they need.

### Q11. What is the key lesson from **Dangerous Permission**?

**Short answer:** Some Android permissions require runtime user approval because they expose sensitive capabilities.

### Q12. What is the key lesson from **Exported Component**?

**Short answer:** Activities, services, receivers, or providers exposed to other apps require deliberate permissions and input validation.

### Q13. What is the key lesson from **Activity**?

**Short answer:** An Activity represents a user-facing Android component and may be launchable through intents.

### Q14. What is the key lesson from **Service**?

**Short answer:** Android Services perform background or bound work and should not expose privileged operations unnecessarily.

### Q15. What is the key lesson from **Broadcast Receiver**?

**Short answer:** Receivers process broadcast intents and need appropriate export/permission controls.

### Q16. What is the key lesson from **Content Provider**?

**Short answer:** Content providers expose structured data and need correct URI permissions and authorization.

### Q17. What is the key lesson from **Intent**?

**Short answer:** Intents carry actions, data, categories, extras, and component targets between Android components.

### Q18. What is the key lesson from **Intent Filter**?

**Short answer:** Intent filters define which implicit intents a component may receive and can unintentionally expose functionality.

### Q19. What is the key lesson from **PendingIntent Awareness**?

**Short answer:** PendingIntent grants another process the ability to perform an app-defined future action and must be scoped/immutable appropriately.

### Q20. What is the key lesson from **Android Deep Link**?

**Short answer:** Deep links route external URIs into application components and require strict destination and parameter validation.

### Q21. What is the key lesson from **Android App Link**?

**Short answer:** Verified app links bind HTTPS domains to the intended Android application and reduce ambiguous handler selection.

### Q22. What is the key lesson from **Custom URL Scheme**?

**Short answer:** Custom schemes can be claimed by multiple apps and should not carry sensitive secrets without additional verification.

### Q23. What is the key lesson from **Android WebView**?

**Short answer:** WebViews embed web content and create a browser-to-native trust boundary.

### Q24. What is the key lesson from **WebView JavaScript**?

**Short answer:** Enable JavaScript only when needed and avoid loading untrusted content with powerful native capabilities.

### Q25. What is the key lesson from **WebView Native Bridge**?

**Short answer:** JavaScript interfaces exposed to WebView content can become high-impact attack surfaces.

### Q26. What is the key lesson from **WebView File Access**?

**Short answer:** File/content URL access should be minimized and configured according to application need.

### Q27. What is the key lesson from **WebView Mixed Content**?

**Short answer:** Loading HTTP resources inside HTTPS content weakens transport security.

### Q28. What is the key lesson from **Android Network Security Config**?

**Short answer:** Android network security configuration can define cleartext policy, custom trust anchors, and certificate pinning behavior.

### Q29. What is the key lesson from **Cleartext Traffic**?

**Short answer:** Sensitive application traffic should not use plaintext HTTP across untrusted networks.

### Q30. What is the key lesson from **TLS Validation**?

**Short answer:** Mobile clients should validate certificate chains and hostnames using supported platform trust mechanisms.

### Q31. What is the key lesson from **Certificate Pinning**?

**Short answer:** Pinning can reduce some interception risks but adds certificate lifecycle and failure-management complexity.

### Q32. What is the key lesson from **Android Keystore**?

**Short answer:** Android Keystore can protect cryptographic keys and may use hardware-backed storage on supported devices.

### Q33. What is the key lesson from **SharedPreferences**?

**Short answer:** Preferences are convenient local storage but should not contain plaintext credentials or high-value secrets.

### Q34. What is the key lesson from **SQLite Storage**?

**Short answer:** Local databases can contain cached sensitive data and need minimization, access protection, and safe backup behavior.

### Q35. What is the key lesson from **File Storage**?

**Short answer:** Internal, external, cache, and shared storage have different exposure and lifecycle characteristics.

### Q36. What is the key lesson from **External Storage Risk**?

**Short answer:** Externally accessible storage may be visible to other apps/users depending on platform/version and should not contain secrets.

### Q37. What is the key lesson from **Backup Configuration**?

**Short answer:** App backup settings can unintentionally copy sensitive local data to backups.

### Q38. What is the key lesson from **Clipboard Risk**?

**Short answer:** Sensitive tokens or credentials copied to the clipboard may be visible to other apps or users.

### Q39. What is the key lesson from **Screenshot Risk**?

**Short answer:** Sensitive screens may require platform protections against screenshots or recent-app previews when justified.

### Q40. What is the key lesson from **Logcat**?

**Short answer:** Application logs should not expose passwords, tokens, session identifiers, personal information, or cryptographic secrets.

### Q41. What is the key lesson from **Debuggable Flag**?

**Short answer:** Production Android applications should not normally be debuggable.

### Q42. What is the key lesson from **Test-Only Components**?

**Short answer:** Development activities, test endpoints, debug menus, and mock services should not remain exposed in production builds.

### Q43. What is the key lesson from **Hardcoded Secret**?

**Short answer:** API keys, passwords, symmetric keys, and private credentials embedded in a mobile binary should be assumed extractable.

### Q44. What is the key lesson from **Obfuscation**?

**Short answer:** Code obfuscation raises reverse-engineering cost but is not a secret-storage mechanism.

### Q45. What is the key lesson from **JADX**?

**Short answer:** JADX decompiles Android DEX bytecode into Java-like source for static analysis.

### Q46. What is the key lesson from **apktool Awareness**?

**Short answer:** apktool decodes resources and smali-level structure and can help inspect manifests and resources.

### Q47. What is the key lesson from **Smali Awareness**?

**Short answer:** Smali is an assembly-like representation of Dalvik bytecode useful for understanding low-level Android logic.

### Q48. What is the key lesson from **Native Library Awareness**?

**Short answer:** JNI/native libraries expand the attack surface and may require native-code analysis for sensitive functions.

### Q49. What is the key lesson from **ADB**?

**Short answer:** Android Debug Bridge provides authorized device/emulator interaction for installation, shell access, logs, and testing.

### Q50. What is the key lesson from **ADB Device Enumeration**?

**Short answer:** Verify that only intended test devices are connected before running commands.

### Q51. What is the key lesson from **ADB Shell**?

**Short answer:** The device shell helps inspect platform state, files available to the test context, and package information.

### Q52. What is the key lesson from **Application Data Directory**?

**Short answer:** App-private data should not be accessible to unrelated unprivileged apps under normal platform security.

### Q53. What is the key lesson from **Rooted Device Awareness**?

**Short answer:** Rooting changes device security assumptions and is useful only for dedicated test devices when authorized.

### Q54. What is the key lesson from **Emulator**?

**Short answer:** Emulators provide reproducible snapshots and instrumentation for Android security testing.

### Q55. What is the key lesson from **Frida Awareness**?

**Short answer:** Frida provides dynamic instrumentation for observing or changing runtime behavior in owned/authorized applications.

### Q56. What is the key lesson from **Dynamic Instrumentation Boundary**?

**Short answer:** Use instrumentation to understand application logic, not to bypass controls on third-party apps without permission.

### Q57. What is the key lesson from **Runtime Method Observation**?

**Short answer:** Observing method inputs/outputs can confirm whether secrets, keys, or authorization decisions exist only on the client.

### Q58. What is the key lesson from **Client-Side Trust**?

**Short answer:** A hostile user controls their own client; security-critical decisions must be enforced on the server or protected platform boundary.

### Q59. What is the key lesson from **Root Detection Awareness**?

**Short answer:** Root detection can signal risk but can often be bypassed and should not be the sole control protecting backend authorization.

### Q60. What is the key lesson from **Anti-Tamper Awareness**?

**Short answer:** Integrity checks can raise attacker cost but do not replace secure backend design.

### Q61. What is the key lesson from **Biometric Authentication**?

**Short answer:** Biometrics should unlock a protected local credential or authorize a platform-mediated action rather than serve as a standalone backend identity.

### Q62. What is the key lesson from **Biometric Bypass Risk**?

**Short answer:** If the app only hides a screen after biometric success while a token remains accessible, the control may be cosmetic.

### Q63. What is the key lesson from **Android Cryptography**?

**Short answer:** Use platform cryptographic APIs and strong random generation rather than custom algorithms.

### Q64. What is the key lesson from **Random Number Generation**?

**Short answer:** Security tokens and keys require cryptographically secure random sources.

### Q65. What is the key lesson from **Key Management**?

**Short answer:** Long-lived keys should remain in platform-protected storage or backend systems rather than plaintext app files.

### Q66. What is the key lesson from **Android IPC Security**?

**Short answer:** Binder/IPC components should validate callers, permissions, and input.

### Q67. What is the key lesson from **Content URI Security**?

**Short answer:** Content URIs and temporary grants should expose only intended resources for limited duration.

### Q68. What is the key lesson from **FileProvider**?

**Short answer:** FileProvider can share files through controlled content URIs instead of exposing raw filesystem paths.

### Q69. What is the key lesson from **iOS Application Architecture**?

**Short answer:** iOS apps include an executable, Info.

### Q70. What is the key lesson from **IPA**?

**Short answer:** An IPA is an iOS application archive containing the app bundle and resources.

### Q71. What is the key lesson from **Info.plist**?

**Short answer:** Info.

### Q72. What is the key lesson from **Entitlements**?

**Short answer:** Entitlements grant platform capabilities such as keychain groups, associated domains, push, or app groups.

### Q73. What is the key lesson from **ATS**?

**Short answer:** App Transport Security encourages secure TLS networking and should not be broadly disabled.

### Q74. What is the key lesson from **iOS URL Scheme**?

**Short answer:** Custom URL schemes can expose routing logic and require careful validation.

### Q75. What is the key lesson from **Universal Link**?

**Short answer:** Universal Links bind approved HTTPS domains to an iOS application.

### Q76. What is the key lesson from **iOS Keychain**?

**Short answer:** The Keychain stores credentials and cryptographic material with configurable accessibility classes.

### Q77. What is the key lesson from **NSUserDefaults Awareness**?

**Short answer:** NSUserDefaults is not appropriate for high-value plaintext secrets.

### Q78. What is the key lesson from **iOS File Protection**?

**Short answer:** Data-protection classes control when encrypted files become accessible relative to device unlock state.

### Q79. What is the key lesson from **App Group Storage**?

**Short answer:** Shared app-group containers increase the number of processes that may access data and require careful entitlement governance.

### Q80. What is the key lesson from **Pasteboard Risk**?

**Short answer:** Sensitive clipboard data can leak between apps or remain longer than intended.

### Q81. What is the key lesson from **Jailbreak Awareness**?

**Short answer:** Jailbroken test devices can expose otherwise protected files and enable instrumentation, changing normal platform assumptions.

### Q82. What is the key lesson from **iOS Simulator**?

**Short answer:** The simulator provides convenient testing but does not reproduce every hardware security property of a physical device.

### Q83. What is the key lesson from **Static iOS Analysis**?

**Short answer:** Inspect Info.

### Q84. What is the key lesson from **Dynamic iOS Analysis Awareness**?

**Short answer:** Authorized dynamic instrumentation can observe runtime behavior on dedicated test devices.

### Q85. What is the key lesson from **Mobile Network Interception**?

**Short answer:** Use a controlled proxy on your own device/app to inspect application traffic when policy permits.

### Q86. What is the key lesson from **Proxy CA Trust**?

**Short answer:** Installing a lab proxy CA changes the device trust environment and should be reverted after testing.

### Q87. What is the key lesson from **Certificate Pinning Test**?

**Short answer:** Determine whether pinning is implemented and whether its lifecycle/failure behavior matches the threat model.

### Q88. What is the key lesson from **Backend API Scope**?

**Short answer:** Mobile application testing commonly requires backend API testing, which must be explicitly included in scope.

### Q89. What is the key lesson from **Mobile API Authentication**?

**Short answer:** Review token issuance, renewal, storage, device binding, logout, and MFA.

### Q90. What is the key lesson from **Mobile API Authorization**?

**Short answer:** Server-side object and function authorization must not rely on the mobile UI.

### Q91. What is the key lesson from **Device Identifier Trust**?

**Short answer:** Device identifiers can change or be spoofed and should not be treated as strong identity by themselves.

### Q92. What is the key lesson from **Push Notification Security**?

**Short answer:** Notifications can expose sensitive content on lock screens and device tokens need protected lifecycle.

### Q93. What is the key lesson from **Push Token**?

**Short answer:** Push tokens identify app/device delivery channels but should not act as standalone user authentication.

### Q94. What is the key lesson from **In-App Browser / Custom Tabs Awareness**?

**Short answer:** Authentication flows using browser-based components should preserve origin, redirect, state, and PKCE protections.

### Q95. What is the key lesson from **OAuth in Mobile Apps**?

**Short answer:** Public mobile clients should use authorization code with PKCE rather than embedded client secrets.

### Q96. What is the key lesson from **Redirect URI Handling**?

**Short answer:** Mobile OAuth redirects must be tightly bound to the intended app through verified links or robust scheme controls.

### Q97. What is the key lesson from **SSO Token Storage**?

**Short answer:** SSO tokens are high-value bearer credentials and need secure local handling and revocation.

### Q98. What is the key lesson from **Offline Mode**?

**Short answer:** Cached authorization and data in offline mode require expiry and conflict-handling rules.

### Q99. What is the key lesson from **Local Data Minimization**?

**Short answer:** Store only the data required for offline or performance needs and clear it at appropriate lifecycle points.

### Q100. What is the key lesson from **Logout Data Cleanup**?

**Short answer:** Logout should remove or invalidate local secrets, cached sensitive data, and server-side sessions as appropriate.

### Q101. What is the key lesson from **Multi-Account Switching**?

**Short answer:** Switching accounts should not leak cached data, files, notifications, or WebView sessions between users.

### Q102. What is the key lesson from **Screen Overlay Awareness**?

**Short answer:** Sensitive input flows may need platform protections against overlay or tapjacking risks depending on threat model.

### Q103. What is the key lesson from **Keyboard / IME Risk Awareness**?

**Short answer:** Highly sensitive input can interact with third-party keyboards; application design should minimize unnecessary secret entry.

### Q104. What is the key lesson from **Accessibility Service Risk Awareness**?

**Short answer:** Accessibility services have powerful UI visibility and control; apps should not rely solely on client UI secrecy.

### Q105. What is the key lesson from **Mobile Logging to SIEM**?

**Short answer:** Important authentication, device-registration, token, and high-risk actions should be visible through backend telemetry.

### Q106. What is the key lesson from **Mobile Finding Evidence**?

**Short answer:** Record app version, device/emulator, OS version, component, test account, and exact action.

### Q107. What is the key lesson from **Mobile Finding Remediation**?

**Short answer:** Fix root cause in platform configuration, app code, local storage, or backend authorization as appropriate.

### Q108. What is the key lesson from **Mobile Retest**?

**Short answer:** Repeat the same static/dynamic/API validation after the fix.

### Q109. What is the key lesson from **Mobile Application Penetration Testing Final Mental Model**?

**Short answer:** Treat the mobile client as user-controlled, validate platform storage/IPC/network behavior, and enforce real authorization and data protection on trusted backend/platform boundaries.

---

## Completion Checklist

- [ ] I completed the core topics.
- [ ] I completed at least 35 labs.
- [ ] I completed the mini project.
- [ ] I can explain the trust boundary before using a tool.
- [ ] I can use synthetic test identities safely.
- [ ] I can demonstrate impact with minimal evidence.
- [ ] I can document remediation and retest.
- [ ] I cleaned up the lab.
