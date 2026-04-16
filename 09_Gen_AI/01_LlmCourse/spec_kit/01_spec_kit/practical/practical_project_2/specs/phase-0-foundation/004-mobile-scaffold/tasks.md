# Tasks: Mobile Scaffold

**Input**: `specs/phase-0-foundation/004-mobile-scaffold/`
**Spec**: [spec.md](spec.md)

> **For LLM agents**: All files live under `mobile/`. No authentication logic, real API calls,
> offline storage of user data, or training domain models. All screens are placeholder widgets.
> Null safety is mandatory throughout. Key content, platform-specific config values, and
> pubspec entries are specified inline. Commit after each phase.

---

## Phase 1: Setup — pubspec, Analysis Config, and Directory Skeleton

- [ ] T001 Create `mobile/pubspec.yaml` with all required dependencies and correct SDK constraint (FR-001, FR-002, FR-003, FR-004, Edge Case):

  ```yaml
  name: gymos_mobile
  description: GymOS mobile app — adaptive training intelligence platform.
  publish_to: "none"

  version: 0.1.0+1

  environment:
    sdk: ">=3.0.0 <4.0.0"

  dependencies:
    flutter:
      sdk: flutter
    flutter_riverpod: ^2.5.1
    dio: ^5.4.3
    hive_flutter: ^1.1.0
    hive: ^2.2.3

  dev_dependencies:
    flutter_test:
      sdk: flutter
    flutter_lints: ^4.0.0

  flutter:
    uses-material-design: true
  ```

  After creating the file, run `flutter pub get` from `mobile/` to fetch and lock dependencies. Commit the generated `pubspec.lock` (FR-010, Edge Case).

- [ ] T002 Create `mobile/analysis_options.yaml` with recommended lint rules enabled (FR-008):

  ```yaml
  include: package:flutter_lints/flutter.yaml

  analyzer:
    errors:
      unused_import: error
      unused_local_variable: error
    strong-mode:
      implicit-casts: false
      implicit-dynamic: false

  linter:
    rules:
      - always_declare_return_types
      - avoid_print
      - prefer_const_constructors
      - prefer_const_declarations
      - prefer_final_fields
      - prefer_single_quotes
      - sort_pub_dependencies
      - use_super_parameters
  ```

- [ ] T003 Create the full `mobile/lib/` directory skeleton with `.gitkeep` files (FR-005):
  ```
  mkdir -p mobile/lib/core/api
  mkdir -p mobile/lib/core/storage
  mkdir -p mobile/lib/core/sync
  mkdir -p mobile/lib/features/auth/presentation/screens
  mkdir -p mobile/lib/features/workout/data
  mkdir -p mobile/lib/features/workout/domain
  mkdir -p mobile/lib/features/workout/presentation
  mkdir -p mobile/lib/features/history/data
  mkdir -p mobile/lib/features/history/domain
  mkdir -p mobile/lib/features/history/presentation
  mkdir -p mobile/lib/features/readiness/data
  mkdir -p mobile/lib/features/readiness/domain
  mkdir -p mobile/lib/features/readiness/presentation
  mkdir -p mobile/lib/shared
  touch mobile/lib/core/storage/.gitkeep
  touch mobile/lib/core/sync/.gitkeep
  touch mobile/lib/features/workout/data/.gitkeep
  touch mobile/lib/features/workout/domain/.gitkeep
  touch mobile/lib/features/workout/presentation/.gitkeep
  touch mobile/lib/features/history/data/.gitkeep
  touch mobile/lib/features/history/domain/.gitkeep
  touch mobile/lib/features/history/presentation/.gitkeep
  touch mobile/lib/features/readiness/data/.gitkeep
  touch mobile/lib/features/readiness/domain/.gitkeep
  touch mobile/lib/features/readiness/presentation/.gitkeep
  touch mobile/lib/shared/.gitkeep
  ```

**Checkpoint — Phase 1**: `flutter pub get` exits 0. `flutter analyze` exits 0 (no Dart files yet). Directory tree matches Plan.md spec.

---

## Phase 2: Foundational — App Config and Dio Client

**Purpose**: App configuration and the Dio client must exist before `main.dart` can reference them.

- [ ] T004 Create `mobile/lib/core/api/app_config.dart` — provides the API base URL from a compile-time constant (FR-003, FR-007, Edge Case):

  ```dart
  class AppConfig {
    const AppConfig._();

    /// API base URL — set via `--dart-define=API_BASE_URL=...` at build time.
    /// Example: flutter run --dart-define=API_BASE_URL=http://localhost:8000
    static const String apiBaseUrl = String.fromEnvironment(
      'API_BASE_URL',
      defaultValue: '',
    );

    /// Returns true if the app is correctly configured.
    static bool get isConfigured => apiBaseUrl.isNotEmpty;
  }
  ```

  > **Note**: `defaultValue: ''` is intentional — an empty string triggers the error screen
  > in `main.dart` rather than a crash. Never set a default localhost URL here.

- [ ] T005 Create `mobile/lib/core/api/dio_client.dart` — a Riverpod provider exposing a configured `Dio` instance (FR-003):

  ```dart
  import 'package:dio/dio.dart';
  import 'package:flutter_riverpod/flutter_riverpod.dart';

  import 'app_config.dart';

  final dioProvider = Provider<Dio>((ref) {
    final dio = Dio(
      BaseOptions(
        baseUrl: AppConfig.apiBaseUrl,
        connectTimeout: const Duration(seconds: 10),
        receiveTimeout: const Duration(seconds: 30),
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      ),
    );
    return dio;
  });
  ```

**Checkpoint — Phase 2**: `flutter analyze` exits 0 against both new files.

---

## Phase 3: User Story 1 — App Runs on Both Platforms Without Errors (Priority: P1) 🎯 MVP

**Goal**: `flutter run` on Android and iOS shows the Home placeholder screen. No red error screen, no crash.

**Independent test** (SC-001, SC-005): `flutter run -d <device>` → placeholder screen appears; if API_BASE_URL is missing, config error widget shown (not a red screen).

- [ ] T006 [P] [US1] Create `mobile/lib/features/auth/presentation/screens/login_screen.dart` — placeholder login screen (FR-006):

  ```dart
  import 'package:flutter/material.dart';

  class LoginScreen extends StatelessWidget {
    const LoginScreen({super.key});

    @override
    Widget build(BuildContext context) {
      return const Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'GymOS',
                style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 8),
              Text('Login — coming in Phase 1'),
            ],
          ),
        ),
      );
    }
  }
  ```

- [ ] T007 [P] [US1] Create `mobile/lib/features/auth/presentation/screens/home_screen.dart` — placeholder home screen (FR-006):

  ```dart
  import 'package:flutter/material.dart';

  class HomeScreen extends StatelessWidget {
    const HomeScreen({super.key});

    @override
    Widget build(BuildContext context) {
      return Scaffold(
        appBar: AppBar(title: const Text('GymOS')),
        body: const Center(
          child: Text('Home — Phase 4 workout features coming soon'),
        ),
      );
    }
  }
  ```

- [ ] T008 [US1] Create `mobile/lib/main.dart` — entry point with Hive init, ProviderScope, MaterialApp, and config guard (FR-002, FR-004, FR-007, Edge Cases):

  ```dart
  import 'package:flutter/material.dart';
  import 'package:flutter_riverpod/flutter_riverpod.dart';
  import 'package:hive_flutter/hive_flutter.dart';

  import 'core/api/app_config.dart';
  import 'features/auth/presentation/screens/home_screen.dart';
  import 'features/auth/presentation/screens/login_screen.dart';

  Future<void> main() async {
    WidgetsFlutterBinding.ensureInitialized();

    // Hive MUST be initialised before runApp (Edge Case)
    await Hive.initFlutter();

    runApp(
      // ProviderScope MUST wrap the entire app at root level (Edge Case)
      const ProviderScope(
        child: GymOSApp(),
      ),
    );
  }

  class GymOSApp extends StatelessWidget {
    const GymOSApp({super.key});

    @override
    Widget build(BuildContext context) {
      // Guard: show config error screen if API URL is not provided (FR-007)
      if (!AppConfig.isConfigured) {
        return const MaterialApp(
          home: _ConfigErrorScreen(),
        );
      }

      return MaterialApp(
        title: 'GymOS',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
          useMaterial3: true,
        ),
        initialRoute: '/login',
        routes: {
          '/login': (_) => const LoginScreen(),
          '/home': (_) => const HomeScreen(),
        },
      );
    }
  }

  class _ConfigErrorScreen extends StatelessWidget {
    const _ConfigErrorScreen();

    @override
    Widget build(BuildContext context) {
      return const Scaffold(
        body: Center(
          child: Padding(
            padding: EdgeInsets.all(24),
            child: Text(
              'Configuration error: API_BASE_URL is not set.\n\n'
              'Run with: flutter run --dart-define=API_BASE_URL=http://localhost:8000',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 16),
            ),
          ),
        ),
      );
    }
  }
  ```

- [ ] T009 [US1] Set iOS minimum deployment target to 14.0 in `mobile/ios/Podfile` (Edge Case). Open the file and set/update:
  ```ruby
  platform :ios, '14.0'
  ```
  This line must be uncommented and set to `14.0` or higher. If the file does not exist yet, run `flutter build ios --no-codesign` to generate platform files first.

- [ ] T010 [US1] Set Android minimum SDK version in `mobile/android/app/build.gradle` (Edge Case). Find the `defaultConfig` block and set:
  ```groovy
  defaultConfig {
      minSdkVersion 21
      // ... (keep other existing values)
  }
  ```
  The `minSdkVersion` must be 21 or higher.

**Checkpoint — US1**: `flutter run -d <device>` shows Home screen. `flutter run --dart-define=API_BASE_URL=` (empty) shows config error widget, no crash.

---

## Phase 4: User Story 2 — Flutter Analyze Reports Zero Issues (Priority: P2)

**Goal**: `flutter analyze` exits 0, "No issues found!" (or equivalent).

**Independent test** (SC-002): `flutter analyze` exits 0 from `mobile/`.

- [ ] T011 [US2] Run `flutter analyze` from `mobile/` and fix all reported issues (FR-008). Common scaffold issues to check:
  - Unused imports → remove them
  - Missing `const` on const-eligible constructors → add `const`
  - `print()` calls → replace with a structured log or remove
  - `prefer_single_quotes` violations → change to single quotes
  
  Re-run until `flutter analyze` exits 0 with zero issues.

**Checkpoint — US2**: `flutter analyze` exits 0. Introduce a deliberate unused import, run `flutter analyze` — it reports the violation. Remove the import, re-run — back to 0.

---

## Phase 5: User Story 3 — Feature Directory Structure Matches Plan.md (Priority: P3)

**Goal**: All feature directories from Plan.md exist after `git clone`. Hive initializes. ProviderScope is at root.

**Independent test** (SC-004): `find mobile/lib -type d` output matches expected tree.

- [ ] T012 [US3] Verify the directory structure created in T003 is complete. Run:
  ```
  find mobile/lib -type d | sort
  ```
  Expected directories (must all appear):
  ```
  mobile/lib/core
  mobile/lib/core/api
  mobile/lib/core/storage
  mobile/lib/core/sync
  mobile/lib/features
  mobile/lib/features/auth
  mobile/lib/features/auth/presentation
  mobile/lib/features/auth/presentation/screens
  mobile/lib/features/history
  mobile/lib/features/history/data
  mobile/lib/features/history/domain
  mobile/lib/features/history/presentation
  mobile/lib/features/readiness
  mobile/lib/features/readiness/data
  mobile/lib/features/readiness/domain
  mobile/lib/features/readiness/presentation
  mobile/lib/features/workout
  mobile/lib/features/workout/data
  mobile/lib/features/workout/domain
  mobile/lib/features/workout/presentation
  mobile/lib/shared
  ```
  If any are missing, create them with `.gitkeep`.

**Checkpoint — US3**: All directories present. `ProviderScope` is the root widget in `main.dart`. Hive is initialized before `runApp`.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T013 [P] Create `mobile/README.md` with: (1) **Prerequisites** — Flutter SDK stable channel, Android Studio / Xcode; (2) **Setup** — `flutter pub get`; (3) **Run** — `flutter run --dart-define=API_BASE_URL=http://localhost:8000`; (4) **Analyze** — `flutter analyze`; (5) **Test** — `flutter test`; (6) **iOS minimum** — iOS 14.0; (7) **Android minimum** — API 21; (8) **pubspec.lock** — must be committed, do not delete it.

- [ ] T014 Run `flutter test` from `mobile/` — must exit 0 with zero test files present (FR-009, SC-003).

- [ ] T015 Confirm `pubspec.lock` exists and is committed (FR-010, Edge Case). Run `git status mobile/pubspec.lock` — must show as tracked (not in `.gitignore`). If it is in `.gitignore`, remove the exception.

- [ ] T016 [P] Confirm `mobile/.gitignore` excludes (Edge Case): `GoogleService-Info.plist`, `google-services.json`. Open `mobile/.gitignore` and verify these lines are present. Add them if missing. Do NOT commit these files.

---

## Dependencies & Execution Order

```
Phase 1 (T001–T003) — T001 first; T002 and T003 parallel after T001
  └─► Phase 2 (T004, T005) — parallel with each other after Phase 1
        └─► Phase 3 (T006–T010) — T006 and T007 parallel; T008 after T006+T007; T009 and T010 parallel after T008
        └─► Phase 4 (T011) — after Phase 3 (needs all Dart files in place)
        └─► Phase 5 (T012) — after Phase 1 (verification only)
              └─► Phase 6 (T013–T016) — after all phases complete
```

---

## Notes for LLM Agents

- **Null safety mandatory** — `sdk: ">=3.0.0 <4.0.0"` in pubspec.yaml; all Dart code uses null safety (FR-001)
- **Hive before runApp** — `await Hive.initFlutter()` MUST appear before `runApp()` (Edge Case)
- **ProviderScope at root** — MUST be the top-level widget in `main()`, not inside a subtree (Edge Case)
- **No Firebase** — do NOT add `firebase_core`, FCM, or any Firebase packages (FR-011, FR-012)
- **Commit `pubspec.lock`** — this is intentional for reproducibility; do not add to `.gitignore`
- **API_BASE_URL via --dart-define** — not from `dotenv` or hardcoded; empty default triggers config error screen
- **Commit message**: `feat(mobile): add Flutter scaffold with Riverpod, Dio, Hive, and placeholder screens`
