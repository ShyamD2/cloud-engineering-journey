# Day 3: Automated Job / Cron Script — Filesystem Lifecycle Management
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 1: Basic Python Scripting & Core Data Structures (Days 1 to 6)**

---

## 🎯 Goal
Automate disk hygiene and temporary file pruning on production Linux/Windows servers using Python filesystem timestamp APIs (`os.path.getmtime`), safe deletion protocols (`os.remove`), dry-run simulations, and cron scheduling.

---

## 📂 Deliverables

### `auto_cleanup.py`
A production-ready filesystem cleanup automation script that:
- Recursively scans target directories for stale ephemeral files (`.tmp`, `.bak`, `.old`, `.cache`).
- Determines exact file age in days using `time.time() - os.path.getmtime(path)`.
- Implements a `--dry-run` safety flag for zero-risk pre-execution audits.
- Deletes expired files cleanly while catching filesystem race conditions and `PermissionError`s.
- Writes an append-only audit trail with timestamps and freed space metrics to `cleanup.log`.
- Provides an automated test harness with mock file timestamp creation via `os.utime()`.

**Usage:**
```bash
# 1. Preview which files would be removed without deleting (Dry-Run)
python auto_cleanup.py --dir /var/tmp --days 2 --dry-run

# 2. Execute live cleanup on directory for files older than 48 hours
python auto_cleanup.py --dir /tmp/scratch --days 2

# 3. Run automated verification test suite
python auto_cleanup.py --test
```

---

## ⏰ Cron Integration (Linux Production Deployment)
To automate this script on a Linux server every midnight using `crontab -e`:

```cron
# Run daily at 00:00 UTC, purge /tmp files older than 3 days, log output
0 0 * * * /usr/bin/python3 /opt/scripts/auto_cleanup.py --dir /tmp --days 3 --log /var/log/tmp_cleanup.log >> /var/log/cron_cleanup.err 2>&1
```

---

## 💡 Key Engineering Takeaways
1. **Always implement `--dry-run`**: Deleting production files based on programmatic glob patterns must always be verified in dry-run mode first.
2. **mtime vs ctime**: `st_mtime` tracks file content modification time. On Linux, `st_ctime` tracks inode metadata changes (e.g. permissions), not file creation time. `mtime` is the standard signal for staleness.
3. **Handle open file locks safely**: Especially on Windows, files being actively held by running services can fail deletion. Trapping `PermissionError` prevents batch aborts.
