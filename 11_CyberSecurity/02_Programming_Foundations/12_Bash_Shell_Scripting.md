# Bash Shell Scripting

> **Phase 2 — Programming Foundations**

This version is intentionally example-driven. Every major concept includes code, execution reasoning, and practical infrastructure/security-oriented examples. Do not only read the code: type it, change it, break it, and repair it.

## 1. Topic Title

**Bash Shell Scripting**

## 2. Learning Objectives

- Understand command execution, exit status, expansions, and quoting.
- Use variables, conditions, loops, functions, pipelines, and redirection safely.
- Automate Linux operational tasks defensively.
- Use common text-processing commands.
- Structure maintainable scripts with logging, cleanup, CLI handling, and safe filesystem operations.

## 3. Prerequisites

- Phase 1 Operating Systems Fundamentals.
- Basic Linux terminal navigation.
- Introduction to Programming.

## 4. Core Concepts Explanation

### 1. Bash Command Execution and Exit Status

Every command returns an exit status. Convention: `0` success, non-zero failure.

```bash
mkdir demo
printf 'exit=%s\n' "$?"
```

Use status directly:

```bash
if grep -q 'ERROR' app.log; then
    echo "errors detected"
else
    echo "no matching errors"
fi
```

`&&` and `||` are status-driven:

```bash
mkdir -p reports && echo "directory ready"
command_that_may_fail || echo "command failed" >&2
```

Do not parse human-readable output when a command already communicates success through status.

### 2. Variables and Why Quoting Matters

Assignment has no spaces around `=`:

```bash
host="web-01"
port=443
printf '%s:%s\n' "$host" "$port"
```

Unquoted expansion can split words and expand wildcards:

```bash
path="reports/my report.txt"

# risky
# cat $path

# correct
cat "$path"
```

Safe default: **quote variable and command-substitution expansions** unless you intentionally need splitting/globbing.

### 3. Environment Variables

A normal shell variable is not automatically inherited by child processes.

```bash
APP_ENV=prod
export APP_ENV
python app.py
```

Or:

```bash
APP_ENV=prod python app.py
```

In Python:

```python
import os
print(os.getenv("APP_ENV"))
```

Environment variables are common configuration mechanisms in containers and CI/CD, but they are not a complete secret-management solution.

### 4. Quoting Rules: Single vs Double Quotes

Single quotes preserve literal text:

```bash
name="Ahmed"
echo '$name'   # prints: $name
```

Double quotes allow expansion:

```bash
echo "$name"   # prints: Ahmed
```

Command substitution:

```bash
now="$(date -Iseconds)"
echo "$now"
```

When building scripts, many bugs that appear to be "Bash weirdness" are actually quoting/expansion mistakes.

### 5. Redirection and Standard Streams

Three standard streams:

```text
0 stdin
1 stdout
2 stderr
```

Examples:

```bash
command >output.txt
command >>output.txt
command 2>error.txt
command >output.txt 2>error.txt
```

A good CLI sends normal machine-readable result to stdout and diagnostics/errors to stderr.

```bash
log_error() {
    printf 'ERROR: %s\n' "$*" >&2
}
```

This allows pipelines to consume data without accidentally consuming error messages.

### 6. Pipelines and pipefail

Pipeline:

```bash
grep 'ERROR' app.log | awk '{print $3}' | sort | uniq -c
```

Without `pipefail`, pipeline status is normally the status of the last command. Enable:

```bash
set -o pipefail
```

Now an earlier failure can cause the pipeline to fail.

Example:

```bash
if ! grep 'ERROR' app.log | sort >errors.txt; then
    echo "pipeline failed" >&2
fi
```

Be aware that `grep` returning `1` can mean "no matches" rather than operational failure. Understand command-specific exit semantics.

### 7. Conditions and [[ ... ]]

File tests:

```bash
config="/etc/myapp/config.conf"

if [[ -f "$config" && -r "$config" ]]; then
    echo "config exists and is readable"
else
    echo "config missing/unreadable" >&2
fi
```

String validation:

```bash
if [[ -z "${APP_ENV:-}" ]]; then
    echo "APP_ENV is required" >&2
    exit 2
fi
```

Numeric comparison:

```bash
usage=92
if (( usage >= 90 )); then
    echo critical
fi
```

### 8. Loops and Safe Line Reading

For loop over explicit values:

```bash
for service in nginx sshd docker; do
    echo "checking $service"
done
```

Safe line reading:

```bash
while IFS= read -r line; do
    printf 'record=%s\n' "$line"
done < servers.txt
```

Avoid:

```bash
# bad: breaks on whitespace/globbing
# for file in $(ls *.log); do ...; done
```

Use globbing directly:

```bash
for file in ./*.log; do
    [[ -e "$file" ]] || continue
    printf '%s\n' "$file"
done
```

### 9. Functions and local Variables

```bash
log_info() {
    local message=$1
    printf '%s INFO %s\n' "$(date -Iseconds)" "$message"
}

require_file() {
    local path=$1
    if [[ ! -f "$path" ]]; then
        printf 'missing file: %s\n' "$path" >&2
        return 1
    fi
}

if require_file "app.log"; then
    log_info "log file ready"
fi
```

Functions return status with `return 0..255`; larger structured results should normally be printed carefully or handled through another mechanism/file/tool.

### 10. case and Command-Line Interfaces

`case` is ideal for subcommands:

```bash
case "${1:-}" in
    health)
        echo "running health check"
        ;;
    logs)
        echo "analyzing logs"
        ;;
    --help|-h|"")
        echo "usage: $0 {health|logs}"
        ;;
    *)
        echo "unknown command: $1" >&2
        exit 2
        ;;
esac
```

This pattern later maps naturally to DevOps utility scripts.

### 11. grep, awk, sed, sort, uniq

Given synthetic log lines:

```text
2026-08-17 ERROR auth failed-login
2026-08-17 INFO api request-ok
2026-08-17 ERROR db timeout
2026-08-17 ERROR auth failed-login
```

Count error component frequency:

```bash
grep ' ERROR ' app.log | awk '{print $3}' | sort | uniq -c | sort -nr
```

Output:

```text
2 auth
1 db
```

For complex CSV/JSON, use format-aware tools (`jq`, Python `csv`, etc.) instead of fragile whitespace parsing.

### 12. find and Safe Filesystem Automation

Find `.log` files older than 7 days:

```bash
find /var/tmp/myapp -type f -name '*.log' -mtime +7 -print
```

Before deleting, dry-run first. A safer script pattern:

```bash
base="/var/tmp/myapp"

if [[ ! -d "$base" ]]; then
    echo "invalid base directory" >&2
    exit 2
fi

find "$base" -type f -name '*.log' -mtime +7 -print
```

Only add deletion after validating the target and understanding `find` behavior. Filesystem automation has a large blast radius when variables are wrong.

### 13. set -u, -e, and pipefail

A common strict-mode style:

```bash
set -u
set -o pipefail
```

`set -e` is often added:

```bash
set -euo pipefail
```

But `-e` has nuanced semantics around conditions, pipelines, subshells, and command lists. Do not assume it replaces explicit error handling.

For critical operations:

```bash
if ! cp -- "$source" "$destination"; then
    echo "copy failed" >&2
    exit 1
fi
```

Explicit checks document intent clearly.

### 14. trap and Temporary Resources

Create a safe temp directory:

```bash
tmpdir="$(mktemp -d)"

cleanup() {
    rm -rf -- "$tmpdir"
}

trap cleanup EXIT
```

Now normal exit and many failure paths clean the temporary directory. Validate variables carefully before destructive cleanup commands.

### 15. Worked Example: Operations Health Script

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

log() {
    local level=$1
    shift
    printf '%s %-5s %s\n' "$(date -Iseconds)" "$level" "$*"
}

check_disk() {
    local threshold=${1:-90}
    local usage

    usage=$(df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}') || return 1

    if (( usage >= threshold )); then
        log WARN "root filesystem usage=${usage}%"
        return 1
    fi

    log INFO "root filesystem usage=${usage}%"
    return 0
}

main() {
    local failed=0
    check_disk 90 || failed=1
    return "$failed"
}

main "$@"
```

This example shows:

- functions,
- local variables,
- command substitution,
- pipeline parsing,
- arithmetic condition,
- logging,
- meaningful return status.

For production use, you would also validate command availability and account for platform differences in `df` output.


# Enhanced Deep-Dive — Bash Execution, Automation, Reliability, and Security

The original material already establishes the most important Bash habits: quoting, exit-status-driven control flow, pipelines, `pipefail`, arrays, associative arrays, safe line reading, `find`, `mktemp`, traps, dry-run behavior, ShellCheck, and defensive automation. This enhancement preserves those foundations and expands the course into the shell-execution model, advanced parameter expansion, file descriptors, job control, reliable concurrency, testability, portability, idempotency, atomic updates, locking, structured output, security hardening, and production-grade script architecture.

The main mental model for this course is:

```text
User / CI / systemd / cron
        ↓
      Bash
        ↓
Parse shell grammar
        ↓
Perform expansions
        ↓
Construct argument vector
        ↓
Apply redirections
        ↓
Execute builtin/function/external process
        ↓
Collect exit status
        ↓
Control flow / pipeline / trap / caller
```

A second engineering model is:

```text
Requirement
   ↓
Validate inputs
   ↓
Preserve argument boundaries
   ↓
Execute smallest safe command
   ↓
Check exact exit semantics
   ↓
Emit stable stdout
   ↓
Emit diagnostics to stderr
   ↓
Clean up resources
   ↓
Return meaningful status
```


### Deep Dive — Shell, Terminal, and Process Model

A terminal is an interface for interacting with a process. A shell is a command interpreter. Bash is one shell implementation.

When Bash launches an external command, the command normally becomes a child process. Shell builtins such as `cd`, `export`, `read`, and `umask` must often execute inside the current shell because they modify shell/process state.

#### Mental Model

```text
Terminal
   ↓
Bash process
├─ builtin: cd
├─ function: log
└─ external command
       ↓
    child process
```

#### Example

```bash
type cd
type printf
type grep
command -V awk
```

#### Why It Matters

Understanding whether a command is a builtin, function, alias, or external executable explains scope, performance, and side effects.



### Deep Dive — How Bash Finds a Command

For a command name, Bash may resolve aliases, functions, builtins, hashed locations, and executables on `PATH`.

Use `type` or `command -V` when diagnosing which implementation is actually running.

#### Example

```bash
type -a printf
type -a python
command -v shellcheck
```

#### Practical Use

Debugging PATH problems, minimal containers, CI runners, and shadowed commands.

#### Common Failure / Troubleshooting

Do not assume `which` fully describes shell resolution semantics. `command -v` or `type` is generally more useful inside Bash.



### Deep Dive — The Parse-and-Expansion Pipeline

Bash does not simply replace `$var` and execute text. It parses shell syntax and then performs several expansions.

A simplified mental model is:

1. Parse shell operators and quoting.
2. Brace expansion.
3. Tilde expansion.
4. Parameter/variable expansion.
5. Command substitution.
6. Arithmetic expansion.
7. Word splitting where allowed.
8. Filename generation/globbing where allowed.
9. Quote removal.
10. Redirection setup.
11. Command execution.

The exact Bash rules are nuanced, but this model explains why quoting is central.

#### Mental Model

```text
source text
   ↓
shell grammar
   ↓
expansions
   ↓
word splitting?
   ↓
globbing?
   ↓
final argv[]
   ↓
exec / builtin
```

#### Why It Matters

Many shell bugs are actually argument-construction bugs.



### Deep Dive — Argument Boundaries Are the Core Safety Concept

Programs do not receive one command string. They receive an array of arguments.

Quoting preserves intended argument boundaries.

#### Mental Model

```text
Wanted:

argv[0] = cat
argv[1] = reports/my report.txt

Unquoted expansion may become:

argv[0] = cat
argv[1] = reports/my
argv[2] = report.txt
```

#### Example

```bash
path="reports/my report.txt"

printf '<%s>\n' "$path"
# one argument

# printf '<%s>\n' $path
# potentially multiple arguments
```

#### Why It Matters

Thinking in argv rather than text is one of the strongest Bash mental models.



### Deep Dive — Single Quotes, Double Quotes, and ANSI-C Quotes

Single quotes suppress shell expansion. Double quotes preserve most expansion while preventing word splitting and globbing of expanded results.

Bash also supports ANSI-C quoting `$'...'`, which interprets escape sequences such as `\n` and `\t`.

#### Example

```bash
name="Ahmed"

printf '%s\n' '$name'
printf '%s\n' "$name"
printf '%s\n' $'line1\nline2'
```

#### Expected Behavior / Output

```text
$name
Ahmed
line1
line2
```

#### Common Failure / Troubleshooting

Use `$'...'` only when you explicitly need interpreted escapes. Ordinary data should usually remain ordinary quoted strings.



### Deep Dive — `printf` vs `echo`

`printf` is generally more predictable for scripts because its format behavior is explicit.

`echo` behavior around options and backslash escapes varies across implementations.

#### Example

```bash
printf '%s\n' "$message"
printf 'count=%d\n' "$count"
printf 'path=<%s>\n' "$path"
```

#### Why It Matters

Stable output matters when scripts feed other automation.



### Deep Dive — Special Parameters

Bash exposes useful special parameters:

```text
$0      script/shell name
$1..$9  positional parameters
$#      argument count
"$@"    all positional arguments, preserving boundaries
"$*"    all positional arguments as one combined expansion inside quotes
$?      previous exit status
$$      current shell PID
$!      PID of most recent background job
```

#### Example

```bash
printf 'script=%s\n' "$0"
printf 'argc=%d\n' "$#"

for arg in "$@"; do
    printf 'arg=<%s>\n' "$arg"
done
```

#### Why It Matters

`"$@"` is the normal way to forward arbitrary arguments safely.



### Deep Dive — `$@` vs `$*`

Inside double quotes, `"$@"` preserves each positional parameter as a separate argument.

`"$*"` joins all positional parameters into a single argument using the first character of `IFS`.

#### Example

```bash
show() {
    printf 'argc=%d\n' "$#"
    printf '<%s>\n' "$@"
}

forward_at() {
    show "$@"
}

forward_star() {
    show "$*"
}
```

#### Why It Matters

This difference is critical when writing wrapper scripts.



### Deep Dive — Parameter Expansion Defaults and Required Values

Bash can validate or supply defaults during parameter expansion.

```text
${VAR:-default}  use default if unset or empty
${VAR-default}   use default if unset only
${VAR:=default}  assign default if unset or empty
${VAR:?message}  fail expansion if unset/empty
${VAR:+value}    substitute value if VAR is set/non-empty
```

#### Example

```bash
region=${REGION:-eu-west-1}
: "${APP_ENV:?APP_ENV is required}"

printf 'region=%s env=%s\n' "$region" "$APP_ENV"
```

#### Why It Matters

These forms are concise, but use explicit validation when business rules are more complex.



### Deep Dive — Substring, Length, and Pattern Parameter Expansion

Bash can manipulate simple strings without launching external tools.

Examples:
- `${#var}` length
- `${var#pattern}` remove shortest matching prefix
- `${var##pattern}` remove longest prefix
- `${var%pattern}` remove shortest suffix
- `${var%%pattern}` remove longest suffix
- `${var/pat/repl}` replace first match
- `${var//pat/repl}` replace all matches

#### Example

```bash
file="/var/log/app/server.log"

name=${file##*/}
dir=${file%/*}
stem=${name%.log}

printf 'dir=%s name=%s stem=%s\n' "$dir" "$name" "$stem"
```

#### Why It Matters

For simple shell-native transformations, this avoids unnecessary subprocesses.



### Deep Dive — Indirect Expansion and Nameref Awareness

`${!name}` performs indirect expansion: the value of one variable is used as another variable name.

Modern Bash also supports name references with `declare -n`, useful in reusable functions but easy to overuse.

#### Example

```bash
require_env() {
    local name=$1

    if [[ -z "${!name:-}" ]]; then
        printf 'missing environment variable: %s\n' "$name" >&2
        return 1
    fi
}
```

#### Why It Matters

Indirect behavior is powerful but harder to read; prefer direct variables when practical.



### Deep Dive — Arithmetic Expansion and Arithmetic Context

Bash supports integer arithmetic.

Use:
- `$(( ... ))` to produce a numeric expansion.
- `(( ... ))` as arithmetic command context.

#### Example

```bash
count=4
next=$((count + 1))

if (( next >= 5 )); then
    printf 'threshold reached\n'
fi

((count += 1))
```

#### Why It Matters

Do not use string comparison operators for numeric logic.



### Deep Dive — `[[ ... ]]` vs `[ ... ]`

`[[ ... ]]` is a Bash conditional construct with safer parsing and richer features such as pattern matching and regex matching.

`[ ... ]` is the traditional test command and is more portable to POSIX shell.

#### Example

```bash
value="web-01"

if [[ "$value" == web-* ]]; then
    printf 'web host\n'
fi

if [[ "$value" =~ ^web-[0-9]+$ ]]; then
    printf 'valid pattern\n'
fi
```

#### Why It Matters

Use `[[ ... ]]` in Bash-specific scripts unless POSIX portability is a requirement.



### Deep Dive — Regex Matching in Bash

Inside `[[ string =~ regex ]]`, Bash performs regular-expression matching.

The right-hand regex should normally not be quoted as a whole when you intend regex semantics.

#### Example

```bash
threshold=${1:-}

if [[ ! "$threshold" =~ ^[0-9]+$ ]]; then
    printf 'threshold must be an integer\n' >&2
    exit 2
fi
```

#### Common Failure / Troubleshooting

Regex syntax is not the same as glob syntax. Keep complex parsing in dedicated tools or Python.



### Deep Dive — `case` Patterns

`case` is not only for subcommands. It is also a clear pattern-matching tool.

#### Example

```bash
case "$filename" in
    *.log)  kind=log ;;
    *.json) kind=json ;;
    *.csv)  kind=csv ;;
    *)      kind=unknown ;;
esac
```

#### Why It Matters

Readable multi-branch matching is often clearer than repeated `if` statements.



### Deep Dive — Globbing and Filename Expansion

Patterns such as `*.log` are expanded by the shell before the command runs.

This means the target command usually receives actual matching filenames rather than the literal wildcard.

#### Mental Model

```text
command *.log
   ↓ shell globbing
command a.log b.log c.log
   ↓
program receives 3 filename arguments
```

#### Example

```bash
for file in ./*.log; do
    [[ -e "$file" ]] || continue
    printf '%s\n' "$file"
done
```

#### Why It Matters

Understanding who expands the wildcard prevents many command-line misconceptions.



### Deep Dive — `nullglob`, `failglob`, and `dotglob` Awareness

Bash `shopt` options can change glob behavior.

- `nullglob`: unmatched glob expands to nothing.
- `failglob`: unmatched glob causes an error.
- `dotglob`: `*` can include hidden names.

These settings affect surrounding code, so use them deliberately and document them.

#### Example

```bash
shopt -s nullglob
files=(./*.log)
shopt -u nullglob

printf 'log_count=%d\n' "${#files[@]}"
```

#### Why It Matters

Arrays plus controlled glob options are useful for predictable batch processing.



### Deep Dive — Arrays

Indexed arrays preserve element boundaries and are one of the safest ways to build commands dynamically.

#### Example

```bash
services=("ssh server" "nginx" "docker")

for service in "${services[@]}"; do
    printf 'checking <%s>\n' "$service"
done
```

#### Why It Matters

Arrays are preferred over concatenating command strings.



### Deep Dive — Command Arrays Instead of Command Strings

If a command is dynamic, store each argument in an array and invoke the array.

Do not build one string and pass it through `eval`.

#### Example

```bash
cmd=(find "$base" -type f -name '*.log')

if [[ -n "${days:-}" ]]; then
    cmd+=(-mtime "+$days")
fi

cmd+=(-print)

"${cmd[@]}"
```

#### Why It Matters

Argument boundaries remain explicit and untrusted text does not become shell syntax.



### Deep Dive — Associative Arrays

Associative arrays provide simple key/value mappings.

#### Example

```bash
declare -A ports=(
    [ssh]=22
    [http]=80
    [https]=443
)

for name in "${!ports[@]}"; do
    printf '%s=%s\n' "$name" "${ports[$name]}"
done
```

#### Practical Use

Small lookup tables and simple counters.

#### Common Failure / Troubleshooting

If the data becomes nested or schema-heavy, move to Python or a structured format.



### Deep Dive — `read`, IFS, and Backslash Safety

The robust line-reading pattern is:

```bash
while IFS= read -r line; do
    ...
done
```

- `IFS=` prevents trimming/splitting.
- `-r` prevents backslash interpretation.

#### Example

```bash
while IFS= read -r line; do
    printf '<%s>\n' "$line"
done < input.txt
```

#### Why It Matters

This preserves line content as data.



### Deep Dive — `mapfile` / `readarray`

Bash can load lines directly into an array with `mapfile` (also called `readarray`).

#### Example

```bash
mapfile -t lines < servers.txt

for line in "${lines[@]}"; do
    printf '<%s>\n' "$line"
done
```

#### Why It Matters

Useful for moderate-size inputs when retaining all lines is acceptable.

#### Common Failure / Troubleshooting

Do not load enormous streams into memory when streaming processing is sufficient.



### Deep Dive — Command Substitution

`$(command)` captures stdout into a shell expansion.

Trailing newlines are removed by command substitution.

#### Example

```bash
now="$(date -Iseconds)"
printf 'time=%s\n' "$now"
```

#### Common Failure / Troubleshooting

Do not capture huge output into one variable. Keep large data as a stream or file.



### Deep Dive — Subshells and Group Commands

Parentheses create a subshell environment. Braces group commands in the current shell.

#### Example

```bash
value=1
(value=2)
printf '%s\n' "$value"   # 1

{ value=3; }
printf '%s\n' "$value"   # 3
```

#### Why It Matters

This distinction matters for variable scope, current directory, traps, and pipeline behavior.



### Deep Dive — Pipeline Subshell Behavior

Shells often run pipeline stages in separate process environments. A classic surprise is modifying a variable inside a `while` loop fed by a pipe and losing the change afterward.

#### Example

```bash
count=0

while IFS= read -r line; do
    ((count += 1))
done < <(printf '%s\n' a b c)

printf 'count=%d\n' "$count"
```

#### Expected Behavior / Output

```text
count=3
```

#### Why It Matters

Process substitution lets the loop run in the current shell in this pattern.



### Deep Dive — Process Substitution

Process substitution `< <(command)` or `>(command)` exposes a command's stream through a filename-like interface.

It is Bash-specific.

#### Example

```bash
while IFS= read -r service; do
    printf 'service=%s\n' "$service"
done < <(printf '%s\n' sshd nginx docker)
```

#### Practical Use

Feed command output into a loop without the common pipeline-subshell variable issue.



### Deep Dive — Here Documents

A here-document supplies multi-line stdin to a command.

#### Example

```bash
cat <<'EOF'
literal $HOME
literal $(date)
EOF
```

#### Why It Matters

Quoting the delimiter prevents shell expansion inside the document.

#### Practical Use

Generate config snippets, test input, SQL/CLI input where appropriate.



### Deep Dive — Here Strings

A here-string sends one expanded string to a command's stdin.

#### Example

```bash
read -r first rest <<< "alpha beta gamma"
printf 'first=%s rest=%s\n' "$first" "$rest"
```

#### Why It Matters

Useful for small local strings; avoid for huge data.



### Deep Dive — Standard File Descriptors

Every process conventionally starts with:

```text
0 stdin
1 stdout
2 stderr
```

Redirection changes where those descriptors point before command execution.

#### Mental Model

```text
keyboard/file → fd 0 → process
process → fd 1 → terminal/file/pipe
process → fd 2 → terminal/error file
```

#### Why It Matters

File-descriptor thinking makes redirection much easier to reason about.



### Deep Dive — Redirection Ordering

Redirections are processed left to right, and order can change the result.

#### Example

```bash
command >all.log 2>&1

# stdout first goes to all.log
# stderr is then duplicated to the same destination
```

#### Why It Matters

This is different from redirecting stderr first and then moving stdout elsewhere.



### Deep Dive — Custom File Descriptors

Scripts can open additional descriptors for dedicated logs or data streams.

#### Example

```bash
exec 3>>audit.log

printf '%s INFO started\n' "$(date -Iseconds)" >&3

exec 3>&-
```

#### Why It Matters

Useful when stdout must remain machine-readable while diagnostics/audit go elsewhere.



### Deep Dive — `exec` for Redirection and Process Replacement

`exec` without a command can modify the current shell's file descriptors. With a command, it replaces the shell process with the target command.

#### Example

```bash
# Redirect all later stderr from this shell:
exec 2>>script-errors.log

# At the end of a wrapper:
# exec python app.py "$@"
```

#### Why It Matters

Process replacement avoids an unnecessary wrapper process when no post-command cleanup is needed.



### Deep Dive — Pipelines and `PIPESTATUS`

`pipefail` gives one aggregate pipeline status, but Bash also provides `PIPESTATUS`, an array containing each stage's status immediately after the pipeline.

#### Example

```bash
grep 'ERROR' app.log | sort | uniq -c
statuses=("${PIPESTATUS[@]}")

printf 'grep=%s sort=%s uniq=%s\n'     "${statuses[0]}" "${statuses[1]}" "${statuses[2]}"
```

#### Why It Matters

Useful when different pipeline stages have different meaningful exit semantics.



### Deep Dive — `set -e` Nuance

`set -e` (`errexit`) is not a universal exception mechanism. Its behavior changes in contexts such as condition tests, `&&`, `||`, pipeline elements, command substitutions, and subshells.

Use it as one layer, not as your complete error-handling strategy.

#### Example

```bash
set -euo pipefail

if ! cp -- "$source" "$destination"; then
    printf 'copy failed: %s -> %s\n' "$source" "$destination" >&2
    exit 1
fi
```

#### Why It Matters

Explicit handling communicates which failures are expected and what should happen.



### Deep Dive — `set -u` and Safe Defaults

`set -u` treats expansion of an unset variable as an error.

Use parameter-expansion defaults when optional variables are legitimate.

#### Example

```bash
set -u

region=${REGION:-eu-west-1}
verbose=${VERBOSE:-0}
```

#### Common Failure / Troubleshooting

An unset optional parameter can terminate a script if expanded directly under `set -u`.



### Deep Dive — `pipefail` and Command-Specific Exit Codes

`pipefail` surfaces earlier pipeline failures, but some commands use non-zero statuses for normal states.

`grep` commonly uses:
- 0 → match
- 1 → no match
- 2 → error

#### Example

```bash
grep -q 'ERROR' "$logfile"
status=$?

case $status in
    0) printf 'matches found\n' ;;
    1) printf 'no matches\n' ;;
    *) printf 'grep failed\n' >&2; exit "$status" ;;
esac
```

#### Why It Matters

A non-zero status is not automatically 'unexpected failure'; understand each command's contract.



### Deep Dive — Functions, `local`, and Return Status

Functions should usually use local variables and communicate success/failure through return status.

Return codes are 0–255. Complex data should normally be written to stdout, files, arrays passed by reference, or a more suitable language.

#### Example

```bash
require_file() {
    local path=$1

    [[ -f "$path" && -r "$path" ]] || {
        printf 'invalid file: %s\n' "$path" >&2
        return 1
    }
}
```

#### Why It Matters

Local scope reduces accidental coupling between functions.



### Deep Dive — Output vs Return Value

A common Bash mistake is confusing function stdout with return status.

```text
stdout → data
return status → success/failure
```

#### Example

```bash
get_hostname() {
    hostname
}

if host=$(get_hostname); then
    printf 'host=%s\n' "$host"
else
    printf 'hostname lookup failed\n' >&2
fi
```

#### Why It Matters

This separation matches Unix process design.



### Deep Dive — Library Scripts and `BASH_SOURCE`

Reusable function libraries should be loaded relative to the script's own directory, not the caller's current working directory.

#### Example

```bash
script_dir=$(
    cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1
    pwd -P
)

# shellcheck source=lib/logging.sh
source "$script_dir/lib/logging.sh"
```

#### Why It Matters

A script should work whether launched from its own directory, `/tmp`, CI, or systemd.



### Deep Dive — Sourcing Is Code Execution

`source file` executes that file in the current shell.

Therefore a configuration file that is sourced is executable code, not merely data.

#### Mental Model

```text
trusted config.sh
    ↓ source
current shell executes statements

untrusted config data
    ✗ do not source
    ↓
parse as data with safe parser
```

#### Why It Matters

This is a major security boundary.



### Deep Dive — CLI Parsing with `while` + `case`

Manual long-option parsing is often clearer than forcing `getopts` to handle unsupported syntax.

#### Example

```bash
dry_run=0
output=""

while (($#)); do
    case "$1" in
        --dry-run)
            dry_run=1
            shift
            ;;
        --output)
            (($# >= 2)) || {
                printf 'missing --output value\n' >&2
                exit 2
            }
            output=$2
            shift 2
            ;;
        --)
            shift
            break
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            printf 'unknown option: %s\n' "$1" >&2
            exit 2
            ;;
    esac
done
```

#### Why It Matters

Every consumed option/value must be removed with the correct `shift`.



### Deep Dive — `getopts` Awareness

`getopts` is a shell builtin for short POSIX-style options such as `-v` and `-o file`.

It does not natively provide GNU-style long options such as `--output`.

#### Example

```bash
while getopts ":vo:" opt; do
    case "$opt" in
        v) verbose=1 ;;
        o) output=$OPTARG ;;
        :) printf 'missing value for -%s\n' "$OPTARG" >&2; exit 2 ;;
        \?) printf 'unknown option -%s\n' "$OPTARG" >&2; exit 2 ;;
    esac
done

shift "$((OPTIND - 1))"
```

#### Why It Matters

Useful for portable short-option CLIs.



### Deep Dive — Exit-Code Design

Scripts should return statuses that allow calling automation to make decisions.

A practical local convention might be:
- 0 success
- 1 operational failure
- 2 usage/configuration error
- other codes for explicitly documented cases

#### Why It Matters

Consistency matters more than inventing many codes.

#### Practical Use

CI jobs, systemd units, monitoring checks, wrapper scripts.



### Deep Dive — Logging and Structured Output

Keep machine-readable output on stdout and diagnostics on stderr.

For automation, stable key/value or JSON output is easier to consume than decorative terminal text.

#### Example

```bash
log() {
    local level=$1
    shift
    printf '%s %-5s %s\n' "$(date -Iseconds)" "$level" "$*" >&2
}

printf 'hostname=%s\n' "$(hostname)"
log INFO "health report completed"
```

#### Why It Matters

The caller can pipe stdout without accidentally consuming logs.



### Deep Dive — JSON Output with `jq`

For true JSON, use a JSON-aware tool rather than hand-escaping strings.

#### Example

```bash
jq -n   --arg host "$(hostname)"   --arg env "${APP_ENV:-unknown}"   '{hostname: $host, environment: $env}'
```

#### Why It Matters

Manual JSON construction breaks when values contain quotes, newlines, or control characters.



### Deep Dive — `grep`, `sed`, and `awk` Roles

A practical mental split:

- `grep`: select matching records.
- `sed`: simple stream transformations.
- `awk`: field-oriented processing and aggregation.

#### Example

```bash
awk '
    $2 == "ERROR" {
        count[$3]++
    }
    END {
        for (component in count)
            print count[component], component
    }
' app.log
```

#### Why It Matters

Do not create a long pipeline when one clear `awk` program is simpler.



### Deep Dive — Why Real CSV and JSON Need Format-Aware Parsers

Whitespace splitting is not CSV parsing. Commas can occur inside quoted CSV fields. JSON contains escaping, nesting, arrays, and types.

Use:
- `jq` for JSON
- Python `csv` for real CSV
- YAML-aware tools for YAML

#### Why It Matters

A parser must understand the format's grammar, not just delimiters.



### Deep Dive — `find -exec` vs `xargs`

`find -exec ... {} +` can batch matching paths into command invocations without using a text delimiter.

`xargs -0` is also robust when paired with null-delimited input.

#### Example

```bash
find "$base" -type f -name '*.log'     -exec wc -l -- {} +

find "$base" -type f -name '*.log' -print0 |
    xargs -0 -r wc -l
```

#### Why It Matters

Filenames can contain spaces, tabs, quotes, and newlines.



### Deep Dive — Null-Delimited Filename Processing

Newline is not a universally safe filename delimiter on Unix-like systems.

The null byte cannot appear inside a filename and is therefore the robust delimiter for arbitrary paths.

#### Mental Model

```text
filename1\0filename with spaces\0filename-with-newline\0
```

#### Practical Use

Bulk file processing, cleanup tools, archives, search pipelines.



### Deep Dive — Safe Temporary Files and Directories

Use `mktemp` rather than predictable shared names.

#### Example

```bash
workdir=$(mktemp -d) || {
    printf 'failed to create temporary directory\n' >&2
    exit 1
}

cleanup() {
    rm -rf -- "$workdir"
}

trap cleanup EXIT
```

#### Why It Matters

Predictable names can collide or interact with attacker-controlled filesystem objects.



### Deep Dive — `trap` and Signal Handling

`trap` can register handlers for shell exit and signals.

Common uses:
- cleanup
- restoring state
- removing lock files
- forwarding termination to child jobs

#### Example

```bash
cleanup() {
    printf 'cleanup\n' >&2
}

trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
```

#### Why It Matters

Shutdown behavior is part of script correctness.



### Deep Dive — Trap Inheritance and Scope Awareness

Traps interact with functions, subshells, command substitution, and child processes in nuanced ways.

Do not assume a trap automatically manages resources created by unrelated child processes.

#### Why It Matters

For complex process supervision, use systemd, a process supervisor, or a more suitable language.



### Deep Dive — Background Jobs and `$!`

Appending `&` starts a job asynchronously. `$!` captures the PID of the most recently launched background process.

#### Example

```bash
check_one web-01 &
pid=$!

if wait "$pid"; then
    printf 'check succeeded\n'
else
    status=$?
    printf 'check failed status=%d\n' "$status" >&2
fi
```

#### Why It Matters

Always collect background statuses if failure matters.



### Deep Dive — Parallel Jobs with `wait`

Parallelism can reduce wall-clock time for independent I/O-heavy checks, but complicates:
- output ordering
- failure aggregation
- rate limits
- shared files/state

#### Example

```bash
pids=()

for host in "${hosts[@]}"; do
    check_one "$host" &
    pids+=("$!")
done

failed=0
for pid in "${pids[@]}"; do
    wait "$pid" || failed=1
done

exit "$failed"
```

#### Why It Matters

Background work without `wait` can let scripts exit before work completes.



### Deep Dive — Bounded Parallelism

Launching thousands of jobs at once can exhaust CPU, memory, file descriptors, or remote service limits.

Use bounded concurrency.

#### Example

```bash
printf '%s\0' "${hosts[@]}" |
    xargs -0 -n1 -P4 bash -c '
        host=$1
        printf "checking %s\n" "$host"
    ' _
```

#### Why It Matters

Concurrency is a resource-management problem, not simply adding `&` everywhere.

#### Common Failure / Troubleshooting

Be cautious when embedding shell code in `bash -c`; positional parameters should be passed as arguments, not interpolated into the code string.



### Deep Dive — Locking with `flock` Awareness

Two copies of the same maintenance script can interfere with each other.

On Linux systems with `flock`, a lock file descriptor can serialize critical sections.

#### Example

```bash
exec 9>/run/lock/my-task.lock

if ! flock -n 9; then
    printf 'another instance is already running\n' >&2
    exit 1
fi
```

#### Why It Matters

Useful for cron/systemd jobs that must not overlap.

#### Common Failure / Troubleshooting

`flock` availability and filesystem semantics are platform-dependent.



### Deep Dive — Idempotency

An idempotent operation can be repeated without creating unintended additional changes.

Automation becomes safer when rerunning after partial failure produces the desired final state.

#### Example

```bash
mkdir -p -- "$target_dir"

if ! grep -qxF "$line" "$config"; then
    printf '%s\n' "$line" >>"$config"
fi
```

#### Why It Matters

CI/CD, provisioning, and recovery frequently retry operations.



### Deep Dive — Atomic File Replacement

For important generated files, write a complete temporary file first, validate it, then rename it into place.

On the same filesystem, rename is typically atomic from readers' perspective.

#### Example

```bash
tmp=$(mktemp "${config}.tmp.XXXXXX") || exit 1
trap 'rm -f -- "$tmp"' EXIT

generate_config >"$tmp" || exit 1
validate_config "$tmp" || exit 1

mv -f -- "$tmp" "$config"
trap - EXIT
```

#### Why It Matters

Avoid leaving half-written configuration after a failure.



### Deep Dive — Retry with Backoff

Retries are appropriate only for failures that are plausibly transient.

A bounded retry loop should:
- cap attempts
- log each attempt
- preserve final failure status
- delay between attempts

#### Example

```bash
retry() {
    local attempts=$1
    shift

    local i status

    for ((i=1; i<=attempts; i++)); do
        if "$@"; then
            return 0
        fi

        status=$?

        if (( i == attempts )); then
            return "$status"
        fi

        sleep "$i"
    done
}
```

#### Why It Matters

Blind infinite retry can hide persistent faults and create load storms.



### Deep Dive — Timeouts

Automation should not wait forever for external operations.

On GNU/Linux, `timeout` can bound a command's runtime.

#### Example

```bash
if timeout 10s some_command; then
    printf 'completed\n'
else
    status=$?
    printf 'command failed/timed out status=%d\n' "$status" >&2
fi
```

#### Common Failure / Troubleshooting

The exact `timeout` command and exit statuses are implementation-specific; document the platform.



### Deep Dive — Dry-Run as a First-Class Interface

A dry-run should use the same validated arguments and decision logic as apply mode, but stop before mutation.

Printing shell-escaped arguments with `%q` helps show what would execute.

#### Example

```bash
run() {
    if (( dry_run )); then
        printf 'DRY-RUN:' >&2
        printf ' %q' "$@" >&2
        printf '\n' >&2
    else
        "$@"
    fi
}
```

#### Why It Matters

Dry-run reduces blast radius and improves reviewability.



### Deep Dive — Why `eval` Is Dangerous

`eval` reparses generated text as shell code.

If external or variable data enters that text, data can become operators, redirections, substitutions, or commands.

#### Mental Model

```text
untrusted text
   ↓
string concatenation
   ↓
eval
   ↓
reparse as shell syntax
   ↓
command injection risk
```

#### Example

```bash
# Avoid:
# eval "$user_text"

# Prefer:
cmd=(printf '%s\n' "$user_text")
"${cmd[@]}"
```

#### Why It Matters

Preserve data as arguments instead of converting it back into code.



### Deep Dive — Shell Injection and Remote Commands

A shell-injection risk appears whenever untrusted data is inserted into text that another shell will parse.

Remote command execution over SSH is a common place where quoting becomes multi-layered because a local shell and remote shell may both parse text.

#### Why It Matters

Prefer APIs, fixed remote scripts with positional arguments, or carefully constrained data channels instead of constructing arbitrary remote command strings.

#### Common Failure / Troubleshooting

Never assume local quoting automatically protects a second shell on another host.



### Deep Dive — Secrets and Environment Variables

Environment variables are convenient configuration, but secrets can leak through:
- debug tracing
- child processes
- diagnostics
- process inspection depending on platform
- accidental `env` dumps
- CI logs

Use platform secret stores and minimize exposure.

#### Why It Matters

Configuration convenience is not equivalent to secret protection.



### Deep Dive — `set -x`, PS4, and Secret Leakage

Execution tracing prints expanded commands and can expose credentials.

Use tracing only in controlled environments and disable it before secret-bearing commands.

#### Example

```bash
set -x
safe_command
set +x

# secret-consuming command here
```

#### Why It Matters

Debug features can become data-exfiltration channels if logs are retained.



### Deep Dive — `umask` and File Permissions

`umask` influences default permission bits when new files/directories are created.

A script that creates sensitive material should define an appropriate permission strategy.

#### Example

```bash
old_umask=$(umask)
umask 077

secret_file=$(mktemp)
printf '%s\n' "sensitive" >"$secret_file"

umask "$old_umask"
```

#### Why It Matters

Do not assume the caller's default umask is suitable for sensitive temporary files.



### Deep Dive — Path Validation and `--`

Commands that accept `--` use it to end option parsing.

This prevents a filename such as `-rf` from being interpreted as an option.

#### Example

```bash
rm -- "$file"
cp -- "$source" "$destination"
mv -- "$source" "$destination"
```

#### Why It Matters

Always preserve filename data as filename arguments.



### Deep Dive — Canonicalization and Base-Directory Checks

Checking whether a path is inside an approved directory can be more subtle than matching a raw string because paths may contain `..`, symlinks, or alternate spellings.

For safety-critical cleanup tools:
- constrain the base
- resolve paths using platform-appropriate tools
- reject ambiguous targets
- avoid following symlinks unless intended

#### Why It Matters

A destructive command's correctness depends as much on target selection as command syntax.



### Deep Dive — `find` Expression Ordering

`find` expressions combine predicates and actions. Understanding evaluation order matters before adding destructive actions such as `-delete`.

#### Example

```bash
find "$base"     -type f     -name '*.log'     -mtime +7     -print
```

#### Why It Matters

Build and verify the selection expression first; only then add mutation.



### Deep Dive — ShellCheck

ShellCheck statically analyzes shell scripts for quoting problems, array mistakes, portability issues, and suspicious constructs.

Treat findings as prompts to understand behavior, not warnings to suppress automatically.

#### Example

```bash
shellcheck script.sh
```

#### Why It Matters

It catches many classes of errors before runtime.



### Deep Dive — `bash -n` Syntax Check

`bash -n` parses a script without executing commands.

#### Example

```bash
bash -n ops.sh
```

#### Why It Matters

Useful as the first CI quality gate.



### Deep Dive — `shfmt` Awareness

`shfmt` formats shell code consistently.

Formatting cannot make incorrect code correct, but consistency improves reviewability.

#### Practical Use

CI formatting checks and team style.



### Deep Dive — Bats Testing Awareness

Bats (Bash Automated Testing System) is a common framework for testing command-line behavior.

Tests can verify:
- exit status
- stdout
- stderr
- filesystem effects

#### Example

```bash
# Conceptual Bats test
@test "health returns success" {
    run ./ops.sh health
    [ "$status" -eq 0 ]
}
```

#### Why It Matters

Shell scripts benefit from automated tests just like Python programs.



### Deep Dive — Testing with Temporary Directories

Tests should isolate filesystem state with temporary directories rather than modifying real system paths.

#### Example

```bash
testdir=$(mktemp -d)
trap 'rm -rf -- "$testdir"' EXIT

mkdir -p "$testdir/logs"
printf 'sample\n' >"$testdir/logs/app.log"
```

#### Why It Matters

Reproducible tests require controlled state.



### Deep Dive — Dependency Injection in Shell

Shell scripts can be made testable by allowing command paths or functions to be replaced.

For example, an environment variable can point to a fake command in tests, or functions can wrap external commands.

#### Example

```bash
SYSTEMCTL=${SYSTEMCTL:-systemctl}

check_service() {
    "$SYSTEMCTL" is-active --quiet "$1"
}
```

#### Why It Matters

Tests can provide a fake executable without requiring a real systemd environment.



### Deep Dive — Portability: Bash vs POSIX `sh`

Bash features such as:
- arrays
- associative arrays
- `[[ ... ]]`
- process substitution
- `mapfile`
- `BASH_SOURCE`
are not portable POSIX shell features.

Choose one target explicitly.

#### Mental Model

```text
Need portability to minimal /bin/sh?
        ↓ yes
use POSIX shell subset

Need Bash features / Linux ops?
        ↓
declare #!/usr/bin/env bash
```

#### Why It Matters

Accidental Bash syntax in a `/bin/sh` script is a common deployment failure.



### Deep Dive — Shebang

The shebang selects the interpreter when the script is executed directly.

Common Bash form:

#### Example

```bash
#!/usr/bin/env bash
```

#### Why It Matters

`env` finds Bash through PATH; a fixed `/bin/bash` path may be preferable in tightly controlled environments. Choose intentionally.



### Deep Dive — Locale and Stable Parsing

Command output can vary by locale.

If a script parses command text, locale differences may break assumptions.

#### Example

```bash
LC_ALL=C some_command
```

#### Why It Matters

Prefer machine-readable command options over locale-dependent human output.

#### Common Failure / Troubleshooting

Do not globally override locale unless the entire script expects that behavior.



### Deep Dive — Current Working Directory Is an Input

A script inherits the caller's working directory.

Relative paths therefore refer to the caller's context, not necessarily the script file's directory.

#### Mental Model

```text
/tmp $ /opt/tool/ops.sh

pwd inside script
→ /tmp

script location
→ /opt/tool
```

#### Why It Matters

Use explicit paths and derive `script_dir` when accessing bundled resources.



### Deep Dive — Environment Inheritance

Exported environment variables are inherited by child processes. Changes made by a child do not modify the parent's environment.

#### Mental Model

```text
Bash parent
APP_ENV=prod (exported)
    ↓ child
python sees APP_ENV=prod

child changes APP_ENV
    ✗ parent unchanged
```

#### Why It Matters

This is process inheritance, not shared mutable state.



### Deep Dive — Signal Exit Status Awareness

When a process terminates because of a signal, shells often report statuses related to `128 + signal_number`.

Treat this as a convention useful for diagnostics rather than designing complicated business semantics around signal numbers.

#### Practical Use

CI cancellation, SIGTERM from systemd/container shutdown.



### Deep Dive — Systemd and Cron Integration

Shell scripts often run non-interactively under schedulers.

Production scripts should:
- not require a TTY
- use absolute/stable paths
- validate PATH dependencies
- emit meaningful exit codes
- avoid interactive prompts
- handle termination

#### Mental Model

```text
systemd timer / cron / CI
        ↓
      script
        ↓
non-interactive execution
```

#### Why It Matters

A script that only works in your interactive terminal is not automation-ready.



### Deep Dive — CI-Friendly Behavior

A CI script should be deterministic and machine-friendly.

Good properties:
- no hidden prompts
- no ANSI decoration unless requested
- meaningful status
- stable output
- no secret logging
- dependencies checked first

#### Example

```bash
: "${APP_ENV:?APP_ENV is required}"
: "${CONFIG_PATH:?CONFIG_PATH is required}"

[[ -r "$CONFIG_PATH" ]] || {
    printf 'config unreadable: %s\n' "$CONFIG_PATH" >&2
    exit 2
}
```

#### Why It Matters

CI environments expose assumptions that interactive shells hide.



### Deep Dive — Idempotent Preflight Before Mutation

Validate all requirements before the highest-blast-radius step.

Preflight may include:
- commands exist
- variables exist
- files readable
- disk space sufficient
- target environment explicitly approved
- configuration syntax valid

#### Mental Model

```text
Validate everything
       ↓
any failure?
 ├─ yes → stop before mutation
 └─ no  → perform operation
```

#### Why It Matters

Failing early is cheaper and safer than partial deployment.



### Deep Dive — When Bash Becomes the Wrong Language

Move core logic to Python or another language when the script develops:
- deeply nested structures
- complex JSON/YAML transformations
- rich domain models
- sophisticated retries/state machines
- complex concurrency
- large test/mocking needs
- hundreds of lines of branching

#### Mental Model

```text
Bash:
orchestrate processes/files
        ↓ complexity grows
Python:
model data + state + tests
        ↓
Bash remains thin launcher if useful
```

#### Why It Matters

Choosing the language is part of engineering quality.



### Deep Dive — Production Script Architecture

A maintainable operations utility separates concerns.

#### Mental Model

```text
CLI / main
   ↓
validation
   ↓
business / orchestration functions
   ↓
command adapters
   ↓
filesystem / systemd / network tools

cross-cutting:
logging
cleanup
exit statuses
```

#### Why It Matters

Do not let argument parsing, logging, filesystem mutation, and command output parsing become one giant function.



### Deep Dive — Final Bash Mental Model

Strong Bash is not about clever one-liners. It is about preserving data boundaries, validating assumptions, controlling side effects, and communicating precisely with other Unix processes.

#### Mental Model

```text
Input
  ↓
Validate
  ↓
Quote / preserve argv boundaries
  ↓
Execute
  ↓
Check exact status
  ↓
stdout data / stderr diagnostics
  ↓
cleanup
  ↓
meaningful exit status
```

#### Why It Matters

This model scales from a five-line helper to CI/CD and incident-response utilities.



## 5. Hands-on Lab / Practical Exercises

### Lab — Health report

1. Create `health_report.sh`.
2. Report hostname, uptime, disk usage, memory, and selected service state.
3. Separate normal output from errors.
4. Return non-zero when a required check fails.
5. Run ShellCheck.

**Starter / reference code:**

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

check_command() {
    command -v "$1" >/dev/null 2>&1
}

for cmd in hostname df awk; do
    if ! check_command "$cmd"; then
        echo "missing command: $cmd" >&2
        exit 2
    fi
done

printf 'hostname=%s\n' "$(hostname)"
df -h /
```

**Expected result:** A predictable operational script with dependency validation.

### Lab — Log summary pipeline

1. Create a synthetic log.
2. Count ERROR records by component.
3. Add input-file validation.
4. Enable pipefail.
5. Handle no-match separately from true command failure.

**Starter / reference code:**

```bash
logfile=${1:-}
[[ -n "$logfile" && -r "$logfile" ]] || { echo "usage: $0 LOGFILE" >&2; exit 2; }

awk '$2 == "ERROR" {print $3}' "$logfile" | sort | uniq -c | sort -nr
```

**Expected result:** A robust text-processing utility.

### Lab — Dry-run cleanup

1. Create lab files in a safe temporary directory.
2. List files older than a threshold.
3. Add `--apply` before deletion.
4. Validate the target directory against an approved base.
5. Use `--` with commands that support it.

**Starter / reference code:**

```bash
mode=${1:---dry-run}
base=${2:-}

if [[ "$base" != /tmp/cleanup-lab/* ]]; then
    echo "refusing path outside lab base" >&2
    exit 2
fi

if [[ "$mode" == "--dry-run" ]]; then
    find "$base" -type f -mtime +7 -print
else
    find "$base" -type f -mtime +7 -print -delete
fi
```

**Expected result:** A defensive automation pattern that limits blast radius.


## Enhanced Hands-on Labs

### Enhanced Lab 1 — Shell Resolution

Use `type -a` and `command -V` for at least 10 commands. Classify builtin/function/external executable.

### Enhanced Lab 2 — Expansion Trace

Create examples showing parameter expansion, word splitting, and globbing. Predict final argument count before running.

### Enhanced Lab 3 — Argument Boundary Lab

Pass filenames containing spaces, wildcard characters, and leading dashes safely to a function.

### Enhanced Lab 4 — Special Parameters

Write a script that prints `$0`, `$#`, every argument via `"$@"`, and demonstrates `$?` and `$!`.

### Enhanced Lab 5 — Parameter Defaults

Use `:-`, `:=`, `:?`, and `:+` in a configuration-validation script.

### Enhanced Lab 6 — Pattern Expansion

Extract directory, filename, extension, and stem using parameter expansion only.

### Enhanced Lab 7 — Arithmetic

Validate an integer threshold, calculate percentages, and compare using `(( ... ))`.

### Enhanced Lab 8 — Regex Validation

Validate simple environment names and numeric ranges using `[[ ... =~ ... ]]` plus arithmetic checks.

### Enhanced Lab 9 — Globbing Modes

Compare default glob behavior with `nullglob` inside a temporary directory.

### Enhanced Lab 10 — Command Arrays

Build a dynamic `find` invocation with optional arguments using an array, never `eval`.

### Enhanced Lab 11 — Associative Arrays

Create a service→port map and print it safely.

### Enhanced Lab 12 — Mapfile

Load a moderate text file into an array and compare with streaming line-by-line processing.

### Enhanced Lab 13 — Subshell vs Group

Change variables and directories inside `(...)` and `{ ...; }` and explain the differences.

### Enhanced Lab 14 — Pipeline Scope

Demonstrate a pipeline-fed `while` variable issue, then fix it with process substitution.

### Enhanced Lab 15 — Here Document

Generate a sample configuration with both expanded and literal here-doc variants.

### Enhanced Lab 16 — File Descriptor Lab

Send structured stdout, diagnostics stderr, and audit lines to fd 3.

### Enhanced Lab 17 — Redirection Ordering

Compare several `>file 2>&1`/descriptor ordering examples in a safe lab.

### Enhanced Lab 18 — PIPESTATUS

Run a three-stage pipeline where the first, second, and third commands fail separately; inspect each status.

### Enhanced Lab 19 — Errexit Experiment

Create controlled examples showing where `set -e` exits and where conditional contexts suppress it. Document observations.

### Enhanced Lab 20 — CLI Parser

Implement `--dry-run`, `--output VALUE`, `--verbose`, `--help`, and `--` using `while` + `case`.

### Enhanced Lab 21 — getopts

Build a short-option equivalent with `-v`, `-o FILE`, and error handling.

### Enhanced Lab 22 — Exit Codes

Define and test a small exit-code contract for usage, validation, and operational failure.

### Enhanced Lab 23 — Machine Output

Produce key/value and JSON output while keeping logs on stderr.

### Enhanced Lab 24 — AWK Aggregation

Replace a multi-process grep/sort/uniq pipeline with one clear awk aggregation.

### Enhanced Lab 25 — Null-Delimited Files

Create lab filenames with spaces/tabs/newlines and process them with `find -print0` plus a null-aware consumer.

### Enhanced Lab 26 — find -exec

Compare `-exec ... {} +` with `xargs -0` for a safe read-only command.

### Enhanced Lab 27 — mktemp Security

Create temp files/directories with restrictive umask and cleanup traps.

### Enhanced Lab 28 — Signal Cleanup

Start a long-running lab script, send INT/TERM, and verify cleanup behavior.

### Enhanced Lab 29 — Background Status

Launch three child jobs, collect PIDs, wait for all, and aggregate failures.

### Enhanced Lab 30 — Bounded Parallelism

Process 20 synthetic hosts with maximum concurrency 4 and compare runtime with sequential mode.

### Enhanced Lab 31 — Locking

Use `flock` if available so two copies of a lab task cannot enter the critical section simultaneously.

### Enhanced Lab 32 — Idempotency

Make a configuration-update function safe to run repeatedly without duplicate lines.

### Enhanced Lab 33 — Atomic Replace

Generate a config into a temp file, validate, then rename it atomically into place.

### Enhanced Lab 34 — Retry

Implement bounded retry around a deliberately flaky local test command.

### Enhanced Lab 35 — Timeout

Bound a sleeping command with `timeout` where available and inspect status.

### Enhanced Lab 36 — Dry Run

Create one mutating lab operation whose dry-run uses exactly the same validated arguments.

### Enhanced Lab 37 — Eval Refactor

Take an unsafe command-string+eval example and rewrite it with arrays.

### Enhanced Lab 38 — Injection Review

Explain how untrusted text can become shell syntax and rewrite examples so data stays data.

### Enhanced Lab 39 — Secret Tracing

Demonstrate in a fake-token lab why `set -x` leaks expanded values, then design safe tracing boundaries.

### Enhanced Lab 40 — Path Safety

Reject empty, `/`, and out-of-base cleanup targets. Add `--` to file operations.

### Enhanced Lab 41 — ShellCheck

Run ShellCheck and maintain a table: warning → reason → repair.

### Enhanced Lab 42 — Syntax Gate

Add `bash -n` and ShellCheck to a local CI-like validation script.

### Enhanced Lab 43 — Bats Awareness

If Bats is installed, write tests for status/stdout/stderr. Otherwise write a manual test harness with the same assertions.

### Enhanced Lab 44 — Fake Commands

Inject a fake `systemctl` executable to test service-check logic without systemd.

### Enhanced Lab 45 — Portability Audit

Mark every Bash-specific construct in the file and state what would break under POSIX sh.

### Enhanced Lab 46 — Locale

Compare one text command under default locale and `LC_ALL=C`; explain why parsing human output is fragile.

### Enhanced Lab 47 — Working Directory

Run one script from three different directories and make bundled-resource loading work every time.

### Enhanced Lab 48 — Scheduler Readiness

Prepare a script for cron/systemd/CI: no prompts, explicit PATH assumptions, stable output, clean termination.

### Enhanced Lab 49 — Preflight

Build a deployment preflight that runs all checks, aggregates failures, and refuses mutation when any check fails.

### Enhanced Lab 50 — Bash-to-Python Boundary

Take a complex pseudo-requirement and divide it into Bash orchestration vs Python data-processing responsibilities.

### Enhanced Lab 51 — Capstone

Build the Production Linux Operations Toolkit described in the expanded capstone section.


## 6. Mini Project

### Mini Project — Linux Operations Toolkit

Create:

```text
ops-toolkit/
├── ops.sh
├── lib/
│   ├── logging.sh
│   ├── validation.sh
│   └── checks.sh
└── README.md
```

Subcommands:

```bash
./ops.sh health
./ops.sh logs app.log
./ops.sh service-check sshd
./ops.sh cleanup --dry-run /tmp/cleanup-lab/demo
```

**Requirements**

- Quote expansions safely.
- Validate arguments and dependencies.
- Use meaningful exit statuses.
- Errors to stderr.
- Dry-run for destructive actions.
- Use `trap` for temporary resources.
- Pass ShellCheck with no unexplained important findings.
- Document why Bash is appropriate for each operation and identify at least one feature that would be better implemented in Python.


### Expanded Capstone — Production Linux Operations Toolkit

Expand the original `ops-toolkit` into a production-style, local-only operations utility.

```text
ops-toolkit/
├── ops.sh
├── lib/
│   ├── logging.sh
│   ├── validation.sh
│   ├── cli.sh
│   ├── process.sh
│   ├── filesystem.sh
│   └── checks.sh
├── tests/
│   ├── test_cli.sh
│   ├── test_validation.sh
│   ├── test_cleanup.sh
│   └── fakes/
│       └── systemctl
├── fixtures/
│   ├── app.log
│   └── servers.txt
├── docs/
│   ├── exit-codes.md
│   ├── security.md
│   ├── portability.md
│   └── bash-vs-python.md
└── README.md
```

Required commands:

```bash
./ops.sh health
./ops.sh service-check sshd
./ops.sh logs --file app.log
./ops.sh cleanup --dry-run --base /tmp/cleanup-lab/demo
./ops.sh cleanup --apply   --base /tmp/cleanup-lab/demo
./ops.sh preflight
./ops.sh recent-errors --json
```

Required engineering properties:

```text
Safe argument parsing
Quoted expansions
No eval
Command arrays
No parsing ls
Null-delimited filename handling where needed
Meaningful exit statuses
stdout for data
stderr for diagnostics
Dry-run before destructive mode
Validated cleanup base path
mktemp + trap cleanup
Dependency checks
No CWD assumption
No TTY requirement
No secret printing
ShellCheck
bash -n
Test harness / Bats if available
```

### `ops.sh` Skeleton

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

script_dir=$(
    cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1
    pwd -P
)

source "$script_dir/lib/logging.sh"
source "$script_dir/lib/validation.sh"
source "$script_dir/lib/checks.sh"

usage() {
    cat >&2 <<'EOF'
usage:
  ops.sh health
  ops.sh service-check SERVICE
  ops.sh logs --file FILE
  ops.sh cleanup (--dry-run|--apply) --base DIR
  ops.sh preflight
EOF
}
```

### Logging Contract

```bash
log() {
    local level=$1
    shift
    printf '%s %-5s %s\n' "$(date -Iseconds)" "$level" "$*" >&2
}
```

When a subcommand emits structured output, logs must remain on stderr.

### Validation Library

Implement:

```text
require_command
require_file
require_directory
require_integer
require_percentage
require_env
require_safe_cleanup_base
```

Every function must:
- quote inputs
- return status
- write diagnostics to stderr

### Health Subcommand

Report at least:

```text
hostname
uptime
root disk usage
memory summary
selected service states
```

Requirements:
- validate required commands
- aggregate check failures
- machine-readable mode

Example normal output:

```text
hostname=web-01
root_usage_percent=42
sshd=active
docker=active
```

### Log Analysis

Given deliberately simple synthetic whitespace-delimited logs:

```text
2026-08-19 ERROR auth failed-login
2026-08-19 INFO api ok
2026-08-19 ERROR db timeout
```

Provide:
- total ERROR count
- counts by component
- optional JSON using `jq`

Do not claim the whitespace parser is suitable for real arbitrary log formats.

### Cleanup Subcommand

Required safety sequence:

```text
parse arguments
   ↓
require exactly one mode
   ↓
validate non-empty base
   ↓
validate approved lab prefix
   ↓
resolve/inspect target
   ↓
find candidate files
   ↓
print candidates
   ↓
dry-run? → stop
   ↓
apply deletion
```

Deletion is allowed only inside a lab path such as:

```text
/tmp/cleanup-lab/...
```

### Process Helpers

Implement bounded background checks:

```text
max concurrency configurable
collect every PID
wait every PID
aggregate failure
```

Keep the lab local; do not use this to probe external systems.

### Locking

If `flock` exists, prevent overlapping cleanup runs.

If unavailable, document that the feature is skipped rather than inventing unsafe lock behavior.

### Atomic Report Generation

Generate a report into a temporary file:

```text
mktemp
↓
write complete content
↓
validate non-empty / syntax if relevant
↓
mv into final path
```

### Retry Policy

Implement a bounded retry helper for a synthetic flaky local command.

Document:
- attempts
- delay
- final status
- why retries are not used for permanent validation errors

### Tests

Test at least:

```text
no args
unknown subcommand
missing option value
missing file
unreadable file
bad percentage
empty cleanup path
cleanup outside lab prefix
dry-run performs no delete
apply deletes only selected lab files
service fake returns active/inactive
working directory different from script directory
stdout/stderr separation
pipeline stage failure
```

### Static Quality Gates

Your local validation command should run:

```bash
bash -n ops.sh
shellcheck ops.sh lib/*.sh tests/*.sh
```

If `shfmt` is available, add formatting validation.

### Security Review

Create `docs/security.md` and explain:

```text
why expansions are quoted
why command arrays are used
why eval is forbidden
why sourced configuration must be trusted
why temp files use mktemp
why tracing can leak secrets
why cleanup is base-constrained
why -- is used with file paths
why dry-run exists
why machine output excludes secrets
```

### Bash vs Python Decision

Create `docs/bash-vs-python.md`.

Keep in Bash:
- command orchestration
- service checks
- simple file selection
- small text pipelines
- process launching

Move to Python when:
- nested JSON
- schemas
- joins across multiple datasets
- complex retry/state machines
- large domain logic
- rich unit mocking
- database/API clients
- hundreds of lines of branching

The final goal is not merely to make the script work.

It is to make its behavior predictable under:

```text
missing dependencies
bad arguments
different working directory
strange filenames
partial command failure
concurrent execution
scheduler execution
termination signals
dry-run mode
CI execution
```


## 7. Recommended Resources

- GNU Bash Reference Manual.
- GNU Coreutils manual.
- ShellCheck documentation.
- Linux man pages for `find`, `grep`, `awk`, `sed`, `sort`, `xargs`, `test`, and related commands.
- POSIX shell specification when portability beyond Bash matters.

## 8. Certification Relevance

Bash is directly valuable for RHCSA-style administration and almost every DevOps workflow. It appears in bootstrap scripts, CI jobs, Docker images, incident-response utilities, and cloud automation glue. Strong shell fundamentals also reduce mistakes when you later use Ansible, Terraform, Kubernetes, and CI/CD platforms.

## 9. Common Mistakes & Best Practices

- **Mistake:** Leaving `$var` unquoted.
  - **Best practice:** Use `"$var"` by default.
- **Mistake:** Parsing `ls`.
  - **Best practice:** Use globbing, `find`, or safe line/null-delimited approaches.
- **Mistake:** Assuming `set -e` catches everything.
  - **Best practice:** Understand semantics and explicitly check critical commands.
- **Mistake:** Deleting files before a dry run.
  - **Best practice:** Validate path/base and show intended targets first.
- **Mistake:** Mixing diagnostic text into stdout data.
  - **Best practice:** Use stderr for errors/logs when stdout is machine-readable output.
- **Mistake:** Scraping human tables when machine-readable output exists.
  - **Best practice:** Prefer stable machine formats/options or format-aware tools.
- **Mistake:** Using Bash for complex structured-data applications.
  - **Best practice:** Move complex logic to Python or another suitable language.


### Additional Bash Mistakes & Engineering Corrections

- **Mistake:** Thinking shell commands receive one command string.
  - **Best practice:** Think in argument arrays (`argv`) and preserve boundaries.
- **Mistake:** Using `"$*"` to forward arguments.
  - **Best practice:** Use `"$@"`.
- **Mistake:** Building commands as strings.
  - **Best practice:** Use arrays and direct invocation.
- **Mistake:** Treating sourced config as harmless data.
  - **Best practice:** Source only trusted shell code.
- **Mistake:** Capturing huge command output into a variable.
  - **Best practice:** Stream large data.
- **Mistake:** Forgetting command substitution removes trailing newlines.
  - **Best practice:** Do not use it when exact trailing-newline preservation matters.
- **Mistake:** Assuming pipeline loops always mutate the parent shell.
  - **Best practice:** Understand subshell behavior or use process substitution.
- **Mistake:** Treating `set -e` as exceptions.
  - **Best practice:** Explicitly handle important failure paths.
- **Mistake:** Ignoring individual pipeline statuses.
  - **Best practice:** Use `PIPESTATUS` when each stage matters.
- **Mistake:** Using newline-delimited filenames.
  - **Best practice:** Use null-delimited processing for arbitrary paths.
- **Mistake:** Launching unlimited `&` jobs.
  - **Best practice:** Bound concurrency and collect every status.
- **Mistake:** Running overlapping maintenance jobs.
  - **Best practice:** Use platform-appropriate locking such as `flock` where available.
- **Mistake:** Writing critical files in place.
  - **Best practice:** Generate/validate a temporary file then rename.
- **Mistake:** Infinite retries.
  - **Best practice:** Retry only transient failures with bounded attempts.
- **Mistake:** Tracing secret-bearing commands.
  - **Best practice:** Disable `set -x` around secrets.
- **Mistake:** Assuming a script runs from its own directory.
  - **Best practice:** Resolve bundled resources from `BASH_SOURCE`.
- **Mistake:** Declaring `/bin/sh` while using Bash features.
  - **Best practice:** Match shebang to language features.
- **Mistake:** Parsing locale-dependent human output.
  - **Best practice:** Prefer machine-readable modes or stabilize locale intentionally.
- **Mistake:** Using Bash after the data model becomes complex.
  - **Best practice:** Move core logic to Python while keeping Bash as orchestration glue.


## 10. Self-Assessment Questions (with short answers)

### Q1. What does exit status 0 mean conventionally?

**Answer:** Success.

### Q2. Why quote `"$var"`?

**Answer:** Prevents unintended word splitting and pathname expansion.

### Q3. What does `2>` redirect?

**Answer:** stderr.

### Q4. What does `|` do?

**Answer:** Connects stdout of one command to stdin of another.

### Q5. What does `pipefail` change?

**Answer:** A pipeline can fail when an earlier stage fails, not only based on the last stage.

### Q6. Why use `local` in functions?

**Answer:** Reduces accidental mutation of broader shell variables.

### Q7. Why avoid `for x in $(ls ...)`?

**Answer:** Command substitution and word splitting break filenames and are unnecessary.

### Q8. What does `trap ... EXIT` help with?

**Answer:** Cleanup on shell exit.

### Q9. Why use dry-run before deletion?

**Answer:** Reduces blast radius and lets you verify targets.

### Q10. When is Python usually better than Bash?

**Answer:** When data structures, parsing, testing, error handling, or program complexity becomes substantial.


## Extended Self-Assessment

### Extended Q1. What is the difference between a shell and a terminal?

**Answer:** A shell interprets commands; a terminal is an interface/transport for interacting with processes.

### Extended Q2. Why do some commands need to be shell builtins?

**Answer:** Commands such as cd/export must modify the current shell's process state.

### Extended Q3. What is the safest mental model for quoting?

**Answer:** Preserve intended argument boundaries.

### Extended Q4. What does `"$@"` do?

**Answer:** Expands each positional parameter as a separate quoted argument.

### Extended Q5. What does `"$*"` do?

**Answer:** Joins positional parameters into one argument using the first IFS character.

### Extended Q6. What does `${VAR:-x}` mean?

**Answer:** Use x when VAR is unset or empty.

### Extended Q7. What does `${VAR:?message}` do?

**Answer:** Fails expansion with a message if VAR is unset/empty.

### Extended Q8. What is `[[ ... ]]`?

**Answer:** A Bash conditional construct with safer parsing and richer pattern/regex support.

### Extended Q9. Why are arrays safer for dynamic commands?

**Answer:** They preserve each argument separately without reparsing text.

### Extended Q10. What does `IFS= read -r` protect?

**Answer:** Whitespace/backslashes are preserved rather than split/interpreted.

### Extended Q11. What does command substitution do to trailing newlines?

**Answer:** Removes them.

### Extended Q12. Subshell parentheses vs braces?

**Answer:** Parentheses run in a subshell; braces run in the current shell.

### Extended Q13. What is process substitution?

**Answer:** Bash mechanism exposing command streams through filename-like descriptors.

### Extended Q14. What are fd 0, 1, and 2?

**Answer:** stdin, stdout, stderr.

### Extended Q15. Why does redirection order matter?

**Answer:** Descriptors are changed left-to-right.

### Extended Q16. What is `PIPESTATUS`?

**Answer:** Array containing statuses of each command in the most recent foreground pipeline.

### Extended Q17. Why isn't `set -e` enough?

**Answer:** Its semantics have contextual exceptions and it does not express recovery intent.

### Extended Q18. What is a robust CLI forwarding expansion?

**Answer:** `"$@"`.

### Extended Q19. Why should logs go to stderr?

**Answer:** Keep stdout clean for machine-readable data.

### Extended Q20. Why use jq for JSON output?

**Answer:** It performs correct escaping and structure generation.

### Extended Q21. Why is whitespace not a safe filename delimiter?

**Answer:** Unix filenames may contain spaces, tabs, and newlines.

### Extended Q22. What is the robust filename delimiter?

**Answer:** NUL/null byte.

### Extended Q23. Why use mktemp?

**Answer:** Avoid predictable temporary-path collisions and related filesystem risks.

### Extended Q24. What does trap EXIT commonly do?

**Answer:** Centralized cleanup on shell exit.

### Extended Q25. What does `$!` contain?

**Answer:** PID of the most recently launched background job.

### Extended Q26. Why must background jobs be waited on?

**Answer:** To collect completion/failure and avoid premature script exit.

### Extended Q27. Why bound concurrency?

**Answer:** Prevent resource exhaustion and service overload.

### Extended Q28. What is idempotency?

**Answer:** Repeated execution converges to the same intended final state.

### Extended Q29. Why write then rename a config?

**Answer:** Avoid exposing partial files after failure.

### Extended Q30. When should a command be retried?

**Answer:** Only when failure is plausibly transient and retry is bounded.

### Extended Q31. Why is eval dangerous?

**Answer:** It reparses data as shell code, enabling injection.

### Extended Q32. Why can set -x expose secrets?

**Answer:** It logs expanded command arguments.

### Extended Q33. What does umask control?

**Answer:** Default permission bits for newly created filesystem objects.

### Extended Q34. Why pass `--` before filenames?

**Answer:** Stop option parsing so leading-dash filenames remain data.

### Extended Q35. What does bash -n do?

**Answer:** Syntax-checks without executing commands.

### Extended Q36. What does ShellCheck do?

**Answer:** Static analysis for common shell mistakes and portability issues.

### Extended Q37. Why is POSIX sh different from Bash?

**Answer:** Many Bash constructs such as arrays and `[[ ]]` are not POSIX.

### Extended Q38. Why is current working directory important?

**Answer:** Relative paths resolve against the caller's working directory.

### Extended Q39. Why may LC_ALL=C help parsing?

**Answer:** It can stabilize locale-dependent text, though machine formats are preferable.

### Extended Q40. When should Bash hand work to Python?

**Answer:** When data structures, parsing, state, testing, or program complexity becomes substantial.


## End-of-Module Practice Checklist

- [ ] I typed the examples myself instead of only reading them.
- [ ] I changed inputs and predicted results before running the code.
- [ ] I intentionally introduced at least three errors and debugged them.
- [ ] I completed the labs without copying the final solution first.
- [ ] I completed the mini project and wrote a short README.
- [ ] I can explain the important design choices aloud.

## Extended Worked Exercises

### Exercise 1 — Quoting failure

```bash
file="my report.txt"
printf '%s\n' $file
```

The unquoted expansion becomes multiple words. Compare with:

```bash
printf '%s\n' "$file"
```

### Exercise 2 — Safer argument parsing

```bash
while (($#)); do
    case $1 in
        --verbose) verbose=1; shift ;;
        --output) output=${2:?missing value}; shift 2 ;;
        --) shift; break ;;
        *) echo "unknown argument: $1" >&2; exit 2 ;;
    esac
done
```

Explain why each `shift` is required.

### Exercise 3 — Subshell behavior

```bash
value=1
(value=2)
echo "$value"  # still 1
```

Then compare with braces:

```bash
value=1
{ value=2; }
echo "$value"  # 2
```

### Exercise 4 — Null-delimited filenames

For robust processing of arbitrary filenames, study `find -print0` and commands that accept null-delimited input. Whitespace alone is not a safe filename delimiter.

### Exercise 5 — ShellCheck lesson log

Run ShellCheck and keep a Markdown table:

```text
warning | original code | fixed code | what I learned
```

Do not suppress warnings until you understand why they occur.

### Operational Failure Scenarios

- Empty variable used in an `rm` path.
- Command missing from `PATH` in a minimal container.
- Pipeline first stage fails while last stage succeeds.
- `grep` no-match status confused with an execution failure.
- Script assumes interactive working directory.
- Log parser breaks on whitespace or locale changes.

For each scenario, write the preventive validation you would add.


## Practical Code Notebook — Bash

### Example A — Reliable argument validation

```bash
#!/usr/bin/env bash
set -u

usage() {
    echo "usage: $0 --file PATH [--verbose]" >&2
}

file=""
verbose=0

while (($#)); do
    case "$1" in
        --file)
            (($# >= 2)) || { usage; exit 2; }
            file=$2
            shift 2
            ;;
        --verbose)
            verbose=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "unknown argument: $1" >&2
            usage
            exit 2
            ;;
    esac
done

[[ -n "$file" ]] || { echo "--file is required" >&2; exit 2; }
[[ -r "$file" ]] || { echo "not readable: $file" >&2; exit 2; }
```

This is more predictable than relying on positional arguments without validation.

### Example B — Arrays

```bash
services=(nginx sshd docker)

for service in "${services[@]}"; do
    printf 'checking %s\n' "$service"
done
```

`"${services[@]}"` expands each element as one quoted argument, preserving spaces inside individual elements.

### Example C — Associative arrays

```bash
declare -A ports=(
    [ssh]=22
    [http]=80
    [https]=443
)

printf 'HTTPS port: %s\n' "${ports[https]}"
```

Associative arrays can handle simple mappings, but if your data becomes deeply nested or JSON-like, Python is often easier to maintain.

### Example D — Reading command output safely

```bash
if output=$(some_command 2>&1); then
    printf 'success: %s\n' "$output"
else
    status=$?
    printf 'failed with %d: %s\n' "$status" "$output" >&2
fi
```

Capture only when the output is reasonably small. Large streams should usually remain streams.

### Example E — Service check

```bash
check_service() {
    local service=$1

    if systemctl is-active --quiet "$service"; then
        printf '%s active\n' "$service"
        return 0
    fi

    printf '%s inactive\n' "$service" >&2
    return 1
}
```

This relies on `systemctl` exit status rather than parsing its formatted status display.

### Example F — Prevent empty dangerous paths

```bash
target=${TARGET_DIR:-}

if [[ -z "$target" ]]; then
    echo "TARGET_DIR is empty; refusing" >&2
    exit 2
fi

case "$target" in
    /tmp/cleanup-lab/*) ;;
    *) echo "target outside approved lab path" >&2; exit 2 ;;
esac
```

Only after these checks should a cleanup command be considered.

### Example G — Temporary file with trap

```bash
tmpfile=$(mktemp)

cleanup() {
    rm -f -- "$tmpfile"
}
trap cleanup EXIT

printf 'temporary data\n' >"$tmpfile"
cat "$tmpfile"
```

The trap centralizes cleanup.

### Example H — `read` with multiple fields

Input:

```text
web-01,10.0.0.10,prod
```

Script:

```bash
while IFS=, read -r host ip env; do
    printf 'host=%s ip=%s env=%s\n' "$host" "$ip" "$env"
done < servers.csv
```

This is acceptable for deliberately simple delimiter-separated data. Real CSV with quoting/embedded commas should use a proper CSV parser.

### Example I — Process substitutions

Compare variable scope issues around pipelines. One Bash approach:

```bash
count=0
while IFS= read -r line; do
    ((count += 1))
done < <(printf '%s\n' a b c)

echo "$count"
```

The loop runs in the current shell in this construction, so `count` remains changed afterward.

### Example J — Parallel jobs carefully

```bash
check_one() {
    local host=$1
    sleep 1
    printf '%s checked\n' "$host"
}

pids=()
for host in web-01 db-01 cache-01; do
    check_one "$host" &
    pids+=("$!")
done

failed=0
for pid in "${pids[@]}"; do
    wait "$pid" || failed=1
done

exit "$failed"
```

Parallelism complicates output ordering and error handling. Use it only when the workload benefits.

### Example K — Function libraries

`lib/logging.sh`:

```bash
log_info() {
    printf '%s INFO %s\n' "$(date -Iseconds)" "$*"
}
```

Main script:

```bash
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
# shellcheck source=lib/logging.sh
source "$script_dir/lib/logging.sh"

log_info "started"
```

Deriving `script_dir` avoids assuming the current working directory equals the script directory.

### Example L — `xargs` and filenames

Whitespace-delimited pipelines can break on unusual filenames. A robust pattern for compatible tools is null-delimited data:

```bash
find "$base" -type f -name '*.log' -print0 |
    xargs -0 -r wc -l
```

Understand tool support before using this style on different platforms.

### Example M — When to stop using Bash

If a script begins to require nested dictionaries, JSON transformation, complex retry state, hundreds of lines of branching, or extensive testing mocks, move core logic to Python and keep Bash as a thin launcher/orchestration layer. Choosing the correct language is part of engineering judgment.


## Guided Walkthroughs — Bash Operations

### Walkthrough 1 — Build a reusable logger

```bash
log() {
    local level=$1
    shift
    printf '%s %-5s %s\n' "$(date -Iseconds)" "$level" "$*" >&2
}

log INFO "starting health check"
log WARN "disk usage high"
```

Sending logs to stderr keeps stdout available for machine-readable results.

### Walkthrough 2 — Require a command

```bash
require_command() {
    local name=$1
    if ! command -v "$name" >/dev/null 2>&1; then
        log ERROR "required command not found: $name"
        return 1
    fi
}

require_command awk || exit 2
require_command find || exit 2
```

Minimal containers often omit commands you assume exist on a full workstation.

### Walkthrough 3 — Validate integer input

```bash
threshold=${1:-}

if [[ ! "$threshold" =~ ^[0-9]+$ ]]; then
    echo "threshold must be a non-negative integer" >&2
    exit 2
fi

if (( threshold > 100 )); then
    echo "threshold must be <= 100" >&2
    exit 2
fi
```

Bash regex matching inside `[[ ... ]]` is useful for simple validation.

### Walkthrough 4 — Default values without crashing under `set -u`

```bash
set -u

region=${REGION:-eu-west-1}
required=${REQUIRED_VALUE:?REQUIRED_VALUE must be set}
```

`${VAR:-default}` supplies a default when unset/empty. `${VAR:?message}` aborts expansion with a message when missing.

### Walkthrough 5 — Safe script-directory discovery

```bash
script_dir=$(
    cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1
    pwd -P
)
```

Use this when a script needs files stored relative to itself rather than relative to the caller's working directory.

### Walkthrough 6 — Read configuration carefully

Sourcing a file executes it as shell code:

```bash
source ./config.sh
```

Therefore, only source trusted configuration. If configuration is data from untrusted users, use a data format and parser rather than executing it.

### Walkthrough 7 — Distinguish no-match from grep failure

`grep` commonly uses:

```text
0 match found
1 no match
2 error
```

Example:

```bash
grep -q 'ERROR' "$logfile"
status=$?
case $status in
    0) echo "error records exist" ;;
    1) echo "no error records" ;;
    *) echo "grep failed" >&2; exit "$status" ;;
esac
```

This is more precise than treating every non-zero value as the same failure.

### Walkthrough 8 — Pipeline output with `awk`

```bash
df -P / | awk 'NR==2 {
    gsub(/%/, "", $5)
    print $5
}'
```

The first line is a header; `NR==2` selects the data row. `gsub` removes `%`. The output can feed an arithmetic comparison.

### Walkthrough 9 — Avoid temporary files when a pipe is enough

Instead of:

```bash
command1 > /tmp/a
command2 < /tmp/a
rm /tmp/a
```

use:

```bash
command1 | command2
```

Use temporary files only when you need persistence, random access, debugging artifacts, or a tool requires a path.

### Walkthrough 10 — Use `mktemp -d` for a workspace

```bash
workdir=$(mktemp -d)
trap 'rm -rf -- "$workdir"' EXIT

input="$workdir/input.txt"
output="$workdir/output.txt"
```

Never use predictable shared filenames such as `/tmp/myapp.txt` when collisions or symlink attacks could matter.

### Walkthrough 11 — Dry-run pattern

```bash
dry_run=1

run() {
    if (( dry_run )); then
        printf 'DRY-RUN:' >&2
        printf ' %q' "$@" >&2
        printf '\n' >&2
    else
        "$@"
    fi
}

run rm -- "$target"
```

Passing commands as arguments avoids constructing/evaluating a command string.

### Walkthrough 12 — Avoid `eval`

Dangerous pattern:

```bash
# eval "$user_text"
```

`eval` reparses text as shell code. If the text includes untrusted input, data can become executable commands. Prefer arrays and direct command invocation.

### Walkthrough 13 — Command arrays

```bash
cmd=(find "$base" -type f -name '*.log' -mtime +7 -print)
"${cmd[@]}"
```

Arrays preserve argument boundaries and are much safer than building one command string.

### Walkthrough 14 — Pipeline versus Python decision

Good Bash:

```bash
awk '$2 == "ERROR" {print $3}' app.log | sort | uniq -c
```

Potentially better Python: nested JSON, multiple joins between data sets, complex validation, retry policies, unit-test-heavy logic, or hundreds of lines of branching.

### Walkthrough 15 — CI-friendly script behavior

A CI-friendly script should:

- write clear diagnostics,
- use stable non-interactive behavior,
- return meaningful exit status,
- avoid relying on current directory,
- avoid assuming a TTY,
- validate required environment variables,
- avoid prompts unless explicitly requested,
- never print secrets.

Example:

```bash
: "${APP_ENV:?APP_ENV is required}"
: "${CONFIG_PATH:?CONFIG_PATH is required}"
[[ -r "$CONFIG_PATH" ]] || { echo "config unreadable" >&2; exit 2; }
```

### Walkthrough 16 — Service loop with aggregated status

```bash
services=(sshd docker nginx)
failed=0

for service in "${services[@]}"; do
    if systemctl is-active --quiet "$service"; then
        printf '%s OK\n' "$service"
    else
        printf '%s FAILED\n' "$service" >&2
        failed=1
    fi
done

exit "$failed"
```

The script checks every service but still reports overall failure to the calling automation.

### Walkthrough 17 — Why shell quoting is a security issue

If external text is expanded unquoted, it can change argument boundaries and glob patterns. If it is passed through `eval` or a shell command string, it may become shell syntax. Safe shell programming is therefore not only about filenames with spaces; it is part of command-injection prevention.


## Case Study — Build a Deployment Preflight Script

A deployment pipeline should fail before deployment when required conditions are missing.

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

log() {
    local level=$1
    shift
    printf '%s %-5s %s\n' "$(date -Iseconds)" "$level" "$*" >&2
}

require_command() {
    local cmd=$1
    command -v "$cmd" >/dev/null 2>&1 || {
        log ERROR "missing command: $cmd"
        return 1
    }
}

require_env() {
    local name=$1
    if [[ -z "${!name:-}" ]]; then
        log ERROR "missing environment variable: $name"
        return 1
    fi
}

main() {
    local failed=0

    for cmd in git python docker; do
        require_command "$cmd" || failed=1
    done

    for var in APP_ENV IMAGE_TAG; do
        require_env "$var" || failed=1
    done

    if [[ "${APP_ENV:-}" == "prod" && "${ALLOW_PROD:-0}" != "1" ]]; then
        log ERROR "production deployment not explicitly enabled"
        failed=1
    fi

    if (( failed )); then
        log ERROR "preflight failed"
        return 1
    fi

    log INFO "preflight passed"
}

main "$@"
```

This script demonstrates an important DevOps principle: validate dependencies and environment **before** an operation with a larger blast radius.

### Indirect parameter expansion

`${!name}` means "use the value of variable `name` as another variable name." If `name=APP_ENV`, `${!name}` retrieves the value of `APP_ENV`. This is useful in validation loops but should be used carefully because indirect behavior is harder to read than direct variables.

## Case Study — Produce a Machine-Readable Key/Value Report

```bash
#!/usr/bin/env bash
set -u
set -o pipefail

hostname_value=$(hostname) || exit 1
root_usage=$(df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}') || exit 1

printf 'hostname=%s\n' "$hostname_value"
printf 'root_usage_percent=%s\n' "$root_usage"
```

A calling process can parse stable key/value output. Avoid decorative banners if the output is intended for automation.

## Case Study — Compare Bash and Python for the Same Task

Bash is concise for command orchestration:

```bash
find logs -type f -name '*.log' -print0 |
    xargs -0 -r grep -h ' ERROR ' |
    awk '{print $3}' |
    sort |
    uniq -c |
    sort -nr
```

If the log becomes JSON and you must group by nested fields, apply time windows, validate schemas, and generate structured output, Python will often be clearer. Engineering skill includes knowing when a shell pipeline has crossed the maintainability boundary.

## Additional Shell Debugging Techniques

Run with execution tracing in a non-secret lab:

```bash
bash -x ./script.sh
```

Or inside a script for a small section:

```bash
set -x
some_command
set +x
```

**Warning:** tracing prints expanded commands and may expose secrets. Never enable it carelessly in production/CI when tokens or passwords can appear.

Syntax check without execution:

```bash
bash -n script.sh
```

Static analysis:

```bash
shellcheck script.sh
```

A useful debugging sequence is:

1. `bash -n` for syntax.
2. ShellCheck for suspicious constructs.
3. Run with controlled test input.
4. Add explicit logging around assumptions.
5. Use `bash -x` only when needed and safe.

## Additional Practice Tasks

1. Write `require_directory PATH` and test empty, missing, file-not-directory, and valid directory cases.
2. Write a function that accepts a percentage threshold and validates `0..100`.
3. Create `--dry-run` and `--apply` modes for a lab-only file move operation.
4. Add aggregated failure reporting so all preflight checks run before the script exits.
5. Capture a child process PID, wait for it, and propagate its exit status.
6. Write a script that works when called from a different current working directory.
7. Run the script in a minimal container and list assumptions that failed.
8. Explain why `eval`, unquoted expansions, and uncontrolled `rm -rf` are high-risk constructs.


## Enhanced Completion Checklist

- [ ] I understand shell/terminal/process distinctions.
- [ ] I understand command resolution and Bash's parse/expansion model.
- [ ] I think in argument boundaries rather than command strings.
- [ ] I can use special parameters and forward `"$@"` safely.
- [ ] I can use advanced parameter expansion intentionally.
- [ ] I understand arrays, associative arrays, mapfile, and safe reading.
- [ ] I understand subshells, grouping, pipelines, and process substitution.
- [ ] I can reason about stdin/stdout/stderr and custom file descriptors.
- [ ] I understand redirection ordering and `PIPESTATUS`.
- [ ] I understand `set -e`, `set -u`, and `pipefail` limitations.
- [ ] I can design a stable CLI with meaningful exit codes.
- [ ] I keep machine output on stdout and diagnostics on stderr.
- [ ] I use format-aware parsers for JSON/CSV.
- [ ] I can safely process arbitrary filenames with null delimiters.
- [ ] I use `mktemp`, traps, dry-run, and constrained targets.
- [ ] I can manage background jobs and bounded concurrency.
- [ ] I understand locking, idempotency, atomic replace, retry, and timeout patterns.
- [ ] I avoid `eval` and preserve untrusted data as data.
- [ ] I understand tracing, environment, umask, and secret-leakage risks.
- [ ] I can test scripts with syntax checks, ShellCheck, fakes, and temporary fixtures.
- [ ] I understand Bash vs POSIX portability boundaries.
- [ ] I can make a script work under CI/cron/systemd without CWD/TTY assumptions.
- [ ] I know when Bash should remain orchestration and Python should own complex logic.
- [ ] I completed the enhanced labs.
- [ ] I completed the Production Linux Operations Toolkit capstone.
