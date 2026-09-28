"""
Day 7: Linux Filesystem Hierarchy & OS Diagnostics
Script: inspect_proc.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Deep-dives into the virtual /proc filesystem on Linux systems
- Parses /proc/cpuinfo: extracts model name, physical core count, and CPU flags
- Parses /proc/meminfo: computes total, free, and available memory in MB
- Parses /proc/loadavg: calculates 1-min, 5-min, and 15-min load averages
- Cross-platform fallback: simulates virtual /proc parser with built-in test suite
- Generates a clean tabular system telemetry report
"""

from __future__ import annotations
import argparse
import os
import platform
import sys
from typing import Dict, Optional


def parse_meminfo(proc_path: str = "/proc/meminfo") -> Dict[str, float]:
    """
    Parses /proc/meminfo key-value pairs (in kB) and converts to megabytes (MB).
    """
    if not os.path.exists(proc_path):
        raise FileNotFoundError(f"Virtual filesystem entry '{proc_path}' not found")

    mem_data: Dict[str, float] = {}
    with open(proc_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) == 2:
                key = parts[0].strip()
                val_str = parts[1].strip().split()[0]
                try:
                    # Values in /proc/meminfo are typically in kB
                    val_kb = float(val_str)
                    mem_data[key] = val_kb / 1024.0  # Convert to MB
                except ValueError:
                    pass

    total_mb = mem_data.get("MemTotal", 0.0)
    avail_mb = mem_data.get("MemAvailable", mem_data.get("MemFree", 0.0))
    used_mb = max(0.0, total_mb - avail_mb)
    usage_pct = (used_mb / total_mb * 100.0) if total_mb > 0 else 0.0

    return {
        "total_mb": total_mb,
        "available_mb": avail_mb,
        "used_mb": used_mb,
        "usage_pct": usage_pct,
    }


def parse_cpuinfo(proc_path: str = "/proc/cpuinfo") -> Dict[str, any]:
    """
    Parses /proc/cpuinfo to extract processor model and core topology.
    """
    if not os.path.exists(proc_path):
        raise FileNotFoundError(f"Virtual filesystem entry '{proc_path}' not found")

    cores = 0
    model_name = "Unknown"
    cache_size = "Unknown"

    with open(proc_path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, val = [p.strip() for p in line.split(":", 1)]
                if key == "processor":
                    cores += 1
                elif key == "model name" and model_name == "Unknown":
                    model_name = val
                elif key == "cache size" and cache_size == "Unknown":
                    cache_size = val

    return {
        "model_name": model_name,
        "core_count": max(1, cores),
        "cache_size": cache_size,
    }


def parse_loadavg(proc_path: str = "/proc/loadavg") -> Dict[str, float]:
    """
    Parses /proc/loadavg for 1, 5, and 15 minute system load averages.
    """
    if not os.path.exists(proc_path):
        raise FileNotFoundError(f"Virtual filesystem entry '{proc_path}' not found")

    with open(proc_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        parts = content.split()
        if len(parts) >= 3:
            return {
                "load_1m": float(parts[0]),
                "load_5m": float(parts[1]),
                "load_15m": float(parts[2]),
            }

    return {"load_1m": 0.0, "load_5m": 0.0, "load_15m": 0.0}


def run_tests() -> None:
    """Automated unit verification using a simulated /proc sandbox."""
    print("\n[TEST] Running automated test suite for inspect_proc.py...")
    test_dir = os.path.abspath("test_mock_proc")

    try:
        os.makedirs(test_dir, exist_ok=True)
        mock_mem = os.path.join(test_dir, "meminfo")
        mock_cpu = os.path.join(test_dir, "cpuinfo")
        mock_load = os.path.join(test_dir, "loadavg")

        # Mock /proc/meminfo
        with open(mock_mem, "w") as f:
            f.write(
                "MemTotal:       16384000 kB\n"
                "MemFree:         4096000 kB\n"
                "MemAvailable:    8192000 kB\n"
                "Buffers:          512000 kB\n"
                "Cached:          4096000 kB\n"
            )

        # Mock /proc/cpuinfo
        with open(mock_cpu, "w") as f:
            f.write(
                "processor       : 0\n"
                "model name      : AMD EPYC 7763 64-Core Processor\n"
                "cache size      : 512 KB\n\n"
                "processor       : 1\n"
                "model name      : AMD EPYC 7763 64-Core Processor\n"
                "cache size      : 512 KB\n"
            )

        # Mock /proc/loadavg
        with open(mock_load, "w") as f:
            f.write("0.45 0.52 0.38 1/450 12890\n")

        # Test meminfo parsing
        mem = parse_meminfo(mock_mem)
        assert abs(mem["total_mb"] - 16000.0) < 1.0, f"Expected 16000 MB, got {mem['total_mb']}"
        assert abs(mem["available_mb"] - 8000.0) < 1.0
        assert abs(mem["used_mb"] - 8000.0) < 1.0
        assert abs(mem["usage_pct"] - 50.0) < 0.1

        # Test cpuinfo parsing
        cpu = parse_cpuinfo(mock_cpu)
        assert cpu["core_count"] == 2
        assert "AMD EPYC" in cpu["model_name"]

        # Test loadavg parsing
        load = parse_loadavg(mock_load)
        assert load["load_1m"] == 0.45
        assert load["load_5m"] == 0.52
        assert load["load_15m"] == 0.38

        print("[PASS] Virtual /proc/meminfo parsing validated.")
        print("[PASS] Virtual /proc/cpuinfo topology parsing validated.")
        print("[PASS] Virtual /proc/loadavg extraction validated.\n")
    finally:
        for f_name in ("meminfo", "cpuinfo", "loadavg"):
            p = os.path.join(test_dir, f_name)
            if os.path.exists(p):
                os.remove(p)
        if os.path.exists(test_dir):
            try:
                os.rmdir(test_dir)
            except OSError:
                pass


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Day 7: Inspect Linux kernel parameters and hardware topology via /proc"
    )
    parser.add_argument("--test", action="store_true", help="Run automated self-tests with mock /proc")
    args = parser.parse_args()

    if args.test:
        run_tests()
        sys.exit(0)

    # Check if running on native Linux /proc
    is_linux = platform.system() == "Linux" and os.path.exists("/proc/meminfo")

    print("=" * 65)
    print("  LINUX KERNEL & HARDWARE TOPOLOGY INSPECTOR (/proc)")
    print("=" * 65)
    print(f"  Host Platform     : {platform.system()} ({platform.release()})")
    print(f"  Architecture      : {platform.machine()}")

    if is_linux:
        mem = parse_meminfo("/proc/meminfo")
        cpu = parse_cpuinfo("/proc/cpuinfo")
        load = parse_loadavg("/proc/loadavg")

        print("-" * 65)
        print("  CPU Topology:")
        print(f"    - Model Name    : {cpu['model_name']}")
        print(f"    - Logical Cores : {cpu['core_count']}")
        print(f"    - L2/L3 Cache   : {cpu['cache_size']}")
        print("-" * 65)
        print("  Memory Utilization:")
        print(f"    - Total RAM     : {mem['total_mb']:.1f} MB ({mem['total_mb'] / 1024.0:.2f} GB)")
        print(f"    - Available RAM : {mem['available_mb']:.1f} MB")
        print(f"    - Used RAM      : {mem['used_mb']:.1f} MB ({mem['usage_pct']:.1f}%)")
        print("-" * 65)
        print("  System Load Averages:")
        print(f"    - 1-min  Load   : {load['load_1m']:.2f}")
        print(f"    - 5-min  Load   : {load['load_5m']:.2f}")
        print(f"    - 15-min Load   : {load['load_15m']:.2f}")
    else:
        print("  [NOTE] Native /proc not detected (Running on Windows/macOS).")
        print("         Running self-test mode to verify parser against simulated /proc...")
        run_tests()
    print("=" * 65)


if __name__ == "__main__":
    main()
