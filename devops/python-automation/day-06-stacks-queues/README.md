# Day 6: Basic DSA — Stacks & Queues in DevOps Automation
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 1: Basic Python Scripting & Core Data Structures (Days 1 to 6) — FINAL DAY OF PHASE 1**

---

## 🎯 Goal
Master LIFO (Stack) and FIFO (Queue) mechanics, implement configuration linting with bracket syntax tree traversal, build a rate-limited API ingress buffer with `collections.deque`, and solve LeetCode #20.

---

## 📂 Deliverables

### 1. `bracket_validator.py`
A stack-based configuration file linter:
- Uses LIFO (Last-In, First-Out) with Python list `.append()` and `.pop()`.
- Validates matching brackets `()`, `[]`, `{}` across JSON, YAML, and Terraform HCL scripts.
- Pinpoints syntax errors with exact line and column numbers.

**Execution:**
```bash
python bracket_validator.py
```

---

### 2. `request_buffer.py`
A production simulation of an ingress rate-limiting buffer:
- Implements a fixed-capacity 3-request buffer using `collections.deque` ($O(1)$ enqueue and dequeue).
- Supports backpressure rejection (`HTTP 429 Too Many Requests`) and telemetry drop policies (`drop_oldest`).
- Demonstrates fair FIFO queue worker dispatch.

**Execution:**
```bash
python request_buffer.py
```

---

### 3. `leetcode_20_valid_parentheses.py`
Optimized algorithmic solution to **LeetCode #20: Valid Parentheses**:
- $O(N)$ linear time complexity.
- $O(N)$ space complexity using stack state tracking.
- Handles edge cases: single bracket, unclosed nested brackets, odd-length strings, and immediate mismatches.

**Execution:**
```bash
python leetcode_20_valid_parentheses.py
```

---

## 💡 Real-World DevOps Applications
- **Infrastructure as Code (IaC) Linters**: `tflint`, `ansible-lint`, and Kubernetes YAML parsers use stack-based bracket parsers to catch syntax failures prior to deployment.
- **Message Queues & Event Buses**: RabbitMQ, Amazon SQS, and Celery worker pools rely on FIFO queue semantics to process asynchronous tasks without dropping burst traffic.
- **Circuit Breakers & Retries**: Queues manage retry backoff states when upstream microservices throttle connections.
