# 45. Git and Version Control Systems

> Phase 10 — Git & Configuration Automation

Git is not merely a command used to upload code to GitHub. It is a **distributed content-addressed version-control system** that records the history of files, supports parallel development, enables review and rollback, and becomes the audit foundation for modern Infrastructure as Code and automation.

**Reference baseline:** Git **2.55.x** documentation. The concepts and commands in this course are intentionally version-stable.

The mental model for Git is:

```text
Working Tree
    |
    | git add
    v
Staging Area / Index
    |
    | git commit
    v
Local Repository
    |
    | git push
    v
Remote Repository
```

But the deeper model is:

```text
Files
  ↓
Blobs

Directory Structure
  ↓
Trees

Snapshot + Metadata + Parent
  ↓
Commit

Human-Friendly Name
  ↓
Branch / Tag

Current Checked-Out Commit
  ↓
HEAD
```

Git becomes especially important for infrastructure because the same repository can store:

```text
Ansible
Terraform
Kubernetes YAML
Dockerfiles
CI/CD
Shell scripts
Documentation
Security policy
Runbooks
```

This course uses:

```text
Concept
  ↓
Diagram
  ↓
Git command
  ↓
Repository state
  ↓
Expected output
  ↓
Failure scenario
  ↓
Recovery
```

---

## 1. Topic Title

**Git and Version Control Systems**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain why version control exists.
- Differentiate centralized and distributed version control.
- Explain the Git working tree, index, object database, refs, and HEAD.
- Explain blobs, trees, commits, and tags.
- Initialize, clone, inspect, and configure repositories.
- Stage files selectively.
- Create meaningful commits.
- Read Git status and diffs accurately.
- Use `.gitignore` correctly.
- Understand branches as movable references.
- Create, switch, rename, and delete branches.
- Explain detached HEAD.
- Merge branches and resolve conflicts.
- Explain fast-forward, three-way, and squash-style workflows.
- Rebase branches safely.
- Explain merge versus rebase.
- Use interactive rebase on unpublished history.
- Work with remotes and remote-tracking branches.
- Understand fetch, pull, and push.
- Understand upstream branches.
- Resolve non-fast-forward push failures.
- Use `restore`, `reset`, and `revert` correctly.
- Recover work with reflog.
- Use stash.
- Create annotated and lightweight tags.
- Understand signed commits/tags conceptually.
- Use `git log`, `show`, `diff`, and blame appropriately.
- Find regressions with `git bisect`.
- Use `git worktree`.
- Understand submodules and their operational risks.
- Understand hooks.
- Understand Git attributes and line endings.
- Manage binary/large-file concerns.
- Understand branch protection and pull/merge-request workflows.
- Apply Git to Infrastructure as Code.
- Protect credentials and secrets.
- Design a professional Git repository and team workflow.
- Troubleshoot common Git failures without losing work.

---

## 3. Prerequisites

Required:

- Linux command-line fundamentals
- Bash fundamentals
- Files and directories
- SSH fundamentals
- Text editor basics

Lab tools:

```bash
git --version
ssh -V
```

Example identity configuration:

```bash
git config --global user.name "Lab User"
git config --global user.email "lab@example.com"
```

Use a disposable lab repository for destructive experiments.

---

## 4. Core Concepts Explanation

# Part 1 — Why Version Control Exists

Without version control, teams often create files such as:

```text
config.conf
config-final.conf
config-final2.conf
config-final-really-final.conf
```

Version control replaces manual copies with a structured history:

```text
Version A
  ↓
Version B
  ↓
Version C
```

Each change records who changed what, when, and—through the commit message—why.

# Part 2 — Centralized vs Distributed Version Control

A centralized VCS depends primarily on one central repository. Git is distributed:

```text
Remote Repository
   ↕
Developer A Repository

Remote Repository
   ↕
Developer B Repository
```

Each clone normally contains project history, so many operations work offline and collaboration is not limited to one central server.

# Part 3 — Repository

A Git repository is the project history plus metadata.

In a normal working repository:

```text
project/
├── .git/
├── files...
└── directories...
```

`.git/` contains object storage, references, configuration, index information, logs, and other Git metadata.

# Part 4 — Working Tree

The working tree is the checked-out file view you edit.

```text
Git commit
   ↓ checkout
Working Tree
   ↓ edit
Modified files
```

A modified file is not yet part of a new commit.

# Part 5 — Staging Area / Index

The index is the proposed next snapshot.

```text
working file
  |
git add
  v
index
```

This lets you commit only selected changes instead of every modified file.

# Part 6 — Local Repository

A commit is written to your local repository first.

```text
Working Tree
 → Index
 → Local Commit
```

A remote server is not required to create Git history.

# Part 7 — Three-State Mental Model

A file can be:

```text
modified
staged
committed
```

Example:

```bash
echo "v2" >> config.txt
git status
git add config.txt
git status
git commit -m "Update config"
```

Observe how the state changes after each command.

# Part 8 — `git init`

Initialize:

```bash
mkdir git-lab
cd git-lab
git init
```

Git creates `.git/`.

Inspect:

```bash
ls -la
```

A newly initialized repository has no commits until you create one.

# Part 9 — `git status`

`git status` is one of the safest and most important Git commands.

```bash
git status
```

It tells you:

```text
current branch
staged changes
unstaged changes
untracked files
upstream divergence
```

Run it before potentially destructive operations.

# Part 10 — Untracked Files

A new file is initially untracked.

```bash
touch app.conf
git status
```

Git does not automatically include every file in history. You explicitly add files to the next snapshot.

# Part 11 — `git add`

Stage a file:

```bash
git add app.conf
```

Stage selected paths:

```bash
git add src/ docs/
```

Avoid habitual `git add .` until you have reviewed what it will stage.

# Part 12 — Patch Staging

Stage only some hunks:

```bash
git add -p
```

This is valuable when one file contains two unrelated changes.

A good commit should represent one coherent change rather than whatever happened since the last commit.

# Part 13 — `git diff`

Unstaged differences:

```bash
git diff
```

Staged differences:

```bash
git diff --staged
```

Compare:

```text
working tree ↔ index
index ↔ HEAD
```

Review both before committing.

# Part 14 — `git commit`

Create snapshot:

```bash
git commit -m "Add baseline NGINX configuration"
```

A commit includes:

```text
tree snapshot
author
committer
timestamp
message
parent commit(s)
```

# Part 15 — Commit Message Quality

Weak:

```text
update
fix
changes
```

Better:

```text
Add production NGINX TLS baseline
```

The message should help a future engineer answer:

```text
what changed?
why was it necessary?
```

# Part 16 — Commit as Snapshot

Git conceptually stores project snapshots, not a simple list of line edits.

```text
Commit A → Tree A
Commit B → Tree B
```

Diffs are calculated by comparing snapshots.

# Part 17 — Blob Object

A blob stores file content.

Concept:

```text
"hello
"
   ↓ hash
blob object
```

A blob does not inherently store the filename. The tree object maps names to objects.

# Part 18 — Tree Object

A tree represents a directory snapshot.

```text
tree
├── README.md → blob
├── app.py    → blob
└── config/   → tree
```

This produces Git's hierarchical snapshot.

# Part 19 — Commit Object

Commit points to a root tree and parent commit(s).

```text
Commit C
 ├─ tree → project snapshot
 ├─ parent → Commit B
 ├─ author
 ├─ committer
 └─ message
```

A merge commit can have multiple parents.

# Part 20 — Content Addressing

Git objects are identified using hashes derived from content/object representation.

Concept:

```text
content
  ↓ hash
object ID
```

If tracked content changes, the object identity changes.

This supports integrity and deduplication of identical content.

# Part 21 — `git cat-file`

Inspect internals in a lab:

```bash
git rev-parse HEAD
git cat-file -t HEAD
git cat-file -p HEAD
```

Then inspect the tree hash shown by the commit.

This makes the object model concrete.

# Part 22 — References

A ref is a human-friendly pointer to a Git object.

Examples:

```text
refs/heads/main
refs/tags/v1.0
refs/remotes/origin/main
```

Branches are references, not separate copies of all files.

# Part 23 — Branch

Concept:

```text
A -- B -- C
          ↑
         main
```

Create branch:

```bash
git branch feature
```

Both refs can initially point to C.

# Part 24 — HEAD

HEAD indicates what you currently have checked out.

Normally:

```text
HEAD → main → commit C
```

Inspect:

```bash
git symbolic-ref HEAD
```

or:

```bash
git rev-parse --abbrev-ref HEAD
```

# Part 25 — `git switch`

Create and switch:

```bash
git switch -c feature/login
```

Switch existing:

```bash
git switch main
```

`git switch` is clearer for branch switching than overloading `checkout`.

# Part 26 — Branch Commit Movement

If HEAD points to `feature` and you commit:

```text
A -- B -- C
          ↑
         main
                     D
           ↑
        feature
```

Only the checked-out branch reference moves.

# Part 27 — Detached HEAD

Checkout a commit directly:

```bash
git switch --detach <commit>
```

Now:

```text
HEAD → commit
```

not:

```text
HEAD → branch
```

Commits created here can become unreachable unless you create a branch/tag before losing the reference.

# Part 28 — Create Branch from Detached HEAD

Recover a useful detached commit:

```bash
git switch -c recovered-work
```

Now the commit is anchored by a branch reference.

# Part 29 — Rename Branch

Rename current branch:

```bash
git branch -m new-name
```

If the branch was already published, coordinate the remote rename/deletion and upstream tracking with collaborators.

# Part 30 — Delete Branch

Safe local deletion:

```bash
git branch -d feature
```

Force:

```bash
git branch -D feature
```

`-D` can remove a branch whose commits are not merged, so review history first.

# Part 31 — History

Readable graph:

```bash
git log --oneline --graph --decorate --all
```

This should become a routine command when understanding branch topology.

# Part 32 — `git show`

Inspect one commit:

```bash
git show HEAD
git show <commit>
```

Shows metadata and diff introduced by the commit.

# Part 33 — Revision Syntax

Useful examples:

```text
HEAD       current commit
HEAD~1     first-parent one commit before
HEAD^      parent
main~3     three first-parent steps behind main
```

Do not use relative revisions in destructive commands unless you confirm the target.

# Part 34 — Merge

Merge combines histories.

```text
A---B---C main
           D---E feature
```

From main:

```bash
git merge feature
```

Git determines common ancestor and combines changes.

# Part 35 — Fast-Forward Merge

If main has not advanced:

```text
A---B main
           C---D feature
```

Git can simply move main:

```text
A---B---C---D
            ↑
       main, feature
```

No merge commit is required.

# Part 36 — Three-Way Merge

If both sides changed:

```text
      C---D feature
     /
A---B---E main
```

Git combines:

```text
base B
main E
feature D
```

and normally creates a merge commit if successful.

# Part 37 — Merge Conflict

Conflict occurs when Git cannot automatically reconcile competing edits.

Markers:

```text
<<<<<<< HEAD
main version
=======
feature version
>>>>>>> feature
```

Resolve the actual desired content, remove markers, stage, and continue the merge.

# Part 38 — Conflict Resolution Workflow

```bash
git status
# edit conflicted files
git diff
git add resolved-file
git commit
```

To abandon:

```bash
git merge --abort
```

Use abort before making unrelated changes during conflict resolution.

# Part 39 — Rebase

Rebase replays commits on a new base.

Before:

```text
A---B---C main
           D---E feature
```

Rebase feature onto main:

```text
A---B---C---D'---E'
```

D' and E' are new commits with new IDs.

# Part 40 — Rebase Command

```bash
git switch feature
git rebase main
```

If conflict:

```bash
# resolve
git add file
git rebase --continue
```

Abort:

```bash
git rebase --abort
```

# Part 41 — Merge vs Rebase

Merge preserves explicit topology:

```text
history joined by merge
```

Rebase creates linearized rewritten history.

Rule:

```text
rebase your unpublished/local work freely
avoid rewriting shared public history without coordination
```

# Part 42 — Interactive Rebase

For local unpublished commits:

```bash
git rebase -i HEAD~4
```

You can:

```text
pick
reword
edit
squash
fixup
drop
```

This cleans history before review.

# Part 43 — Amend

Modify latest unpublished commit:

```bash
git add forgotten-file
git commit --amend
```

Amend replaces the commit with a new one.

Do not casually amend a commit others already pulled.

# Part 44 — Remote Repository

Remote is another repository location.

```bash
git remote -v
```

Typical name:

```text
origin
```

`origin` is a convention, not a special Git keyword with magical server behavior.

# Part 45 — Add Remote

```bash
git remote add origin git@example.com:team/repo.git
```

Verify:

```bash
git remote -v
```

Use SSH or HTTPS according to organization policy.

# Part 46 — `git clone`

```bash
git clone <url>
```

Clone generally creates:

```text
working tree
local object database
remote named origin
remote-tracking refs
checked-out default branch
```

# Part 47 — Remote-Tracking Branch

`origin/main` is your local record of the remote's main branch state from the last fetch/update.

```text
main
origin/main
```

are different refs.

# Part 48 — `git fetch`

```bash
git fetch origin
```

Fetch downloads new objects and updates remote-tracking refs without automatically merging them into your current branch.

This makes it a safe first step.

# Part 49 — `git pull`

Conceptually:

```text
git pull
=
git fetch
+
integration step
```

Integration can be merge or rebase depending on configuration/options.

Engineers should understand this rather than treating pull as a mysterious sync command.

# Part 50 — `git push`

```bash
git push origin main
```

Push asks remote to update a ref using objects from your repository.

The remote can reject the update due to policy or non-fast-forward history.

# Part 51 — Set Upstream

First push:

```bash
git push -u origin feature/api
```

Now local branch tracks:

```text
origin/feature/api
```

and simple `git pull`/`git push` can infer the remote branch.

# Part 52 — Ahead and Behind

If local has two commits not on remote:

```text
ahead 2
```

If remote has three not local:

```text
behind 3
```

You can be both ahead and behind after histories diverge.

# Part 53 — Non-Fast-Forward Push

Remote:

```text
A---B---C
```

Local:

```text
A---B---D
```

Pushing D over C would lose remote history, so Git rejects normal push.

Fetch, inspect, integrate, then push.

# Part 54 — Force Push

Dangerous:

```bash
git push --force
```

Safer when intentionally rewriting your own remote branch:

```bash
git push --force-with-lease
```

`--force-with-lease` checks that the remote ref is still what you expect, reducing accidental overwrites.

# Part 55 — Fork / Pull Request Workflow

Hosted platforms often add a review layer:

```text
fork/branch
  ↓
commit
  ↓
push
  ↓
pull/merge request
  ↓
review
  ↓
CI
  ↓
merge
```

Git provides the repository mechanics; the hosting platform provides review/workflow features.

# Part 56 — Protected Branch

Organizations often protect `main` so it cannot be directly force-pushed or updated without review/checks.

This turns Git history into a controlled change-management record.

# Part 57 — `.gitignore`

Example:

```gitignore
.env
*.log
__pycache__/
.venv/
terraform.tfstate
```

`.gitignore` affects untracked files. It does not automatically remove files already committed.

# Part 58 — Stop Tracking an Already Tracked File

If a file should remain locally but stop being tracked:

```bash
git rm --cached .env
```

Then add it to `.gitignore`.

If the file contained a secret, removing it from the latest tree does **not** remove it from historical commits.

# Part 59 — Secret Exposure in Git

If a secret is committed:

```text
1. Assume exposed.
2. Rotate/revoke it.
3. Remove it from current code.
4. Consider history rewriting only as secondary cleanup.
```

A rewritten repository cannot revoke a copied credential.

# Part 60 — `.gitattributes`

`.gitattributes` controls path-specific Git behavior.

Example line-ending policy:

```gitattributes
* text=auto
*.sh text eol=lf
*.ps1 text eol=crlf
```

It can also configure merge/diff behavior and large-file tooling.

# Part 61 — Line Endings

Cross-platform repositories can encounter:

```text
LF
CRLF
```

A bad configuration can make every line appear changed.

Standardize with `.gitattributes` rather than relying only on each developer's local setting.

# Part 62 — File Permissions

Git tracks the executable bit on supported filesystems.

For scripts:

```bash
chmod +x deploy.sh
git add deploy.sh
```

The executable-bit change can be part of the commit.

# Part 63 — Binary Files

Git works best with text. Large frequently changing binaries can inflate repository history because Git must retain object versions.

Use artifact repositories or Git LFS where appropriate rather than storing VM images, database dumps, or installer ISOs directly in normal Git history.

# Part 64 — Stash

Temporarily save uncommitted changes:

```bash
git stash push -m "WIP firewall config"
```

List:

```bash
git stash list
```

Restore:

```bash
git stash pop
```

# Part 65 — Stash Risk

Stash is not a long-term project-management system.

Important work should become a branch/commit.

A named commit is easier to review, back up, and recover than a pile of forgotten stashes.

# Part 66 — `git restore`

Restore a working-tree file from index/commit:

```bash
git restore file.txt
```

Restore staged state:

```bash
git restore --staged file.txt
```

This makes intent clearer than some historical `checkout` usages.

# Part 67 — `git reset` Mental Model

Reset moves a branch/HEAD reference and optionally changes index/working tree.

Modes:

```text
--soft   move ref, keep index + files
--mixed  move ref, reset index, keep files
--hard   move ref, reset index + files
```

`--hard` can discard local uncommitted work.

# Part 68 — Soft Reset

```bash
git reset --soft HEAD~1
```

The latest commit disappears from branch history, but its changes remain staged.

Useful for rewriting unpublished commit structure.

# Part 69 — Mixed Reset

Default:

```bash
git reset HEAD~1
```

Changes remain in the working tree but become unstaged.

This is useful when you want to recommit differently.

# Part 70 — Hard Reset

```bash
git reset --hard HEAD~1
```

This resets branch, index, and working tree.

Before using it:

```bash
git status
git log --oneline
```

and verify no needed uncommitted changes exist.

# Part 71 — `git revert`

Revert creates a **new commit** that reverses an earlier commit.

```bash
git revert <commit>
```

This is normally safer for shared history because it does not erase published commits.

# Part 72 — Reset vs Revert

```text
reset
  rewrites/moves history reference
  best for local/unpublished correction

revert
  adds inverse commit
  best for shared/published history
```

# Part 73 — Reflog

Reflog records local ref movements.

```bash
git reflog
```

It can recover commits after:

```text
reset
rebase
branch deletion
detached HEAD mistake
```

Reflog is one of Git's most important recovery tools.

# Part 74 — Recover After Bad Reset

Suppose you ran:

```bash
git reset --hard HEAD~3
```

and realize it was wrong.

```bash
git reflog
git branch recovery <old-commit>
```

Recover the old state before doing more destructive operations.

# Part 75 — Tags

Tags name important commits.

Lightweight:

```bash
git tag v1.0.0
```

Annotated:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
```

Annotated tags include metadata and are generally better for releases.

# Part 76 — Push Tags

Tags are not necessarily pushed automatically.

```bash
git push origin v1.0.0
```

All local tags:

```bash
git push origin --tags
```

Review before pushing every experimental tag.

# Part 77 — Signed Commits and Tags

Git supports cryptographic signing workflows.

Purpose:

```text
prove that a commit/tag was signed by a controlled key/identity
```

Signing does not automatically prove the code is safe; it strengthens provenance.

# Part 78 — `git blame`

```bash
git blame config.yml
```

Shows which commit last changed each line.

Use it to find context, not to assign blame to people.

Follow the commit into `git show` to understand why the change happened.

# Part 79 — `git bisect`

Bisect performs binary search across history to locate a regression.

```text
good commit
bad commit
  ↓
Git checks midpoint
  ↓
you classify good/bad
  ↓
repeat
```

This can turn hundreds of commits into a small number of tests.

# Part 80 — Bisect Commands

```bash
git bisect start
git bisect bad
git bisect good <known-good>
```

Test each checked-out revision:

```bash
git bisect good
# or
git bisect bad
```

Finish:

```bash
git bisect reset
```

# Part 81 — Automated Bisect

If a script exits 0 for good and nonzero for bad:

```bash
git bisect run ./test-regression.sh
```

Git can automatically locate the first bad commit.

# Part 82 — `git worktree`

Worktrees allow multiple branches checked out simultaneously.

```bash
git worktree add ../hotfix hotfix
```

Useful when you are working on a feature but need an urgent hotfix without stashing/switching the current tree.

# Part 83 — Worktree Use Case

```text
repo-main/
  feature branch

repo-hotfix/
  hotfix branch

same object database
```

This reduces duplicated clones and context switching.

# Part 84 — Submodules

A submodule records another Git repository at a specific commit.

```text
parent repo
  |
  +-- vendor/tool → commit abc123 in another repo
```

The parent records the submodule commit pointer, not all of its history as normal parent files.

# Part 85 — Submodule Commands

Clone with submodules:

```bash
git clone --recurse-submodules <url>
```

Existing clone:

```bash
git submodule update --init --recursive
```

Submodules add lifecycle complexity; use them deliberately.

# Part 86 — Submodule Detached HEAD

Submodules are often checked out at the exact commit recorded by the parent, which may appear as detached HEAD.

To develop the submodule, explicitly switch/create a branch inside the submodule repository.

# Part 87 — Hooks

Git hooks are scripts triggered by Git events.

Examples:

```text
pre-commit
commit-msg
pre-push
post-merge
```

Use cases:

```text
linting
secret scanning
format checks
policy checks
```

# Part 88 — Local Hook Limit

Client-side hooks are not automatically enforced for every clone.

Critical policy should also run server-side or in CI.

A developer can often bypass a local hook.

# Part 89 — Pre-Commit Concept

Example hook logic:

```bash
#!/usr/bin/env bash
set -e

./scripts/lint.sh
./scripts/scan-secrets.sh
```

The commit should fail if required validation fails.

# Part 90 — Git Configuration Layers

Configuration scopes:

```text
system
global
local repository
worktree/command-specific contexts
```

Inspect origin:

```bash
git config --list --show-origin
```

# Part 91 — User Identity Configuration

```bash
git config --global user.name "Ahmed Engineer"
git config --global user.email "ahmed@example.com"
```

A commit's author identity is metadata, not strong authentication. Use signing/hosting identity controls where provenance matters.

# Part 92 — Default Branch

Set preference:

```bash
git config --global init.defaultBranch main
```

This affects new repositories; it does not rename existing branches automatically.

# Part 93 — Aliases

Example:

```bash
git config --global alias.lg "log --oneline --graph --decorate --all"
```

Then:

```bash
git lg
```

Do not use opaque aliases in shared automation where readability matters.

# Part 94 — SSH Authentication for Remotes

Architecture:

```text
Git client
  |
SSH private key
  |
Git hosting server
```

Protect private keys and prefer passphrases/agents or organizational identity mechanisms.

# Part 95 — HTTPS Authentication

Hosted Git systems commonly use tokens or credential helpers for HTTPS rather than account passwords.

Never embed access tokens directly in remote URLs committed to scripts.

# Part 96 — Credential Helpers

Git credential helpers can integrate with OS credential storage.

This is safer than a plaintext token in:

```text
shell history
scripts
.git/config URL
```

# Part 97 — Remote URL Inspection

```bash
git remote -v
git remote get-url origin
```

Check this before pushing sensitive code to ensure you are targeting the intended repository.

# Part 98 — Multiple Remotes

A repository can have:

```text
origin
upstream
backup
```

Example open-source model:

```text
origin   → your fork
upstream → canonical repository
```

# Part 99 — Fetch from Upstream

```bash
git fetch upstream
git switch main
git merge --ff-only upstream/main
```

Then push your fork if needed.

`--ff-only` prevents accidental merge commits in a branch expected to mirror upstream.

# Part 100 — Branching Strategy

Common strategies include:

```text
trunk-based development
short-lived feature branches
release branches
GitFlow-style models
```

Choose based on release process and team needs rather than fashion.

# Part 101 — Trunk-Based Development

Model:

```text
main
 ↑
small frequent merges
```

Features use very short-lived branches, strong CI, and feature flags where needed.

This reduces long-lived branch divergence.

# Part 102 — Long-Lived Feature Branch Risk

As time passes:

```text
main changes
feature changes
```

Integration distance grows.

Result:

```text
larger conflicts
harder review
delayed feedback
```

Prefer small reviewable increments.

# Part 103 — Release Branch

A release branch can stabilize a version while main continues.

```text
main → next development
release/2.0 → final fixes
```

Every fix may need a deliberate merge/cherry-pick strategy to prevent divergence.

# Part 104 — `git cherry-pick`

Apply one existing commit onto current branch:

```bash
git cherry-pick <commit>
```

This creates a new commit with the same patch but a different parent/history identity.

# Part 105 — Cherry-Pick Use Case

Example:

```text
main has security fix
release/1.0 needs same fix
```

Cherry-pick can apply the specific commit.

Overusing cherry-pick across many branches can create duplicated/confusing history.

# Part 106 — Merge Commit Policy

Teams may choose:

```text
merge commit
squash merge
rebase + fast-forward
```

Each preserves different history information.

Document the policy so contributors know what review history will look like.

# Part 107 — Squash Merge Concept

Many feature commits become one main-branch commit.

```text
feature:
A-B-C-D

main after squash:
A'  (combined changes)
```

Good for clean main history, but individual branch commits are not preserved as main ancestors.

# Part 108 — Repository Hygiene

Keep out:

```text
secrets
build output
logs
dependency caches
large artifacts
temporary files
machine-specific IDE state
```

Keep in:

```text
source
configuration
tests
documentation
automation
schema/migrations
```

# Part 109 — Version-Controlled Infrastructure

For infrastructure:

```text
Desired Config
     ↓
Git
     ↓
Review
     ↓
CI validation
     ↓
Automation
     ↓
Servers
```

Git becomes the auditable source of change.

# Part 110 — GitOps Concept

GitOps extends this idea:

```text
Git desired state
   ↓
automated reconciliation
   ↓
runtime environment
```

The important concept is **Git as declared source of truth plus automated reconciliation**, not merely storing YAML in Git.

# Part 111 — Infrastructure Commit Design

Bad:

```text
"update servers"
```

Better:

```text
"Harden SSH ciphers on production web hosts"
```

Infrastructure history should explain operational intent because it may later be used during incident response.

# Part 112 — Code Review for Infrastructure

Review should ask:

```text
What systems change?
Is it idempotent?
Is rollback possible?
Are secrets exposed?
Is blast radius controlled?
Are tests present?
```

Git enables this review before execution.

# Part 113 — Atomic Commits

One commit should ideally represent one coherent change.

Benefit:

```text
review easier
revert safer
bisect useful
cherry-pick precise
```

Avoid mixing formatting, refactoring, and a production firewall change in one commit.

# Part 114 — Commit Buildability

Aim for commits that leave the repository in a valid/testable state.

This improves:

```text
bisect
review
rollback
CI
```

# Part 115 — Protected Secrets Pattern

Repository:

```text
config.example.yml
```

Secret system:

```text
production password
API key
private certificate key
```

Automation combines them at runtime.

# Part 116 — Signed Release Tags

For important automation releases:

```bash
git tag -s v2.0.0 -m "Automation release 2.0.0"
```

when your organizational signing setup supports it.

A signed release tag helps establish provenance.

# Part 117 — Audit Trail Limitations

Git records repository history, but it does not automatically prove:

```text
who executed a deployment
what environment actually changed
whether a commit was reviewed
```

Combine Git with CI/CD logs, identity controls, and runtime audit logs.

# Part 118 — Repository Backup

A distributed clone is useful but is not necessarily a complete backup of hosting-platform metadata such as:

```text
pull requests
issues
branch protections
CI secrets
```

Back up critical repository and platform state according to business requirements.

# Part 119 — Repository Corruption Check

Git can verify object connectivity/integrity:

```bash
git fsck
```

Use it during repository diagnosis.

Do not delete `.git/objects` manually.

# Part 120 — Garbage Collection

Git manages unreachable/packed objects through maintenance/GC.

```bash
git gc
```

Most users should let Git perform maintenance automatically unless diagnosing/storage-optimizing large repositories.

# Part 121 — Packfiles

Git compresses many objects into packfiles.

This improves:

```text
storage
clone/fetch efficiency
```

Object model remains logically blobs/trees/commits even when physically packed.

# Part 122 — Shallow Clone

Example:

```bash
git clone --depth 1 <url>
```

Useful for some CI jobs.

Tradeoff:

```text
limited history
bisect/history operations restricted
```

# Part 123 — Partial Clone Concept

Partial clone can omit certain objects until needed.

Use case:

```text
very large repository
```

This is an optimization; understand tool/server compatibility before standardizing it.

# Part 124 — Sparse Checkout

Sparse checkout lets a working tree contain only selected paths from a large repository while history can remain broader.

Useful for monorepos where an engineer needs one subsystem.

# Part 125 — Monorepo vs Multirepo

Monorepo:

```text
many components in one Git repository
```

Multirepo:

```text
component per repository
```

Tradeoffs involve ownership, CI scale, atomic cross-component changes, permissions, and release independence.

# Part 126 — Semantic Versioning Concept

A common release convention:

```text
MAJOR.MINOR.PATCH
```

Git tags can identify releases:

```text
v2.3.1
```

Git itself does not enforce semantic versioning.

# Part 127 — Release Notes from Git

Useful:

```bash
git log v1.0.0..v1.1.0 --oneline
```

This lists commits between tags.

Good commit messages make release-note generation much more useful.

# Part 128 — Compare Branches

```bash
git diff main...feature
```

Three-dot comparison is useful for reviewing changes introduced on a branch relative to the merge base.

Understand whether your tool uses two-dot or three-dot semantics.

# Part 129 — `git range-diff`

`range-diff` compares two versions of a patch series.

Useful after rebasing a reviewed branch to answer:

```text
what changed between old and new revision of the commits?
```

# Part 130 — Merge Base

Find common ancestor:

```bash
git merge-base main feature
```

Merge/rebase/diff behavior often depends on this commit.

# Part 131 — Conflict Prevention

Reduce conflicts through:

```text
small branches
frequent integration
clear ownership
modular files
automatic formatting
```

Conflict resolution is easier than avoiding collaboration, but architecture can reduce unnecessary conflicts.

# Part 132 — Recover Deleted Branch

If a branch was deleted but commit was recent:

```bash
git reflog
git branch restored <commit>
```

This works while the commit remains reachable through reflog/object retention.

# Part 133 — Recover Uncommitted Changes

Git can only reliably recover content Git knew about.

Untracked or unstaged overwritten files may be unrecoverable.

Therefore:

```text
commit early on a private branch
```

is a practical safety technique.

# Part 134 — Before Destructive Git Commands

Use this checklist:

```bash
git status
git log --oneline --graph --decorate --all -20
git reflog -10
```

Then decide whether you mean:

```text
restore?
reset?
revert?
rebase?
```

# Part 135 — Git Troubleshooting Workflow

```text
1. Stop typing random commands.
2. Run git status.
3. Draw branch graph.
4. Identify local and remote refs.
5. Protect current work with branch/commit if needed.
6. Use reflog before assuming data is lost.
7. Apply the smallest correction.
```

---

# Enhanced Deep-Study Layer — Git and Version Control Systems

This enhancement preserves the complete uploaded Course 45 and adds a deeper layer on Git internals, recovery, collaboration, security, repository scale, CI policy, and infrastructure change control.

The goal is to move beyond command memorization. You should be able to **predict Git state before running a command**, draw the commit/ref graph, distinguish working tree/index/object database/remote state, recover safely, and design a professional repository workflow for infrastructure and software teams.

The additional learning sequence used throughout is:

```text
Concept
  ↓
Detailed Explanation
  ↓
Internal / Architecture Model
  ↓
Commands / Code / Configuration
  ↓
Expected State / Output
  ↓
Why It Works
  ↓
Production Example
  ↓
Failure / Troubleshooting
  ↓
Best Practice
```

## Advanced Deep Dive 1 — Git's Object Database and the Snapshot Graph

### Concept and Detailed Explanation
Git's real database is not a table of file versions. It is a graph of immutable objects. File contents become blobs, directory snapshots become trees, commits point to a root tree plus parent commit(s), and annotated tags point to another object. Branches are mutable references outside that immutable object graph.

This explains why commits are cheap, branches are lightweight, and many recovery operations are possible: most commands move references or create new objects rather than modifying old objects in place.

### Internal / Architecture Model
```text
refs/heads/main
      |
      v
   Commit C
   /      parent B   tree T3
   |       /    Commit B  blob  tree
   |
Commit A

Object database:
.git/objects/
```

### Commands / Code / Configuration
```text
git rev-parse HEAD
git cat-file -t HEAD
git cat-file -p HEAD
git ls-tree -r HEAD
git count-objects -v
```

### Expected State / Output
HEAD resolves to a commit object; that commit points to a tree; the tree maps names/modes to blob/tree IDs.

### Why It Works
Git can reconstruct any committed snapshot by following immutable object references.

### Production Example
An infrastructure repository can recover a deleted branch because the commits still exist in the object database and reflog even after the branch ref is removed.

### Failure / Troubleshooting Workflow
```text
confusing history
  ↓
identify refs
  ↓
resolve commit IDs
  ↓
inspect commit/tree/blob
  ↓
determine which ref moved
  ↓
recover with new ref
```

### Best Practice
Learn the object graph before memorizing recovery commands.

---

## Advanced Deep Dive 2 — Porcelain vs Plumbing Commands

### Concept and Detailed Explanation
Git exposes high-level 'porcelain' commands for daily work and lower-level 'plumbing' commands for inspecting/manipulating internals. Porcelain commands such as `commit`, `switch`, and `merge` combine several internal operations. Plumbing commands such as `hash-object`, `cat-file`, `update-ref`, and `write-tree` reveal how Git actually works.

You normally use porcelain in production and plumbing for diagnostics, education, or specialized tooling.

### Internal / Architecture Model
```text
Porcelain:
git add
git commit
git merge
git switch

        ↓ implemented using concepts ↓

Plumbing:
hash-object
update-index
write-tree
commit-tree
update-ref
cat-file
```

### Commands / Code / Configuration
```text
printf 'hello
' > demo.txt
git hash-object demo.txt
git hash-object -w demo.txt
git cat-file -t $(git hash-object demo.txt)
```

### Expected State / Output
A blob ID is calculated from the content; with `-w` the object is stored in the object database.

### Why It Works
High-level commands are composed from lower-level object/ref/index operations.

### Production Example
A forensic or repository-repair script may use `cat-file --batch` to inspect many objects without checking out files.

### Failure / Troubleshooting Workflow
```text
porcelain result unexpected
  ↓
git status
  ↓
inspect refs/index/object IDs
  ↓
use plumbing read-only commands
  ↓
understand high-level behavior
```

### Best Practice
Use plumbing to understand Git, but avoid direct ref/object mutation unless you know the consequences.

---

## Advanced Deep Dive 3 — The Index as a Real Data Structure

### Concept and Detailed Explanation
The staging area is not merely 'files waiting to be committed.' It is an index containing path, mode, object ID, and conflict-stage entries. It represents the exact tree Git would write if you committed now.

This is why a file can have one version in HEAD, another staged in the index, and a third in the working tree.

### Internal / Architecture Model
```text
HEAD snapshot
    |
    | git restore --staged / git add
    v
INDEX
path → blob ID + mode
    |
    | checkout/write
    v
WORKING TREE
```

### Commands / Code / Configuration
```text
git ls-files --stage
git diff --cached
git diff
git status --short
```

### Expected State / Output
`git ls-files --stage` shows staged object IDs and file modes, while the two diff commands show index↔HEAD and working-tree↔index changes.

### Why It Works
The index is Git's proposed next tree, not simply a list of filenames.

### Production Example
A reviewer can split a large working-tree change into two atomic commits by staging only selected hunks into the index.

### Failure / Troubleshooting Workflow
```text
wrong content staged
  ↓
git status
  ↓
git diff --cached
  ↓
git restore --staged <path>
  ↓
stage correct hunks
  ↓
verify again
```

### Best Practice
Review `git diff --cached` before every meaningful commit.

---

## Advanced Deep Dive 4 — Conflict Stages in the Index

### Concept and Detailed Explanation
During an unresolved merge, the index can hold up to three entries for the same path: stage 1 is the merge base, stage 2 is 'ours', and stage 3 is 'theirs'. Understanding these stages makes conflict resolution much more concrete than staring only at conflict markers.

### Internal / Architecture Model
```text
Index during conflict:

stage 1 → BASE
stage 2 → OURS
stage 3 → THEIRS

working tree → editable resolution
```

### Commands / Code / Configuration
```text
git ls-files -u
git show :1:path/to/file
git show :2:path/to/file
git show :3:path/to/file
git diff --cc
```

### Expected State / Output
You can inspect base, ours, and theirs independently and then stage the final resolved working-tree version.

### Why It Works
A three-way merge needs the common ancestor plus both branch tips to decide what changed on each side.

### Production Example
A complex infrastructure YAML conflict can be resolved by comparing base/ours/theirs rather than guessing from conflict markers.

### Failure / Troubleshooting Workflow
```text
merge conflict
  ↓
inspect stage 1/2/3
  ↓
understand semantic intent
  ↓
edit final file
  ↓
validate syntax/tests
  ↓
git add
  ↓
continue merge/rebase
```

### Best Practice
Resolve the desired final state, not merely 'pick ours' or 'pick theirs'.

---

## Advanced Deep Dive 5 — HEAD, Symbolic References, and Detached State

### Concept and Detailed Explanation
Normally HEAD is a symbolic reference to a branch, and the branch points to a commit. In detached HEAD, HEAD points directly to a commit. Commits made in detached state are valid objects, but they are not protected by a branch ref unless you create one.

### Internal / Architecture Model
```text
Normal:
HEAD → refs/heads/main → C

Detached:
HEAD → C

New detached commit:
HEAD → D
(no branch ref)
```

### Commands / Code / Configuration
```text
git symbolic-ref -q HEAD || echo "detached"
git rev-parse HEAD
git branch --show-current
git switch --detach HEAD~1
git switch -c rescue-work
```

### Expected State / Output
In detached state, `git branch --show-current` is empty; creating a branch anchors the current commit.

### Why It Works
References determine reachability and human navigation. A detached commit can eventually become unreachable if no ref/reflog protects it.

### Production Example
CI often checks out exact commit IDs in detached HEAD intentionally because it wants reproducible build input rather than a moving branch.

### Failure / Troubleshooting Workflow
```text
detached HEAD surprise
  ↓
git status
  ↓
did you create useful commits?
  ↓ yes
git switch -c <name>
  ↓
verify log
```

### Best Practice
Detached HEAD is not an error; understand whether it is intentional before 'fixing' it.

---

## Advanced Deep Dive 6 — Commit Identity vs Authentication

### Concept and Detailed Explanation
Git commit metadata contains author and committer names/emails, but those fields are not strong proof of real-world identity. Anyone can configure arbitrary author metadata. Provenance is strengthened through hosted identity controls, protected branches, signed commits/tags, CI attestations, and audit logs.

### Internal / Architecture Model
```text
Commit metadata:
author name/email
committer name/email
timestamp
message
      |
NOT cryptographic identity by itself

Stronger provenance:
signing + hosting auth + review + CI
```

### Commands / Code / Configuration
```text
git config user.name
git config user.email
git show --show-signature HEAD
git log --format='%h %an <%ae> %G? %s' -10
```

### Expected State / Output
You can distinguish ordinary identity metadata from a verified signature status.

### Why It Works
Git stores metadata supplied by the client; authenticity must come from additional trust mechanisms.

### Production Example
A security-sensitive IaC repository requires signed release tags and protected merge workflows rather than trusting email strings alone.

### Failure / Troubleshooting Workflow
```text
suspicious commit identity
  ↓
inspect hosting audit log
  ↓
signature status
  ↓
review/merge record
  ↓
CI provenance
  ↓
account/key ownership
```

### Best Practice
Treat commit metadata as attribution; use independent controls for authentication and approval.

---

## Advanced Deep Dive 7 — Object Reachability and Why Recovery Works

### Concept and Detailed Explanation
Git considers objects reachable when they can be traversed from a reference such as a branch, tag, or certain reflog entries. Deleting a branch usually removes the reference, not the commit objects immediately. This is why reflog and object inspection can recover recent work.

### Internal / Architecture Model
```text
refs → commits → trees → blobs
 |
reachable objects survive normal use

deleted ref
   |
commit may still be protected by reflog
   |
eventually eligible for pruning
```

### Commands / Code / Configuration
```text
git reflog --all
git fsck --unreachable
git fsck --lost-found
git branch recovery <commit-id>
```

### Expected State / Output
Recent deleted commits often appear in reflog or fsck output and can be re-anchored with a branch.

### Why It Works
Git garbage collection normally waits before pruning unreachable objects, giving a recovery window.

### Production Example
An engineer deletes a feature branch after a mistaken assumption that it was merged; reflog recovers the unmerged commit.

### Failure / Troubleshooting Workflow
```text
work appears lost
  ↓
STOP destructive commands
  ↓
git reflog --all
  ↓
git fsck --unreachable
  ↓
inspect candidate commit
  ↓
create recovery branch
```

### Best Practice
Create a recovery branch before experimenting further with a potentially lost commit.

---

## Advanced Deep Dive 8 — Reflog Semantics and Limits

### Concept and Detailed Explanation
Reflog records local movements of refs such as HEAD and branches. It is local to a repository clone and is not normally shared when pushing. It is therefore a powerful local recovery mechanism but not a substitute for pushing/backup.

### Internal / Architecture Model
```text
Local actions:
commit/reset/rebase/switch
        |
      reflog
        |
old HEAD / old branch tips

Remote collaborators do not automatically receive it.
```

### Commands / Code / Configuration
```text
git reflog
git reflog show main
git show HEAD@{3}
git branch recovery HEAD@{3}
```

### Expected State / Output
You can inspect previous local ref positions using time/index notation such as `HEAD@{3}`.

### Why It Works
Reflog tracks reference movements rather than repository-wide authoritative history.

### Production Example
A developer's local reflog can recover a reset commit that does not exist in another teammate's clone.

### Failure / Troubleshooting Workflow
```text
need old state
  ↓
which local ref moved?
  ↓
git reflog show <ref>
  ↓
inspect candidate
  ↓
anchor with branch/tag
```

### Best Practice
Do not rely on reflog as long-term backup; push or back up important history.

---

## Advanced Deep Dive 9 — Packfiles, Delta Compression, and Repository Size

### Concept and Detailed Explanation
Git may physically store many objects inside packfiles and delta-compress similar objects for efficiency. The logical object model remains unchanged. Large binary files can still cause repository growth because each changed binary version may be difficult to delta efficiently.

### Internal / Architecture Model
```text
Logical:
blob/tree/commit/tag objects
       |
packing / delta compression
       |
.git/objects/pack/*.pack
```

### Commands / Code / Configuration
```text
git count-objects -vH
git verify-pack -v .git/objects/pack/*.idx 2>/dev/null | head
git gc
```

### Expected State / Output
After normal maintenance, loose objects may be packed and repository storage becomes more efficient.

### Why It Works
Git separates logical object identity from physical storage representation.

### Production Example
Committing VM images or database dumps repeatedly can make clones extremely large despite garbage collection.

### Failure / Troubleshooting Workflow
```text
repo unexpectedly huge
  ↓
git count-objects -vH
  ↓
identify large historical blobs
  ↓
decide LFS/artifact storage/history cleanup
  ↓
coordinate rewrite if required
```

### Best Practice
Keep build artifacts, VM images, and database dumps out of ordinary Git history.

---

## Advanced Deep Dive 10 — Garbage Collection and Pruning Safety

### Concept and Detailed Explanation
Git maintenance packs objects and eventually removes unreachable objects according to expiration rules. Manual aggressive pruning can destroy the recovery window provided by reflogs/unreachable objects.

### Internal / Architecture Model
```text
Reachable objects → retained
Recent unreachable → often retained temporarily
Expired unreachable → eligible for prune
```

### Commands / Code / Configuration
```text
git gc
git reflog expire --dry-run --all
git prune --dry-run
```

### Expected State / Output
Dry-run commands show what could expire/prune without deleting objects.

### Why It Works
Git intentionally delays some cleanup because recently unreachable objects may represent recoverable mistakes.

### Production Example
Running aggressive prune immediately after a bad reset can remove commits that reflog recovery would otherwise save.

### Failure / Troubleshooting Workflow
```text
disk cleanup request
  ↓
verify backups
  ↓
inspect reachability/reflogs
  ↓
normal git maintenance first
  ↓
avoid aggressive prune during recovery incident
```

### Best Practice
Never run aggressive object cleanup while trying to recover lost work.

---

## Advanced Deep Dive 11 — Hash Algorithms and Object IDs

### Concept and Detailed Explanation
Git object IDs are content-derived identifiers. Older repositories traditionally use SHA-1 object IDs; newer Git supports transition mechanisms toward SHA-256 repositories. The operational principle remains the same: an object ID identifies exact content/object representation, not a mutable filename.

### Internal / Architecture Model
```text
object header + content
        |
       hash
        |
 object ID
        |
immutable object
```

### Commands / Code / Configuration
```text
git rev-parse --show-object-format 2>/dev/null || true
git hash-object README.md
git rev-parse HEAD^{tree}
```

### Expected State / Output
The repository reports its object format where supported and object IDs remain stable for unchanged objects.

### Why It Works
Content addressing enables integrity checks, deduplication, and immutable references.

### Production Example
A deployment manifest can record a commit ID to identify an exact infrastructure revision rather than 'whatever main points to later'.

### Failure / Troubleshooting Workflow
```text
unexpected object ID
  ↓
verify repository/object format
  ↓
verify exact object/content
  ↓
do not compare IDs from unrelated rewritten repositories blindly
```

### Best Practice
Use commit IDs as precise immutable references, but do not treat the hash algorithm alone as a full security-signature mechanism.

---

## Advanced Deep Dive 12 — Commit Graph Topology and First-Parent History

### Concept and Detailed Explanation
Git history is a directed acyclic graph, not a simple line. Merge commits have multiple parents. First-parent history follows the branch's integration path and is useful for understanding what was merged into a main/release branch.

### Internal / Architecture Model
```text
F1---F2
     /       A---B---C-----M---D
                ↑
               main

M parent1 = C
M parent2 = F2
```

### Commands / Code / Configuration
```text
git log --graph --oneline --decorate --all
git log --first-parent --oneline main
git show --pretty=raw <merge-commit>
```

### Expected State / Output
Full graph shows branch topology; first-parent view emphasizes integration commits on the main line.

### Why It Works
Merge commits preserve topology by recording both branch tips as parents.

### Production Example
Release notes may use first-parent history to list merged features without every intermediate feature-branch commit.

### Failure / Troubleshooting Workflow
```text
history looks duplicated/confusing
  ↓
draw graph
  ↓
inspect merge parents
  ↓
compare full vs first-parent history
```

### Best Practice
Choose log views based on the question you are answering.

---

## Advanced Deep Dive 13 — Merge Base as the Foundation of Integration

### Concept and Detailed Explanation
The merge base is the best common ancestor Git uses to determine what each side changed. Merges, three-dot diffs, and many rebases depend on this concept.

### Internal / Architecture Model
```text
F1---F2   feature
       /
A---B---C---D    main
    ↑
merge base may be B
```

### Commands / Code / Configuration
```text
git merge-base main feature
git diff $(git merge-base main feature)..feature
git diff main...feature
```

### Expected State / Output
The merge-base commit identifies the common starting snapshot for branch-change comparison.

### Why It Works
Git compares each branch against their common ancestor rather than merely comparing two tip snapshots without context.

### Production Example
A code review uses `main...feature` to show changes introduced by the feature since divergence.

### Failure / Troubleshooting Workflow
```text
unexpected review diff
  ↓
git merge-base main feature
  ↓
inspect branch tips
  ↓
check whether branch was rebased/merged recently
```

### Best Practice
Understand the merge base before interpreting three-dot diffs.

---

## Advanced Deep Dive 14 — Fast-Forward, No-FF, and Merge Commit Policy

### Concept and Detailed Explanation
A fast-forward merge moves a branch ref when the target history already contains the current branch tip as an ancestor. `--no-ff` forces a merge commit even when a fast-forward is possible, preserving an explicit integration event.

### Internal / Architecture Model
```text
Fast-forward:
A--B main
         C--D feature

main simply moves to D

--no-ff:
A--B------M main
    \    /
     C--D
```

### Commands / Code / Configuration
```text
git merge --ff-only feature
git merge --no-ff feature
git log --graph --oneline --decorate
```

### Expected State / Output
`--ff-only` fails if histories diverged; `--no-ff` creates an explicit merge commit for an otherwise fast-forwardable branch.

### Why It Works
Merge policy controls the topology and audit shape of history.

### Production Example
A regulated infrastructure repository may prefer reviewed merge commits that correspond to approved change requests.

### Failure / Troubleshooting Workflow
```text
merge policy failure
  ↓
what topology is required?
  ↓
can fast-forward?
  ↓
protected-branch/hosting policy?
  ↓
integrate using approved method
```

### Best Practice
Document merge policy instead of letting every contributor choose a different history style.

---

## Advanced Deep Dive 15 — Squash Merge Semantics

### Concept and Detailed Explanation
A squash merge applies the combined diff from a branch but does not make the feature commits ancestors of the target branch. This produces a single clean integration commit but changes how later merges and history analysis behave.

### Internal / Architecture Model
```text
Feature:
A--B--C--D

Squash to main:
A--S
   |
S contains combined B+C+D changes
but B/C/D are not parents of S
```

### Commands / Code / Configuration
```text
git switch main
git merge --squash feature
git commit -m "Add feature"
git log --graph --oneline --all
```

### Expected State / Output
The main branch gets one new commit containing the feature result, while the original feature commits remain separate history.

### Why It Works
Squash merges copy the net change rather than recording a merge relationship.

### Production Example
A team uses squash merge so each pull request becomes one revertible commit on main.

### Failure / Troubleshooting Workflow
```text
feature later reused/merged
  ↓
remember squash did not record ancestry
  ↓
inspect diff/merge-base
  ↓
avoid assuming Git knows branch was merged
```

### Best Practice
Use squash merge intentionally when PR-level atomic history is more valuable than preserving branch ancestry.

---

## Advanced Deep Dive 16 — Three-Way Merge Conflict Resolution as Semantic Work

### Concept and Detailed Explanation
A merge conflict is not simply a text-formatting problem. Git can tell that two branches changed overlapping content, but only the engineer understands which resulting configuration is valid. Correct conflict resolution must therefore combine Git history, application semantics, tests, and deployment intent.

For infrastructure repositories, a syntactically resolved file can still be operationally dangerous.

### Internal / Architecture Model
```text
BASE
  |
  +-- OURS
  |
  +-- THEIRS

Git detects incompatible overlap
        |
Human resolves intended final state
        |
syntax / policy / functional validation
```

### Commands / Code / Configuration
```text
git status
git diff --cc
git show :1:config.yml
git show :2:config.yml
git show :3:config.yml

# After editing:
yamllint config.yml 2>/dev/null || true
git add config.yml
git diff --cached
```

### Expected State / Output
The conflict markers disappear, the index contains the intended resolved file, and validation confirms the configuration is still valid.

### Why It Works
Git can combine text but cannot know application policy, security constraints, or deployment dependencies.

### Production Example
Two teams change the same firewall policy file. A naïve resolution keeps both rules and accidentally permits an overly broad network range.

### Failure / Troubleshooting Workflow
```text
conflict
  ↓
inspect base / ours / theirs
  ↓
understand both business intents
  ↓
produce final state
  ↓
validate syntax
  ↓
run policy/tests
  ↓
stage and continue
```

### Best Practice
Treat conflict resolution as design review, especially for infrastructure and security configuration.

---

## Advanced Deep Dive 17 — `git rerere` and Repeated Conflict Reuse

### Concept and Detailed Explanation
`rerere` means 'reuse recorded resolution.' When enabled, Git can remember how you resolved a conflict and automatically reuse that resolution when the same conflict appears again.

This is useful in long-running rebases or maintenance branches, but automatic reuse still requires review because surrounding context may have changed.

### Internal / Architecture Model
```text
Conflict A
  ↓
human resolution
  ↓
rerere records preimage/postimage
  ↓
same conflict appears later
  ↓
Git reuses candidate resolution
```

### Commands / Code / Configuration
```text
git config rerere.enabled true
git rerere status
git rerere diff
```

### Expected State / Output
After resolving a repeated conflict, Git can pre-apply the recorded resolution instead of requiring identical manual work.

### Why It Works
Conflict patterns can recur when replaying or repeatedly integrating the same patch series.

### Production Example
A release-maintenance branch repeatedly receives the same security patch and conflicts with a vendor customization; rerere saves the known resolution.

### Failure / Troubleshooting Workflow
```text
rerere auto-resolution appears
  ↓
review diff
  ↓
run tests
  ↓
confirm context still valid
  ↓
stage/continue
```

### Best Practice
Use rerere to reduce repetitive work, never to skip validation.

---

## Advanced Deep Dive 18 — Rebase as Commit Replay

### Concept and Detailed Explanation
Rebase does not physically move existing commits. It identifies a set of commits, computes their changes, and creates new commits on a new base. New parent relationships mean new commit IDs.

This is why rebasing shared history forces collaborators to reconcile two lineages containing similar patches but different commit identities.

### Internal / Architecture Model
```text
Before:
A--B--C main
         D--E feature

Rebase feature onto C:
A--B--C--D'--E'

D' and E' are new commits
```

### Commands / Code / Configuration
```text
git switch feature
git log --oneline --graph --all
git rebase main
git range-diff main@{1}..feature@{1} main..feature 2>/dev/null || true
```

### Expected State / Output
The rebased branch has equivalent intended changes but different commit IDs and new parents.

### Why It Works
Commit identity includes the parent relationship, so changing the base necessarily changes the commit object.

### Production Example
A feature branch is rebased onto the latest main before review so the final history is linear and conflicts are solved once by the feature owner.

### Failure / Troubleshooting Workflow
```text
rebase surprise
  ↓
git status
  ↓
git reflog
  ↓
identify old branch tip
  ↓
compare with range-diff/log
  ↓
abort or continue deliberately
```

### Best Practice
Rebase local/unpublished work freely; coordinate before rewriting history that others consume.

---

## Advanced Deep Dive 19 — Interactive Rebase as Local History Editing

### Concept and Detailed Explanation
Interactive rebase is a controlled way to rewrite unpublished commits. It can reorder, combine, edit, drop, or reword commits. The goal is not cosmetic perfection; it is to produce a reviewable series where each commit represents a coherent, testable change.

### Internal / Architecture Model
```text
WIP commits:
A--B--C--D--E

Interactive plan:
pick B
fixup C
reword D
drop E

Result:
A--B'--D'
```

### Commands / Code / Configuration
```text
git log --oneline -6
git rebase -i HEAD~4

# Common todo actions:
# pick
# reword
# edit
# squash
# fixup
# drop
```

### Expected State / Output
The resulting local history contains fewer, clearer commits with new IDs.

### Why It Works
Interactive rebase reconstructs selected commits according to the todo plan.

### Production Example
A Terraform change contains separate commits for formatting, a variable rename, and the actual security-group change; the author combines noise before review.

### Failure / Troubleshooting Workflow
```text
interactive rebase wrong
  ↓
git rebase --abort if still active
  ↓
otherwise git reflog
  ↓
find pre-rebase tip
  ↓
create recovery branch
```

### Best Practice
Create a backup branch before complex history surgery if the work is valuable.

---

## Advanced Deep Dive 20 — Rebase `--onto` for Surgical History Repair

### Concept and Detailed Explanation
`git rebase --onto` lets you replay a chosen commit range onto a different base. It is useful when a branch was created from the wrong branch or when one subseries should be moved without replaying unrelated commits.

### Internal / Architecture Model
```text
Wrong:
main -- A
               feature-base -- B -- C  feature

Desired:
main -- A -- B' -- C'
```

### Commands / Code / Configuration
```text
# Generic form:
git rebase --onto <new-base> <old-base> <branch>

# Inspect first:
git log --graph --oneline --decorate --all
```

### Expected State / Output
Only commits after `<old-base>` on the selected branch are replayed onto `<new-base>`.

### Why It Works
Rebase selects a commit set and gives those changes a new parent chain.

### Production Example
A security hotfix branch accidentally started from an experimental feature branch; `--onto` extracts only the hotfix commits onto the production release branch.

### Failure / Troubleshooting Workflow
```text
need surgical move
  ↓
draw graph
  ↓
identify new base
  ↓
identify old base/exclusion point
  ↓
create backup branch
  ↓
rebase --onto
  ↓
range-diff/test
```

### Best Practice
Never use `--onto` until you can draw exactly which commits will be selected.

---

## Advanced Deep Dive 21 — Cherry-Pick and Duplicate Patch Identity

### Concept and Detailed Explanation
Cherry-pick applies the change introduced by an existing commit onto the current branch and creates a new commit with a different parent and therefore a different ID. The patch may be equivalent, but Git sees two different commits.

This is useful for isolated backports but dangerous as a general synchronization strategy because repeated cherry-picks can create duplicate-history confusion.

### Internal / Architecture Model
```text
main:
A--B--SECURITY_FIX

release:
A--R1
           SECURITY_FIX'  ← cherry-picked patch
```

### Commands / Code / Configuration
```text
git show <commit>
git switch release/1.0
git cherry-pick <commit>
git log --cherry --oneline main...release/1.0
```

### Expected State / Output
The release branch receives an equivalent patch as a new commit.

### Why It Works
Commit identity depends on parent/history context, not only the textual diff.

### Production Example
A critical SSH hardening fix from main is backported to a supported older release branch without merging unrelated development.

### Failure / Troubleshooting Workflow
```text
cherry-pick conflict
  ↓
inspect commit intent
  ↓
resolve against release context
  ↓
run release-specific tests
  ↓
git cherry-pick --continue
  ↓
or --abort
```

### Best Practice
Use cherry-pick for deliberate isolated backports, not as a substitute for a coherent branching strategy.

---

## Advanced Deep Dive 22 — Remote-Tracking References Are Local Observations

### Concept and Detailed Explanation
`origin/main` is not the remote branch itself. It is a local remote-tracking ref recording what your repository last learned about the remote through fetch/push. It can become stale.

This explains why `git fetch` is a safe diagnostic step: it updates your knowledge without integrating it into your current branch.

### Internal / Architecture Model
```text
Remote server:
refs/heads/main → R

Local clone:
refs/heads/main → L
refs/remotes/origin/main → last fetched R
```

### Commands / Code / Configuration
```text
git remote -v
git branch -vv
git fetch origin
git log --oneline --left-right main...origin/main
```

### Expected State / Output
After fetch, `origin/main` reflects the current remote state while local `main` remains unchanged.

### Why It Works
Git separates communication from integration: fetch transfers objects/refs; merge/rebase changes local branch topology.

### Production Example
Before repairing a rejected push, an engineer fetches and inspects exact local/remote divergence instead of blindly pulling.

### Failure / Troubleshooting Workflow
```text
push rejected
  ↓
git fetch origin
  ↓
compare main...origin/main
  ↓
understand divergence
  ↓
merge/rebase as policy requires
  ↓
push
```

### Best Practice
Fetch first, inspect second, integrate third.

---

## Advanced Deep Dive 23 — Upstream Tracking Configuration

### Concept and Detailed Explanation
A local branch can record an upstream branch used by status, pull, push defaults, and ahead/behind calculations. Tracking is metadata; it does not make branches automatically identical.

### Internal / Architecture Model
```text
local feature/api
       |
tracks
       v
origin/feature/api
```

### Commands / Code / Configuration
```text
git branch -vv
git rev-parse --abbrev-ref --symbolic-full-name @{u}
git push -u origin feature/api
git branch --set-upstream-to=origin/main local-main 2>/dev/null || true
```

### Expected State / Output
`git status` can report the branch's divergence relative to its configured upstream.

### Why It Works
Git uses branch configuration such as `branch.<name>.remote` and `.merge` to infer defaults.

### Production Example
A renamed remote branch leaves a local branch tracking a deleted upstream; `git branch -vv` reveals `[gone]`.

### Failure / Troubleshooting Workflow
```text
pull/push targets wrong branch
  ↓
git branch -vv
  ↓
inspect @{u}
  ↓
fix upstream
  ↓
fetch and verify divergence
```

### Best Practice
Verify upstream metadata after branch renames or repository migrations.

---

## Advanced Deep Dive 24 — Pull Strategies and Explicit Integration

### Concept and Detailed Explanation
`git pull` combines fetch with an integration policy. Depending on configuration it may merge, rebase, or refuse non-fast-forward integration. Teams should configure this intentionally to avoid surprising history.

### Internal / Architecture Model
```text
git pull
   |
 fetch
   |
 integration policy:
 merge?
 rebase?
 ff-only?
```

### Commands / Code / Configuration
```text
git config --show-origin --get pull.rebase
git config --show-origin --get pull.ff

git pull --ff-only
git pull --rebase
```

### Expected State / Output
`--ff-only` refuses divergence; `--rebase` replays local commits when appropriate; default behavior follows configuration.

### Why It Works
Fetch and integration are distinct operations even when the convenience command combines them.

### Production Example
A release branch is configured `pull.ff=only` so accidental local merge commits cannot appear during synchronization.

### Failure / Troubleshooting Workflow
```text
pull unexpected
  ↓
git status
  ↓
inspect pull.rebase / pull.ff
  ↓
git reflog if history changed
  ↓
restore desired topology
```

### Best Practice
Prefer explicit pull policy, especially on protected or release branches.

---

## Advanced Deep Dive 25 — Non-Fast-Forward Push Rejection as Data Protection

### Concept and Detailed Explanation
A normal push is rejected when updating the remote ref would discard commits that the remote currently contains. This is a safety feature, not a network error.

### Internal / Architecture Model
```text
Remote:
A--B--C

Local:
A--B--D

Setting remote main → D
would drop C
→ normal push rejected
```

### Commands / Code / Configuration
```text
git fetch origin
git log --graph --oneline --decorate --all
git log --left-right --cherry-pick main...origin/main
```

### Expected State / Output
The push remains rejected until histories are integrated or an authorized history rewrite is performed.

### Why It Works
Git requires the remote's current commit to be an ancestor of the proposed new tip for a fast-forward update.

### Production Example
Two engineers publish independent infrastructure changes; the second push is rejected, preventing the first engineer's approved change from being overwritten.

### Failure / Troubleshooting Workflow
```text
non-fast-forward
  ↓
fetch
  ↓
draw graph
  ↓
integrate remote changes
  ↓
test
  ↓
push again
```

### Best Practice
Never solve non-fast-forward rejection with force until you understand which remote commits would disappear.

---

## Advanced Deep Dive 26 — `--force-with-lease` and Optimistic Concurrency

### Concept and Detailed Explanation
`--force-with-lease` is safer than `--force` because it rewrites the remote only if the remote ref is still at the value your clone expects. It behaves like an optimistic concurrency check.

It does not make history rewriting universally safe; collaborators can still have based work on the old history.

### Internal / Architecture Model
```text
Expected remote:
origin/feature → C

You want:
feature → C'

Push with lease:
if remote still C → update
if remote changed to D → reject
```

### Commands / Code / Configuration
```text
git fetch origin
git log --graph --oneline --decorate --all
git push --force-with-lease origin feature
```

### Expected State / Output
The forced update succeeds only when the remote ref matches the expected old value.

### Why It Works
The lease protects against overwriting a remote change you have not observed.

### Production Example
After rebasing a personal review branch, an engineer uses force-with-lease so a reviewer's newly pushed fix is not silently deleted.

### Failure / Troubleshooting Workflow
```text
lease rejected
  ↓
STOP
  ↓
fetch
  ↓
inspect new remote commits
  ↓
integrate/coordinate
  ↓
retry only if rewrite still intended
```

### Best Practice
Use force-with-lease only on branches whose rewrite policy is explicitly allowed.

---

## Advanced Deep Dive 27 — Remote Refspecs

### Concept and Detailed Explanation
A refspec maps source refs to destination refs during fetch or push. Most daily Git use hides this detail, but understanding it explains how branch names map, why remote-tracking refs live under `refs/remotes/`, and how advanced mirroring works.

### Internal / Architecture Model
```text
Fetch refspec:
+refs/heads/*:refs/remotes/origin/*

Remote branch main
        ↓
local refs/remotes/origin/main
```

### Commands / Code / Configuration
```text
git config --get-all remote.origin.fetch
git fetch origin main:refs/remotes/origin/main
git show-ref
```

### Expected State / Output
The configured fetch refspec shows which remote refs are copied into which local namespace.

### Why It Works
Git transfers objects and then updates refs according to explicit mapping rules.

### Production Example
A repository mirror intentionally fetches more namespaces than a normal developer clone.

### Failure / Troubleshooting Workflow
```text
branch not appearing after fetch
  ↓
inspect remote refs
  ↓
inspect fetch refspec
  ↓
verify namespace mapping
```

### Best Practice
Do not customize refspecs in ordinary repositories unless the workflow requires it.

---

## Advanced Deep Dive 28 — Remote Pruning and Deleted Branch Hygiene

### Concept and Detailed Explanation
Deleting a branch on the remote does not immediately remove the corresponding remote-tracking ref from every clone. Pruning removes stale remote-tracking refs so the local view matches remote branch existence more accurately.

### Internal / Architecture Model
```text
Remote:
feature deleted

Local before prune:
origin/feature still exists

After prune:
stale ref removed
```

### Commands / Code / Configuration
```text
git fetch --prune origin
git remote prune origin --dry-run
git branch -r
git branch -vv
```

### Expected State / Output
Stale remote-tracking refs disappear while local branches remain unless explicitly deleted.

### Why It Works
Remote-tracking refs are local cache entries that require update/prune.

### Production Example
An old `origin/feature` causes a teammate to believe a branch is still active months after it was merged and deleted.

### Failure / Troubleshooting Workflow
```text
stale branch confusion
  ↓
git fetch --prune
  ↓
inspect remote branches
  ↓
inspect local branches/upstreams
```

### Best Practice
Enable pruning if your team frequently deletes short-lived remote branches.

---

## Advanced Deep Dive 29 — Multiple Remotes and Trust Boundaries

### Concept and Detailed Explanation
A repository can use several remotes: origin, upstream, backup, deployment mirror, or read-only vendor source. Every remote represents a destination/source trust boundary. Pushing to the wrong remote can expose sensitive code or publish history unexpectedly.

### Internal / Architecture Model
```text
upstream
             ↑
             |
local repo → origin
             |
             → backup

Each URL has different ownership/access.
```

### Commands / Code / Configuration
```text
git remote -v
git remote get-url --all origin
git remote show origin
git push --dry-run origin main
```

### Expected State / Output
Each remote URL and push destination is explicit and reviewed before sensitive changes are published.

### Why It Works
Git has no intrinsic understanding of which remote is confidential or authoritative.

### Production Example
An engineer clones a public upstream and accidentally configures the company's private fork as the wrong push target.

### Failure / Troubleshooting Workflow
```text
before sensitive push
  ↓
git remote -v
  ↓
verify repository ownership/classification
  ↓
dry-run or protected workflow
  ↓
push
```

### Best Practice
Inspect remote URLs before publishing secrets, proprietary code, or security-sensitive infrastructure.

---

## Advanced Deep Dive 30 — Repository Migration Without Losing Intent

### Concept and Detailed Explanation
Moving a repository between hosting platforms requires more than copying the latest files. Branches, tags, Git LFS objects, submodules, issues, pull requests, branch rules, CI secrets, webhooks, and signing/trust configuration may all need separate migration.

### Internal / Architecture Model
```text
Git objects/refs
  +
hosting metadata:
PRs
issues
rules
CI
secrets
webhooks
LFS
  |
migration plan
```

### Commands / Code / Configuration
```text
git clone --mirror <old-url> repo.git
cd repo.git
git remote set-url --push origin <new-url>
git push --mirror

# Review carefully before using --mirror against a destination.
```

### Expected State / Output
Git refs can be copied completely, while hosting-platform metadata is handled by a separate documented migration process.

### Why It Works
A normal clone contains repository history but not all provider-specific collaboration state.

### Production Example
After migration, code exists but branch protection and required CI checks are missing, allowing direct production changes.

### Failure / Troubleshooting Workflow
```text
migration
  ↓
inventory refs/tags/LFS/submodules
  ↓
inventory hosting metadata
  ↓
test destination
  ↓
freeze/cutover
  ↓
validate permissions/rules/CI
```

### Best Practice
Treat repository hosting migration as a platform migration, not a file copy.

---

## Advanced Deep Dive 31 — `.gitignore` Matching Semantics

### Concept and Detailed Explanation
`.gitignore` uses path-pattern rules that are often misunderstood. Patterns can match names anywhere, paths relative to the ignore file, directory-only patterns, negation rules, and wildcards. Importantly, ignore rules apply to untracked content; they do not automatically untrack files already committed.

### Internal / Architecture Model
```text
Working tree path
   |
already tracked?
  / yes  no
 |    |
ignore does not   evaluate .gitignore
remove tracking       |
                   ignored or visible
```

### Commands / Code / Configuration
```text
git status --ignored
git check-ignore -v path/to/file
git ls-files path/to/file
```

### Expected State / Output
`git check-ignore -v` identifies the exact ignore rule that matched a path.

### Why It Works
Git decides whether to show untracked paths using layered ignore patterns from repository and local configuration.

### Production Example
A `.env` file remains in history after being added to `.gitignore` because it was already tracked.

### Failure / Troubleshooting Workflow
```text
file unexpectedly tracked/visible
  ↓
git ls-files <path>
  ↓
git check-ignore -v <path>
  ↓
if tracked and should not be:
git rm --cached <path>
  ↓
commit policy change
```

### Best Practice
Use `git check-ignore -v` instead of guessing why a pattern behaves differently.

---

## Advanced Deep Dive 32 — Ignore Rules vs Security Controls

### Concept and Detailed Explanation
Ignore files are convenience filters, not secret-management controls. A developer can still explicitly add an ignored file with force, and previously tracked secrets remain in history.

Secret protection requires secret stores, CI scanning, pre-commit detection, review, credential rotation, and server-side policy.

### Internal / Architecture Model
```text
.gitignore
   |
reduces accidental staging

Security controls:
secret manager
scanner
CI/server policy
credential rotation
```

### Commands / Code / Configuration
```text
git add -f .env   # demonstrates ignore can be overridden
git grep -nE 'password|token|secret' -- . ':!examples'
```

### Expected State / Output
Teams understand that ignored paths can still be committed and do not rely on ignore patterns as the only safeguard.

### Why It Works
Gitignore affects path discovery, not authorization or content classification.

### Production Example
A developer force-adds an ignored kubeconfig containing a live credential.

### Failure / Troubleshooting Workflow
```text
secret committed
  ↓
assume exposed
  ↓
rotate/revoke
  ↓
remove current copy
  ↓
scan history
  ↓
history cleanup if required
```

### Best Practice
Design secret handling so the real secret never needs to exist in tracked form.

---

## Advanced Deep Dive 33 — `.gitattributes` and Repository-Wide Normalization

### Concept and Detailed Explanation
`.gitattributes` defines path-specific Git behavior such as text normalization, end-of-line policy, binary classification, merge drivers, and diff drivers. Unlike individual developer settings, it travels with the repository and therefore helps enforce consistent behavior.

### Internal / Architecture Model
```text
Repository policy:
.gitattributes
   |
checkout on Windows/Linux
   |
consistent normalized Git content
   |
platform-specific working-tree EOL when specified
```

### Commands / Code / Configuration
```text
git check-attr -a -- scripts/deploy.sh
git ls-files --eol

# Example:
# * text=auto
# *.sh text eol=lf
# *.ps1 text eol=crlf
```

### Expected State / Output
Git reports the intended text/EOL attributes and avoids whole-file line-ending churn.

### Why It Works
Git stores normalized content while applying working-tree conversion according to attributes.

### Production Example
A mixed Linux/Windows operations team stops seeing 500-line diffs caused only by CRLF/LF conversion.

### Failure / Troubleshooting Workflow
```text
whole file appears changed
  ↓
git diff --ignore-space-at-eol
  ↓
git ls-files --eol
  ↓
git check-attr
  ↓
fix attributes
  ↓
renormalize deliberately
```

### Best Practice
Store line-ending policy in `.gitattributes`, not only in developer-specific `core.autocrlf` settings.

---

## Advanced Deep Dive 34 — Renormalization After Attribute Changes

### Concept and Detailed Explanation
When line-ending or text attributes are introduced to an existing repository, existing index content may not immediately reflect the new policy. A deliberate renormalization commit can rewrite tracked content into the intended normalized representation.

### Internal / Architecture Model
```text
Old history:
mixed EOL

Add .gitattributes
   |
git add --renormalize .
   |
one deliberate normalization commit
   |
future diffs cleaner
```

### Commands / Code / Configuration
```text
git status
git add .gitattributes
git add --renormalize .
git diff --cached --stat
git diff --cached
```

### Expected State / Output
The normalization changes are isolated in a dedicated commit and later feature changes are easier to review.

### Why It Works
Attributes affect how Git interprets content at index/working-tree boundaries.

### Production Example
A team introduces LF policy for shell scripts and isolates the mechanical change before making functional edits.

### Failure / Troubleshooting Workflow
```text
normalization diff huge
  ↓
ensure no functional edits mixed in
  ↓
review attributes
  ↓
commit normalization separately
  ↓
rebase feature work if needed
```

### Best Practice
Never combine repository-wide EOL normalization with application logic changes.

---

## Advanced Deep Dive 35 — Executable Bit Tracking

### Concept and Detailed Explanation
Git tracks a limited set of file-mode information, most notably the executable bit on supported platforms. A script whose content is correct can still fail deployment if the executable bit is missing.

### Internal / Architecture Model
```text
Tree entry:
100644 → normal file
100755 → executable file

content blob may be identical
but tree mode differs
```

### Commands / Code / Configuration
```text
git ls-files --stage scripts/deploy.sh
chmod +x scripts/deploy.sh
git diff --summary
git update-index --chmod=+x scripts/deploy.sh
```

### Expected State / Output
The tree entry changes from a non-executable to executable mode without needing content changes.

### Why It Works
Git trees store both object ID and path mode.

### Production Example
A Linux deployment pipeline checks out a shell script that cannot execute because a Windows contributor created it without preserving executable mode.

### Failure / Troubleshooting Workflow
```text
script permission issue
  ↓
git ls-files --stage
  ↓
working-tree permissions
  ↓
filesystem/core.fileMode behavior
  ↓
commit mode fix
```

### Best Practice
Treat executable-bit changes as real reviewable repository changes.

---

## Advanced Deep Dive 36 — Git LFS and Large Binary Pointers

### Concept and Detailed Explanation
Git LFS replaces large tracked file content with small pointer files in the normal Git object graph while storing actual binaries in a separate LFS object service. This improves repository behavior for selected large assets but adds a second storage/authentication dependency.

### Internal / Architecture Model
```text
Git repository:
pointer text file
  |
oid + size
  |
Git LFS server
  |
large binary content
```

### Commands / Code / Configuration
```text
git lfs install 2>/dev/null || true
git lfs track "*.bin" 2>/dev/null || true
git lfs ls-files 2>/dev/null || true
cat .gitattributes
```

### Expected State / Output
Large-file paths are represented by LFS pointers in Git and fetched from the configured LFS service.

### Why It Works
Normal Git history is optimized for source/text objects, while LFS separates large binary transfer/storage.

### Production Example
A machine-learning repository tracks model artifacts with LFS instead of putting multi-gigabyte binaries in every clone's ordinary Git history.

### Failure / Troubleshooting Workflow
```text
LFS file missing
  ↓
is git-lfs installed?
  ↓
LFS endpoint/auth?
  ↓
pointer present?
  ↓
object uploaded?
  ↓
fetch LFS object
```

### Best Practice
Use LFS only when the hosting/backup/CI environment supports its additional object store.

---

## Advanced Deep Dive 37 — History Rewriting for Secret Cleanup

### Concept and Detailed Explanation
Removing a secret from the current branch tip does not remove it from historical objects. History-rewriting tools can remove paths or replace content, but rewriting is secondary to credential rotation because anyone may already have cloned the old secret.

History rewrite also changes commit IDs and requires coordinated force updates and clone cleanup.

### Internal / Architecture Model
```text
Secret committed
   |
ROTATE / REVOKE FIRST
   |
remove current use
   |
rewrite history if policy requires
   |
force-update refs
   |
collaborators re-clone/rebase carefully
```

### Commands / Code / Configuration
```text
# Conceptual modern workflow often uses git-filter-repo if installed:
git filter-repo --path path/to/secret --invert-paths 2>/dev/null || true

# Verify:
git log --all -- path/to/secret
git grep <FAKE_SECRET_PATTERN> $(git rev-list --all) 2>/dev/null || true
```

### Expected State / Output
The credential is invalidated independently of repository cleanup; rewritten refs no longer expose the unwanted historical path/content where the cleanup covered all relevant refs.

### Why It Works
A Git rewrite cannot recall secret copies from developer clones, CI caches, logs, or mirrors.

### Production Example
A cloud API key is accidentally committed. Security revokes it immediately, then the repository is cleaned to reduce future exposure.

### Failure / Troubleshooting Workflow
```text
secret incident
  ↓
revoke/rotate
  ↓
identify all refs/tags
  ↓
rewrite in isolated clone
  ↓
verify
  ↓
coordinate push/re-clone
  ↓
scan mirrors/caches
```

### Best Practice
Credential revocation is the incident response; history rewriting is repository hygiene.

---

## Advanced Deep Dive 38 — Commit and Tag Signing Models

### Concept and Detailed Explanation
Git can sign commits/tags using supported signing mechanisms such as GPG or SSH-based signing, depending on organizational setup. A valid signature proves that the object was signed by a private key corresponding to a trusted public identity; it does not prove the code is correct or reviewed.

### Internal / Architecture Model
```text
Commit / Tag
   |
cryptographic signature
   |
trusted public key / identity mapping
   |
verified provenance

Still requires:
review + CI + authorization
```

### Commands / Code / Configuration
```text
git config --get user.signingkey
git log --show-signature -5
git tag -v v1.0.0 2>/dev/null || true
```

### Expected State / Output
Signed objects display signature verification when the verifier has the required trust/key configuration.

### Why It Works
Signatures protect provenance/integrity of the signed object, not semantic safety.

### Production Example
A release pipeline accepts only signed release tags created by a controlled release key after CI approval.

### Failure / Troubleshooting Workflow
```text
signature invalid/unknown
  ↓
object changed?
  ↓
signer key available?
  ↓
trust mapping correct?
  ↓
key expired/revoked?
  ↓
hosting verification policy?
```

### Best Practice
Use signing as one layer in a broader trusted-release process.

---

## Advanced Deep Dive 39 — SSH Host Keys and Git Remote Trust

### Concept and Detailed Explanation
SSH authentication has two directions of trust: the server authenticates the client key, and the client should verify the server's host key. Ignoring changed host-key warnings can expose Git credentials or code to a man-in-the-middle endpoint.

### Internal / Architecture Model
```text
Developer
  |
client private key → server authenticates user
  |
server host key → client authenticates server
  |
Git SSH endpoint
```

### Commands / Code / Configuration
```text
ssh -T git@example.com
ssh-keygen -F example.com
ssh -G git@example.com | head
```

### Expected State / Output
SSH connects only when the client trusts the expected server identity and the server accepts the authorized user key.

### Why It Works
Public-key authentication does not help if the client sends credentials/data to an impersonated server.

### Production Example
A corporate Git host is rebuilt and its legitimate host key changes; the team verifies the new fingerprint through a trusted channel rather than deleting warnings blindly.

### Failure / Troubleshooting Workflow
```text
HOST IDENTIFICATION HAS CHANGED
  ↓
STOP
  ↓
verify DNS/network
  ↓
obtain trusted fingerprint
  ↓
compare
  ↓
update known_hosts only after validation
```

### Best Practice
Treat SSH host-key changes as security events until independently verified.

---

## Advanced Deep Dive 40 — Credential Helpers and Token Storage

### Concept and Detailed Explanation
HTTPS Git workflows often rely on credential helpers or OS keychains to store access tokens. Plaintext tokens in shell scripts, remote URLs, environment dumps, or shell history are easier to leak.

### Internal / Architecture Model
```text
Git
  |
credential helper
  |
OS keychain / secure store
  |
HTTPS hosting service
```

### Commands / Code / Configuration
```text
git config --show-origin --get-all credential.helper
git remote get-url origin

# Inspect configuration; do not print actual secrets.
```

### Expected State / Output
Authentication occurs without embedding the secret in the remote URL or repository files.

### Why It Works
Credential helpers move secret storage into a system designed for credential lifecycle rather than ordinary text configuration.

### Production Example
A token in `https://token@host/repo.git` leaks into screenshots and process/debug output.

### Failure / Troubleshooting Workflow
```text
HTTPS auth failure
  ↓
remote URL
  ↓
credential helper
  ↓
token expiry/scope
  ↓
SSO policy
  ↓
rotate/re-authenticate
```

### Best Practice
Use short-lived/scoped tokens and platform credential storage where possible.

---

## Advanced Deep Dive 41 — `safe.directory` and Repository Ownership Security

### Concept and Detailed Explanation
Git can refuse to operate on a repository owned by another user in security-sensitive ownership scenarios. The `safe.directory` mechanism exists to reduce attacks where an untrusted repository owner controls configuration/hooks while a privileged user runs Git.

### Internal / Architecture Model
```text
Privileged user
  |
opens repo owned by another identity
  |
Git ownership safety check
  |
refuse unless explicitly trusted
```

### Commands / Code / Configuration
```text
git config --show-origin --get-all safe.directory
git status
```

### Expected State / Output
Git warns/refuses in suspicious ownership contexts rather than automatically trusting every filesystem repository.

### Why It Works
Repository-local configuration and hooks can influence Git behavior, so trust in repository ownership matters.

### Production Example
An administrator runs Git as root inside a directory writable by an unprivileged service account; ownership protections reduce risk.

### Failure / Troubleshooting Workflow
```text
dubious ownership warning
  ↓
verify actual owner/path
  ↓
why are you using another user's repo?
  ↓
fix ownership if wrong
  ↓
add narrow safe.directory only if intentionally trusted
```

### Best Practice
Do not solve ownership warnings by globally trusting `*` without understanding the security boundary.

---

## Advanced Deep Dive 42 — Hooks as Local Automation, Not Central Enforcement

### Concept and Detailed Explanation
Git hooks can run linting, formatting, secret checks, commit-message validation, or deployment logic at lifecycle events. Client-side hooks live outside normal committed history by default and can often be bypassed, so important policy must also exist in CI/server controls.

### Internal / Architecture Model
```text
Developer action
   |
local hook
   |
fast feedback

Authoritative policy
   |
CI / server-side checks
   |
merge decision
```

### Commands / Code / Configuration
```text
ls .git/hooks
git config --get core.hooksPath

# Example shared hooks path:
git config core.hooksPath .githooks
```

### Expected State / Output
Local hooks provide fast feedback while CI remains the enforceable source of policy.

### Why It Works
Local developer environments are not centrally trusted enforcement points.

### Production Example
A pre-commit secret scanner is bypassed with `--no-verify`, but the CI secret-scanning job still blocks the pull request.

### Failure / Troubleshooting Workflow
```text
hook not running
  ↓
hook path?
  ↓
executable bit?
  ↓
interpreter?
  ↓
bypassed?
  ↓
CI equivalent present?
```

### Best Practice
Use hooks for developer ergonomics; enforce critical controls independently.

---

## Advanced Deep Dive 43 — CODEOWNERS and Review Routing

### Concept and Detailed Explanation
Hosted Git platforms can use ownership rules to automatically request reviewers for paths. Although CODEOWNERS is a hosting feature rather than core Git behavior, it turns repository structure into a review-control model.

For infrastructure, network, security, and production paths may require different experts.

### Internal / Architecture Model
```text
infra/network/** → Network Team
infra/security/** → Security Team
ansible/prod/**   → Platform Team

Change
  ↓
automatic reviewer routing
  ↓
required approvals
```

### Commands / Code / Configuration
```text
# Conceptual CODEOWNERS examples:
# /network/ @network-team
# /security/ @security-team
# /prod/ @platform-ops
```

### Expected State / Output
Changes to sensitive paths automatically involve the appropriate reviewers when the hosting platform enforces those rules.

### Why It Works
Repository paths become policy boundaries for review ownership.

### Production Example
A developer changes a production firewall file and the platform automatically requires network-security approval.

### Failure / Troubleshooting Workflow
```text
review not requested
  ↓
path pattern correct?
  ↓
CODEOWNERS branch/location?
  ↓
team access valid?
  ↓
branch rule requires owner approval?
```

### Best Practice
Use CODEOWNERS together with protected-branch rules; ownership suggestions alone are not enforcement.

---

## Advanced Deep Dive 44 — Protected Branches and Server-Side Rules

### Concept and Detailed Explanation
Protected branches can prohibit direct pushes, force pushes, branch deletion, or merges without required reviews and status checks. These controls exist on the hosting platform, not in the Git object model itself.

### Internal / Architecture Model
```text
feature branch
  ↓
pull request
  ↓
review
  ↓
CI checks
  ↓
server-side branch rule
  ↓
main
```

### Commands / Code / Configuration
```text
Policy checklist:
- direct push disabled
- force push disabled
- required reviews
- required CI checks
- signed commits/tags if needed
- conversation resolution
- restricted administrators if required
```

### Expected State / Output
Main/release branches can be updated only through the approved workflow.

### Why It Works
Local Git cannot prevent a credentialed user from attempting a push; server policy decides whether the ref update is accepted.

### Production Example
A production IaC repository blocks direct force-push even if an engineer runs `git push --force` locally.

### Failure / Troubleshooting Workflow
```text
unexpected protected-branch update
  ↓
hosting audit log
  ↓
branch rule history
  ↓
admin bypass?
  ↓
token/account identity
  ↓
correct policy and investigate
```

### Best Practice
Treat branch rules as part of infrastructure change control and back up/document them.

---

## Advanced Deep Dive 45 — CI Status Checks as Merge Evidence

### Concept and Detailed Explanation
Continuous integration converts repository changes into automated evidence: linting, tests, policy checks, secret scans, IaC validation, and artifact builds. A green check is not proof of correctness, but required checks create a repeatable minimum quality gate before protected branches change.

### Internal / Architecture Model
```text
Commit / PR
   |
CI pipeline
   |
+-- lint
+-- unit tests
+-- secret scan
+-- IaC validate
+-- security policy
   |
status checks
   |
merge rule
```

### Commands / Code / Configuration
```text
# Example repository validation script
set -euo pipefail
./scripts/lint.sh
./scripts/test.sh
./scripts/scan-secrets.sh
```

### Expected State / Output
The same commit produces repeatable pass/fail evidence and merge is blocked when required checks fail.

### Why It Works
Automation applies consistent validation before a ref update becomes production history.

### Production Example
A Terraform pull request cannot merge because policy checks detect an unrestricted 0.0.0.0/0 SSH rule.

### Failure / Troubleshooting Workflow
```text
CI red
  ↓
identify exact failing check
  ↓
reproduce locally where possible
  ↓
fix cause
  ↓
push new commit
  ↓
do not bypass without authorized exception
```

### Best Practice
Keep required checks deterministic, documented, and fast enough that contributors do not feel pressure to bypass them.

---

## Advanced Deep Dive 46 — Merge Queues and Integration Race Conditions

### Concept and Detailed Explanation
A pull request can pass CI against today's main and still fail when several approved pull requests merge concurrently. Merge queues reduce this race by testing the actual candidate integration order before updating the protected branch.

### Internal / Architecture Model
```text
PR A passes vs main
PR B passes vs same main

Without queue:
A merges
B may now conflict/break

With queue:
test candidate main+A+B
  ↓
merge only validated sequence
```

### Commands / Code / Configuration
```text
Conceptual checks:
- required CI on merge result
- serialization or bounded queue
- automatic re-test when base changes
```

### Expected State / Output
The branch receives a sequence of integrations that were tested against the state they actually merge into.

### Why It Works
Concurrent development creates a moving base; validation against stale base state can miss integration failures.

### Production Example
Two independent configuration changes both alter a shared variable indirectly; individually green PRs fail only when combined.

### Failure / Troubleshooting Workflow
```text
main breaks after multiple merges
  ↓
identify merge sequence
  ↓
reproduce combined state
  ↓
enable merge-result testing / queue
```

### Best Practice
For high-change protected branches, validate the merge result, not only each PR head.

---

## Advanced Deep Dive 47 — Trunk-Based Development for Infrastructure

### Concept and Detailed Explanation
Trunk-based development uses a stable main branch with short-lived branches and frequent integration. For infrastructure, this reduces large divergent branches and helps keep the desired-state repository close to what can actually be deployed.

### Internal / Architecture Model
```text
main
 | | feature-small
 |/
 main updated
 | | next-small-change
```

### Commands / Code / Configuration
```text
git switch -c change/ssh-hardening
# make small atomic commits
git fetch origin
git rebase origin/main
# review/test/merge quickly
```

### Expected State / Output
Branches remain short-lived and conflicts are discovered early.

### Why It Works
Integration cost grows with branch lifetime and divergence.

### Production Example
A platform team merges one reviewed hardening change at a time instead of keeping a three-month 'infrastructure-redesign' branch.

### Failure / Troubleshooting Workflow
```text
long-lived branch pain
  ↓
split change into smaller slices
  ↓
rebase/integrate frequently
  ↓
use feature flags or staged config where appropriate
```

### Best Practice
Prefer small deployable changes over large branch-based batches.

---

## Advanced Deep Dive 48 — Release Branches and Backport Discipline

### Concept and Detailed Explanation
Release branches can stabilize supported versions while main continues forward. Every fix must have a defined propagation strategy so a patch is not applied to one line and forgotten elsewhere.

### Internal / Architecture Model
```text
main:       A--B--C--D
             release/1:    R1--R2

security fix:
main gets F
release gets F' via deliberate backport
```

### Commands / Code / Configuration
```text
git log --oneline main
git log --oneline release/1
git cherry-pick <fix-commit>
git tag -a v1.0.1 -m "Maintenance release"
```

### Expected State / Output
Supported branches contain the intended fixes and release tags identify exact published states.

### Why It Works
Parallel maintenance lines intentionally diverge; backport decisions must be explicit.

### Production Example
A critical Ansible security hardening change is applied to both current and supported legacy release branches.

### Failure / Troubleshooting Workflow
```text
fix missing on one release
  ↓
identify source commit
  ↓
determine applicability
  ↓
backport/cherry-pick
  ↓
release-specific tests
  ↓
tag/document
```

### Best Practice
Track which supported branches received each security or operational fix.

---

## Advanced Deep Dive 49 — GitFlow Tradeoffs

### Concept and Detailed Explanation
GitFlow-style models use long-lived develop/release/hotfix branches. They can suit scheduled product releases but add merge paths and duplicated history. Infrastructure teams often benefit from simpler trunk-based workflows unless their release governance truly requires multiple long-lived lines.

### Internal / Architecture Model
```text
main
  |
hotfix/*
develop
  |
feature/*
  |
release/*
```

### Commands / Code / Configuration
```text
git log --graph --oneline --decorate --all

Workflow review questions:
How many long-lived branches?
Which is deployable?
Where do hotfixes merge back?
Who owns release propagation?
```

### Expected State / Output
Every branch has a documented purpose and fix-propagation path.

### Why It Works
More permanent branches create more synchronization obligations and conflict opportunities.

### Production Example
A team copies a hotfix into main but forgets develop, causing the bug to reappear in the next release.

### Failure / Troubleshooting Workflow
```text
workflow confusion
  ↓
identify authoritative deployable branches
  ↓
map merge/backport directions
  ↓
simplify if unnecessary
```

### Best Practice
Choose the simplest branching model that satisfies real release constraints.

---

## Advanced Deep Dive 50 — Monorepo Design and Atomic Cross-System Changes

### Concept and Detailed Explanation
A monorepo can hold multiple services or infrastructure components in one history. Its biggest strength is atomic cross-component change; its biggest costs are CI scale, permissions, ownership, and repository size.

### Internal / Architecture Model
```text
repo/
├── network/
├── ansible/
├── terraform/
├── kubernetes/
└── docs/

one commit can change compatible pieces together
```

### Commands / Code / Configuration
```text
git sparse-checkout init --cone 2>/dev/null || true
git sparse-checkout set ansible network 2>/dev/null || true
git diff --name-only HEAD~1
```

### Expected State / Output
A cross-component compatibility change can be reviewed and reverted as one commit while CI targets only affected paths.

### Why It Works
One repository provides one commit graph and one atomic ref update for related components.

### Production Example
A network VLAN definition and the Ansible inventory consuming that VLAN change in the same reviewed commit.

### Failure / Troubleshooting Workflow
```text
monorepo slow/noisy
  ↓
path ownership
  ↓
path-based CI
  ↓
sparse checkout
  ↓
large binary/history audit
```

### Best Practice
Use monorepo only when atomic coordination and shared governance outweigh repository-scale complexity.

---

## Advanced Deep Dive 51 — Multirepo Design and Version Contracts

### Concept and Detailed Explanation
Multirepo separates components into independent histories and permissions. This improves autonomy but means cross-repository changes cannot be one atomic Git commit. Integration therefore needs versioned interfaces and coordinated release references.

### Internal / Architecture Model
```text
network-config repo → release v2
ansible repo        → expects network schema v2
app repo            → release independently
```

### Commands / Code / Configuration
```text
# Record external dependency versions explicitly:
network_schema_version: "2"
ansible_collection_version: "3.4.1"
```

### Expected State / Output
Each repository can release independently while consumers declare compatible versions.

### Why It Works
Separate repositories have separate ref transactions, so integration must occur through version contracts rather than shared commits.

### Production Example
A role repository publishes v3 while the environment repository pins v2 until staging validation succeeds.

### Failure / Troubleshooting Workflow
```text
cross-repo incompatibility
  ↓
identify producer version
  ↓
consumer expectation
  ↓
upgrade contract
  ↓
test coordinated release
```

### Best Practice
Use explicit version contracts between repositories.

---

## Advanced Deep Dive 52 — Sparse Checkout for Large Repositories

### Concept and Detailed Explanation
Sparse checkout limits which paths appear in the working tree while preserving broader repository history. It reduces working-tree noise in monorepos but does not by itself reduce all object transfer.

### Internal / Architecture Model
```text
Full repository history
      |
sparse patterns
      |
working tree:
ansible/
docs/
only
```

### Commands / Code / Configuration
```text
git sparse-checkout init --cone
git sparse-checkout set ansible docs
git sparse-checkout list
git sparse-checkout disable
```

### Expected State / Output
Only selected directories appear in the working tree while Git can still reason about repository history.

### Why It Works
Sparse checkout changes checkout population, not the conceptual commit graph.

### Production Example
An operations engineer working only on Ansible does not need thousands of application-source files in the working tree.

### Failure / Troubleshooting Workflow
```text
expected path missing
  ↓
git sparse-checkout list
  ↓
adjust patterns
  ↓
verify branch contains path
```

### Best Practice
Use sparse checkout for ergonomics; combine with partial clone if transfer size is also a problem.

---

## Advanced Deep Dive 53 — Shallow Clone Tradeoffs in CI

### Concept and Detailed Explanation
A shallow clone downloads limited history, often improving CI checkout speed. The tradeoff is incomplete ancestry: merge-base discovery, describe, blame, changelog generation, or bisect may fail or behave differently.

### Internal / Architecture Model
```text
Remote full history:
A--B--C--D--E

depth 1 clone:
E only
```

### Commands / Code / Configuration
```text
git rev-parse --is-shallow-repository
git fetch --deepen=50
git fetch --unshallow 2>/dev/null || true
```

### Expected State / Output
A shallow job has the history it needs for its task or explicitly deepens before history-dependent operations.

### Why It Works
Git cannot compute ancestry relationships using commits that were never downloaded.

### Production Example
A CI security scanner needs to compare against the previous release tag but fails because the runner fetched only one commit.

### Failure / Troubleshooting Workflow
```text
history-dependent CI fails
  ↓
is repository shallow?
  ↓
required merge base/tag present?
  ↓
deepen/unshallow
```

### Best Practice
Use the shallowest clone that still supports the pipeline's actual history operations.

---

## Advanced Deep Dive 54 — Partial Clone and Promisor Objects

### Concept and Detailed Explanation
Partial clone can avoid downloading selected object classes until they are needed, with the remote acting as a promisor for missing objects. This helps very large repositories but requires server/client compatibility and makes offline assumptions different.

### Internal / Architecture Model
```text
Commit/tree metadata downloaded
       |
large blobs omitted
       |
working operation needs blob
       |
fetch promised object on demand
```

### Commands / Code / Configuration
```text
git clone --filter=blob:none <url> repo-partial 2>/dev/null || true
git config --get remote.origin.promisor 2>/dev/null || true
```

### Expected State / Output
Initial clone transfers fewer blobs, and missing objects are retrieved when operations require them.

### Why It Works
Git can maintain references to objects that the remote promises to provide later.

### Production Example
A very large source monorepo becomes faster to clone for CI jobs that inspect metadata but touch only a small subset of files.

### Failure / Troubleshooting Workflow
```text
offline operation fails
  ↓
partial clone?
  ↓
missing promised object?
  ↓
remote available?
  ↓
prefetch required objects
```

### Best Practice
Validate backup/offline workflows before standardizing partial clones.

---

## Advanced Deep Dive 55 — Submodules as Exact External Commit Pointers

### Concept and Detailed Explanation
A submodule entry records the exact commit expected from another repository. This gives precise dependency pinning but adds two-level repository state: the parent can be clean while the submodule working tree or pointer is wrong.

### Internal / Architecture Model
```text
Parent tree:
libs/tool → gitlink commit abc123

Submodule repository:
...--abc123--def456

Parent chooses abc123
```

### Commands / Code / Configuration
```text
git submodule status
git diff --submodule
git -C path/to/submodule status
git submodule update --init --recursive
```

### Expected State / Output
The submodule is checked out at the commit recorded by the parent repository.

### Why It Works
The parent stores a gitlink object rather than ordinary child repository file contents.

### Production Example
A platform repository pins a vendor automation collection to a tested commit rather than automatically following latest.

### Failure / Troubleshooting Workflow
```text
submodule appears modified
  ↓
is child working tree dirty?
  ↓
is child at different commit?
  ↓
is parent pointer intentionally changing?
  ↓
commit child first if developing it
  ↓
update parent pointer
```

### Best Practice
Use submodules only when the team understands two-repository lifecycle and CI cloning requirements.

---

## Advanced Deep Dive 56 — Subtree as an Alternative Integration Model

### Concept and Detailed Explanation
Git subtree workflows vendor another project's content into a directory while retaining normal files in the parent repository. This avoids submodule checkout complexity but duplicates content/history and requires deliberate subtree update procedures.

### Internal / Architecture Model
```text
Parent repository
└── vendor/tool/
    ordinary tracked files

External source
   ↓ subtree pull/push workflow
```

### Commands / Code / Configuration
```text
git subtree add --prefix=vendor/tool <remote> main --squash 2>/dev/null || true
git subtree pull --prefix=vendor/tool <remote> main --squash 2>/dev/null || true
```

### Expected State / Output
Consumers receive the vendored content with an ordinary clone; updates are explicit subtree operations.

### Why It Works
Subtree trades dependency indirection for copied content and synchronization work.

### Production Example
An offline deployment repository vendors a small script library so builds do not depend on recursive submodule fetch.

### Failure / Troubleshooting Workflow
```text
vendor code outdated
  ↓
identify upstream/version
  ↓
subtree pull
  ↓
review diff
  ↓
test
```

### Best Practice
Choose submodule, subtree, package registry, or vendoring based on dependency lifecycle—not familiarity alone.

---

## Advanced Deep Dive 57 — Git Worktrees for Parallel Operational Branches

### Concept and Detailed Explanation
Worktrees allow multiple branches from one object database to be checked out at different filesystem paths. This is ideal for urgent hotfixes while a large uncommitted feature remains open.

### Internal / Architecture Model
```text
.git object database
   |
+-- worktree A → feature
+-- worktree B → hotfix
+-- worktree C → release
```

### Commands / Code / Configuration
```text
git worktree add ../repo-hotfix hotfix
git worktree list
git worktree remove ../repo-hotfix
git worktree prune
```

### Expected State / Output
Each worktree has its own checked-out branch and working files while sharing repository objects.

### Why It Works
Git separates working-tree/index state from the shared object database.

### Production Example
An engineer keeps a complex feature environment intact and opens a clean hotfix worktree for an urgent production revert.

### Failure / Troubleshooting Workflow
```text
cannot checkout branch
  ↓
git worktree list
  ↓
is branch already checked out elsewhere?
  ↓
use that worktree or choose another branch
```

### Best Practice
Prefer worktrees over duplicate clones when you need simultaneous local branches.

---

## Advanced Deep Dive 58 — Bisect as a Scientific Debugging Workflow

### Concept and Detailed Explanation
`git bisect` turns regression hunting into binary search. Its power comes from a reliable yes/no test. The fastest bisect is not necessarily the best if old commits cannot build or the test is nondeterministic.

### Internal / Architecture Model
```text
known good G
       |
many commits
       |
known bad B

test midpoint
  ↓
halve search space
  ↓
repeat
```

### Commands / Code / Configuration
```text
git bisect start
git bisect bad HEAD
git bisect good <known-good>
# test
git bisect good   # or bad
git bisect reset
```

### Expected State / Output
Git identifies the first commit that transitions from good to bad under the classification supplied.

### Why It Works
Binary search requires logarithmically fewer test points than inspecting every commit.

### Production Example
A configuration regression introduced somewhere across 500 changes is found in roughly a handful of carefully tested revisions.

### Failure / Troubleshooting Workflow
```text
bisect unreliable
  ↓
is test deterministic?
  ↓
can every candidate build?
  ↓
use git bisect skip for untestable commits
  ↓
automate test if possible
```

### Best Practice
Define the regression test first; bisect quality depends on classification quality.

---

## Advanced Deep Dive 59 — Automated Bisect and Exit Codes

### Concept and Detailed Explanation
`git bisect run` executes a script at each candidate commit. Exit 0 means good, 1–127 (except special values) typically means bad, and 125 means skip. This converts a manual search into repeatable automation.

### Internal / Architecture Model
```text
candidate commit
   |
test script
   |
exit code
   |
good / bad / skip
   |
next midpoint
```

### Commands / Code / Configuration
```text
cat > test-regression.sh <<'EOF'
#!/usr/bin/env bash
set -e
./build.sh >/dev/null
./tests/smoke.sh
EOF
chmod +x test-regression.sh

git bisect run ./test-regression.sh
```

### Expected State / Output
Git walks history automatically and stops when it isolates the first bad commit or cannot determine uniquely.

### Why It Works
Deterministic machine-readable test results allow Git to automate the binary search.

### Production Example
A service configuration test automatically identifies the commit that first makes `nginx -t` fail.

### Failure / Troubleshooting Workflow
```text
bisect run gives strange result
  ↓
run test repeatedly on same commit
  ↓
check environment dependencies
  ↓
reset caches/state
  ↓
use exit 125 for untestable commits
```

### Best Practice
Make automated bisect tests hermetic enough that commit state, not leftover environment state, determines the result.

---

## Advanced Deep Dive 60 — Git for Infrastructure Change Control and GitOps

### Concept and Detailed Explanation
For infrastructure, Git is most valuable when a commit becomes the reviewed identifier of desired state. A mature flow connects branch/review, CI validation, merge, deployment/reconciliation, and runtime evidence. GitOps goes further by having an automated controller reconcile the runtime environment toward Git-declared state.

The critical distinction is that Git is the source of approved desired state; execution logs and runtime monitoring prove what actually happened.

### Internal / Architecture Model
```text
Engineer
  |
feature branch
  |
review + CI
  |
protected main
  |
commit ID
  |
deployment / reconciliation
  |
runtime
  |
verification + audit

Git desired state ≠ runtime proof
```

### Commands / Code / Configuration
```text
git rev-parse HEAD
git show --stat --oneline HEAD

# Deployment record example:
echo "deployed_commit=$(git rev-parse HEAD)"
```

### Expected State / Output
Every production change can be correlated to an exact reviewed commit and an execution record.

### Why It Works
Immutable commit IDs give a precise desired-state version; automation connects that version to systems.

### Production Example
During an incident, the team correlates a firewall outage with the exact Git commit, pull request, pipeline run, and target inventory.

### Failure / Troubleshooting Workflow
```text
production incident
  ↓
runtime symptom time
  ↓
deployment/reconciliation run
  ↓
commit ID
  ↓
review/test history
  ↓
revert or forward-fix desired state
  ↓
verify runtime converges
```

### Best Practice
Keep Git history, CI/CD audit logs, deployment identity, and runtime observability connected.

---


# Enhanced Practical Lab Series — Git and Version Control Systems

These labs extend the original labs and are intended to turn the concepts into repeatable operational skills.

## Enhanced Lab 1 — Git's Object Database and the Snapshot Graph

### Objective
Demonstrate **Git's Object Database and the Snapshot Graph** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git rev-parse HEAD
git cat-file -t HEAD
git cat-file -p HEAD
git ls-tree -r HEAD
git count-objects -v
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
HEAD resolves to a commit object; that commit points to a tree; the tree maps names/modes to blob/tree IDs.

### Troubleshooting Path
```text
confusing history
  ↓
identify refs
  ↓
resolve commit IDs
  ↓
inspect commit/tree/blob
  ↓
determine which ref moved
  ↓
recover with new ref
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 2 — Porcelain vs Plumbing Commands

### Objective
Demonstrate **Porcelain vs Plumbing Commands** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
printf 'hello
' > demo.txt
git hash-object demo.txt
git hash-object -w demo.txt
git cat-file -t $(git hash-object demo.txt)
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
A blob ID is calculated from the content; with `-w` the object is stored in the object database.

### Troubleshooting Path
```text
porcelain result unexpected
  ↓
git status
  ↓
inspect refs/index/object IDs
  ↓
use plumbing read-only commands
  ↓
understand high-level behavior
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 3 — The Index as a Real Data Structure

### Objective
Demonstrate **The Index as a Real Data Structure** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git ls-files --stage
git diff --cached
git diff
git status --short
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
`git ls-files --stage` shows staged object IDs and file modes, while the two diff commands show index↔HEAD and working-tree↔index changes.

### Troubleshooting Path
```text
wrong content staged
  ↓
git status
  ↓
git diff --cached
  ↓
git restore --staged <path>
  ↓
stage correct hunks
  ↓
verify again
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 4 — Conflict Stages in the Index

### Objective
Demonstrate **Conflict Stages in the Index** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git ls-files -u
git show :1:path/to/file
git show :2:path/to/file
git show :3:path/to/file
git diff --cc
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
You can inspect base, ours, and theirs independently and then stage the final resolved working-tree version.

### Troubleshooting Path
```text
merge conflict
  ↓
inspect stage 1/2/3
  ↓
understand semantic intent
  ↓
edit final file
  ↓
validate syntax/tests
  ↓
git add
  ↓
continue merge/rebase
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 5 — HEAD, Symbolic References, and Detached State

### Objective
Demonstrate **HEAD, Symbolic References, and Detached State** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git symbolic-ref -q HEAD || echo "detached"
git rev-parse HEAD
git branch --show-current
git switch --detach HEAD~1
git switch -c rescue-work
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
In detached state, `git branch --show-current` is empty; creating a branch anchors the current commit.

### Troubleshooting Path
```text
detached HEAD surprise
  ↓
git status
  ↓
did you create useful commits?
  ↓ yes
git switch -c <name>
  ↓
verify log
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 6 — Commit Identity vs Authentication

### Objective
Demonstrate **Commit Identity vs Authentication** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config user.name
git config user.email
git show --show-signature HEAD
git log --format='%h %an <%ae> %G? %s' -10
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
You can distinguish ordinary identity metadata from a verified signature status.

### Troubleshooting Path
```text
suspicious commit identity
  ↓
inspect hosting audit log
  ↓
signature status
  ↓
review/merge record
  ↓
CI provenance
  ↓
account/key ownership
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 7 — Object Reachability and Why Recovery Works

### Objective
Demonstrate **Object Reachability and Why Recovery Works** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git reflog --all
git fsck --unreachable
git fsck --lost-found
git branch recovery <commit-id>
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Recent deleted commits often appear in reflog or fsck output and can be re-anchored with a branch.

### Troubleshooting Path
```text
work appears lost
  ↓
STOP destructive commands
  ↓
git reflog --all
  ↓
git fsck --unreachable
  ↓
inspect candidate commit
  ↓
create recovery branch
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 8 — Reflog Semantics and Limits

### Objective
Demonstrate **Reflog Semantics and Limits** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git reflog
git reflog show main
git show HEAD@{3}
git branch recovery HEAD@{3}
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
You can inspect previous local ref positions using time/index notation such as `HEAD@{3}`.

### Troubleshooting Path
```text
need old state
  ↓
which local ref moved?
  ↓
git reflog show <ref>
  ↓
inspect candidate
  ↓
anchor with branch/tag
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 9 — Packfiles, Delta Compression, and Repository Size

### Objective
Demonstrate **Packfiles, Delta Compression, and Repository Size** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git count-objects -vH
git verify-pack -v .git/objects/pack/*.idx 2>/dev/null | head
git gc
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
After normal maintenance, loose objects may be packed and repository storage becomes more efficient.

### Troubleshooting Path
```text
repo unexpectedly huge
  ↓
git count-objects -vH
  ↓
identify large historical blobs
  ↓
decide LFS/artifact storage/history cleanup
  ↓
coordinate rewrite if required
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 10 — Garbage Collection and Pruning Safety

### Objective
Demonstrate **Garbage Collection and Pruning Safety** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git gc
git reflog expire --dry-run --all
git prune --dry-run
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Dry-run commands show what could expire/prune without deleting objects.

### Troubleshooting Path
```text
disk cleanup request
  ↓
verify backups
  ↓
inspect reachability/reflogs
  ↓
normal git maintenance first
  ↓
avoid aggressive prune during recovery incident
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 11 — Hash Algorithms and Object IDs

### Objective
Demonstrate **Hash Algorithms and Object IDs** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git rev-parse --show-object-format 2>/dev/null || true
git hash-object README.md
git rev-parse HEAD^{tree}
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The repository reports its object format where supported and object IDs remain stable for unchanged objects.

### Troubleshooting Path
```text
unexpected object ID
  ↓
verify repository/object format
  ↓
verify exact object/content
  ↓
do not compare IDs from unrelated rewritten repositories blindly
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 12 — Commit Graph Topology and First-Parent History

### Objective
Demonstrate **Commit Graph Topology and First-Parent History** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git log --graph --oneline --decorate --all
git log --first-parent --oneline main
git show --pretty=raw <merge-commit>
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Full graph shows branch topology; first-parent view emphasizes integration commits on the main line.

### Troubleshooting Path
```text
history looks duplicated/confusing
  ↓
draw graph
  ↓
inspect merge parents
  ↓
compare full vs first-parent history
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 13 — Merge Base as the Foundation of Integration

### Objective
Demonstrate **Merge Base as the Foundation of Integration** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git merge-base main feature
git diff $(git merge-base main feature)..feature
git diff main...feature
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The merge-base commit identifies the common starting snapshot for branch-change comparison.

### Troubleshooting Path
```text
unexpected review diff
  ↓
git merge-base main feature
  ↓
inspect branch tips
  ↓
check whether branch was rebased/merged recently
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 14 — Fast-Forward, No-FF, and Merge Commit Policy

### Objective
Demonstrate **Fast-Forward, No-FF, and Merge Commit Policy** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git merge --ff-only feature
git merge --no-ff feature
git log --graph --oneline --decorate
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
`--ff-only` fails if histories diverged; `--no-ff` creates an explicit merge commit for an otherwise fast-forwardable branch.

### Troubleshooting Path
```text
merge policy failure
  ↓
what topology is required?
  ↓
can fast-forward?
  ↓
protected-branch/hosting policy?
  ↓
integrate using approved method
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 15 — Squash Merge Semantics

### Objective
Demonstrate **Squash Merge Semantics** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git switch main
git merge --squash feature
git commit -m "Add feature"
git log --graph --oneline --all
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The main branch gets one new commit containing the feature result, while the original feature commits remain separate history.

### Troubleshooting Path
```text
feature later reused/merged
  ↓
remember squash did not record ancestry
  ↓
inspect diff/merge-base
  ↓
avoid assuming Git knows branch was merged
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 16 — Three-Way Merge Conflict Resolution as Semantic Work

### Objective
Demonstrate **Three-Way Merge Conflict Resolution as Semantic Work** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git status
git diff --cc
git show :1:config.yml
git show :2:config.yml
git show :3:config.yml

# After editing:
yamllint config.yml 2>/dev/null || true
git add config.yml
git diff --cached
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The conflict markers disappear, the index contains the intended resolved file, and validation confirms the configuration is still valid.

### Troubleshooting Path
```text
conflict
  ↓
inspect base / ours / theirs
  ↓
understand both business intents
  ↓
produce final state
  ↓
validate syntax
  ↓
run policy/tests
  ↓
stage and continue
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 17 — `git rerere` and Repeated Conflict Reuse

### Objective
Demonstrate **`git rerere` and Repeated Conflict Reuse** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config rerere.enabled true
git rerere status
git rerere diff
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
After resolving a repeated conflict, Git can pre-apply the recorded resolution instead of requiring identical manual work.

### Troubleshooting Path
```text
rerere auto-resolution appears
  ↓
review diff
  ↓
run tests
  ↓
confirm context still valid
  ↓
stage/continue
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 18 — Rebase as Commit Replay

### Objective
Demonstrate **Rebase as Commit Replay** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git switch feature
git log --oneline --graph --all
git rebase main
git range-diff main@{1}..feature@{1} main..feature 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The rebased branch has equivalent intended changes but different commit IDs and new parents.

### Troubleshooting Path
```text
rebase surprise
  ↓
git status
  ↓
git reflog
  ↓
identify old branch tip
  ↓
compare with range-diff/log
  ↓
abort or continue deliberately
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 19 — Interactive Rebase as Local History Editing

### Objective
Demonstrate **Interactive Rebase as Local History Editing** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git log --oneline -6
git rebase -i HEAD~4

# Common todo actions:
# pick
# reword
# edit
# squash
# fixup
# drop
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The resulting local history contains fewer, clearer commits with new IDs.

### Troubleshooting Path
```text
interactive rebase wrong
  ↓
git rebase --abort if still active
  ↓
otherwise git reflog
  ↓
find pre-rebase tip
  ↓
create recovery branch
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 20 — Rebase `--onto` for Surgical History Repair

### Objective
Demonstrate **Rebase `--onto` for Surgical History Repair** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Generic form:
git rebase --onto <new-base> <old-base> <branch>

# Inspect first:
git log --graph --oneline --decorate --all
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Only commits after `<old-base>` on the selected branch are replayed onto `<new-base>`.

### Troubleshooting Path
```text
need surgical move
  ↓
draw graph
  ↓
identify new base
  ↓
identify old base/exclusion point
  ↓
create backup branch
  ↓
rebase --onto
  ↓
range-diff/test
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 21 — Cherry-Pick and Duplicate Patch Identity

### Objective
Demonstrate **Cherry-Pick and Duplicate Patch Identity** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git show <commit>
git switch release/1.0
git cherry-pick <commit>
git log --cherry --oneline main...release/1.0
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The release branch receives an equivalent patch as a new commit.

### Troubleshooting Path
```text
cherry-pick conflict
  ↓
inspect commit intent
  ↓
resolve against release context
  ↓
run release-specific tests
  ↓
git cherry-pick --continue
  ↓
or --abort
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 22 — Remote-Tracking References Are Local Observations

### Objective
Demonstrate **Remote-Tracking References Are Local Observations** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git remote -v
git branch -vv
git fetch origin
git log --oneline --left-right main...origin/main
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
After fetch, `origin/main` reflects the current remote state while local `main` remains unchanged.

### Troubleshooting Path
```text
push rejected
  ↓
git fetch origin
  ↓
compare main...origin/main
  ↓
understand divergence
  ↓
merge/rebase as policy requires
  ↓
push
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 23 — Upstream Tracking Configuration

### Objective
Demonstrate **Upstream Tracking Configuration** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git branch -vv
git rev-parse --abbrev-ref --symbolic-full-name @{u}
git push -u origin feature/api
git branch --set-upstream-to=origin/main local-main 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
`git status` can report the branch's divergence relative to its configured upstream.

### Troubleshooting Path
```text
pull/push targets wrong branch
  ↓
git branch -vv
  ↓
inspect @{u}
  ↓
fix upstream
  ↓
fetch and verify divergence
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 24 — Pull Strategies and Explicit Integration

### Objective
Demonstrate **Pull Strategies and Explicit Integration** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config --show-origin --get pull.rebase
git config --show-origin --get pull.ff

git pull --ff-only
git pull --rebase
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
`--ff-only` refuses divergence; `--rebase` replays local commits when appropriate; default behavior follows configuration.

### Troubleshooting Path
```text
pull unexpected
  ↓
git status
  ↓
inspect pull.rebase / pull.ff
  ↓
git reflog if history changed
  ↓
restore desired topology
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 25 — Non-Fast-Forward Push Rejection as Data Protection

### Objective
Demonstrate **Non-Fast-Forward Push Rejection as Data Protection** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git fetch origin
git log --graph --oneline --decorate --all
git log --left-right --cherry-pick main...origin/main
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The push remains rejected until histories are integrated or an authorized history rewrite is performed.

### Troubleshooting Path
```text
non-fast-forward
  ↓
fetch
  ↓
draw graph
  ↓
integrate remote changes
  ↓
test
  ↓
push again
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 26 — `--force-with-lease` and Optimistic Concurrency

### Objective
Demonstrate **`--force-with-lease` and Optimistic Concurrency** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git fetch origin
git log --graph --oneline --decorate --all
git push --force-with-lease origin feature
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The forced update succeeds only when the remote ref matches the expected old value.

### Troubleshooting Path
```text
lease rejected
  ↓
STOP
  ↓
fetch
  ↓
inspect new remote commits
  ↓
integrate/coordinate
  ↓
retry only if rewrite still intended
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 27 — Remote Refspecs

### Objective
Demonstrate **Remote Refspecs** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config --get-all remote.origin.fetch
git fetch origin main:refs/remotes/origin/main
git show-ref
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The configured fetch refspec shows which remote refs are copied into which local namespace.

### Troubleshooting Path
```text
branch not appearing after fetch
  ↓
inspect remote refs
  ↓
inspect fetch refspec
  ↓
verify namespace mapping
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 28 — Remote Pruning and Deleted Branch Hygiene

### Objective
Demonstrate **Remote Pruning and Deleted Branch Hygiene** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git fetch --prune origin
git remote prune origin --dry-run
git branch -r
git branch -vv
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Stale remote-tracking refs disappear while local branches remain unless explicitly deleted.

### Troubleshooting Path
```text
stale branch confusion
  ↓
git fetch --prune
  ↓
inspect remote branches
  ↓
inspect local branches/upstreams
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 29 — Multiple Remotes and Trust Boundaries

### Objective
Demonstrate **Multiple Remotes and Trust Boundaries** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git remote -v
git remote get-url --all origin
git remote show origin
git push --dry-run origin main
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Each remote URL and push destination is explicit and reviewed before sensitive changes are published.

### Troubleshooting Path
```text
before sensitive push
  ↓
git remote -v
  ↓
verify repository ownership/classification
  ↓
dry-run or protected workflow
  ↓
push
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 30 — Repository Migration Without Losing Intent

### Objective
Demonstrate **Repository Migration Without Losing Intent** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git clone --mirror <old-url> repo.git
cd repo.git
git remote set-url --push origin <new-url>
git push --mirror

# Review carefully before using --mirror against a destination.
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Git refs can be copied completely, while hosting-platform metadata is handled by a separate documented migration process.

### Troubleshooting Path
```text
migration
  ↓
inventory refs/tags/LFS/submodules
  ↓
inventory hosting metadata
  ↓
test destination
  ↓
freeze/cutover
  ↓
validate permissions/rules/CI
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 31 — `.gitignore` Matching Semantics

### Objective
Demonstrate **`.gitignore` Matching Semantics** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git status --ignored
git check-ignore -v path/to/file
git ls-files path/to/file
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
`git check-ignore -v` identifies the exact ignore rule that matched a path.

### Troubleshooting Path
```text
file unexpectedly tracked/visible
  ↓
git ls-files <path>
  ↓
git check-ignore -v <path>
  ↓
if tracked and should not be:
git rm --cached <path>
  ↓
commit policy change
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 32 — Ignore Rules vs Security Controls

### Objective
Demonstrate **Ignore Rules vs Security Controls** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git add -f .env   # demonstrates ignore can be overridden
git grep -nE 'password|token|secret' -- . ':!examples'
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Teams understand that ignored paths can still be committed and do not rely on ignore patterns as the only safeguard.

### Troubleshooting Path
```text
secret committed
  ↓
assume exposed
  ↓
rotate/revoke
  ↓
remove current copy
  ↓
scan history
  ↓
history cleanup if required
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 33 — `.gitattributes` and Repository-Wide Normalization

### Objective
Demonstrate **`.gitattributes` and Repository-Wide Normalization** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git check-attr -a -- scripts/deploy.sh
git ls-files --eol

# Example:
# * text=auto
# *.sh text eol=lf
# *.ps1 text eol=crlf
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Git reports the intended text/EOL attributes and avoids whole-file line-ending churn.

### Troubleshooting Path
```text
whole file appears changed
  ↓
git diff --ignore-space-at-eol
  ↓
git ls-files --eol
  ↓
git check-attr
  ↓
fix attributes
  ↓
renormalize deliberately
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 34 — Renormalization After Attribute Changes

### Objective
Demonstrate **Renormalization After Attribute Changes** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git status
git add .gitattributes
git add --renormalize .
git diff --cached --stat
git diff --cached
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The normalization changes are isolated in a dedicated commit and later feature changes are easier to review.

### Troubleshooting Path
```text
normalization diff huge
  ↓
ensure no functional edits mixed in
  ↓
review attributes
  ↓
commit normalization separately
  ↓
rebase feature work if needed
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 35 — Executable Bit Tracking

### Objective
Demonstrate **Executable Bit Tracking** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git ls-files --stage scripts/deploy.sh
chmod +x scripts/deploy.sh
git diff --summary
git update-index --chmod=+x scripts/deploy.sh
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The tree entry changes from a non-executable to executable mode without needing content changes.

### Troubleshooting Path
```text
script permission issue
  ↓
git ls-files --stage
  ↓
working-tree permissions
  ↓
filesystem/core.fileMode behavior
  ↓
commit mode fix
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 36 — Git LFS and Large Binary Pointers

### Objective
Demonstrate **Git LFS and Large Binary Pointers** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git lfs install 2>/dev/null || true
git lfs track "*.bin" 2>/dev/null || true
git lfs ls-files 2>/dev/null || true
cat .gitattributes
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Large-file paths are represented by LFS pointers in Git and fetched from the configured LFS service.

### Troubleshooting Path
```text
LFS file missing
  ↓
is git-lfs installed?
  ↓
LFS endpoint/auth?
  ↓
pointer present?
  ↓
object uploaded?
  ↓
fetch LFS object
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 37 — History Rewriting for Secret Cleanup

### Objective
Demonstrate **History Rewriting for Secret Cleanup** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Conceptual modern workflow often uses git-filter-repo if installed:
git filter-repo --path path/to/secret --invert-paths 2>/dev/null || true

# Verify:
git log --all -- path/to/secret
git grep <FAKE_SECRET_PATTERN> $(git rev-list --all) 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The credential is invalidated independently of repository cleanup; rewritten refs no longer expose the unwanted historical path/content where the cleanup covered all relevant refs.

### Troubleshooting Path
```text
secret incident
  ↓
revoke/rotate
  ↓
identify all refs/tags
  ↓
rewrite in isolated clone
  ↓
verify
  ↓
coordinate push/re-clone
  ↓
scan mirrors/caches
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 38 — Commit and Tag Signing Models

### Objective
Demonstrate **Commit and Tag Signing Models** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config --get user.signingkey
git log --show-signature -5
git tag -v v1.0.0 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Signed objects display signature verification when the verifier has the required trust/key configuration.

### Troubleshooting Path
```text
signature invalid/unknown
  ↓
object changed?
  ↓
signer key available?
  ↓
trust mapping correct?
  ↓
key expired/revoked?
  ↓
hosting verification policy?
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 39 — SSH Host Keys and Git Remote Trust

### Objective
Demonstrate **SSH Host Keys and Git Remote Trust** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
ssh -T git@example.com
ssh-keygen -F example.com
ssh -G git@example.com | head
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
SSH connects only when the client trusts the expected server identity and the server accepts the authorized user key.

### Troubleshooting Path
```text
HOST IDENTIFICATION HAS CHANGED
  ↓
STOP
  ↓
verify DNS/network
  ↓
obtain trusted fingerprint
  ↓
compare
  ↓
update known_hosts only after validation
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 40 — Credential Helpers and Token Storage

### Objective
Demonstrate **Credential Helpers and Token Storage** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config --show-origin --get-all credential.helper
git remote get-url origin

# Inspect configuration; do not print actual secrets.
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Authentication occurs without embedding the secret in the remote URL or repository files.

### Troubleshooting Path
```text
HTTPS auth failure
  ↓
remote URL
  ↓
credential helper
  ↓
token expiry/scope
  ↓
SSO policy
  ↓
rotate/re-authenticate
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 41 — `safe.directory` and Repository Ownership Security

### Objective
Demonstrate **`safe.directory` and Repository Ownership Security** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git config --show-origin --get-all safe.directory
git status
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Git warns/refuses in suspicious ownership contexts rather than automatically trusting every filesystem repository.

### Troubleshooting Path
```text
dubious ownership warning
  ↓
verify actual owner/path
  ↓
why are you using another user's repo?
  ↓
fix ownership if wrong
  ↓
add narrow safe.directory only if intentionally trusted
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 42 — Hooks as Local Automation, Not Central Enforcement

### Objective
Demonstrate **Hooks as Local Automation, Not Central Enforcement** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
ls .git/hooks
git config --get core.hooksPath

# Example shared hooks path:
git config core.hooksPath .githooks
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Local hooks provide fast feedback while CI remains the enforceable source of policy.

### Troubleshooting Path
```text
hook not running
  ↓
hook path?
  ↓
executable bit?
  ↓
interpreter?
  ↓
bypassed?
  ↓
CI equivalent present?
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 43 — CODEOWNERS and Review Routing

### Objective
Demonstrate **CODEOWNERS and Review Routing** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Conceptual CODEOWNERS examples:
# /network/ @network-team
# /security/ @security-team
# /prod/ @platform-ops
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Changes to sensitive paths automatically involve the appropriate reviewers when the hosting platform enforces those rules.

### Troubleshooting Path
```text
review not requested
  ↓
path pattern correct?
  ↓
CODEOWNERS branch/location?
  ↓
team access valid?
  ↓
branch rule requires owner approval?
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 44 — Protected Branches and Server-Side Rules

### Objective
Demonstrate **Protected Branches and Server-Side Rules** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Policy checklist:
- direct push disabled
- force push disabled
- required reviews
- required CI checks
- signed commits/tags if needed
- conversation resolution
- restricted administrators if required
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Main/release branches can be updated only through the approved workflow.

### Troubleshooting Path
```text
unexpected protected-branch update
  ↓
hosting audit log
  ↓
branch rule history
  ↓
admin bypass?
  ↓
token/account identity
  ↓
correct policy and investigate
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 45 — CI Status Checks as Merge Evidence

### Objective
Demonstrate **CI Status Checks as Merge Evidence** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Example repository validation script
set -euo pipefail
./scripts/lint.sh
./scripts/test.sh
./scripts/scan-secrets.sh
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The same commit produces repeatable pass/fail evidence and merge is blocked when required checks fail.

### Troubleshooting Path
```text
CI red
  ↓
identify exact failing check
  ↓
reproduce locally where possible
  ↓
fix cause
  ↓
push new commit
  ↓
do not bypass without authorized exception
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 46 — Merge Queues and Integration Race Conditions

### Objective
Demonstrate **Merge Queues and Integration Race Conditions** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Conceptual checks:
- required CI on merge result
- serialization or bounded queue
- automatic re-test when base changes
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The branch receives a sequence of integrations that were tested against the state they actually merge into.

### Troubleshooting Path
```text
main breaks after multiple merges
  ↓
identify merge sequence
  ↓
reproduce combined state
  ↓
enable merge-result testing / queue
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 47 — Trunk-Based Development for Infrastructure

### Objective
Demonstrate **Trunk-Based Development for Infrastructure** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git switch -c change/ssh-hardening
# make small atomic commits
git fetch origin
git rebase origin/main
# review/test/merge quickly
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Branches remain short-lived and conflicts are discovered early.

### Troubleshooting Path
```text
long-lived branch pain
  ↓
split change into smaller slices
  ↓
rebase/integrate frequently
  ↓
use feature flags or staged config where appropriate
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 48 — Release Branches and Backport Discipline

### Objective
Demonstrate **Release Branches and Backport Discipline** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git log --oneline main
git log --oneline release/1
git cherry-pick <fix-commit>
git tag -a v1.0.1 -m "Maintenance release"
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Supported branches contain the intended fixes and release tags identify exact published states.

### Troubleshooting Path
```text
fix missing on one release
  ↓
identify source commit
  ↓
determine applicability
  ↓
backport/cherry-pick
  ↓
release-specific tests
  ↓
tag/document
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 49 — GitFlow Tradeoffs

### Objective
Demonstrate **GitFlow Tradeoffs** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git log --graph --oneline --decorate --all

Workflow review questions:
How many long-lived branches?
Which is deployable?
Where do hotfixes merge back?
Who owns release propagation?
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Every branch has a documented purpose and fix-propagation path.

### Troubleshooting Path
```text
workflow confusion
  ↓
identify authoritative deployable branches
  ↓
map merge/backport directions
  ↓
simplify if unnecessary
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 50 — Monorepo Design and Atomic Cross-System Changes

### Objective
Demonstrate **Monorepo Design and Atomic Cross-System Changes** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git sparse-checkout init --cone 2>/dev/null || true
git sparse-checkout set ansible network 2>/dev/null || true
git diff --name-only HEAD~1
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
A cross-component compatibility change can be reviewed and reverted as one commit while CI targets only affected paths.

### Troubleshooting Path
```text
monorepo slow/noisy
  ↓
path ownership
  ↓
path-based CI
  ↓
sparse checkout
  ↓
large binary/history audit
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 51 — Multirepo Design and Version Contracts

### Objective
Demonstrate **Multirepo Design and Version Contracts** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Record external dependency versions explicitly:
network_schema_version: "2"
ansible_collection_version: "3.4.1"
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Each repository can release independently while consumers declare compatible versions.

### Troubleshooting Path
```text
cross-repo incompatibility
  ↓
identify producer version
  ↓
consumer expectation
  ↓
upgrade contract
  ↓
test coordinated release
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 52 — Sparse Checkout for Large Repositories

### Objective
Demonstrate **Sparse Checkout for Large Repositories** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git sparse-checkout init --cone
git sparse-checkout set ansible docs
git sparse-checkout list
git sparse-checkout disable
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Only selected directories appear in the working tree while Git can still reason about repository history.

### Troubleshooting Path
```text
expected path missing
  ↓
git sparse-checkout list
  ↓
adjust patterns
  ↓
verify branch contains path
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 53 — Shallow Clone Tradeoffs in CI

### Objective
Demonstrate **Shallow Clone Tradeoffs in CI** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git rev-parse --is-shallow-repository
git fetch --deepen=50
git fetch --unshallow 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
A shallow job has the history it needs for its task or explicitly deepens before history-dependent operations.

### Troubleshooting Path
```text
history-dependent CI fails
  ↓
is repository shallow?
  ↓
required merge base/tag present?
  ↓
deepen/unshallow
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 54 — Partial Clone and Promisor Objects

### Objective
Demonstrate **Partial Clone and Promisor Objects** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git clone --filter=blob:none <url> repo-partial 2>/dev/null || true
git config --get remote.origin.promisor 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Initial clone transfers fewer blobs, and missing objects are retrieved when operations require them.

### Troubleshooting Path
```text
offline operation fails
  ↓
partial clone?
  ↓
missing promised object?
  ↓
remote available?
  ↓
prefetch required objects
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 55 — Submodules as Exact External Commit Pointers

### Objective
Demonstrate **Submodules as Exact External Commit Pointers** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git submodule status
git diff --submodule
git -C path/to/submodule status
git submodule update --init --recursive
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The submodule is checked out at the commit recorded by the parent repository.

### Troubleshooting Path
```text
submodule appears modified
  ↓
is child working tree dirty?
  ↓
is child at different commit?
  ↓
is parent pointer intentionally changing?
  ↓
commit child first if developing it
  ↓
update parent pointer
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 56 — Subtree as an Alternative Integration Model

### Objective
Demonstrate **Subtree as an Alternative Integration Model** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git subtree add --prefix=vendor/tool <remote> main --squash 2>/dev/null || true
git subtree pull --prefix=vendor/tool <remote> main --squash 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Consumers receive the vendored content with an ordinary clone; updates are explicit subtree operations.

### Troubleshooting Path
```text
vendor code outdated
  ↓
identify upstream/version
  ↓
subtree pull
  ↓
review diff
  ↓
test
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 57 — Git Worktrees for Parallel Operational Branches

### Objective
Demonstrate **Git Worktrees for Parallel Operational Branches** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git worktree add ../repo-hotfix hotfix
git worktree list
git worktree remove ../repo-hotfix
git worktree prune
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Each worktree has its own checked-out branch and working files while sharing repository objects.

### Troubleshooting Path
```text
cannot checkout branch
  ↓
git worktree list
  ↓
is branch already checked out elsewhere?
  ↓
use that worktree or choose another branch
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 58 — Bisect as a Scientific Debugging Workflow

### Objective
Demonstrate **Bisect as a Scientific Debugging Workflow** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git bisect start
git bisect bad HEAD
git bisect good <known-good>
# test
git bisect good   # or bad
git bisect reset
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Git identifies the first commit that transitions from good to bad under the classification supplied.

### Troubleshooting Path
```text
bisect unreliable
  ↓
is test deterministic?
  ↓
can every candidate build?
  ↓
use git bisect skip for untestable commits
  ↓
automate test if possible
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 59 — Automated Bisect and Exit Codes

### Objective
Demonstrate **Automated Bisect and Exit Codes** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
cat > test-regression.sh <<'EOF'
#!/usr/bin/env bash
set -e
./build.sh >/dev/null
./tests/smoke.sh
EOF
chmod +x test-regression.sh

git bisect run ./test-regression.sh
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Git walks history automatically and stops when it isolates the first bad commit or cannot determine uniquely.

### Troubleshooting Path
```text
bisect run gives strange result
  ↓
run test repeatedly on same commit
  ↓
check environment dependencies
  ↓
reset caches/state
  ↓
use exit 125 for untestable commits
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---

## Enhanced Lab 60 — Git for Infrastructure Change Control and GitOps

### Objective
Demonstrate **Git for Infrastructure Change Control and GitOps** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
git rev-parse HEAD
git show --stat --oneline HEAD

# Deployment record example:
echo "deployed_commit=$(git rev-parse HEAD)"
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Every production change can be correlated to an exact reviewed commit and an execution record.

### Troubleshooting Path
```text
production incident
  ↓
runtime symptom time
  ↓
deployment/reconciliation run
  ↓
commit ID
  ↓
review/test history
  ↓
revert or forward-fix desired state
  ↓
verify runtime converges
```

### Safety
Use a disposable repository for history rewriting, force-push simulation, secret-cleanup practice, object recovery, and destructive reset/prune experiments. Use only fake credentials/secrets in labs.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Configure Git

```bash
git --version
git config --global user.name "Lab User"
git config --global user.email "lab@example.com"
git config --global init.defaultBranch main
git config --list --show-origin
```

Explain which configuration file supplies each value.

### Lab 2 — Create the First Repository

```bash
mkdir phase10-git-lab
cd phase10-git-lab
git init

echo "# Infrastructure Lab" > README.md
git status
git add README.md
git commit -m "Initialize infrastructure lab"
```

### Lab 3 — Explore the Three States

Modify two files.

Stage only one.

Run:

```bash
git status
git diff
git diff --staged
```

Draw:

```text
Working Tree
Index
HEAD
```

and place each change correctly.

### Lab 4 — Partial Staging

Make two unrelated changes to one file.

Use:

```bash
git add -p
```

Create two separate commits.

### Lab 5 — Inspect Git Objects

```bash
git rev-parse HEAD
git cat-file -p HEAD
git cat-file -p <tree-id>
git cat-file -t <object-id>
```

Identify commit, tree, and blob.

### Lab 6 — Branching

```bash
git switch -c feature/nginx
```

Create two commits.

Switch to main and draw the graph with:

```bash
git log --oneline --graph --decorate --all
```

### Lab 7 — Fast-Forward Merge

Create a branch from main, make one commit, then:

```bash
git switch main
git merge feature/simple
```

Explain why no merge commit was required.

### Lab 8 — Three-Way Merge

Create independent commits on main and feature.

Merge and inspect the merge commit parents:

```bash
git show --pretty=raw HEAD
```

### Lab 9 — Merge Conflict

Edit the same line differently on two branches.

Merge, then resolve using:

```bash
git status
git diff
git add
git commit
```

Repeat and test:

```bash
git merge --abort
```

### Lab 10 — Rebase

Create divergence, then:

```bash
git switch feature/rebase
git rebase main
```

Draw commit IDs before and after.

Explain why they changed.

### Lab 11 — Interactive Rebase

Create four small local commits.

Run:

```bash
git rebase -i HEAD~4
```

Reword one and squash two.

Do not use a shared branch.

### Lab 12 — Local Bare Remote

Create a remote without Internet:

```bash
cd ..
git init --bare central.git

cd phase10-git-lab
git remote add origin ../central.git
git push -u origin main
```

### Lab 13 — Two-Developer Simulation

Clone twice:

```bash
git clone central.git dev-a
git clone central.git dev-b
```

Create changes from both clones and reproduce a non-fast-forward push.

Resolve safely.

### Lab 14 — Fetch vs Pull

From one clone:

```bash
git fetch origin
git log --oneline --graph --decorate --all
```

Inspect `origin/main` before integrating it.

Then merge/rebase explicitly.

### Lab 15 — `.gitignore`

Create:

```text
.env
app.log
.venv/
```

Add rules.

Verify with:

```bash
git status
git check-ignore -v .env
```

### Lab 16 — Reset Modes

Create disposable commits and test:

```bash
git reset --soft HEAD~1
git reset HEAD~1
git reset --hard HEAD~1
```

After each, record:

```text
branch
index
working tree
```

### Lab 17 — Revert

Create a bad but published-style commit.

Use:

```bash
git revert <commit>
```

Show that both the original and inverse commit remain in history.

### Lab 18 — Reflog Recovery

Create three commits.

Run a destructive reset.

Recover:

```bash
git reflog
git branch recovery <old-id>
```

Verify the files.

### Lab 19 — Stash

Create two uncommitted changes.

```bash
git stash push -m "Lab work"
git stash list
git stash show -p
git stash pop
```

Resolve a stash conflict if possible.

### Lab 20 — Tags

Create:

```bash
git tag -a v1.0.0 -m "First lab release"
git show v1.0.0
```

Push the tag to your local bare remote.

### Lab 21 — Bisect

Create a script whose output is correct in early commits and broken later.

Use:

```bash
git bisect start
git bisect bad
git bisect good <id>
```

Find the first bad commit.

### Lab 22 — Automated Bisect

Create:

```bash
./test.sh
```

that exits 0/1.

Run:

```bash
git bisect run ./test.sh
```

### Lab 23 — Worktrees

```bash
git branch hotfix
git worktree add ../phase10-hotfix hotfix
git worktree list
```

Work on feature and hotfix simultaneously.

### Lab 24 — Submodule

Create two disposable repositories and add one as a submodule.

Inspect:

```bash
cat .gitmodules
git submodule status
```

Clone with `--recurse-submodules`.

### Lab 25 — Git Hook

Create a local `pre-commit` hook that rejects files containing:

```text
DO_NOT_COMMIT_SECRET
```

Verify the commit is blocked.

Then explain why server/CI scanning is still required.

### Lab 26 — Git Attributes and Line Endings

Create:

```gitattributes
* text=auto
*.sh text eol=lf
*.ps1 text eol=crlf
```

Inspect normalized behavior on your OS.

### Lab 27 — Infrastructure Repository

Build:

```text
infra/
├── README.md
├── ansible/
├── scripts/
├── docs/
├── .gitignore
└── .gitattributes
```

Commit each logical step separately.

### Lab 28 — Pull Request Simulation

Without requiring a hosting provider, model:

```text
main
feature branch
review diff
tests
merge
```

Use:

```bash
git diff main...feature
git log main..feature
```

Write a review checklist.

### Lab 29 — Secret Incident Exercise

Commit a **fake** secret string in a disposable repository.

Then:

1. remove it from current tree;
2. inspect history and prove it still exists;
3. document the correct real-world response: rotate/revoke first;
4. practice history cleanup only with fake data.

### Lab 30 — Git Recovery Challenge

Solve all:

```text
deleted branch
bad hard reset
detached HEAD commit
merge conflict
non-fast-forward push
wrong commit message
accidentally staged file
old snapshot of remote branch
```

For each write:

```text
Symptom
Repository State
Safe Evidence Command
Recovery Command
Why It Works
```

---

## 6. Mini Project

# Mini Project — Version-Controlled Infrastructure Repository

Build a repository that will become the base for Courses 46 and 47.

Structure:

```text
infrastructure/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CHANGE_POLICY.md
│   ├── GIT_WORKFLOW.md
│   └── RECOVERY.md
├── ansible/
│   ├── inventories/
│   ├── playbooks/
│   └── roles/
├── scripts/
│   └── validate.sh
├── examples/
├── .gitignore
└── .gitattributes
```

Required workflow:

```text
main protected conceptually
   ↓
short-lived feature branch
   ↓
small commits
   ↓
review diff
   ↓
validation
   ↓
merge
   ↓
annotated release tag
```

Required scenarios:

```text
feature branch
hotfix
merge conflict
rebase
revert
reflog recovery
tagged release
secret incident tabletop
```

Write a `CHANGE_POLICY.md` that defines:

```text
branch naming
commit message style
review requirements
testing
secret handling
force-push policy
release tags
emergency rollback
```

---


# Expanded Capstone — Production-Grade Version-Controlled Infrastructure Repository

Build a repository that can act as the change-control foundation for Ansible, Terraform, Kubernetes, shell automation, CI/CD, security policy, and runbooks.

## Repository Structure

```text
infrastructure-platform/
├── README.md
├── .gitignore
├── .gitattributes
├── CODEOWNERS
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CHANGE_POLICY.md
│   ├── GIT_WORKFLOW.md
│   ├── RELEASE_POLICY.md
│   ├── SECURITY.md
│   ├── SECRET_INCIDENT.md
│   └── RECOVERY.md
├── ansible/
├── terraform/
├── kubernetes/
├── network/
├── scripts/
│   ├── lint.sh
│   ├── test.sh
│   └── scan-secrets.sh
├── tests/
├── examples/
└── .ci/
```

## Required Git Workflow

```text
Issue / Change Requirement
        |
short-lived branch
        |
atomic commits
        |
local validation
        |
push
        |
pull request
        |
CODEOWNERS review
        |
required CI
        |
protected main
        |
annotated/signed release tag where required
        |
deployment / reconciliation
```

## Required Branch Rules

Document:

```text
direct push to main
force push
branch deletion
required reviews
CODEOWNERS approval
required status checks
signed release policy
admin bypass policy
emergency process
```

## Required Commit Scenarios

Create and explain:

```text
fast-forward merge
three-way merge
merge conflict
rebase
interactive rebase
cherry-pick backport
revert
bad reset + reflog recovery
detached HEAD recovery
deleted branch recovery
worktree hotfix
non-fast-forward push
force-with-lease on an allowed personal branch
```

## Repository Security

Demonstrate with **fake** secrets only:

```text
ignored .env
pre-commit secret check
CI secret scan
secret incident response
history inspection
credential rotation as primary response
```

Document why:

```text
.gitignore != secret control
history rewrite != credential revocation
commit author metadata != strong identity
signed commit/tag != code safety
```

## Line Ending and File Policy

Create:

```gitattributes
* text=auto
*.sh text eol=lf
*.ps1 text eol=crlf
```

Verify:

```bash
git ls-files --eol
git check-attr -a -- scripts/deploy.sh
```

## Review Policy for Infrastructure

Every pull request should answer:

```text
What systems change?
What is the blast radius?
Is desired state idempotent?
What validation runs?
Are secrets exposed?
What is the rollback or forward-fix path?
Does this require a maintenance window?
What monitoring proves success?
```

## CI Requirements

Minimum checks:

```text
shell lint
YAML validation
secret scan
IaC validation
policy-as-code
unit/integration tests
documentation links
```

## Recovery Exercise

Create `docs/RECOVERY.md` for:

```text
bad hard reset
bad rebase
deleted branch
detached commit
wrong remote push
accidental secret commit
corrupted working tree
stale remote-tracking ref
```

For each:

```text
Symptom
Evidence Commands
Unsafe Commands to Avoid
Recovery
Verification
```

## Audit Chain

Demonstrate:

```text
Change ticket / issue
   |
Git commit
   |
Pull request
   |
CI run
   |
merge commit / release tag
   |
deployment run
   |
runtime verification
```

Explain what Git proves and what must come from the hosting platform, CI/CD, identity provider, and runtime logs.


## 7. Recommended Resources

This Markdown is intended to contain the full learning path needed for this phase.

For exact command options, use the Git manual installed with Git:

```bash
git help git
git help commit
git help rebase
git help reset
```

The official Git documentation is the authoritative reference for exact version-specific flags.

---

## 8. Certification Relevance

Git is foundational to:

```text
DevOps
Cloud Engineering
SRE
Infrastructure as Code
Cybersecurity Engineering
Platform Engineering
Backend Engineering
Configuration Management
Kubernetes
CI/CD
```

It is a direct prerequisite for:

```text
46. Configuration Management
47. Ansible
62–64. Infrastructure as Code / Terraform
65–69. DevOps and CI/CD
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Treat Git as cloud storage.  
  **Best practice:** understand commits, refs, branches, and local history.

- **Mistake:** `git add .` without review.  
  **Best practice:** inspect `git status`/`git diff` first.

- **Mistake:** Giant commits.  
  **Best practice:** make atomic coherent commits.

- **Mistake:** Weak messages such as `update`.  
  **Best practice:** record operational intent.

- **Mistake:** Rebase shared history casually.  
  **Best practice:** rewrite unpublished work; coordinate published rewrites.

- **Mistake:** `git push --force`.  
  **Best practice:** avoid force; when genuinely required on your own branch, prefer `--force-with-lease`.

- **Mistake:** Use reset on shared history.  
  **Best practice:** use revert for published changes.

- **Mistake:** Assume deleted commit is lost immediately.  
  **Best practice:** inspect reflog.

- **Mistake:** Commit secrets and then merely delete the file.  
  **Best practice:** rotate/revoke secret first because history retains it.

- **Mistake:** Store large VM images/backups in ordinary Git.  
  **Best practice:** use artifact/object storage or purpose-built large-file tooling.

- **Mistake:** Long-lived branches.  
  **Best practice:** integrate small changes frequently.

- **Mistake:** Use Git branches as environment configuration without a clear model.  
  **Best practice:** document environment/promotion strategy explicitly.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What are Git's three main working states?

**Short answer:** Working tree, index/staging area, and committed repository state.

### Q2. What does `git add` do?

**Short answer:** Updates the index with content intended for the next commit.

### Q3. What is a commit?

**Short answer:** A snapshot reference containing a tree, metadata, parent(s), and message.

### Q4. Blob vs tree?

**Short answer:** Blob stores file content; tree maps names/directories to blobs and other trees.

### Q5. What is a branch?

**Short answer:** A movable reference to a commit.

### Q6. What is HEAD?

**Short answer:** Reference describing the currently checked-out branch/commit.

### Q7. What is detached HEAD?

**Short answer:** HEAD points directly to a commit rather than a branch ref.

### Q8. Fast-forward merge?

**Short answer:** Branch pointer advances because no divergent commit needs combining.

### Q9. Three-way merge?

**Short answer:** Git combines two branch tips using their common ancestor.

### Q10. Merge vs rebase?

**Short answer:** Merge joins histories; rebase rewrites/replays commits onto a new base.

### Q11. Why avoid rebasing shared history?

**Short answer:** Rebase creates new commit IDs and disrupts collaborators who based work on old history.

### Q12. Fetch vs pull?

**Short answer:** Fetch updates remote-tracking refs; pull fetches then integrates.

### Q13. What is `origin/main`?

**Short answer:** Local remote-tracking ref recording last fetched state of remote `main`.

### Q14. What does `--force-with-lease` protect against?

**Short answer:** It refuses force update if the remote ref changed unexpectedly.

### Q15. Reset vs revert?

**Short answer:** Reset moves/rebuilds local history state; revert creates a new inverse commit.

### Q16. What is reflog?

**Short answer:** Local history of ref movements useful for recovering commits.

### Q17. What is stash?

**Short answer:** Temporary storage of uncommitted changes.

### Q18. What is an annotated tag?

**Short answer:** Named release/reference object with tagger metadata and message.

### Q19. What does `git bisect` do?

**Short answer:** Binary-searches commit history to find a regression.

### Q20. Why is Git valuable for infrastructure?

**Short answer:** It provides reviewable, auditable, reversible history for desired infrastructure and automation changes.

---

# Expanded Self-Assessment Bank — Git and Version Control Systems

### Q1. What is the most important operational lesson from **Git's Object Database and the Snapshot Graph**?
**Answer:** Learn the object graph before memorizing recovery commands.

### Q2. What is the most important operational lesson from **Porcelain vs Plumbing Commands**?
**Answer:** Use plumbing to understand Git, but avoid direct ref/object mutation unless you know the consequences.

### Q3. What is the most important operational lesson from **The Index as a Real Data Structure**?
**Answer:** Review `git diff --cached` before every meaningful commit.

### Q4. What is the most important operational lesson from **Conflict Stages in the Index**?
**Answer:** Resolve the desired final state, not merely 'pick ours' or 'pick theirs'.

### Q5. What is the most important operational lesson from **HEAD, Symbolic References, and Detached State**?
**Answer:** Detached HEAD is not an error; understand whether it is intentional before 'fixing' it.

### Q6. What is the most important operational lesson from **Commit Identity vs Authentication**?
**Answer:** Treat commit metadata as attribution; use independent controls for authentication and approval.

### Q7. What is the most important operational lesson from **Object Reachability and Why Recovery Works**?
**Answer:** Create a recovery branch before experimenting further with a potentially lost commit.

### Q8. What is the most important operational lesson from **Reflog Semantics and Limits**?
**Answer:** Do not rely on reflog as long-term backup; push or back up important history.

### Q9. What is the most important operational lesson from **Packfiles, Delta Compression, and Repository Size**?
**Answer:** Keep build artifacts, VM images, and database dumps out of ordinary Git history.

### Q10. What is the most important operational lesson from **Garbage Collection and Pruning Safety**?
**Answer:** Never run aggressive object cleanup while trying to recover lost work.

### Q11. What is the most important operational lesson from **Hash Algorithms and Object IDs**?
**Answer:** Use commit IDs as precise immutable references, but do not treat the hash algorithm alone as a full security-signature mechanism.

### Q12. What is the most important operational lesson from **Commit Graph Topology and First-Parent History**?
**Answer:** Choose log views based on the question you are answering.

### Q13. What is the most important operational lesson from **Merge Base as the Foundation of Integration**?
**Answer:** Understand the merge base before interpreting three-dot diffs.

### Q14. What is the most important operational lesson from **Fast-Forward, No-FF, and Merge Commit Policy**?
**Answer:** Document merge policy instead of letting every contributor choose a different history style.

### Q15. What is the most important operational lesson from **Squash Merge Semantics**?
**Answer:** Use squash merge intentionally when PR-level atomic history is more valuable than preserving branch ancestry.

### Q16. What is the most important operational lesson from **Three-Way Merge Conflict Resolution as Semantic Work**?
**Answer:** Treat conflict resolution as design review, especially for infrastructure and security configuration.

### Q17. What is the most important operational lesson from **`git rerere` and Repeated Conflict Reuse**?
**Answer:** Use rerere to reduce repetitive work, never to skip validation.

### Q18. What is the most important operational lesson from **Rebase as Commit Replay**?
**Answer:** Rebase local/unpublished work freely; coordinate before rewriting history that others consume.

### Q19. What is the most important operational lesson from **Interactive Rebase as Local History Editing**?
**Answer:** Create a backup branch before complex history surgery if the work is valuable.

### Q20. What is the most important operational lesson from **Rebase `--onto` for Surgical History Repair**?
**Answer:** Never use `--onto` until you can draw exactly which commits will be selected.

### Q21. What is the most important operational lesson from **Cherry-Pick and Duplicate Patch Identity**?
**Answer:** Use cherry-pick for deliberate isolated backports, not as a substitute for a coherent branching strategy.

### Q22. What is the most important operational lesson from **Remote-Tracking References Are Local Observations**?
**Answer:** Fetch first, inspect second, integrate third.

### Q23. What is the most important operational lesson from **Upstream Tracking Configuration**?
**Answer:** Verify upstream metadata after branch renames or repository migrations.

### Q24. What is the most important operational lesson from **Pull Strategies and Explicit Integration**?
**Answer:** Prefer explicit pull policy, especially on protected or release branches.

### Q25. What is the most important operational lesson from **Non-Fast-Forward Push Rejection as Data Protection**?
**Answer:** Never solve non-fast-forward rejection with force until you understand which remote commits would disappear.

### Q26. What is the most important operational lesson from **`--force-with-lease` and Optimistic Concurrency**?
**Answer:** Use force-with-lease only on branches whose rewrite policy is explicitly allowed.

### Q27. What is the most important operational lesson from **Remote Refspecs**?
**Answer:** Do not customize refspecs in ordinary repositories unless the workflow requires it.

### Q28. What is the most important operational lesson from **Remote Pruning and Deleted Branch Hygiene**?
**Answer:** Enable pruning if your team frequently deletes short-lived remote branches.

### Q29. What is the most important operational lesson from **Multiple Remotes and Trust Boundaries**?
**Answer:** Inspect remote URLs before publishing secrets, proprietary code, or security-sensitive infrastructure.

### Q30. What is the most important operational lesson from **Repository Migration Without Losing Intent**?
**Answer:** Treat repository hosting migration as a platform migration, not a file copy.

### Q31. What is the most important operational lesson from **`.gitignore` Matching Semantics**?
**Answer:** Use `git check-ignore -v` instead of guessing why a pattern behaves differently.

### Q32. What is the most important operational lesson from **Ignore Rules vs Security Controls**?
**Answer:** Design secret handling so the real secret never needs to exist in tracked form.

### Q33. What is the most important operational lesson from **`.gitattributes` and Repository-Wide Normalization**?
**Answer:** Store line-ending policy in `.gitattributes`, not only in developer-specific `core.autocrlf` settings.

### Q34. What is the most important operational lesson from **Renormalization After Attribute Changes**?
**Answer:** Never combine repository-wide EOL normalization with application logic changes.

### Q35. What is the most important operational lesson from **Executable Bit Tracking**?
**Answer:** Treat executable-bit changes as real reviewable repository changes.

### Q36. What is the most important operational lesson from **Git LFS and Large Binary Pointers**?
**Answer:** Use LFS only when the hosting/backup/CI environment supports its additional object store.

### Q37. What is the most important operational lesson from **History Rewriting for Secret Cleanup**?
**Answer:** Credential revocation is the incident response; history rewriting is repository hygiene.

### Q38. What is the most important operational lesson from **Commit and Tag Signing Models**?
**Answer:** Use signing as one layer in a broader trusted-release process.

### Q39. What is the most important operational lesson from **SSH Host Keys and Git Remote Trust**?
**Answer:** Treat SSH host-key changes as security events until independently verified.

### Q40. What is the most important operational lesson from **Credential Helpers and Token Storage**?
**Answer:** Use short-lived/scoped tokens and platform credential storage where possible.

### Q41. What is the most important operational lesson from **`safe.directory` and Repository Ownership Security**?
**Answer:** Do not solve ownership warnings by globally trusting `*` without understanding the security boundary.

### Q42. What is the most important operational lesson from **Hooks as Local Automation, Not Central Enforcement**?
**Answer:** Use hooks for developer ergonomics; enforce critical controls independently.

### Q43. What is the most important operational lesson from **CODEOWNERS and Review Routing**?
**Answer:** Use CODEOWNERS together with protected-branch rules; ownership suggestions alone are not enforcement.

### Q44. What is the most important operational lesson from **Protected Branches and Server-Side Rules**?
**Answer:** Treat branch rules as part of infrastructure change control and back up/document them.

### Q45. What is the most important operational lesson from **CI Status Checks as Merge Evidence**?
**Answer:** Keep required checks deterministic, documented, and fast enough that contributors do not feel pressure to bypass them.

### Q46. What is the most important operational lesson from **Merge Queues and Integration Race Conditions**?
**Answer:** For high-change protected branches, validate the merge result, not only each PR head.

### Q47. What is the most important operational lesson from **Trunk-Based Development for Infrastructure**?
**Answer:** Prefer small deployable changes over large branch-based batches.

### Q48. What is the most important operational lesson from **Release Branches and Backport Discipline**?
**Answer:** Track which supported branches received each security or operational fix.

### Q49. What is the most important operational lesson from **GitFlow Tradeoffs**?
**Answer:** Choose the simplest branching model that satisfies real release constraints.

### Q50. What is the most important operational lesson from **Monorepo Design and Atomic Cross-System Changes**?
**Answer:** Use monorepo only when atomic coordination and shared governance outweigh repository-scale complexity.

### Q51. What is the most important operational lesson from **Multirepo Design and Version Contracts**?
**Answer:** Use explicit version contracts between repositories.

### Q52. What is the most important operational lesson from **Sparse Checkout for Large Repositories**?
**Answer:** Use sparse checkout for ergonomics; combine with partial clone if transfer size is also a problem.

### Q53. What is the most important operational lesson from **Shallow Clone Tradeoffs in CI**?
**Answer:** Use the shallowest clone that still supports the pipeline's actual history operations.

### Q54. What is the most important operational lesson from **Partial Clone and Promisor Objects**?
**Answer:** Validate backup/offline workflows before standardizing partial clones.

### Q55. What is the most important operational lesson from **Submodules as Exact External Commit Pointers**?
**Answer:** Use submodules only when the team understands two-repository lifecycle and CI cloning requirements.

### Q56. What is the most important operational lesson from **Subtree as an Alternative Integration Model**?
**Answer:** Choose submodule, subtree, package registry, or vendoring based on dependency lifecycle—not familiarity alone.

### Q57. What is the most important operational lesson from **Git Worktrees for Parallel Operational Branches**?
**Answer:** Prefer worktrees over duplicate clones when you need simultaneous local branches.

### Q58. What is the most important operational lesson from **Bisect as a Scientific Debugging Workflow**?
**Answer:** Define the regression test first; bisect quality depends on classification quality.

### Q59. What is the most important operational lesson from **Automated Bisect and Exit Codes**?
**Answer:** Make automated bisect tests hermetic enough that commit state, not leftover environment state, determines the result.

### Q60. What is the most important operational lesson from **Git for Infrastructure Change Control and GitOps**?
**Answer:** Keep Git history, CI/CD audit logs, deployment identity, and runtime observability connected.


## Completion Checklist

- [ ] I understand the Git object model.
- [ ] I understand working tree/index/repository.
- [ ] I can stage selectively.
- [ ] I can create good commits.
- [ ] I understand branches and HEAD.
- [ ] I can merge and resolve conflicts.
- [ ] I can rebase safely.
- [ ] I understand remotes/fetch/pull/push.
- [ ] I understand reset/restore/revert.
- [ ] I can recover with reflog.
- [ ] I can use stash/tags/bisect/worktree.
- [ ] I understand submodules/hooks/attributes.
- [ ] I understand secret and binary-file risks.
- [ ] I understand team workflows and protected branches.
- [ ] I understand Git for Infrastructure as Code.
- [ ] I completed all 30 labs.
- [ ] I completed the Version-Controlled Infrastructure Repository project.
