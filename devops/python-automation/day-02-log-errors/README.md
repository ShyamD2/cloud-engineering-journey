# Day 2: Finding Log Errors & File I/O
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 1: Basic Python Scripting & Core Data Structures (Days 1 to 6)**

---

## 🎯 Goal
Safely process server log files using Python's context managers (`with open()`), filter incident errors without exhausting system RAM on multi-gigabyte logs, and export a clean incident report to `errors_only.txt`.

---

## 📂 Deliverables

### 1. `server.log`
A realistic 25-line multi-subsystem server log containing standard production logs across auth, database, payment, ingress, and queue workers with `INFO`, `WARN`, `ERROR`, and `CRITICAL` levels.

### 2. `log_error_finder.py`
A robust streaming log parser that:
- Reads files line-by-line using Python generator streaming (`for line in in_f`) for $O(1)$ memory consumption.
- Identifies `ERROR` and `CRITICAL` entries with regex-assisted subsystem extraction.
- Exports filtered incident lines to `errors_only.txt`.
- Emits a clean terminal dashboard with total lines, error rate percentage, and breakdown by subsystem.
- Includes automated unit tests accessible via `--test`.

**Usage:**
```bash
# Filter errors from default server.log to errors_only.txt
python log_error_finder.py

# Specify custom input and output files
python log_error_finder.py --log /var/log/nginx/error.log --out /tmp/nginx_errors.txt

# Run automated verification tests
python log_error_finder.py --test
```

### 3. `errors_only.txt`
Extracted output containing exactly the 10 flagged incidents (8 `ERROR`, 2 `CRITICAL`) ready for ingestion by incident management tools (PagerDuty / Slack alerts).

---

## 💡 Key Engineering Takeaways
1. **Never use `.readlines()` on production logs**: Loading an entire 10 GB access log into memory via `f.readlines()` causes `MemoryError` and OOM kills. Iterating directly over file handles (`for line in f:`) streams chunks dynamically.
2. **Context Manager Safety**: `with open(...) as f:` guarantees file descriptor closure even if exceptions or keyboard interrupts occur mid-stream.
3. **Encoding & Error Handling**: Always specify `encoding="utf-8"` with `errors="replace"` to avoid crashing on non-ASCII binary artifacts or UTF-8 corruption.
