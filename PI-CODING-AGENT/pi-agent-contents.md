# Pi Coding Agent

## Build your coding workflow around a small terminal agent

There are many coding agents.

This one is mine.

Not because Pi is the biggest coding agent, or because it has the most features. The opposite is the point: Pi keeps the core small and lets you shape the workflow around the way you already work.

Pi is a terminal coding harness. It connects a language model to a local project and gives that model a small set of tools:

- `read` — inspect files
- `write` — create or replace files
- `edit` — apply precise changes
- `bash` — run shell commands

From there, you can add project instructions, reusable skills, prompt templates, TypeScript extensions, themes, and complete Pi packages.

\pimentalmodel

This tutorial walks through the complete workflow: installation, authentication, your first repository task, project context, sessions, safety, automation, and customization.

---

## 1. Install Pi

Pi is distributed as an npm package.

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

The `--ignore-scripts` flag disables dependency lifecycle scripts during installation. Pi does not require install scripts for a normal npm installation.

Check that the command is available:

```bash
pi --version
```

On macOS and Linux, the official installer is another option:

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

The important thing is not the installation method. It is where you start Pi after installation.

Start it inside the project you want it to work on:

```bash
cd /path/to/your/project
pi
```

Do not start an agent in an arbitrary directory and expect it to understand your project. The current working directory is part of the agent's context.

---

## 2. Authenticate with a model provider

Pi can use a supported subscription provider through `/login`, or it can use an API key.

### Subscription login

Start Pi:

```bash
pi
```

Then run:

```text
/login
```

Choose a provider and follow its authentication flow.

### API key

You can set a provider key in your shell before starting Pi:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

Pi also supports many other providers, including OpenAI, Google Gemini, Mistral, Groq, OpenRouter, DeepSeek, Bedrock, and others. The exact environment variable depends on the provider.

You can also use `/login` to store a provider key in Pi's authentication file. Credentials are stored under:

```text
~/.pi/agent/auth.json
```

Never commit this file or place an API key in a project repository.

Once you are authenticated, choose a model with:

```text
/model
```

Or inspect available models from the command line:

```bash
pi --list-models
```

The model is replaceable. Your project workflow should not be tightly coupled to one provider.

---

## 3. Run your first session

Start with an inspection request, not an editing request.

```text
Summarize this repository and tell me how to run its checks.
```

This first request teaches you three things:

1. What Pi can see.
2. What commands it believes the project uses.
3. Whether the model understands the repository before it starts changing files.

A good first session usually follows this order:

1. Ask Pi to inspect the repository.
2. Ask it to locate the relevant files.
3. Ask it to explain the current behavior.
4. Give it one bounded task.
5. Run the project's checks.
6. Inspect the diff yourself.

A coding agent is most useful when you give it a clear boundary. “Improve this project” is not a boundary. “Add validation to this importer, preserve the public function signature, and run the existing importer tests” is a boundary.

\pifirstsession

---

## 4. Understand the four default tools

Pi gives the model four default tools.

\pitoolmap

### `read`

The model can inspect text files and images. This is how it learns the current state of the project.

### `write`

The model can create a new file or replace the contents of an existing file. Because `write` can replace a whole file, use it deliberately.

### `edit`

The model can apply a precise patch to an existing file. This is usually safer for a focused change because the surrounding file remains intact.

### `bash`

The model can run shell commands: tests, formatters, build scripts, Git commands, and other project tools.

The `--tools` option is an allowlist that replaces the default tool set. Pass only read-only tools when you want a read-only review:

```bash
pi --tools read,grep,find,ls -p "Review this repository for risky patterns"
```

This gives the model `read`, `grep`, `find`, and `ls` — not `bash`, `edit`, or `write`.

The small tool set is intentional. Pi does not try to hide all activity behind a large collection of abstractions. You can see which actions are available and shape the rest yourself.

---

## 5. Inspect before you edit

The most reliable Pi workflow is:

> Locate → understand → change → verify.

\piinspectflow

Start by asking Pi to find the relevant entry points and tests.

```text
Find the code responsible for importing CSV files. Explain the current flow and identify the existing tests. Do not edit anything yet.
```

Then ask for a proposal:

```text
Based on what you found, propose the smallest implementation that adds row validation without changing the public API. Wait for my approval before editing.
```

Then implement:

```text
Implement the approved change. Keep the patch focused. Run the focused tests when finished and stop before committing.
```

Finally, verify:

```text
Review the current diff against the original requirement. Run the relevant checks and report anything that remains uncertain.
```

This separation matters. The agent can inspect, reason, edit, and test. You should still decide whether the result is correct.

---

## 6. Prompt for a result

A strong prompt has four parts:

- the goal
- the constraints
- the workflow
- the verification command

For example:

```text
Goal: add CSV validation for the import command.

Constraints:
- preserve the public function signature
- do not add a runtime dependency
- report every invalid row with its line number
- follow the existing project style

Workflow:
1. inspect the importer and existing tests
2. propose the smallest implementation
3. implement it
4. run the focused tests
5. summarize the diff and any remaining risks
```

This is more useful than asking Pi to “make the code better.”

The quality of the result depends partly on the quality of the boundary. If the task is ambiguous, ask Pi to identify the ambiguity instead of silently choosing an architecture.

---

## 7. Attach files and run commands

In interactive mode, type `@` to search for and reference files:

```bash
pi @README.md @src/app.ts "Review these files together and explain the current data flow."
```

You can reference several files in one prompt. Images can also be attached in terminals that support image input.

You can run a shell command from the editor with `!`:

```text
!npm test
```

The command output is sent into the model's context.

Use `!!` when you want to run a command without sending its output to the model:

```text
!!git status --short
```

This distinction helps keep the context useful. Not every command result needs to become part of the conversation.

---

## 8. Give the project permanent instructions

If you repeat the same instructions in every session, move them into an `AGENTS.md` file.

Example:

```markdown
# Project Instructions

- Run `npm run check` after code changes.
- Do not edit generated files directly.
- Preserve the public API unless the task explicitly changes it.
- Never commit secrets or local environment files.
- Keep responses concise and report uncertainty.
```

Pi loads context files from:

- `~/.pi/agent/AGENTS.md` — global instructions
- parent directories — shared instructions
- the current project directory — local instructions
- `CLAUDE.md` — also supported

If a directory contains `AGENTS.override.md`, Pi loads it instead of that directory's `AGENTS.md` or `CLAUDE.md` file. Context files from other directories, including global and parent directories, are still loaded and concatenated.

After changing a context file, run:

```text
/reload
```

Or restart Pi.

Use context files for durable project rules: commands, conventions, constraints, and safety boundaries. Do not use them as a dumping ground for every thought from every session.

---

## 9. Understand project trust

Pi may ask whether you trust a project when it contains project-local resources such as:

- `.pi/settings.json`
- `.pi/extensions/`
- `.pi/skills/`
- `.pi/prompts/`
- `.pi/themes/`
- project packages

Trust controls whether Pi loads those project-local resources. It is useful protection against a repository silently changing the agent's configuration before you inspect it.

But project trust is not a sandbox.

\pitrust

Once Pi is running, its tools use the permissions of your user account. The model can still read and write files and run commands that your account is allowed to run.

For an untrusted repository, generated code you will not monitor closely, or unattended automation, use a real isolation boundary:

- a container
- a virtual machine
- a micro-VM
- a policy-controlled sandbox

Treat repository instructions, comments, documentation, and build output as possible prompt-injection surfaces. Read them as code and configuration, not as authority.

---

## 10. Use Git as your checkpoint

Before asking Pi to make changes, create a rollback point.

```bash
git status --short
git switch -c pi/feature-name
```

Then work on a bounded task:

```text
Implement the issue. Run the focused checks and stop before committing.
```

When Pi finishes:

```bash
git diff
git diff --check
npm test
```

Read the diff yourself. Check that:

- only the intended files changed
- no secrets or generated artifacts were added
- the implementation matches the requirement
- tests cover the behavior that changed
- unrelated cleanup did not sneak into the patch

Pi can make a commit if you explicitly ask it to, but you do not need to give it that responsibility. A useful default is to let Pi implement and verify, then let you decide whether to commit.

\pigitcheckpoint

---

## 11. Use the interactive commands

The interactive interface exposes commands through `/`.

Useful commands include:

```text
/login       authenticate a provider
/logout      clear stored credentials
/trust       save the project trust decision
/model       switch models
/settings    change Pi settings
/session     show session information
/resume      choose a previous session
/new         start a fresh session
/tree        navigate the session tree
/fork        create a session from an earlier user message
/clone       duplicate the active branch
/compact     summarize older context
/reload      reload project resources
/hotkeys     show keyboard shortcuts
/export      export the session
/quit        exit Pi
```

You do not need to memorize everything. Run `/hotkeys` whenever you forget a shortcut.

Common shortcuts:

- `Shift+Enter` — insert a new line
- `Escape` — abort the current operation
- `Ctrl+C` — clear the editor; press twice to quit
- `Ctrl+L` — choose a model
- `Shift+Tab` — cycle thinking levels
- `Ctrl+O` — expand or collapse tool output
- `Escape` twice — open the session tree
- `Alt+Enter` — queue a follow-up message

If modified Enter keys fail inside tmux, add this to `~/.tmux.conf` on tmux 3.5 or newer:

```tmux
set -g extended-keys on
set -g extended-keys-format csi-u
```

Then restart the tmux server.

---

## 12. Treat sessions as recoverable work

Pi saves sessions as JSONL files organized by working directory.

From the shell:

```bash
pi --name "release-audit"
pi -c                 # continue the most recent session
pi -r                 # browse previous sessions
pi --no-session       # run without saving a session
```

Inside a session:

- `/tree` navigates between branches in the same session file.
- `/fork` creates a new session from an earlier user message.
- `/clone` duplicates the current active branch.
- `/resume` opens a previous session.

Use branching when you want to test two approaches without losing the first one.

For example:

1. Ask Pi to investigate two possible implementations.
2. Use `/fork` from the shared starting point.
3. Try one implementation on branch A.
4. Try the alternative on branch B.
5. Compare the results.

Session history is useful, but it is not a replacement for project documentation. If a decision matters after the session ends, write it into a file, issue, or commit message.

\pisessions

---

## 13. Manage a long context

Long coding sessions eventually approach the model's context limit. Pi can automatically compact older conversation, or you can compact manually:

```text
/compact
```

You can give compaction a focus:

```text
/compact Focus on decisions, modified files, remaining tests, and unresolved risks.
```

Compaction summarizes older messages while keeping recent work. It is useful, but it is lossy. The full history remains in the session file, but the model will work from the summary and the retained messages.

A good long-session habit is to periodically write a durable checkpoint:

```markdown
# Current work

## Done
- Added the importer validation layer.

## Remaining
- Add one failure-case test.
- Update the README example.

## Decision
- Validation happens before normalization so line numbers remain accurate.
```

Context management is partly an agent feature and partly an engineering discipline. Keep important knowledge in the repository.

\picompaction

---

## 14. Select models and thinking levels

Switch models interactively:

```text
/model
```

Or from the shell:

```bash
pi --provider openai --model gpt-4o "Review the tests"
pi --model anthropic/claude-sonnet-4 "Implement the fix"
pi --thinking high "Trace this difficult failure"
```

Thinking levels range from `off`, `minimal`, and `low` through higher reasoning levels such as `medium`, `high`, `xhigh`, and `max`, depending on the model.

A practical rule:

- use a faster model for navigation and mechanical edits
- use stronger reasoning for architecture and ambiguous debugging
- use higher thinking levels when the problem benefits from more deliberate analysis
- keep the task itself clear regardless of model choice

Check the footer or run `/session` to see the current model, context usage, tokens, and cost. Do not guess which model is active.

---

## 15. Use print mode for one-shot work

Interactive mode is best when you want to collaborate through a task. Print mode is useful for a single request:

```bash
pi -p "Summarize this codebase"
```

Pipe a file into Pi:

```bash
cat README.md | pi -p "Suggest three documentation improvements"
```

Run a read-only review:

```bash
pi --tools read,grep,find,ls -p "Review this repository for risky patterns"
```

Print mode is useful in scripts and CI, but model output is still untrusted input. If another program consumes the result, validate it before taking action.

\piprintmode

---

## 16. Use JSON event mode for observability

JSON event mode emits session and agent events as JSON lines:

```bash
pi --mode json "List the files in this project"
```

The stream can include:

- session start information
- agent and turn lifecycle events
- assistant message updates
- tool execution events
- queue updates
- compaction events
- retry events

For example:

```bash
pi --mode json "List the files in this project" 2>/dev/null \
  | jq -c 'select(.type == "message_end")'
```

Streaming message updates are deltas, not complete cumulative messages. Assemble them by content index when building a client, and treat the final `message_end` event as authoritative.

Use JSON mode when you need structured output from a one-shot process but do not need to build a full interactive client.

\pijsonmode

---

## 17. Integrate with RPC mode

RPC mode runs Pi as a headless JSON protocol over stdin and stdout:

```bash
pi --mode rpc --no-session
```

Clients send one JSON object per line. Pi returns response objects and streams agent events.

A minimal prompt command looks like this:

```json
{"id":"req-1","type":"prompt","message":"Summarize this repository"}
```

RPC supports prompting, steering, follow-up messages, aborting work, model selection, session inspection, compaction, Bash execution, and more.

Important protocol detail: RPC uses strict LF-delimited JSONL framing. Split records on `\n` only. Do not use a generic reader that treats Unicode line separators as record delimiters because those characters can legally appear inside JSON strings.

RPC is a good fit when:

- your client is written in Python, Go, Rust, or another language
- you want process isolation
- you are building an IDE or custom UI
- you want the agent to run as a separate process

For a Node or TypeScript application in the same process, the SDK is usually more direct.

\pioutputmode{RPC}{JSON over stdin and stdout}{Your application process}

---

## 18. Add a skill

A skill is a self-contained capability package that Pi loads on demand.

Create:

```text
.pi/skills/release-check/SKILL.md
```

With content like:

```markdown
---
name: release-check
description: Checks a repository before a release. Use for release audits.
---

# Release check

1. Read the changelog and package version.
2. Run the project's test and build commands.
3. Inspect the staged diff.
4. Report blockers; do not publish.
```

The skill name must use lowercase letters, numbers, and hyphens. Its description matters because the description helps Pi decide when the skill is relevant.

You can invoke the skill explicitly:

```text
/skill:release-check
```

Use skills for reusable, on-demand procedures. Use `AGENTS.md` for rules that should apply to every task.

\pistack

---

## 19. Turn prompts into commands

Prompt templates turn repeated prompts into slash commands.

Create:

```text
.pi/prompts/review.md
```

```markdown
---
description: Review staged changes
argument-hint: "[focus]"
---

Review the staged git changes.
Focus on: $@.
Report bugs, security issues, and missing tests.
```

The filename becomes the command, so this file becomes:

```text
/review
```

Templates support positional arguments such as `$1` and `$2`, as well as `$@` for all arguments.

A good template captures a repeatable workflow. It should not become a giant personality prompt. Keep it specific enough that the output is consistent and useful.

---

## 20. Use extensions for behavior

Extensions are TypeScript modules. They can:

- register custom tools
- add commands
- intercept tool calls
- respond to lifecycle events
- add safety gates
- customize the terminal UI
- modify compaction
- checkpoint Git
- integrate external systems

A minimal command extension looks like this:

```typescript
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  pi.registerCommand("hello", {
    description: "Show a custom command",
    handler: async (_args, ctx) => {
      ctx.ui.notify("Hello from an extension", "info");
    },
  });
}
```

Load an extension for one run:

```bash
pi -e ./my-extension.ts
```

Or place it in a discovered extension directory such as:

```text
~/.pi/agent/extensions/
.pi/extensions/
```

Extensions are powerful because they are ordinary code with access to the same local environment as Pi. Review them like any other dependency.

---

## 21. Add a safety gate

One useful extension pattern is intercepting dangerous Bash commands:

```typescript
pi.on("tool_call", async (event, ctx) => {
  if (event.toolName !== "bash") return;

  const command = event.input.command ?? "";
  if (command.includes("rm -rf") || command.includes("sudo")) {
    const allowed = await ctx.ui.confirm(
      "Dangerous command",
      command,
    );

    if (!allowed) {
      return { block: true, reason: "Blocked by user" };
    }
  }
});
```

This is a pattern, not a complete security policy. String matching is imperfect. Your real gate should reflect the commands, paths, and environments that matter in your projects.

Other useful safety extensions can:

- protect `.env` and credential files
- block writes inside `.git/` or `node_modules/`
- require confirmation before publishing
- create a Git checkpoint before a turn
- prevent session changes when the repository is dirty

The goal is not to create the illusion of safety. The goal is to make important boundaries explicit and observable.

\pigate

---

## 22. Share a Pi package

When your skills, prompts, extensions, and themes become useful across projects, bundle them into a Pi package.

Install packages from npm:

```bash
pi install npm:@your-org/pi-tools
```

Or from Git:

```bash
pi install git:github.com/your-org/pi-tools@v1
```

Inspect installed packages:

```bash
pi list
```

Update packages:

```bash
pi update --all
```

A package can declare its resources in `package.json`:

```json
{
  "name": "my-pi-package",
  "keywords": ["pi-package"],
  "pi": {
    "extensions": ["./extensions"],
    "skills": ["./skills"],
    "prompts": ["./prompts"],
    "themes": ["./themes"]
  }
}
```

Use `-l` when you want a project-local installation:

```bash
pi install -l npm:@your-org/pi-tools
```

Review package source before installing it. Extensions execute code with your permissions, and skills can instruct the agent to perform actions.

---

## 23. Connect a local or custom model

Pi can load custom providers and models through:

```text
~/.pi/agent/models.json
```

For an OpenAI-compatible local server such as Ollama, the configuration can look like this:

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        { "id": "qwen2.5-coder:7b" }
      ]
    }
  }
}
```

Pi supports these API styles:

- OpenAI Chat Completions
- OpenAI Responses
- Anthropic Messages
- Google Generative AI

Open `/model` after editing `models.json` to reload the model catalog.

Custom model configuration is useful for local inference, private gateways, proxies, and providers not included in the built-in catalog. For an endpoint that does not speak one of the supported API styles or that needs a custom OAuth flow, register a custom provider from a TypeScript extension instead. You are responsible for understanding the compatibility and authentication behavior of the endpoint you connect.

\pilocalmodel

---

## 24. Embed Pi with the SDK

If you are building a Node or TypeScript application, you can use Pi in the same process instead of spawning the CLI.

Install the package:

```bash
npm install @earendil-works/pi-coding-agent
```

Minimal example:

```typescript
import {
  createAgentSession,
  ModelRuntime,
  SessionManager,
} from "@earendil-works/pi-coding-agent";

const modelRuntime = await ModelRuntime.create();

const { session } = await createAgentSession({
  modelRuntime,
  sessionManager: SessionManager.inMemory(),
});

session.subscribe((event) => {
  if (
    event.type === "message_update" &&
    event.assistantMessageEvent.type === "text_delta"
  ) {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("What files are in this project?");
```

The SDK gives you direct access to:

- session state
- model selection
- thinking levels
- message queues
- compaction
- events
- built-in tools
- custom tools
- resource loading
- persistent or in-memory sessions

Use RPC when you want a language-agnostic process boundary. Use the SDK when you want type-safe access inside a Node or TypeScript application.

\pisdk

---

## 25. Sandbox untrusted work

Pi does not include a built-in sandbox. It runs with the permissions of the user who starts it.

For simple local isolation, run the whole process in a container.

A minimal Docker image can install Pi like this:

```dockerfile
FROM node:24-bookworm-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends bash ca-certificates git ripgrep \
  && rm -rf /var/lib/apt/lists/*

RUN npm install -g --ignore-scripts @earendil-works/pi-coding-agent

WORKDIR /workspace
ENTRYPOINT ["pi"]
```

Build and run it:

```bash
docker build -t pi-sandbox -f Dockerfile.pi .

docker run --rm -it \
  -e ANTHROPIC_API_KEY \
  -v "$PWD:/workspace" \
  -v pi-agent-home:/root/.pi/agent \
  pi-sandbox
```

A mounted workspace can still write through to your host. Use read-only mounts when appropriate, and pass only the credentials and network access the task needs.

For stronger isolation, use a VM, micro-VM, or policy-controlled sandbox.

\pisandbox

---

## 26. The capstone workflow

Now use Pi to ship a small, real change.

### Step 1: create a checkpoint

```bash
git status --short
git switch -c pi/capstone-task
```

### Step 2: write acceptance criteria

```text
I need to add a command that validates the imported CSV before processing it.

Acceptance criteria:
- invalid rows include their line number
- valid rows preserve the current output format
- no new runtime dependency
- existing tests continue to pass

First inspect the relevant files and tests. Do not edit until you explain the current flow.
```

### Step 3: implement the smallest change

```text
Implement the smallest change that satisfies the criteria. Keep the public API unchanged. Run the focused tests after editing.
```

### Step 4: review the result

```text
Review the diff against the acceptance criteria. Look for missing tests, accidental scope expansion, and behavior that is only assumed rather than verified.
```

### Step 5: verify it yourself

```bash
git diff
git diff --check
npm test
```

Only commit when you understand the result. Stage only the files you reviewed:

```bash
git add path/to/importer.ts path/to/test_importer.ts
git diff --cached
git commit -m "Validate imported CSV rows"
```

The agent helped produce the change. The evidence is the test output and the diff.

---

## 27. Troubleshooting

### Pi cannot find a model

Run:

```text
/login
/model
```

If you use an API key, check the provider's expected environment variable and verify that the key is available in the shell where Pi starts.

### Pi ignores project instructions

Check that the file is named `AGENTS.md` or `CLAUDE.md`, that it is in the current directory or an ancestor, and that the startup header lists it. Run:

```text
/reload
```

### Modified keys do not work

Check your terminal and tmux configuration. A dedicated terminal with Kitty keyboard protocol support usually gives the best experience.

### The context is too large

Use:

```text
/compact
```

Then continue with a smaller, more focused prompt. Put durable decisions in a project file rather than depending on the session history.

### Pi made the wrong change

Stop. Inspect the diff. Revert deliberately if necessary. Then tighten the prompt with the missing constraint or acceptance criterion.

Do not respond to a wrong change by giving the agent a larger, more emotional prompt. Give it a narrower one.

---

## 28. The operating checklist

Before a task:

- start Pi in the correct project directory
- check the repository status
- create a branch or checkpoint
- define the acceptance criteria
- tell Pi which checks to run

During the task:

- inspect before editing
- keep the task bounded
- read tool calls and outputs
- interrupt when the direction is wrong
- use a focused session for a focused problem

After the task:

- run the tests
- inspect the diff
- check for secrets and generated files
- record important decisions
- commit only what you understand

Customize Pi only after you have repeated the workflow enough to know what should be automated.

---

## Final thought

Pi's value is not that it gives you an autonomous machine that can do anything.

Its value is that it gives you a small, inspectable runtime that you can adapt to your own engineering judgment.

Start with four tools.

Add a project instruction file.

Build one skill for a repeated workflow.

Add a safety gate before you add more power.

Keep the boundary yours.

**Inspect. Shape. Verify.**

---

## Official references

- Pi documentation: <https://pi.dev>
- Pi source repository: <https://github.com/earendil-works/pi-mono>
- npm package: <https://www.npmjs.com/package/@earendil-works/pi-coding-agent>
