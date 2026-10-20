# Cloud & DevOps Engineering Journey

Hey there! 👋 I'm **Shyam Kumar D**, and this repository is where I document my day-to-day journey transitioning into Cloud, DevOps, and Site Reliability Engineering (SRE).

I started this repo on **August 1, 2026**. I got tired of just passively watching tutorials and wanted **undeniable proof of work**. Every single file in this repo comes from real hands-on labs I built, actual terminal commands I ran, errors I broke my head over, and how I resolved them.

---

## 🧭 How This Repo Is Organized

I follow a simple rule: **Separate daily activity from permanent knowledge.**

```text
cloud-engineering-journey/
│
├── README.md               ← You are here (quick overview & project links)
├── new-day.ps1             ← Quick script I run to spin up today's log
│
├── daily-log/              ← Raw, daily work logs (Aug 1, 2026 → Present)
│   ├── 2026-08-01.md
│   ├── 2026-08-02.md
│   └── ...
│
├── aws/                    ← Clean notes & cheat-sheets on AWS services
├── devops/                 ← Terraform, Docker, Kubernetes & CI/CD guides
├── networking/             ← Core networking mental models & debugging tricks
├── security/               ← Hands-on hardening & benchmark checklists
│
└── projects/               ← Deeper writeups on the major projects I'm building
    ├── driftwarden.md                  ← Go 1.24+ AWS 3-Source Drift & GitOps Engine
    ├── kubeforecast.md                 ← Go K8s Scheduler & FinOps Engine on AWS EKS
    ├── project-jarvis.md               ← Autonomous Cyber-Physical AgentOS (19-page spec)
    ├── aegis.md                        ← Autonomous DevSecOps SOAR & S3 WORM Vaults
    └── aws-serverless-url-shortener.md ← Event-Driven Serverless Data Platform
```

* **`daily-log/`**: My daily journal. What I did today, what failed, why it failed, and what I learned from fixing it.
* **`aws/`, `devops/`, `networking/`, `security/`**: Permanent notes. When I figure out something tricky (like stateless NACL ephemeral ports, Terraform state locking, or PreScore scheduler hooks in Go), I write a clean guide here so I never forget it.

---

## 🛠️ Tech Stack I Work With

* **Programming & Systems:** Go 1.24+, Python 3.13, Bash Shell, Linux (Ubuntu/Debian) Systemd internals
* **Cloud Infrastructure:** AWS (EKS v1.31, EC2, VPC, ALB, Auto Scaling, IAM IRSA, S3, RDS, DynamoDB, Lambda, API Gateway, EventBridge, Step Functions, SQS, KMS, CloudWatch, Athena)
* **Infrastructure as Code & GitOps:** Terraform (Modular multi-account, S3 remote state, DynamoDB locking), Helm v3, GitOps PR remediation
* **Containers & Orchestration:** Docker (Distroless multi-stage <25MB), Kubernetes (Custom Go Scheduling Framework plugins, PodDisruptionBudgets, Kind, kubectl)
* **CI/CD & DevSecOps:** GitHub Actions (with AWS OIDC), Trivy container scanning, Checkov, TFLint, CIS AWS Benchmark v3.0, SEC Rule 17a-4 S3 WORM Object Lock
* **Observability & Diagnostics:** Prometheus telemetry, Grafana (5 custom cluster dashboards), CloudWatch Logs/Alarms, Linux `/proc` telemetry

---

## 🚀 Flagship Engineering Projects

| Project | What It Is | Tech Stack | Writeup & Reports |
| :--- | :--- | :--- | :--- |
| **DriftWarden** | **Three-Source AWS Drift Detection & GitOps Reconciliation Engine.** Correlates Git desired configuration, Terraform remote state, and live AWS reality to eradicate configuration drift, shadow ClickOps resources, and unapplied changes with automated CIS AWS v3.0 auditing and GitOps PR remediation. Packaged in a distroless container `<25MB`. | Go 1.24+, AWS SDK v2, Terraform State, Docker Distroless, CIS AWS v3.0, GitHub Actions | [Read Notes](./projects/driftwarden.md) • [Report (PDF)](https://shyamd2-portfolio.netlify.app/reports/DriftWarden_Project_Report.pdf) • [GitHub](https://github.com/ShyamD2/driftwarden) |
| **KubeForecast** | **Kubernetes Predictive Scheduling & FinOps Optimization Engine.** Intercepts pod scheduling with a custom Go Scheduling Framework plugin evaluating candidate nodes in `90.35 ns/op`. Implements 75% dynamic waterline bin-packing, hardware soak-tested on live AWS EKS v1.31 with **50.0%–66.7% node reduction** and 5 Grafana dashboards. | Go 1.23, Kubernetes (AWS EKS v1.31), Terraform, Helm v3, Prometheus, Grafana | [Read Notes](./projects/kubeforecast.md) • [18-Page Research Paper (PDF)](https://shyamd2-portfolio.netlify.app/reports/KubeForecast_Project_Report.pdf) • [GitHub](https://github.com/ShyamD2/KubeForecast) |
| **Project J.A.R.V.I.S. (AgentOS v2.0)** | **Autonomous Cyber-Physical AgentOS.** Unites physical IoT microcontrollers, native Windows computer-use (UIA + Vision + Core Audio COM), and AWS cloud mesh under a 6-stage canonical pipeline. Features dual-channel ground-truth verification, 4-tier blast radius isolation, **183 automated tests (100% pass rate)**, and strict **0.00% false-success rate** on 100-task benchmarks. | Python 3.13, FastAPI, Playwright, Win32 UIAutomation, AWS Boto3, Docker, AsyncIO | [Read Notes](./projects/project-jarvis.md) • [19-Page Specification (PDF)](https://shyamd2-portfolio.netlify.app/reports/JARVIS_Project_Report.pdf) • [GitHub](https://github.com/ShyamD2/project-jarvis) |
| **Project AEGIS** | **Autonomous Cloud Defense & Active SOAR Fabric on AWS.** Eliminates 45-minute incident triage lag by orchestrating EventBridge, Step Functions, and Lambda to isolate compromised workloads and blacklist rogue IPs via AWS WAFv2 in `<820ms`. Streams immutable forensic trails to SEC Rule 17a-4 S3 WORM vaults with KMS encryption. | AWS Multi-Account, Terraform, EventBridge, Step Functions, S3 WORM, KMS, Checkov | [Read Notes](./projects/aegis.md) • [Dossier (PDF)](https://shyamd2-portfolio.netlify.app/reports/AEGIS_Project_Report.pdf) • [GitHub](https://github.com/ShyamD2/aegis-cloud-security) |
| **AWS Serverless Platform** | **Event-Driven Serverless URL Shortener & Real-Time Analytics Platform.** Sub-30ms user redirects via HTTP API Gateway, Lambda, and DynamoDB at $0 idle compute cost. Asynchronous click telemetry decoupled via SQS dead-letter queues to partitioned S3 logs queried in-place via Amazon Athena. | AWS Lambda, API Gateway, DynamoDB, SQS, S3, Athena, Terraform, Python | [Read Notes](./projects/aws-serverless-url-shortener.md) • [Dossier (PDF)](https://shyamd2-portfolio.netlify.app/reports/URL_Shortener_Project_Report.pdf) • [GitHub](https://github.com/ShyamD2/aws-cloud-serverless-url-shortener) |

---

## 📑 Formal Engineering Dossiers & Research Reports

All formal architectural specifications and empirical soak-test reports authored during my journey are published and freely accessible:

1. 📄 **[KubeForecast Empirical Research Dossier (18 Pages • 2.6 MB)](https://shyamd2-portfolio.netlify.app/reports/KubeForecast_Project_Report.pdf)**: Mathematical analysis of waterline bin-packing, Score evaluation hooks, and soak tests on AWS EKS c7i-flex.large node fleets.
2. 📄 **[DriftWarden Engineering Specification Dossier (1.1 MB)](https://shyamd2-portfolio.netlify.app/reports/DriftWarden_Project_Report.pdf)**: Three-source reconciliation engine mechanics, lock-aware S3 state auditing, and CIS v3.0 benchmark algorithms.
3. 📄 **[Project J.A.R.V.I.S. AgentOS Specification (19 Pages • 3.9 MB)](https://shyamd2-portfolio.netlify.app/reports/JARVIS_Project_Report.pdf)**: 6-stage canonical pipeline lifecycle, dual-channel sensory reality checking, and 100-task empirical reliability benchmarks.
4. 📄 **[Project AEGIS SOAR Security Dossier (12.8 MB)](https://shyamd2-portfolio.netlify.app/reports/AEGIS_Project_Report.pdf)**: Autonomous threat detection, blast-radius isolation, and SEC Rule 17a-4 immutable WORM vaulting on AWS.
5. 📄 **[AWS Serverless Platform Architecture Blueprint (10.8 MB)](https://shyamd2-portfolio.netlify.app/reports/URL_Shortener_Project_Report.pdf)**: Event-driven serverless redirect architecture, asynchronous SQS queues, and partitioned Athena SQL query patterns.

---

## 🎓 Verified Certifications & Industry Accreditations

* **AWS Academy Graduate — Cloud Foundations** (Amazon Web Services • Credly Verified)
* **Linux 100: Fundamentals** (TCM Security • cert_w14v5kck)
* **Programming 100: Fundamentals** (TCM Security • cert_smzmggl1)
* **AWS Solution Architect Level-2** (Nminds Academy • Credential 11121329)
* **DevOps vs. SRE vs. Cloud Engineer vs. Platform Engineer Masterclass** (Scaler Masterclass • Sept 2026)
* **Master Agentic Engineering & Workflow Automation Masterclass** (Scaler Masterclass • Sept 2026)
* **The FDE Simulation: Build & Deploy AI in 3 Hours Masterclass** (Scaler Masterclass • Sept 2026)
* **Careers in AI + Wireless Workshop** (Thiagarajar College of Engineering • TECHVISTA'26)
* **Mastercard Cybersecurity Simulation** (Mastercard • Forage Verified)
* **Deloitte Cyber Job Simulation** (Deloitte • Forage Verified)
* **Deloitte Data Analytics Simulation** (Deloitte • Forage Verified)
* **Data for Decision Makers Simulation** (BCG X • Forage Verified)
* **Cloud Computing with Web Development Intern** (Reccsar Pvt. Ltd. • May 2026)

---

## 🚀 36-Day DevOps & Cloud Engineer Master Plan

> **Structured Zero-Fluff Roadmap: 4.5 Hours/Day • 162 Hours Total • Job-Ready Target**  
> Full Syllabus & Progress: [36-Day Master Plan Tracker](./devops/36-DAY-DEVOPS-ROADMAP.md)

| Phase | Days | Topic | Status | Links |
| :--- | :---: | :--- | :---: | :--- |
| **Phase 1** | Days 1–6 | Basic Python Scripting & Core Data Structures | **PHASE 1 COMPLETE (6/6 Days)** | [Day 1: Filesystem Automation](./devops/python-automation/day-01-filesystem/) • [Day 2: Log Errors](./devops/python-automation/day-02-log-errors/) • [Day 3: Auto Cleanup](./devops/python-automation/day-03-auto-cleanup/) • [Day 4: Arrays & Lists](./devops/python-automation/day-04-arrays-lists/) • [Day 5: HashMaps](./devops/python-automation/day-05-dictionaries-hashmaps/) • [Day 6: Stacks & Queues](./devops/python-automation/day-06-stacks-queues/) |
| **Phase 2A** | Days 7–11 | Linux Internals & OS Diagnostics | **IN PROGRESS (Days 7–8 Done)** | [Day 7: Linux Filesystem Hierarchy](./devops/linux-internals/day-07-filesystem-hierarchy/) • [Day 8: Permissions & Ownership](./devops/linux-internals/day-08-permissions-ownership/) |
| **Phase 2B** | Days 12–14 | Computer Networks & Security | Up Next | Subnetting, DNS, Gateway, UFW Firewalls |
| **Phase 3** | Days 15–22 | Docker Containerization & Kubernetes | Up Next | Multi-stage Docker, Compose, K8s Pods & Deployments |
| **Phase 4** | Days 23–26 | CI/CD Pipelines & Observability | Up Next | GitHub Actions, Trivy Security, Prometheus & Grafana |
| **Phase 5** | Days 27–33 | AWS Cloud Architecture & Terraform IaC | Up Next | Multi-tier VPC, ALB, RDS, Terraform Apply & Destroy |
| **Phase 6** | Days 34–36 | High-Scale System Design & Job Sprint | Up Next | 99.9% High Availability, Resume Polish & Applications |

---

## 🤝 Connect & Interactive SRE Cockpit

* **Interactive SRE Portfolio:** [shyamd2-portfolio.netlify.app](https://shyamd2-portfolio.netlify.app)
* **GitHub Profile:** [github.com/ShyamD2](https://github.com/ShyamD2)
* **LinkedIn:** [linkedin.com/in/shyam-kumar-d](https://linkedin.com/in/shyam-kumar-d)
* **Direct Telemetry:** shyamcloud021@gmail.com | +91 7010672248
