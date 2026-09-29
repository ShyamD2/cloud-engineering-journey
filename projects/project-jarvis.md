# Project: J.A.R.V.I.S. (AgentOS) — Cyber-Physical Autonomous Operating System

## The Vision & Architecture
Most AI agent frameworks are limited to text chatbots, mock terminal demos, or brittle browser-only tools. **Project J.A.R.V.I.S.** is a production-grade cyber-physical **AgentOS** that unites:
1. **Physical World**: Real-time IoT microcontrollers (ESP32 dual-relay controllers, ambient lux sensors, Raspberry Pi gateways).
2. **Computer World**: Deep native Windows OS automation (Windows UIAutomation Accessibility Tree + Multi-Modal Vision Grounding, persistent ConPTY terminal sessions, Chrome/Edge DevTools CDP).
3. **Cloud & Mobile Mesh**: AWS cloud infrastructure (EventBridge, S3, SQS, DynamoDB), Telegram 2.0 full ReAct mobile gateway, and Cloudflare HTTPS remote trackpads.

---

## Core Technical Innovations

### 1. Dual-Channel Neuro-Symbolic Computer Control
- Standard OS agents rely exclusively on either visual screenshots (slow, high token consumption, imprecise) or accessibility trees (breaks on canvas/Electron apps).
- J.A.R.V.I.S. implements a **Hybrid Neuro-Symbolic Agent**:
  - Queries the native Win32 UIAutomation tree for deterministic element coordinates and control patterns.
  - Falls back to normalized `[0, 1000]` multi-modal vision grounding when dealing with custom-rendered web apps or gaming engines.
  - Verifies all actions using `VisualSentinel`, comparing pre-action and post-action screen diffs and bounding boxes.

### 2. Hands-Free On-Device Neural Wake-Word (`openWakeWord` ONNX)
- Runs sub-10ms acoustic inference 100% on CPU using local ONNX acoustic models (`hey_jarvis_v0.1.onnx`) and Silero Voice Activity Detection (VAD).
- Dynamic energy thresholding adapts to ambient room noise floor (150–550 RMS).
- Silent Windows background daemonization via `pythonw.exe` and VBScript, registered in Windows Startup and Registry for zero-window ambient listening.

### 3. Telegram 2.0 ReAct Mobile Gateway & Remote Trackpad
- 100% of mobile messages, voice notes, and compound instructions route through the ReAct conversation engine.
- Interactive inline keyboards provide cryptographic HMAC-SHA256 one-tap approval gates for mutating operations.
- Cloudflare HTTPS tunnel hosts a mobile trackpad web application providing multi-touch gesture control, virtual keyboard injection, and live PC screen streaming.

### 4. Enterprise Safety & Resilience Architecture
- **4-Tier Blast Radius Matrix**: Every tool explicitly declares its action tier (`TIER_0_REFLEX` to `TIER_3_DESTRUCTIVE`) bound to parameter SHA-256 HMAC signatures.
- **Differential SystemUndo**: Maintains transactional file and registry snapshots before modifications, supporting instant reverse DAG rollbacks.
- **DevSecOps AST Immune Sandbox**: Pre-execution static analysis blocking unauthorized imports, shell injection vectors, and path jailbreaks.
- **Workstation SRE Watchdog**: Proactive reliability daemon monitoring port health (8000, 8085, 9222), hunting zombie processes, and executing self-healing runbooks.

### 5. Real-Time Recitation Interrupt Service & Multi-Modal Barge-In
- **Sub-10ms Coordinated Interruption**: Engineered centralized singleton `InterruptService` halting audio synthesis, soundboards, and `pygame.mixer` instantaneously upon barge-in.
- **Immediate Acoustic Keyword Interruption**: No wake-word required during active speech recitation. Speaking negative keywords (*"stop"*, *"quiet"*, *"silence"*, *"shut up"*, *"cancel"*, *"pause"*, *"wait"*) cuts audio within <10ms.
- **Clause-Level Progressive Streaming**: Splits multi-sentence explanations into discrete clauses, starting vocal playback in <450ms while enabling instant interruption at 20ms polling intervals.
- **Multi-Modal Controls**: Non-blocking console keyboard hotkeys (<kbd>Space</kbd>, <kbd>Esc</kbd>, <kbd>q</kbd>) and REST endpoints (`POST /api/v1/query/interrupt`).

---

## Verification & Proof of Work
- **100% Green CI on GitHub Actions across 3 continuous integration gates**:
  - `lint.yml` (Syntax, Code Quality & Ruff Static Gate)
  - `security.yml` (Security & Vulnerability Guard, Bandit AST static analysis)
  - `test.yml` (J.A.R.V.I.S. Test & Reliability Suite on Windows Server runner)
- **183 / 183 Automated Tests Passing (100% Pass Rate)**:
  - `tests/unit/` (104 tests — core routes, subsystems, concurrency chaos, disaster recovery, memory, FinOps)
  - `tests/security/` (60 tests — 10 audit invariants, constant-time HMAC tokens, jailbreak defenses, replay protection)
  - `tests/verification/` (12 tests — reality discrepancy, ground-truth verification, zero-trust contracts)
  - `tests/e2e/` (7 tests — real-machine application launching, closing, Docker status, file mutations, Telegram commands)
- **100-Task Empirical Reliability Benchmark**:
  - **98.0% Pass Rate Local** (98/100) / **96.0% Pass Rate on GitHub Actions CI Runner** (96/100)
  - **0.00% False-Success Rate** (Strict Zero-Trust Invariant enforced)
  - **Latency P50**: **5.27 ms** (CI ingress) / **73.99 ms** (Local full pipeline)
- **100/100 Architectural Category Elevation**:
  - **Phase 1: Zero-Trust Security** (`SecurityGuardMiddleware`, AST injection defense)
  - **Phase 2: Production Readiness** (SQLite WAL mode, ACID `MissionControl` persistence)
  - **Phase 3: Computer Control** (Windows Core Audio COM API `<2ms` zero-focus volume/mute)
  - **Phase 4: AI & Agent Architecture** (Hierarchical Working Memory, dynamic cost/complexity routing, pre-flight tool schema validation)
  - **Phase 5: Testing & QA Overhaul** (All 18 core routes tested, subsystem tests, 50-thread WAL chaos tests, persistent EventMesh spooling)

*Source Code Repository:* [https://github.com/ShyamD2/project-jarvis](https://github.com/ShyamD2/project-jarvis)
