# Project AEGIS — Autonomous Cloud Defense & SOAR Fabric on AWS

> **Repository:** [github.com/ShyamD2/aegis-cloud-security](https://github.com/ShyamD2/aegis-cloud-security)  
> **Infrastructure:** 100% Codified Terraform (Multi-Account AWS)  
> **Compliance & Audit:** SEC Rule 17a-4 S3 WORM Vaults & KMS  
> **Technical Dossier:** [AEGIS_Project_Report.pdf](https://shyamd2-portfolio.netlify.app/reports/AEGIS_Project_Report.pdf) (12.8 MB)

---

## 💡 The Problem: Slow Incident Triage & Tamperable Forensics

In modern multi-account enterprise clouds:
1. **Manual Incident Response Lag:** When a workload is compromised (e.g. brute-force SSH, IAM credential leakage, or crypto-mining malware), SOC analysts take an average of 30 to 45 minutes to detect, correlate, and isolate the instance manually.
2. **Fragile Digital Forensics:** Audit logs and containment traces are frequently stored in mutable object storage where an adversary with compromised administrative credentials can wipe evidence before detection.
3. **ClickOps Configuration Drift:** Security group changes made during incident containment are rarely codified back to source control, causing configuration regressions during the next Terraform rollout.

---

## 🛡️ Architecture & Autonomous SOAR Pipeline

Project AEGIS solves this by implementing an **event-driven Security Orchestration, Automation, and Response (SOAR)** fabric codified entirely in Terraform across dedicated AWS accounts:

```
[ Compromised EC2 / VPC ]
            │
            ▼
[ AWS GuardDuty ] ──► (Anomaly Finding JSON)
                             │
                             ▼
                    [ Amazon EventBridge ]
                             │
                             ▼
               [ AWS Step Functions Workflow ]
                ├── Step 1: Query Severity & Blast Radius
                ├── Step 2: Invoke Lambda Isolation Router (<820ms)
                │    ├── Apply Zero-Trust Isolation Security Group (Egress/Ingress DENY)
                │    └── Push Rogue IP Blacklist to AWS WAFv2 WebACL
                └── Step 3: Stream Forensic Hash to S3 Object Lock (SEC 17a-4 WORM)
```

---

## ⚡ Key Engineering Capabilities

### 1. Sub-820ms Active Threat Isolation
* Amazon EventBridge captures GuardDuty finding JSON payloads instantaneously.
* Triggers an AWS Step Function state machine orchestrating Python Lambda execution routers.
* Replaces compromised EC2 security groups with an empty quarantine SG and updates regional AWS WAFv2 IPSets in **under 820ms**.

### 2. SEC Rule 17a-4 Compliant S3 WORM Vaulting
* Digital forensic logs, snapshot metadata, and EventBridge event payloads are streamed directly to an **Amazon S3 Object Lock vault in Compliance Mode**.
* Enforces SEC Rule 17a-4 regulatory compliance: records cannot be deleted, overwritten, or modified even by the AWS root account until the legal hold retention period expires.
* All data encrypted at rest via customer-managed AWS KMS keys with automated annual key rotation.

### 3. Multi-Account Terraform Codification
* Zero manual ClickOps: 100% of the architecture is codified in modular, reusable Terraform modules.
* Separates security tooling (`SecurityToolingAccount`), log archives (`LogArchiveAccount`), and workload VPCs (`ProductionWorkloadAccount`).

### 4. Rigorous CI/CD Security Testing
* Automated test pipelines with **110 passing test suites** verifying IAM policy least privilege, Step Function state machine transitions, and Lambda error recovery.
* Enforced with **Checkov** (IaC security static analysis), **TFLint** (Terraform rules linter), and **Trivy** (container & dependency vulnerability scanner).

---

## 🔗 Quick Links
* **Source Code:** [github.com/ShyamD2/aegis-cloud-security](https://github.com/ShyamD2/aegis-cloud-security)
* **Technical Dossier:** [Download Project AEGIS Security Report (PDF)](https://shyamd2-portfolio.netlify.app/reports/AEGIS_Project_Report.pdf)
