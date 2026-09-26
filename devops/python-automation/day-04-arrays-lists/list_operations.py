"""
Day 4: Basic DSA — Arrays & Lists in DevOps Automation
Script: list_operations.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Demonstrates list operations in infrastructure management: indexing O(1), appending O(1), slicing
- Filters private vs public IP addresses from raw infrastructure inventories
- Implements order-preserving deduplication for security group whitelist rules
- Includes automated test runner verifying list operations and edge cases
"""

from __future__ import annotations
import ipaddress
import time
from typing import List, Tuple


def manage_server_inventory() -> List[str]:
    """Demonstrates standard list manipulation: append, insert, remove, sort."""
    servers: List[str] = ["web-prod-01", "api-prod-01", "db-primary"]

    # O(1) Amortized Append
    servers.append("cache-redis-01")

    # O(N) Insert at specific index
    servers.insert(1, "web-prod-02")

    # O(N) Remove element
    if "db-primary" in servers:
        servers.remove("db-primary")

    # In-place sorting O(N log N)
    servers.sort()
    return servers


def filter_ip_addresses(raw_ips: List[str]) -> Tuple[List[str], List[str], List[str]]:
    """
    Parses and categorizes IP addresses from an infrastructure audit list.
    Returns: (private_ips, public_ips, invalid_ips) with duplicates eliminated while preserving order.
    """
    seen = set()
    private_ips: List[str] = []
    public_ips: List[str] = []
    invalid_ips: List[str] = []

    for raw in raw_ips:
        cleaned = raw.strip()
        if not cleaned:
            continue
        if cleaned in seen:
            continue
        seen.add(cleaned)

        try:
            ip_obj = ipaddress.ip_address(cleaned)
            if ip_obj.is_private:
                private_ips.append(cleaned)
            else:
                public_ips.append(cleaned)
        except ValueError:
            invalid_ips.append(cleaned)

    return private_ips, public_ips, invalid_ips


def paginate_logs(log_entries: List[str], page: int = 1, page_size: int = 5) -> List[str]:
    """
    Demonstrates list slicing [start:stop:step] for terminal log pagination.
    """
    if page < 1:
        page = 1
    start_idx = (page - 1) * page_size
    stop_idx = start_idx + page_size
    return log_entries[start_idx:stop_idx]


def benchmark_lookup() -> None:
    """Demonstrates O(1) direct index lookup vs O(N) linear search on 100,000 items."""
    large_list = [f"node-{i}.internal" for i in range(100_000)]
    target = "node-99999.internal"

    # Index lookup O(1)
    t0 = time.perf_counter()
    _ = large_list[99999]
    t_index = (time.perf_counter() - t0) * 1_000_000

    # Linear search O(N)
    t0 = time.perf_counter()
    _ = target in large_list
    t_search = (time.perf_counter() - t0) * 1_000_000

    print(f"  Benchmark (100,000 items):")
    print(f"    - Direct Index Lookup list[i]  : {t_index:.3f} microseconds (O(1))")
    print(f"    - Linear Membership 'x in list': {t_search:.3f} microseconds (O(N))")


def run_tests() -> None:
    """Automated unit verification for list algorithms."""
    print("\n[TEST] Running automated test suite for list_operations.py...")

    # 1. Server inventory check
    inv = manage_server_inventory()
    assert "web-prod-01" in inv
    assert "web-prod-02" in inv
    assert "cache-redis-01" in inv
    assert "db-primary" not in inv
    assert inv == sorted(inv)
    print("[PASS] Server inventory manipulation & sorting verified.")

    # 2. IP filter check
    test_ips = [
        "192.168.1.1",
        "10.0.4.15",
        "8.8.8.8",
        "192.168.1.1",  # duplicate
        "172.16.0.50",
        "1.1.1.1",
        "999.999.999.999",  # invalid
        "not_an_ip",  # invalid
    ]
    priv, pub, inv_list = filter_ip_addresses(test_ips)
    assert priv == ["192.168.1.1", "10.0.4.15", "172.16.0.50"], f"Unexpected private IPs: {priv}"
    assert pub == ["8.8.8.8", "1.1.1.1"], f"Unexpected public IPs: {pub}"
    assert len(inv_list) == 2
    print("[PASS] IP address classification and deduplication verified.")

    # 3. Log pagination slicing check
    sample_logs = [f"Log entry #{i}" for i in range(12)]
    page1 = paginate_logs(sample_logs, page=1, page_size=5)
    page2 = paginate_logs(sample_logs, page=2, page_size=5)
    page3 = paginate_logs(sample_logs, page=3, page_size=5)
    assert len(page1) == 5 and page1[0] == "Log entry #0"
    assert len(page2) == 5 and page2[0] == "Log entry #5"
    assert len(page3) == 2 and page3[0] == "Log entry #10"
    print("[PASS] List slicing and log pagination verified.\n")


def main() -> None:
    run_tests()
    print("=" * 65)
    print("  DEVOPS LIST & ARRAY MANIPULATION DEMO")
    print("=" * 65)
    inv = manage_server_inventory()
    print(f"  Active Server Fleet   : {inv}")

    sample_ips = ["192.168.1.100", "10.0.1.5", "54.210.12.89", "8.8.4.4", "192.168.1.100", "bad-ip"]
    priv, pub, bad = filter_ip_addresses(sample_ips)
    print(f"  Private Subnet Nodes  : {priv}")
    print(f"  Public Internet Hosts : {pub}")
    print(f"  Malformed Addresses   : {bad}")
    print("-" * 65)
    benchmark_lookup()
    print("=" * 65)


if __name__ == "__main__":
    main()
