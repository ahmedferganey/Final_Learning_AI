# Feature Specification: Mobile Scaffold

**Feature Branch**: `004-mobile-scaffold`
**Created**: 2026-04-09
**Status**: Draft
**Phase**: 0 — Foundation
**Plan Reference**: Plan.md → Spec 0.4

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Developer Runs the App on Both Platforms Without Errors (Priority: P1)

A developer runs `flutter run` targeting an Android emulator and then an iOS simulator.
In both cases, the app launches to a placeholder Home screen without runtime crashes,
Flutter framework errors, or Dart analysis warnings. The app displays a simple screen
confirming it is running.

**Why this priority**: Confirming the app runs on both target platforms before any
feature code exists is essential. Platform-specific configuration issues (build tools,
SDK versions, plugin compatibility) are far easier to resolve on a clean scaffold than
after multiple features are implemented.

**Independent Test**: Can be fully tested by running `flutter run -d android` and
`flutter run -d ios`. Delivers value by confirming the full Flutter + Riverpod + Dio +
Hive dependency chain compiles and runs on both target platforms.

**Acceptance Scenarios**:

1. **Given** Flutter SDK is installed and an Android emulator is running, **When**
   `flutter run -d <android-device-id>` is executed in `mobile/`, **Then** the app
   installs and the Home placeholder screen is displayed with no red error screen.

2. **Given** Flutter SDK is installed and an iOS simulator is running, **When**
   `flutter run -d <ios-device-id>` is executed in `mobile/`, **Then** the app
   installs and the Home placeholder screen is displayed with no red error screen.

3. **Given** the app is running on either platform, **When** the developer opens the
   Flutter DevTools console, **Then** zero error or warning log entries are present
   related to framework or plugin initialisation.

4. **Given** the API base URL is not configured in the environment/config file,
   **When** the app launches, **Then** it displays a configuration error screen
   (not a crash/red screen) and does not attempt to make any network requests.

---

### User Story 2 — Flutter Analyse Reports Zero Issues (Priority: P2)

A developer runs `flutter analyze` from the `mobile/` directory. The analysis completes
and reports zero errors, zero warnings, and zero hints. This confirms the Dart code
follows the project's lint rules and the Riverpod, Dio, and Hive dependencies are
correctly integrated at the type level.

**Why this priority**: `flutter analyze` is the mobile equivalent of `mypy` and `ruff`.
Establishing zero-issue analysis from the scaffold means every future PR can enforce the
same standard with no baseline debt to work around.

**Independent Test**: Can be fully tested by running `flutter analyze`. A zero-issue
result delivers value by confirming the dependency graph, type safety, and lint rules
are correct before any feature code exists.

**Acceptance Scenarios**:

1. **Given** all Flutter dependencies are fetched via `flutter pub get`, **When**
   `flutter analyze` is run, **Then** it exits with code 0 and reports
   "No issues found!" (or an equivalent zero-issue message).

2. **Given** a Dart analysis issue is deliberately introduced (e.g., unused import),
   **When** `flutter analyze` is run, **Then** the issue is reported with file name,
   line number, and rule name — confirming the analyser is active.

3. **Given** `flutter test` is run with zero test files present, **When** the command
   completes, **Then** it exits with code 0 (empty test suite is not a failure).

---

### User Story 3 — Feature Directory Structure Matches Plan.md Contract (Priority: P3)

A developer starting work on Spec 4.2 (mobile active workout flow) navigates to the
`mobile/lib/features/workout/` directory and finds it already exists with the correct
subdirectory structure. They do not need to create or debate the directory layout — it
is already established and matches the architecture defined in Plan.md.

**Why this priority**: Directory structure established after feature code exists leads to
disagreement, inconsistency, and refactoring cost. Establishing it on the scaffold lets
every Phase 4 spec reference canonical paths from the start.

**Independent Test**: Can be tested by verifying the presence of the required directories
using `find mobile/lib -type d`. All feature directories must exist even if they contain
only a `.gitkeep`.

**Acceptance Scenarios**:

1. **Given** the repository is cloned, **When** the `mobile/lib/` directory is listed
   recursively, **Then** the following feature directories exist:
   `core/`, `core/api/`, `core/storage/`, `core/sync/`,
   `features/auth/`, `features/workout/`, `features/history/`, `features/readiness/`,
   `shared/`.

2. **Given** the Hive local storage is initialised in `main.dart`, **When** the app
   starts, **Then** Hive initialisation completes without errors and a Hive box can be
   opened by any feature that needs it.

3. **Given** a Riverpod `ProviderScope` wraps the root widget, **When** any widget in
   the tree calls `ref.watch()` or `ref.read()`, **Then** no "ProviderScope not found"
   error is thrown.

---

### Edge Cases

- **Missing API base URL in config:** The Dio client MUST NOT default to an empty string or
  `localhost` silently. If the API base URL is not provided, the app MUST show a visible
  error screen and log a clear error to the console. It MUST NOT crash with an unhandled
  exception.
- **Hive initialisation order:** Hive MUST be initialised before `runApp()` is called.
  Any attempt to open a Hive box before initialisation causes an unhandled exception.
  `main.dart` enforces this order explicitly.
- **Riverpod ProviderScope placement:** `ProviderScope` MUST wrap the entire app at the
  root level in `main.dart`. Placing it inside a widget subtree causes provider lookup
  failures in sibling subtrees.
- **Flutter null safety:** All Dart code MUST use sound null safety. Any package that
  does not support null safety is prohibited. `pubspec.yaml` MUST declare
  `sdk: ">=3.0.0 <4.0.0"`.
- **iOS minimum deployment target:** `ios/Podfile` MUST specify a minimum iOS deployment
  target of 14.0 or higher. Riverpod and Dio both require a minimum iOS version; failing
  to set this causes build errors on first `flutter build ios`.
- **Android minimum SDK:** `android/app/build.gradle` MUST set `minSdkVersion 21` or
  higher. Hive requires a minimum Android SDK version for its native components.
- **`flutter pub get` in CI:** `pubspec.lock` MUST be committed to the repository to ensure
  reproducible dependency resolution. Running without a lock file in CI can result in
  different dependency versions across environments.
- **Platform-specific config files:** `GoogleService-Info.plist` (iOS) and
  `google-services.json` (Android) MUST NOT be committed — these are Phase 8 concerns
  (notifications). `.gitignore` MUST exclude them.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The Flutter project MUST use null safety (`sdk: ">=3.0.0 <4.0.0"` in
  `pubspec.yaml`). No legacy non-null-safe packages.
- **FR-002**: Riverpod MUST be the state management solution. `flutter_riverpod` MUST be
  declared in `pubspec.yaml` and `ProviderScope` MUST wrap the root widget in `main.dart`.
- **FR-003**: Dio MUST be the HTTP client. A `Dio` instance MUST be configured in
  `lib/core/api/` with the base URL read from an app configuration source (not hardcoded).
- **FR-004**: Hive MUST be the local storage solution. `hive_flutter` MUST be declared
  in `pubspec.yaml` and `Hive.initFlutter()` MUST be called before `runApp()` in
  `main.dart`.
- **FR-005**: The `lib/` directory MUST follow the structure defined in Plan.md:
  `core/api/`, `core/storage/`, `core/sync/`, `features/auth/`, `features/workout/`,
  `features/history/`, `features/readiness/`, `shared/`.
- **FR-006**: Two placeholder screens MUST exist: `LoginScreen` and `HomeScreen`. Both
  render static content. `LoginScreen` is the initial route; `HomeScreen` is reachable
  from `LoginScreen` (e.g., a placeholder "Continue" button — no real auth logic).
- **FR-007**: If the API base URL is missing from configuration at startup, the app MUST
  display a configuration error widget instead of crashing. The error MUST name the
  missing configuration key.
- **FR-008**: `flutter analyze` MUST exit with code 0 and report zero issues against the
  scaffold codebase. The `analysis_options.yaml` MUST enable recommended lint rules.
- **FR-009**: `flutter test` MUST run and exit with code 0 when zero test files are present.
- **FR-010**: `pubspec.lock` MUST be committed to the repository.
- **FR-011**: This spec MUST NOT implement authentication logic, real API calls, offline
  storage of user data, or any training domain models. All screens are placeholders only.
- **FR-012**: Platform-specific push notification configuration files (`GoogleService-Info.plist`,
  `google-services.json`) MUST NOT be committed in this spec.

### Key Entities

- **App Configuration**: A Dart class (or `const` map) that provides configuration values —
  primarily `apiBaseUrl` — loaded from a compile-time constant or environment source.
  Injected into the Dio client at startup.
- **Dio Client Provider**: A Riverpod `Provider<Dio>` that constructs and exposes the
  configured `Dio` instance. Consumed by all feature-level repository classes in future specs.
- **Hive Storage**: Initialised in `main.dart` via `Hive.initFlutter()`. Individual Hive
  boxes are opened by their owning feature module, not centrally.
- **Feature Module Structure**: Each `features/<name>/` directory will follow the pattern:
  `data/` (repositories, data sources), `domain/` (models, if any), `presentation/`
  (screens, widgets, providers). This structure is established but empty in Phase 0.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `flutter run` succeeds and the Home placeholder screen appears on both
  Android and iOS targets with zero crash logs in the console.
- **SC-002**: `flutter analyze` exits with code 0 and zero reported issues against the
  scaffold codebase.
- **SC-003**: `flutter test` exits with code 0 with zero test files present.
- **SC-004**: All required feature directories are present after `git clone` (verified by
  directory listing).
- **SC-005**: The app launches with a missing API base URL and shows the configuration
  error screen rather than a red screen crash.
- **SC-006**: `pubspec.lock` is present and committed — `flutter pub get` in a fresh
  environment uses the locked versions without prompting for resolution.

---

## Assumptions

- Flutter 3.x (stable channel) is the mandated SDK. The exact version is pinned in
  `.fvm/fvm_config.json` (Flutter Version Management) or documented in `mobile/README.md`.
- The app targets Android (API 21+) and iOS (14.0+).
- Riverpod v2 is used (code generation is optional at this stage — no `@riverpod` annotation
  generator required for the scaffold).
- Hive is used for local storage. Drift (SQLite ORM) is the alternative if relational queries
  are needed in offline sync — this decision is deferred to Spec 4.5 (mobile offline cache).
- Firebase-dependent packages (FCM, Analytics) are NOT added in this spec — they are
  introduced in Phase 8 (notifications).
- The `mobile/` directory has its own `README.md` with setup instructions for Android
  Studio / Xcode and emulator/simulator setup.
- No flavour configuration (dev/staging/prod) is implemented in this spec — a single
  configuration source is sufficient for Phase 0.
