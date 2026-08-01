# Networking Fundamentals for Cloud Engineers

Everything in the cloud sits on top of networking. Here are the core concepts I rely on when designing VPCs and debugging connectivity.

---

## 1. CIDR Cheat Sheet
* `/16` = 65,536 addresses (Standard VPC size)
* `/24` = 256 addresses (251 usable in AWS subnets)
* `/28` = 16 addresses (11 usable in AWS)
* `/32` = Exactly 1 single IP address

---

## 2. The TCP 3-Way Handshake
When your browser connects to a server:
1. Client sends `SYN` (Synchronize)
2. Server responds with `SYN-ACK` (Synchronize-Acknowledge)
3. Client replies with `ACK` (Acknowledge)
*Connection is now ESTABLISHED.*
If you send a `SYN` and hear nothing back, check security groups or firewall routing. If you get an immediate `RST` (Reset), the port is reachable but no service is listening on it.
