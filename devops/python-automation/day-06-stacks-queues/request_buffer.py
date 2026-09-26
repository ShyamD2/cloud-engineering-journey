"""
Day 6: Basic DSA — Queues in DevOps Request Processing
Script: request_buffer.py
DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D

Functionality:
- Simulates an API ingress request buffer and worker thread dispatch using FIFO Queue
- Uses collections.deque for true O(1) append (enqueue) and popleft (dequeue) operations
- Enforces a fixed-capacity 3-request buffer with backpressure overflow handling
- Includes automated test runner verifying queue order and buffer boundaries
"""

from __future__ import annotations
from collections import deque
import time
from typing import Dict, List, Optional


class RequestBufferQueue:
    """
    Fixed-capacity FIFO buffer for cloud API rate-limiting and job queuing.
    Demonstrates collections.deque O(1) performance.
    """

    def __init__(self, capacity: int = 3, overflow_policy: str = "reject"):
        """
        overflow_policy:
          - 'reject': Returns False if buffer is full (HTTP 429 Too Many Requests / 503)
          - 'drop_oldest': Drops oldest waiting item to accept new (telemetry queue style)
        """
        self.capacity = capacity
        self.policy = overflow_policy
        self._buffer: deque = deque()
        self.total_received = 0
        self.total_processed = 0
        self.total_rejected = 0

    def enqueue(self, request_id: str, payload: dict) -> Tuple[bool, str]:
        """Adds a request to the tail of the FIFO queue."""
        self.total_received += 1
        item = {
            "id": request_id,
            "payload": payload,
            "enqueued_at": time.time(),
        }

        if len(self._buffer) >= self.capacity:
            if self.policy == "reject":
                self.total_rejected += 1
                return False, f"REJECTED: Buffer capacity ({self.capacity}) reached. Apply backpressure."
            elif self.policy == "drop_oldest":
                dropped = self._buffer.popleft()
                self._buffer.append(item)
                return True, f"ACCEPTED: Dropped oldest item '{dropped['id']}' to accommodate '{request_id}'."

        self._buffer.append(item)
        return True, f"ACCEPTED: '{request_id}' enqueued at position {len(self._buffer)}."

    def dequeue(self) -> Optional[dict]:
        """Processes the next request from the head of the FIFO queue."""
        if not self._buffer:
            return None
        item = self._buffer.popleft()
        self.total_processed += 1
        return item

    def size(self) -> int:
        return len(self._buffer)

    def is_empty(self) -> bool:
        return len(self._buffer) == 0


def run_tests() -> None:
    print("\n[TEST] Running automated test suite for request_buffer.py...")

    # 1. Test FIFO order
    q = RequestBufferQueue(capacity=3, overflow_policy="reject")
    assert q.is_empty()

    ok1, msg1 = q.enqueue("REQ-1", {"action": "scale_up"})
    ok2, msg2 = q.enqueue("REQ-2", {"action": "db_backup"})
    ok3, msg3 = q.enqueue("REQ-3", {"action": "health_check"})

    assert ok1 and ok2 and ok3
    assert q.size() == 3

    # 2. Test rejection policy on 4th request
    ok4, msg4 = q.enqueue("REQ-4", {"action": "restart_pod"})
    assert not ok4, "4th request should have been rejected by 3-request buffer"
    assert "REJECTED" in msg4
    assert q.total_rejected == 1

    # 3. Test FIFO popleft order: REQ-1 first, then REQ-2, then REQ-3
    item1 = q.dequeue()
    assert item1["id"] == "REQ-1"
    item2 = q.dequeue()
    assert item2["id"] == "REQ-2"
    item3 = q.dequeue()
    assert item3["id"] == "REQ-3"
    assert q.dequeue() is None  # Now empty

    # 4. Test drop_oldest policy
    q_drop = RequestBufferQueue(capacity=2, overflow_policy="drop_oldest")
    q_drop.enqueue("REQ-A", {})
    q_drop.enqueue("REQ-B", {})
    q_drop.enqueue("REQ-C", {})  # Should drop REQ-A

    assert q_drop.size() == 2
    first = q_drop.dequeue()
    assert first["id"] == "REQ-B", f"Expected REQ-B after REQ-A dropped, got {first['id']}"

    print("[PASS] FIFO dispatch order verified.")
    print("[PASS] Fixed-capacity 3-request buffer enforcement validated.")
    print("[PASS] Rejection backpressure and drop policies verified.\n")


def main() -> None:
    run_tests()
    print("=" * 65)
    print("  SIMULATION: 3-REQUEST WORKER INGRESS BUFFER (FIFO QUEUE)")
    print("=" * 65)
    queue = RequestBufferQueue(capacity=3, overflow_policy="reject")

    requests = [
        ("req_101", {"endpoint": "/api/checkout", "user": "alice"}),
        ("req_102", {"endpoint": "/api/inventory", "user": "bob"}),
        ("req_103", {"endpoint": "/api/metrics", "user": "prometheus"}),
        ("req_104", {"endpoint": "/api/report", "user": "charlie"}),  # Will be rejected
    ]

    for req_id, payload in requests:
        ok, msg = queue.enqueue(req_id, payload)
        status = "[ENQUEUED]" if ok else "[DROPPED] "
        print(f"  {status} {msg}")

    print("-" * 65)
    print("  Worker Consumer Dispatching Requests in FIFO Order:")
    while not queue.is_empty():
        req = queue.dequeue()
        print(f"    - Processing {req['id']} ({req['payload']['endpoint']})")
    print("=" * 65)


if __name__ == "__main__":
    main()
