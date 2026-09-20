# Day 1: Python Basics & Filesystem Automation
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 1: Basic Python Scripting & Core Data Structures (Days 1 to 6)**

---

## 🎯 Goal
Automate manual system chores, inspect directories and file sizes, and establish core Python fundamentals for DevOps automation.

---

## 📂 Deliverables

### 1. `file_inspector.py`
Inspects any directory path passed as a CLI argument or interactive input, lists all files and directories, converts raw byte sizes into kilobytes (KB), and prints a structured summary.

**Usage:**
```bash
# Inspect current directory
python file_inspector.py .

# Inspect a specific project or log directory
python file_inspector.py /var/log
```

**Key Concepts Mastered:**
- `import os`
- Directory scanning via `os.listdir()`
- Path joining via `os.path.join()`
- Metadata inspection via `os.path.getsize()`, `os.path.isfile()`, `os.path.isdir()`
- Safe exception handling for `FileNotFoundError` and `PermissionError`

---

### 2. `hackerrank_warmups.py`
Solutions and automated verification tests for foundational Python warmup exercises:
1. Say Hello, World! with Python
2. Python If-Else (Conditionals)
3. Arithmetic Operators
4. Integer & Floating Point Division
5. Loops & List Comprehensions
6. Leap Year Function Calculation

**Test Execution:**
```bash
python hackerrank_warmups.py
```
Output:
```text
=== Testing HackerRank Python Warmups ===
[PASS] All HackerRank Python warmup tests passed successfully!
```
