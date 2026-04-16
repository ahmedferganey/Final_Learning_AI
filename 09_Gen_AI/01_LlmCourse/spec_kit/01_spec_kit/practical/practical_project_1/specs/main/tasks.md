# Tasks: AI-Powered Backend System

**Input**: Design documents from `/specs/main/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Contract and integration tests are included because the specification requires strict validation, RBAC enforcement, and documented API contracts.

**Organization**: Tasks are grouped by user story so auth, user, and RAG capabilities can be implemented and validated incrementally.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the backend project skeleton and documentation alignment

- [ ] T001 Create the backend source tree described in `specs/main/plan.md`
- [ ] T002 Initialize FastAPI application bootstrap in `backend/app/main.py`
- [ ] T003 [P] Add dependency and tool configuration for FastAPI, SQLAlchemy, Alembic, and pytest in repository project files
- [ ] T004 [P] Add environment and settings handling in `backend/app/core/config.py`
- [ ] T005 [P] Copy the versioned API contracts from `specs/main/contracts/` to `specs/api/` and keep them synchronized

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create the shared infrastructure that all stories depend on

- [ ] T006 Create database session and metadata bootstrap in `backend/app/db/session.py` and `backend/app/db/base.py`
- [ ] T007 [P] Implement ORM models for `User`, `Role`, `RefreshSession`, `AuditEvent`, `KnowledgeCollection`, and `DocumentChunk` in `backend/app/db/models/`
- [ ] T008 [P] Implement JWT signing, password hashing, and token parsing in `backend/app/core/security.py`
- [ ] T009 [P] Implement RBAC permission helpers in `backend/app/core/permissions.py`
- [ ] T010 [P] Implement structured audit and request logging in `backend/app/core/logging.py`
- [ ] T011 Create shared Pydantic schemas for auth, users, and RAG in `backend/app/schemas/`
- [ ] T012 Create API router registration and global exception handlers in `backend/app/api/`

**Checkpoint**: Foundation ready for independent story implementation

---

## Phase 3: User Story 1 - Secure Authentication and Session Management (Priority: P1) 🎯 MVP

**Goal**: Deliver registration, login, refresh, logout, and current-user access with JWT and rotating refresh tokens

**Independent Test**: Register a user, log in, refresh the session, call `GET /v1/users/me`, and verify forbidden access to an admin-only endpoint

### Tests for User Story 1

- [ ] T013 [P] [US1] Add contract tests for `specs/main/contracts/auth.yaml` in `backend/tests/contract/test_auth_contract.py`
- [ ] T014 [P] [US1] Add integration tests for registration, login, refresh rotation, and logout in `backend/tests/integration/test_auth_flow.py`

### Implementation for User Story 1

- [ ] T015 [P] [US1] Implement auth request and response schemas in `backend/app/schemas/auth.py`
- [ ] T016 [US1] Implement refresh-session persistence and replay protection in `backend/app/services/token_service.py`
- [ ] T017 [US1] Implement registration, login, refresh, and logout business logic in `backend/app/services/auth_service.py`
- [ ] T018 [US1] Implement `/v1/auth/*` routes in `backend/app/api/v1/auth.py`
- [ ] T019 [US1] Implement authenticated current-user dependency and `GET /v1/users/me` read path in `backend/app/api/v1/users.py`

**Checkpoint**: Authentication and session management work independently

---

## Phase 4: User Story 2 - User Profile and Role Administration (Priority: P2)

**Goal**: Deliver profile updates and administrator role management with RBAC and audit logging

**Independent Test**: Update the current user's profile and replace another user's roles as an admin while confirming a non-admin receives HTTP 403

### Tests for User Story 2

- [ ] T020 [P] [US2] Add contract tests for `specs/main/contracts/users.yaml` in `backend/tests/contract/test_users_contract.py`
- [ ] T021 [P] [US2] Add integration tests for profile updates and role replacement in `backend/tests/integration/test_user_service.py`

### Implementation for User Story 2

- [ ] T022 [P] [US2] Implement user profile and role schemas in `backend/app/schemas/users.py`
- [ ] T023 [US2] Implement profile update and administrative role management logic in `backend/app/services/user_service.py`
- [ ] T024 [US2] Implement `PATCH /v1/users/me` and `PUT /v1/users/{user_id}/roles` in `backend/app/api/v1/users.py`
- [ ] T025 [US2] Add audit-event creation for role changes and activation changes in `backend/app/services/user_service.py`

**Checkpoint**: User administration works independently

---

## Phase 5: User Story 3 - Retrieval-Augmented Generation Query Flow (Priority: P3)

**Goal**: Deliver an authenticated RAG query endpoint with retrieval, generation, and citations

**Independent Test**: Submit a valid query to `POST /v1/rag/query`, receive an answer with citations, and verify invalid and unauthorized requests are rejected

### Tests for User Story 3

- [ ] T026 [P] [US3] Add contract tests for `specs/main/contracts/rag.yaml` in `backend/tests/contract/test_rag_contract.py`
- [ ] T027 [P] [US3] Add integration tests for retrieval, generation, and authorization scenarios in `backend/tests/integration/test_rag_query.py`

### Implementation for User Story 3

- [ ] T028 [P] [US3] Implement RAG request and response schemas in `backend/app/schemas/rag.py`
- [ ] T029 [P] [US3] Implement retrieval logic in `backend/app/services/retrieval_service.py`
- [ ] T030 [P] [US3] Implement provider-facing generation logic in `backend/app/services/generation_service.py`
- [ ] T031 [US3] Implement orchestration in `backend/app/services/rag_service.py`
- [ ] T032 [US3] Implement `POST /v1/rag/query` in `backend/app/api/v1/rag.py`

**Checkpoint**: RAG query flow works independently

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Harden documentation, observability, and validation across stories

- [ ] T033 [P] Add API examples and error payload examples to all files in `specs/main/contracts/` and `specs/api/`
- [ ] T034 Add rate limiting and abuse protection strategy to auth and RAG endpoints
- [ ] T035 [P] Add unit tests for security helpers, RBAC rules, and RAG orchestration in `backend/tests/unit/`
- [ ] T036 Run `quickstart.md` validation against the implemented backend and update mismatches

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: starts immediately
- **Foundational (Phase 2)**: depends on Setup and blocks all user stories
- **User Stories (Phase 3-5)**: depend on Foundational completion
- **Polish (Phase 6)**: depends on selected story completion

### User Story Dependencies

- **User Story 1 (P1)**: no dependency on later stories and defines the MVP
- **User Story 2 (P2)**: depends on User Story 1 authentication primitives
- **User Story 3 (P3)**: depends on auth, users, and foundational data access

### Parallel Opportunities

- Tasks marked `[P]` can run in parallel when they target different files
- Contract tests for separate services can proceed in parallel after contracts stabilize
- Retrieval and generation service work can proceed in parallel before orchestration integration
