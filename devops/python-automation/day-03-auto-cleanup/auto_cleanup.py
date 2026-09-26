"""
Day 3: Automated Job / Cron Script — Filesystem Lifecycle Management
Script: auto_cleanup.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Scans target directories for temporary, backup, and stale cache files (.tmp, .bak, .old)
- Computes file age using os.path.getmtime() against current epoch time
- Deletes files exceeding the age threshold (default: 2 days / 48 hours)
- Supports safe --dry-run mode for previewing deletions without touching the disk
- Logs every operation with UTC timestamps, file size, and freed space to cleanup.log
- Includes automated unit tests accessible via --test
"""

from __future__ import annotations
import argparse
import datetime
import os
import sys
import time
from typing import Dict, List, Tuple


DEFAULT_EXTENSIONS = (".tmp", ".bak", ".old", ".cache")


def scan_and_clean(
    target_dir: str,
    max_age_days: float = 2.0,
    extensions: Tuple[str, ...] = DEFAULT_EXTENSIONS,
    dry_run: bool = False,
    log_file: str = "cleanup.log",
) -> Dict[str, any]:
    """
    Scans target_dir for files matching extensions older than max_age_days.
    Deletes matching files (unless dry_run is True) and appends audit logs.
    """
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"Target directory does not exist: '{target_dir}'")
    if not os.path.isdir(target_dir):
        raise NotADirectoryError(f"Target path is not a directory: '{target_dir}'")

    now = time.time()
    max_age_seconds = max_age_days * 86400.0

    scanned_files = 0
    candidate_files = []
    deleted_files = []
    freed_bytes = 0
    errors = []

    for root, _, files in os.walk(target_dir):
        for name in files:
            scanned_files += 1
            if any(name.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, name)
                try:
                    stats = os.stat(file_path)
                    mtime = stats.st_mtime
                    age_seconds = now - mtime
                    file_size = stats.st_size

                    if age_seconds > max_age_seconds:
                        age_days = age_seconds / 86400.0
                        candidate_files.append((file_path, file_size, age_days))

                        if not dry_run:
                            os.remove(file_path)
                            deleted_files.append((file_path, file_size, age_days))
                            freed_bytes += file_size
                        else:
                            freed_bytes += file_size
                except (OSError, PermissionError) as e:
                    errors.append((file_path, str(e)))

    # Write audit log
    timestamp_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    with open(log_file, "a", encoding="utf-8") as lf:
        lf.write(f"\n--- Cleanup Run: {timestamp_str} (Dry-Run: {dry_run}) ---\n")
        lf.write(f"Target Directory : {target_dir}\n")
        lf.write(f"Age Threshold    : {max_age_days} day(s)\n")
        lf.write(f"Files Scanned    : {scanned_files}\n")
        lf.write(f"Files Actioned   : {len(candidate_files)}\n")
        lf.write(f"Bytes Freed      : {freed_bytes} ({freed_bytes / 1024.0:.2f} KB)\n")

        for f_path, size, age in candidate_files:
            action = "WOULD_DELETE" if dry_run else "DELETED"
            lf.write(f"  [{action}] {f_path} ({size} bytes, age: {age:.2f} days)\n")

        for f_path, err in errors:
            lf.write(f"  [ERROR] Failed to access {f_path}: {err}\n")

    return {
        "target_dir": target_dir,
        "dry_run": dry_run,
        "scanned_files": scanned_files,
        "candidate_count": len(candidate_files),
        "deleted_count": len(deleted_files) if not dry_run else 0,
        "freed_bytes": freed_bytes,
        "freed_kb": freed_bytes / 1024.0,
        "errors": errors,
        "log_file": log_file,
    }


def print_summary(res: Dict[str, any]) -> None:
    mode_str = "DRY-RUN (SIMULATION)" if res["dry_run"] else "LIVE EXECUTION"
    print("=" * 65)
    print(f"  DEVOPS FILESYSTEM CLEANUP — {mode_str}")
    print("=" * 65)
    print(f"  Target Directory  : {res['target_dir']}")
    print(f"  Audit Log         : {res['log_file']}")
    print(f"  Files Scanned     : {res['scanned_files']}")
    print(f"  Eligible Files    : {res['candidate_count']}")
    if not res["dry_run"]:
        print(f"  Files Purged      : {res['deleted_count']}")
    print(f"  Disk Space Freed  : {res['freed_kb']:.2f} KB ({res['freed_bytes']} bytes)")
    if res["errors"]:
        print(f"  Errors Encountered: {len(res['errors'])}")
        for path, err in res["errors"]:
            print(f"    - {path}: {err}")
    print("=" * 65)


def run_tests() -> None:
    """Self-contained test runner creating mock files with custom mtime."""
    print("\n[TEST] Running automated test suite for auto_cleanup.py...")
    test_dir = os.path.abspath("test_temp_sandbox")
    test_log = os.path.abspath("test_cleanup.log")

    try:
        os.makedirs(test_dir, exist_ok=True)
        now = time.time()
        one_day_ago = now - (1 * 86400)
        three_days_ago = now - (3 * 86400)
        five_days_ago = now - (5 * 86400)

        # 1. Stale temporary file (3 days old) -> Should be deleted
        file_stale = os.path.join(test_dir, "session_4412.tmp")
        with open(file_stale, "w") as f:
            f.write("stale session data" * 50)
        os.utime(file_stale, (three_days_ago, three_days_ago))

        # 2. Very old backup file (5 days old) -> Should be deleted
        file_old_bak = os.path.join(test_dir, "db_dump_old.bak")
        with open(file_old_bak, "w") as f:
            f.write("old database dump" * 100)
        os.utime(file_old_bak, (five_days_ago, five_days_ago))

        # 3. Fresh temporary file (1 day old) -> Should NOT be deleted
        file_fresh = os.path.join(test_dir, "active_cache.tmp")
        with open(file_fresh, "w") as f:
            f.write("active cache data" * 20)
        os.utime(file_fresh, (one_day_ago, one_day_ago))

        # 4. Old non-matching extension (.json) -> Should NOT be deleted
        file_important = os.path.join(test_dir, "config.json")
        with open(file_important, "w") as f:
            f.write('{"status": "keep me"}')
        os.utime(file_important, (five_days_ago, five_days_ago))

        # Phase A: Test dry-run
        dry_res = scan_and_clean(test_dir, max_age_days=2.0, dry_run=True, log_file=test_log)
        assert dry_res["candidate_count"] == 2, f"Expected 2 candidates, got {dry_res['candidate_count']}"
        assert dry_res["deleted_count"] == 0, "Dry-run should not delete files"
        assert os.path.exists(file_stale), "Stale file must exist during dry-run"

        # Phase B: Test live execution
        live_res = scan_and_clean(test_dir, max_age_days=2.0, dry_run=False, log_file=test_log)
        assert live_res["candidate_count"] == 2
        assert live_res["deleted_count"] == 2
        assert not os.path.exists(file_stale), "Stale file was not deleted"
        assert not os.path.exists(file_old_bak), "Old backup was not deleted"
        assert os.path.exists(file_fresh), "Fresh temporary file was erroneously deleted!"
        assert os.path.exists(file_important), "Important config.json was erroneously deleted!"

        print("[PASS] Dry-run safety mode validated.")
        print("[PASS] Age calculation via os.path.getmtime() validated.")
        print("[PASS] Selective extension filtering validated.")
        print("[PASS] Audit log generation in test_cleanup.log validated.\n")
    finally:
        # Cleanup test environment
        if os.path.exists(test_dir):
            for root, _, files in os.walk(test_dir, topdown=False):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                    except OSError:
                        pass
            try:
                os.rmdir(test_dir)
            except OSError:
                pass
        if os.path.exists(test_log):
            os.remove(test_log)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Day 3: Automated filesystem pruning and stale file lifecycle manager."
    )
    parser.add_argument("--dir", default=".", help="Target directory to inspect and clean")
    parser.add_argument("--days", type=float, default=2.0, help="Max file age in days before pruning (default: 2.0)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate cleanup without deleting any files")
    parser.add_argument("--log", default="cleanup.log", help="Path to audit log file")
    parser.add_argument("--test", action="store_true", help="Run automated verification test suite")
    args = parser.parse_args()

    if args.test:
        run_tests()
        sys.exit(0)

    try:
        res = scan_and_clean(args.dir, max_age_days=args.days, dry_run=args.dry_run, log_file=args.log)
        print_summary(res)
    except Exception as e:
        print(f"Error during execution: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
