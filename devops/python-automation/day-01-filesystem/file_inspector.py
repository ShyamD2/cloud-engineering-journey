"""
Day 1: Python Basics & Filesystem Automation
Script: file_inspector.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Prompts user for a target directory (or accepts command-line argument)
- Scans directory using os.listdir()
- Inspects each file using os.path.getsize() and converts bytes to KB
- Formats and displays a clean tabular summary of files and total disk usage
- Handles invalid directories and permission errors gracefully
"""

from __future__ import annotations
import os
import sys


def inspect_directory(target_path: str) -> dict:
    """
    Inspects files in the given directory and returns metadata and size breakdown.
    """
    if not os.path.exists(target_path):
        raise FileNotFoundError(f"Directory not found: '{target_path}'")
    if not os.path.isdir(target_path):
        raise NotADirectoryError(f"Path is not a directory: '{target_path}'")

    entries = []
    total_bytes = 0

    try:
        filenames = os.listdir(target_path)
    except PermissionError as e:
        raise PermissionError(f"Permission denied accessing '{target_path}': {e}")

    for name in sorted(filenames):
        full_path = os.path.join(target_path, name)
        is_file = os.path.isfile(full_path)
        is_dir = os.path.isdir(full_path)

        if is_file:
            try:
                size_bytes = os.path.getsize(full_path)
            except (OSError, PermissionError):
                size_bytes = 0
            size_kb = size_bytes / 1024.0
            total_bytes += size_bytes
            entries.append({
                "name": name,
                "type": "FILE",
                "size_bytes": size_bytes,
                "size_kb": size_kb
            })
        elif is_dir:
            entries.append({
                "name": name,
                "type": "DIR",
                "size_bytes": 0,
                "size_kb": 0.0
            })

    return {
        "target_path": os.path.abspath(target_path),
        "total_items": len(entries),
        "files_count": sum(1 for e in entries if e["type"] == "FILE"),
        "dirs_count": sum(1 for e in entries if e["type"] == "DIR"),
        "total_size_bytes": total_bytes,
        "total_size_kb": total_bytes / 1024.0,
        "entries": entries
    }


def print_inspection_report(report: dict):
    """Prints a structured, human-readable terminal report."""
    target = report["target_path"]
    entries = report["entries"]

    print("=" * 75)
    print(f"  FILE INSPECTOR REPORT: {target}")
    print("=" * 75)
    print(f"{'TYPE':<6} | {'SIZE (KB)':>12} | {'NAME'}")
    print("-" * 75)

    for item in entries:
        if item["type"] == "FILE":
            size_str = f"{item['size_kb']:>10.2f} KB"
        else:
            size_str = f"{'<DIR>':>12}"
        print(f"{item['type']:<6} | {size_str} | {item['name']}")

    print("-" * 75)
    print(f"Summary: {report['files_count']} files, {report['dirs_count']} subdirectories")
    print(f"Total Disk Usage: {report['total_size_kb']:.2f} KB ({report['total_size_bytes']:,} bytes)")
    print("=" * 75)


def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter directory path to inspect (press Enter for current folder '.'): ").strip()
        if not folder:
            folder = "."

    try:
        report = inspect_directory(folder)
        print_inspection_report(report)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
