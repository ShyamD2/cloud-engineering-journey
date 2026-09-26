# Day 4: Basic DSA — Arrays & Lists in DevOps Automation
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 1: Basic Python Scripting & Core Data Structures (Days 1 to 6)**

---

## 🎯 Goal
Master dynamic array operations in Python (`list`), understand time-complexity implications for cloud server inventories, implement IP address classification, paginate server log streams, and solve LeetCode #1929.

---

## 📂 Deliverables

### 1. `list_operations.py`
Practical infrastructure list manipulation demonstrating:
- Dynamic insertion, appending ($O(1)$ amortized), removal, and TimSort ($O(N \log N)$).
- **IP Address Sanitization**: Segregates RFC1918 private CIDR nodes (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) from public internet nodes while stripping malformed records and preserving order without duplicates.
- **Log Stream Pagination**: Uses Python slice notation `[start:stop:step]` for terminal log chunking.
- **Performance Benchmark**: Proves $O(1)$ direct index access vs $O(N)$ linear membership search over 100,000 nodes.

**Run Demo & Unit Tests:**
```bash
python list_operations.py
```

---

### 2. `leetcode_1929_concatenation.py`
High-efficiency implementations of **LeetCode #1929: Concatenation of Array**:
- Operator Concatenation (`nums + nums`)
- In-place `.extend()`
- Pre-allocated zero array assignment (systems-level memory layout)

**Test Execution:**
```bash
python leetcode_1929_concatenation.py
```

---

## 💡 Big-O Cheat Sheet for DevOps Lists
| Operation | Time Complexity | Real-World Cloud Implication |
| :--- | :---: | :--- |
| `list[i]` (Index Lookup) | $O(1)$ | Instant lookup by node slot ID |
| `list.append(x)` | $O(1)$ amortized | Adding new metrics or log lines |
| `list.pop()` | $O(1)$ | Removing last element (Stack behavior) |
| `x in list` (Search) | $O(N)$ | Searching through thousands of server hostnames — switch to `set` for $O(1)$ |
| `list.insert(0, x)` | $O(N)$ | Prepending requires shifting all pointers in memory — use `deque` instead |
| `list.sort()` | $O(N \log N)$ | Sorting resource metrics before reporting |
