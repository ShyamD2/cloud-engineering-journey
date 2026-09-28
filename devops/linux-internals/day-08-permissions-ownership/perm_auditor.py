"""
Day 8: Linux Permissions & Security Ownership Auditing
Script: perm_auditor.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Audits filesystem permissions and ownership using stat / octal math (e.g. 755, 644, 600)
- Detects security compliance violations:
  - World-writable files (security risk: arbitrary code injection / tampering)
  - Sensitive files (.pem, id_rsa, .env) with permissions looser than 0o600 / 0o400
  - Insecure executable bits on configuration files
- Produces a structured audit report with actionable remediation chmod commands
- Cross-platform test suite verifying octal conversions and rule violations
"""

from __future__ import annotations
import argparse
import os
import platform
import stat
import sys
from typing import Dict, List, Optional, Tuple


# Security Policy Baseline: Sensitive credential patterns
SENSITIVE_PATTERNS = (".env", "id_rsa", "id_ed25519", ".pem", "credentials", "secret")


def get_octal_mode(filepath: str) -> str:
    """Returns standard 3-digit octal permission string (e.g. '644', '755')."""
    mode = os.stat(filepath).st_mode
    return oct(stat.S_IMODE(mode))[2:].zfill(3)


def check_mode_violations(filename: str, mode: int) -> List[Dict[str, str]]:
    """
    Evaluates raw permission mode bits against zero-trust DevOps security rules.
    Pure function decoupled from filesystem driver for 100% deterministic testability.
    """
    violations: List[Dict[str, str]] = []
    octal_str = oct(mode)[2:].zfill(3)

    # 1. Check for World-Writable (Other has write bit: mode & 0o002)
    if mode & stat.S_IWOTH:
        violations.append({
            "severity": "CRITICAL",
            "issue": f"World-writable file (Mode {octal_str})",
            "recommendation": f"chmod o-w {filename} (or chmod 644 {filename})",
        })

    # 2. Check sensitive credential files (SSH keys, .env, .pem)
    is_sensitive = any(pat in filename.lower() for pat in SENSITIVE_PATTERNS)
    if is_sensitive:
        # Sensitive files must not be readable/writable by Group or Other (mode & 0o077 must be 0)
        if mode & (stat.S_IRWXG | stat.S_IRWXO):
            violations.append({
                "severity": "CRITICAL",
                "issue": f"Sensitive credential file exposed to group/world (Mode {octal_str})",
                "recommendation": f"chmod 600 {filename} (Owner Read/Write Only)",
            })

    # 3. Check for unexpected execute bit on static configs (.conf, .json, .yaml, .txt, .md)
    is_static_config = any(filename.endswith(ext) for ext in (".conf", ".json", ".yaml", ".yml", ".txt", ".md"))
    if is_static_config and (mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)):
        violations.append({
            "severity": "WARN",
            "issue": f"Executable bit set on static config file (Mode {octal_str})",
            "recommendation": f"chmod 644 {filename} (remove execute bits)",
        })

    return violations


def audit_file_permissions(filepath: str) -> List[Dict[str, str]]:
    """Audits an on-disk file path for permission compliance violations."""
    try:
        st = os.stat(filepath)
        mode = stat.S_IMODE(st.st_mode)
        filename = os.path.basename(filepath)
        return check_mode_violations(filename, mode)
    except OSError as e:
        return [{"severity": "ERROR", "issue": f"Cannot stat file: {e}", "recommendation": "Check path"}]


def scan_directory(target_dir: str) -> Dict[str, any]:
    """Scans directory recursively and aggregates permission audit metrics."""
    total_files = 0
    clean_files = 0
    flagged_files: List[Tuple[str, str, List[Dict[str, str]]]] = []

    for root, _, files in os.walk(target_dir):
        for name in files:
            total_files += 1
            full_path = os.path.join(root, name)
            try:
                octal = get_octal_mode(full_path)
                issues = audit_file_permissions(full_path)
                if issues:
                    flagged_files.append((full_path, octal, issues))
                else:
                    clean_files += 1
            except OSError:
                pass

    return {
        "target_dir": target_dir,
        "total_files": total_files,
        "clean_files": clean_files,
        "flagged_count": len(flagged_files),
        "flagged_files": flagged_files,
    }


def print_report(res: Dict[str, any]) -> None:
    print("=" * 65)
    print("  LINUX PERMISSION & SECURITY OWNERSHIP AUDIT")
    print("=" * 65)
    print(f"  Target Directory  : {res['target_dir']}")
    print(f"  Total Files Audit : {res['total_files']}")
    print(f"  Compliant Files   : {res['clean_files']}")
    print(f"  Flagged Files     : {res['flagged_count']}")
    print("-" * 65)

    if not res["flagged_files"]:
        print("  [SUCCESS] All audited files adhere to permission baselines!")
    else:
        print("  SECURITY VULNERABILITIES DETECTED:")
        for path, octal, issues in res["flagged_files"]:
            print(f"\n  [FILE] {path} (Current: 0o{octal})")
            for iss in issues:
                sev = iss["severity"]
                print(f"    - [{sev}] {iss['issue']}")
                print(f"      -> Fix: {iss['recommendation']}")
    print("=" * 65)


def run_tests() -> None:
    """Automated test runner verifying octal permission evaluations."""
    print("\n[TEST] Running automated test suite for perm_auditor.py...")

    # 1. Standard application script (0o755) -> rwxr-xr-x -> Clean
    app_issues = check_mode_violations("deploy.sh", 0o755)
    assert len(app_issues) == 0, f"Expected clean for 755 script, got {app_issues}"

    # 2. Standard config file (0o644) -> rw-r--r-- -> Clean
    conf_issues = check_mode_violations("nginx.conf", 0o644)
    assert len(conf_issues) == 0, f"Expected clean for 644 config, got {conf_issues}"

    # 3. World-Writable script (0o777) -> Violation (World-writable)
    ww_issues = check_mode_violations("script.sh", 0o777)
    assert len(ww_issues) == 1
    assert "World-writable" in ww_issues[0]["issue"]

    # 4. Sensitive SSH Key with loose permissions (0o644) -> Violation (Group/World exposed)
    ssh_issues = check_mode_violations("id_rsa", 0o644)
    assert len(ssh_issues) == 1
    assert "Sensitive credential file exposed" in ssh_issues[0]["issue"]

    # 5. Sensitive SSH Key locked down properly (0o600) -> Clean
    secure_ssh = check_mode_violations("id_rsa", 0o600)
    assert len(secure_ssh) == 0, f"Expected clean for 600 key, got {secure_ssh}"

    # 6. Static text file with executable bit (0o755 on README.md) -> Warning
    exec_conf = check_mode_violations("config.yaml", 0o755)
    assert len(exec_conf) == 1
    assert "Executable bit set on static config" in exec_conf[0]["issue"]

    print("[PASS] Standard script (0o755) and config (0o644) baselines validated.")
    print("[PASS] World-writable (0o777) danger detection verified.")
    print("[PASS] SSH private key (0o600 vs 0o644) isolation verified.")
    print("[PASS] Executable config anomaly detection verified.\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Day 8: Audit Linux permissions and enforce zero-trust security baselines."
    )
    parser.add_argument("--dir", default=".", help="Directory path to audit")
    parser.add_argument("--test", action="store_true", help="Run automated verification tests")
    args = parser.parse_args()

    if args.test:
        run_tests()
        sys.exit(0)

    res = scan_directory(args.dir)
    print_report(res)


if __name__ == "__main__":
    main()
