# DevOps & Cloud Engineer 36-Day Master Plan
> **Candidate:** Shyam Kumar D  
> **Target:** Job-Ready Cloud & DevOps Engineer (162 Hours Total / 4.5 Hours per Day)  
> **Rule:** Zero fluff. Hands-on practical automation, core data structures, Linux diagnostics, Docker, Kubernetes, CI/CD, AWS & Terraform.

---

## 📊 Progress Tracker

| Phase | Days | Focus Area | Status |
| :--- | :--- | :--- | :---: |
| **Phase 1** | Days 1–6 | Basic Python Scripting & Core Data Structures | **PHASE 1 COMPLETE (6/6 Days)** |
| **Phase 2A** | Days 7–11 | Linux Internals & OS Diagnostics | UP NEXT (Day 7) |
| **Phase 2B** | Days 12–14 | Computer Networks & Security | UPCOMING |
| **Phase 3** | Days 15–22 | Docker Containerization & Kubernetes Orchestration | UPCOMING |
| **Phase 4** | Days 23–26 | CI/CD Pipelines & Observability | UPCOMING |
| **Phase 5** | Days 27–33 | AWS Cloud Architecture & Terraform IaC | UPCOMING |
| **Phase 6** | Days 34–36 | High-Scale System Design & Job Applications | UPCOMING |

---

## 🗓️ Detailed Daily Breakdown

### Phase 1: Python Scripting & Core Data Structures (Days 1–6)
* [x] **Day 1: Python Basics & Filesystem Automation**
  - **Script**: [`file_inspector.py`](./python-automation/day-01-filesystem/file_inspector.py) — Directory scanning with `os.listdir()`, size calculation with `os.path.getsize()`, tabular KB formatting.
  - **Warmups**: [`hackerrank_warmups.py`](./python-automation/day-01-filesystem/hackerrank_warmups.py) — Conditionals, division, loops, functions.
  - **Docs**: [Day 1 Walkthrough & Notes](./python-automation/day-01-filesystem/README.md)
* [x] **Day 2: Finding Log Errors & File I/O**
  - **Script**: [`log_error_finder.py`](./python-automation/day-02-log-errors/log_error_finder.py) — Safe streaming line-by-line via `with open()`, regex subsystem tags.
  - **Output**: [`errors_only.txt`](./python-automation/day-02-log-errors/errors_only.txt) — Extracted 10 server incidents.
  - **Docs**: [Day 2 Walkthrough & Notes](./python-automation/day-02-log-errors/README.md)
* [x] **Day 3: Automated Job / Cron Script**
  - **Script**: [`auto_cleanup.py`](./python-automation/day-03-auto-cleanup/auto_cleanup.py) — Mtime-based file lifecycle pruner with `--dry-run` and audit logging.
  - **Docs**: [Day 3 Walkthrough & Notes](./python-automation/day-03-auto-cleanup/README.md)
* [x] **Day 4: Basic DSA — Arrays & Lists**
  - **Script**: [`list_operations.py`](./python-automation/day-04-arrays-lists/list_operations.py) — Fleet management, RFC1918 IP address classifier & log slicing.
  - **Warmup**: [`leetcode_1929_concatenation.py`](./python-automation/day-04-arrays-lists/leetcode_1929_concatenation.py) — LeetCode #1929 solution.
  - **Docs**: [Day 4 Walkthrough & Notes](./python-automation/day-04-arrays-lists/README.md)
* [x] **Day 5: Basic DSA — Dictionaries & HashMaps**
  - **Script**: [`http_status_counter.py`](./python-automation/day-05-dictionaries-hashmaps/http_status_counter.py) — O(1) HTTP status frequency aggregator & SLO alerting.
  - **Warmup**: [`leetcode_217_contains_duplicate.py`](./python-automation/day-05-dictionaries-hashmaps/leetcode_217_contains_duplicate.py) — LeetCode #217 solution.
  - **Docs**: [Day 5 Walkthrough & Notes](./python-automation/day-05-dictionaries-hashmaps/README.md)
* [x] **Day 6: Basic DSA — Stacks & Queues**
  - **Script**: [`bracket_validator.py`](./python-automation/day-06-stacks-queues/bracket_validator.py) — LIFO Stack for IaC HCL/JSON syntax linting.
  - **Buffer**: [`request_buffer.py`](./python-automation/day-06-stacks-queues/request_buffer.py) — FIFO Queue with `collections.deque` and backpressure.
  - **Warmup**: [`leetcode_20_valid_parentheses.py`](./python-automation/day-06-stacks-queues/leetcode_20_valid_parentheses.py) — LeetCode #20 solution.
  - **Docs**: [Day 6 Walkthrough & Notes](./python-automation/day-06-stacks-queues/README.md)

---

### Phase 2A: Linux Internals & OS Diagnostics (Days 7–11)
* [ ] **Day 7: Linux Filesystem Hierarchy** (`/etc`, `/var`, `/proc`, `/dev`, Bandit 0–5)
* [ ] **Day 8: Permissions & Ownership** (`chmod`, `chown`, octal math, Bandit 6–10)
* [ ] **Day 9: Process Management & Signals** (`ps aux`, `top`, `pgrep`, `kill -9`, runaway process killer)
* [ ] **Day 10: Memory, Disk & Systemd Services** (`free -m`, `df -h`, custom `.service` unit)
* [ ] **Day 11: Linux Cron Daemon Automation** (System health watchdog script every 15 mins)

---

### Phase 2B: Computer Networks & Security (Days 12–14)
* [ ] **Day 12: IP Addressing & Subnetting Basics** (CIDR, /24 vs /16, usable host calculation)
* [ ] **Day 13: DNS, DHCP & Gateway Troubleshooting** (`ss -tulpn`, `dig`, `nslookup`, `traceroute`)
* [ ] **Day 14: Firewall Security & Hardening** (UFW allow 22/80/443, deny all, brute-force protection)

---

### Phase 3: Docker Containerization & Kubernetes (Days 15–22)
* [ ] **Day 15: Docker Basics & Images** (Dockerfile, layers, image caching)
* [ ] **Day 16: Container Networking & Port Forwarding** (Port mapping, container bridge networks)
* [ ] **Day 17: Container Storage & Persistent Volumes** (Named volumes vs bind mounts)
* [ ] **Day 18: Multi-Stage Docker Builds & Optimization** (Shrinking image from 800MB to <50MB)
* [ ] **Day 19: Docker Compose (Multi-Container)** (Python API + PostgreSQL on shared network)
* [ ] **Day 20: Kubernetes Architecture & Pods** (Control plane, worker nodes, `pod.yaml`)
* [ ] **Day 21: K8s Deployments & Services** (3 replicas, rolling updates, ClusterIP, NodePort)
* [ ] **Day 22: ConfigMaps, Secrets & Health Probes** (`livenessProbe`, `readinessProbe`, self-healing pods)

---

### Phase 4: CI/CD Pipelines & Observability (Days 23–26)
* [ ] **Day 23: GitHub Actions Basics** (Workflows, automated testing on push)
* [ ] **Day 24: Automated Docker Build in CI** (Build & push image to Docker Hub on merge)
* [ ] **Day 25: Container Security Scanning** (Trivy vulnerability scanner blocking CVEs)
* [ ] **Day 26: Observability: Prometheus & Grafana** (Metrics scraping, PromQL, Grafana dashboard)

---

### Phase 5: AWS Cloud Engineering & Terraform (Days 27–33)
* [ ] **Day 27: AWS Setup & EC2 Compute** (MFA, IAM admin user, Ubuntu t3.micro, SSH)
* [ ] **Day 28: AWS S3 Storage & RDS Database** (S3 versioning, PostgreSQL RDS)
* [ ] **Day 29: AWS Custom VPC & Subnets** (Multi-AZ VPC, 2 public + 2 private subnets, IGW)
* [ ] **Day 30: NAT Gateways & Application Load Balancers** (Private subnet egress, ALB traffic routing)
* [ ] **Day 31: IAM Least Privilege & Instance Profiles** (S3 IAM role attached to EC2 profile)
* [ ] **Day 32: Terraform Infrastructure as Code** (Modular VPC, subnets, EC2 with `terraform apply`)
* [ ] **Day 33: Cloud Cost Optimization & Alarms** (CloudWatch spend alarms, S3 lifecycle policies)

---

### Phase 6: High-Scale System Design & Job Applications (Days 34–36)
* [ ] **Day 34: High-Scale System Design Essentials** (99.9% uptime architecture on AWS)
* [ ] **Day 35: Resume Overhaul & Portfolio Polish** (Metric-driven bullets, LaTeX resume)
* [ ] **Day 36: Technical Mock Interview & Job Applications** (5 applications/day sprint)
