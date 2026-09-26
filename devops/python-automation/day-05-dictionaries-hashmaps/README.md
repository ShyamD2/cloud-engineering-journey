# Day 5: Basic DSA — Dictionaries & HashMaps in DevOps Observability
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 1: Basic Python Scripting & Core Data Structures (Days 1 to 6)**

---

## 🎯 Goal
Understand hash table mechanics in Python (`dict` and `set`), achieve $O(1)$ average time complexity for frequency counting, build a real-time HTTP log traffic analyzer, and solve LeetCode #217.

---

## 📂 Deliverables

### 1. `http_status_counter.py`
A high-performance frequency aggregator for web access logs:
- Aggregates status code occurrences in $O(N)$ linear time and $O(K)$ space using Python dictionaries.
- Categorizes traffic into standard RFC response families:
  - `2xx`: Success
  - `3xx`: Redirection
  - `4xx`: Client Errors
  - `5xx`: Server Errors
- Computes error rate percentage ($4xx + 5xx$) and triggers automated SLO breach flags when error rates exceed threshold (5%).
- Includes built-in self-tests.

**Execution:**
```bash
python http_status_counter.py
```

---

### 2. `leetcode_217_contains_duplicate.py`
Three distinct algorithmic approaches to solve **LeetCode #217: Contains Duplicate**:
1. **HashSet Length Comparison**: Pythonic one-liner using `len(nums) != len(set(nums))` ($O(N)$ time, $O(N)$ space).
2. **Early-Exit Streaming Set**: Streams integers and terminates immediately upon discovering the first duplicate (Best case $O(1)$, worst case $O(N)$).
3. **In-Place Sorting**: Sorts first and checks adjacent neighbors ($O(N \log N)$ time, $O(1)$ auxiliary space) for memory-constrained embedded environments.

**Execution:**
```bash
python leetcode_217_contains_duplicate.py
```

---

## 💡 Real-World DevOps Applications
- **Prometheus Metrics**: Hash maps form the bedrock of Prometheus labels (`{"status": "500", "handler": "/checkout"}`).
- **Rate Limiting & Token Buckets**: Tracking API client quotas by IP address in Redis or in-memory Python dictionaries.
- **Log Anomaly Detection**: Detecting sudden spikes in $5xx$ error frequencies to trigger automated rollback deployments.
