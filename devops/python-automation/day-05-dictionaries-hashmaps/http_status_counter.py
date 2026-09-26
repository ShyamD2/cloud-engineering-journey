"""
Day 5: Basic DSA — Dictionaries & HashMaps in DevOps Observability
Script: http_status_counter.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Computes frequency distribution of HTTP status codes using hash tables (dict) in O(N) time
- Aggregates status codes into standard HTTP categories (2xx, 3xx, 4xx, 5xx)
- Calculates service error rate percentage and alerts if thresholds are breached
- Demonstrates O(1) dictionary key lookups vs O(N) list searches
- Includes automated test suite verifying edge cases and empty streams
"""

from __future__ import annotations
from typing import Dict, List, Tuple


def count_http_status_codes(codes: List[int]) -> Dict[int, int]:
    """
    Counts frequency of each HTTP status code using an O(1) lookup dictionary.
    """
    counts: Dict[int, int] = {}
    for code in codes:
        counts[code] = counts.get(code, 0) + 1
    return counts


def analyze_http_traffic(codes: List[int]) -> Dict[str, any]:
    """
    Categorizes status codes into families and computes error rates.
    """
    total = len(codes)
    freq = count_http_status_codes(codes)

    categories: Dict[str, int] = {
        "2xx_Success": 0,
        "3xx_Redirect": 0,
        "4xx_ClientError": 0,
        "5xx_ServerError": 0,
        "Other": 0,
    }

    for code, count in freq.items():
        if 200 <= code <= 299:
            categories["2xx_Success"] += count
        elif 300 <= code <= 399:
            categories["3xx_Redirect"] += count
        elif 400 <= code <= 499:
            categories["4xx_ClientError"] += count
        elif 500 <= code <= 599:
            categories["5xx_ServerError"] += count
        else:
            categories["Other"] += count

    client_errors = categories["4xx_ClientError"]
    server_errors = categories["5xx_ServerError"]
    error_rate = ((client_errors + server_errors) / total * 100.0) if total > 0 else 0.0

    return {
        "total_requests": total,
        "frequencies": freq,
        "categories": categories,
        "error_rate_pct": error_rate,
        "healthy": error_rate < 5.0,  # Alert threshold: 5% error rate
    }


def print_dashboard(metrics: Dict[str, any]) -> None:
    print("=" * 65)
    print("  HTTP TRAFFIC & API HEALTH METRICS (HASHMAP ANALYTICS)")
    print("=" * 65)
    print(f"  Total Ingested Requests : {metrics['total_requests']}")
    print(f"  Overall Error Rate      : {metrics['error_rate_pct']:.2f}%")
    status_label = "HEALTHY" if metrics["healthy"] else "DEGRADED / ALERT"
    print(f"  Service SLO Status      : {status_label}")
    print("-" * 65)
    print("  Status Code Frequencies:")
    for code, count in sorted(metrics["frequencies"].items()):
        pct = (count / metrics["total_requests"]) * 100.0
        print(f"    - HTTP {code:<5}: {count:<6} requests ({pct:5.1f}%)")
    print("-" * 65)
    print("  Category Distribution:")
    for cat, count in metrics["categories"].items():
        print(f"    - {cat:<18}: {count} request(s)")
    print("=" * 65)


def run_tests() -> None:
    print("\n[TEST] Running automated test suite for http_status_counter.py...")

    sample_codes = [200, 404, 200, 500, 200, 301, 502, 404, 200, 200, 204]
    metrics = analyze_http_traffic(sample_codes)

    assert metrics["total_requests"] == 11
    assert metrics["frequencies"][200] == 5
    assert metrics["frequencies"][404] == 2
    assert metrics["frequencies"][500] == 1
    assert metrics["frequencies"][502] == 1
    assert metrics["categories"]["2xx_Success"] == 6
    assert metrics["categories"]["4xx_ClientError"] == 2
    assert metrics["categories"]["5xx_ServerError"] == 2

    # Error rate = 4/11 = 36.36% -> Degraded
    assert not metrics["healthy"]
    assert abs(metrics["error_rate_pct"] - 36.36) < 0.1

    # Empty list check
    empty_res = analyze_http_traffic([])
    assert empty_res["total_requests"] == 0
    assert empty_res["error_rate_pct"] == 0.0

    print("[PASS] HTTP frequency aggregation verified.")
    print("[PASS] Category distribution and SLO calculations validated.")
    print("[PASS] Zero-traffic edge case handled gracefully.\n")


def main() -> None:
    run_tests()
    live_traffic = [
        200, 200, 200, 200, 200, 200, 201, 204,
        301, 302,
        400, 401, 403, 404, 404,
        500, 502, 503
    ]
    metrics = analyze_http_traffic(live_traffic)
    print_dashboard(metrics)


if __name__ == "__main__":
    main()
