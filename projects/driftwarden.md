# DriftWarden — AWS Infrastructure Drift Detection & GitOps Reconciliation Engine

> **Repository:** [github.com/ShyamD2/driftwarden](https://github.com/ShyamD2/driftwarden)  
> **Language:** Go 1.24+  
> **Status:** Production-Ready & Open Source  
> **Technical Dossier:** [DriftWarden_Project_Report.pdf](https://shyamd2-portfolio.netlify.app/reports/DriftWarden_Project_Report.pdf) (1.1 MB)

---

## 💡 The Problem: The Blindspot in Modern Cloud Infrastructure

Traditional drift detection utilities (like `terraform plan -detailed-exitcode` or standard scheduled scanners) have a fundamental flaw: **they only compare two sources**:
$$\text{Terraform State} \longleftrightarrow \text{AWS Live Reality}$$

This two-source model completely misses:
1. **Unapplied Git Commits:** Infrastructure changes pushed and merged to Git that were never applied to the Terraform state file.
2. **Shadow & Out-of-Band Cloud Resources:** Resources provisioned via the AWS Management Console (ClickOps) or emergency CLI scripts that exist neither in Git nor in Terraform state.
3. **CIS Benchmark & Security Drift:** Security group rules modified out-of-band to allow ingress from `0.0.0.0/0` on port 22/3389, or public S3 bucket policies applied without state awareness.
4. **False-Positive Operational Storms:** High-frequency polling flags temporary AWS API eventual-consistency lag, generating hundreds of useless Slack and PagerDuty alerts.

---

## 🏛️ The Three-Source Architecture

DriftWarden eliminates this blindspot by introducing a **deterministic three-source correlation engine**:

```
                       ┌─────────────────────────┐
                       │   Git Repository (IaC)  │
                       │   (Desired Intention)   │
                       └────────────┬────────────┘
                                    │
                                    │ Parser (HCL v2)
                                    ▼
       ┌────────────────────► Correlation ◄────────────────────┐
       │                         Engine                        │
       │                       (Go 1.24+)                      │
       ▼                                                       ▼
┌──────────────┐                                        ┌──────────────┐
│  Terraform   │                                        │   Live AWS   │
│  State (S3)  │                                        │ Environment  │
│ (Recorded)   │                                        │   (Reality)  │
└──────────────┘                                        └──────────────┘
```

By correlating all three vectors simultaneously, DriftWarden categorizes every anomaly into clear operational buckets:
* **True Drift:** In Git & State, but modified in AWS Live.
* **Shadow Resource:** Present in AWS Live, but missing from Git & State.
* **Unapplied Git Change:** Present in Git, but missing from State & Live.
* **Ghost Resource:** Present in State, but already deleted in AWS Live.

---

## ⚡ Core Engineering Highlights

### 1. High-Performance Concurrency in Go 1.24+
* Utilizes Go goroutines with bounded worker pools (`sync.WaitGroup` + buffered semaphore channels) to scan multi-account, multi-region AWS environments without hitting AWS API rate limits (`RequestLimitExceeded`).
* Implemented AWS SDK v2 with exponential backoff and jitter algorithms.

### 2. Lock-Aware S3 State Auditing
* Inspects remote Terraform S3 state files while respecting DynamoDB state lock leases (`LockID`).
* Guarantees zero race conditions or state corruption during concurrent CI/CD pipeline runs.

### 3. Consistency Re-Probing (Anti-Flapping Engine)
* Solves the AWS eventual consistency problem by issuing automated verification re-probes with configurable delay windows before raising operational alerts.
* Eliminates over 95% of transient false-positive alarms.

### 4. CIS AWS Benchmark v3.0 Compliance
* Built-in security rules engine auditing live resource attributes against CIS AWS Foundations Benchmark:
  * Open SSH (`0.0.0.0/0:22`) and RDP (`0.0.0.0/0:3389`) detection.
  * Public S3 bucket ACL and bucket policy checks.
  * Unencrypted EBS volumes and missing KMS key rotations.

### 5. Automated GitOps PR Remediation
* **Safe Dry-Run Engine:** Emits detailed JSON diff evidence and JUnit test reports for CI/CD gates.
* **Terraform 1.5+ Import Generation:** Automatically generates declarative `import { to = ... id = ... }` HCL blocks to adopt shadow resources into GitOps management without manual ClickOps.

---

## 📦 Container Packaging & Footprint

* Packaged as an ultra-lean multi-stage Docker build based on `gcr.io/distroless/static-debian12:nonroot`.
* Final image size: **< 25 MB** with zero OS package managers, shells, or unneeded attack surface.
* Automated CI quality gates in GitHub Actions testing code formatting (`gofmt`), static analysis (`golangci-lint`), unit tests (`go test -race -v`), and Trivy container vulnerability scans.

---

## 🔗 Quick Links
* **Source Code:** [github.com/ShyamD2/driftwarden](https://github.com/ShyamD2/driftwarden)
* **Technical Dossier:** [Download DriftWarden Specification Report (PDF)](https://shyamd2-portfolio.netlify.app/reports/DriftWarden_Project_Report.pdf)
