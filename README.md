# Cloud & DevOps Engineering Journey

Hey there! 👋 I'm **Shyam Kumar**, and this repository is where I document my day-to-day journey transitioning into Cloud and DevOps engineering.

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
    ├── aws-serverless-url-shortener.md
    ├── aegis.md
    └── kubeforecast.md
```

* **`daily-log/`**: My daily journal. What I did today, what failed, why it failed, and what I learned from fixing it.
* **`aws/`, `devops/`, `networking/`, `security/`**: Permanent notes. When I figure out something tricky (like stateless NACL ephemeral ports or Terraform state locking), I write a clean guide here so I never forget it.

---

## 🛠️ Tech Stack I Work With

* **Cloud:** AWS (VPC, EC2, IAM, S3, RDS, DynamoDB, Lambda, API Gateway, CloudWatch, SSM)
* **Infrastructure as Code:** Terraform
* **Containers & Orchestration:** Docker, Docker Compose, Kubernetes (Kind, kubectl)
* **CI/CD & Scripting:** GitHub Actions (with AWS OIDC), Bash, Python (Boto3)
* **Core Skills:** Linux systems administration, TCP/IP networking, DNS troubleshooting, Cloud security & cost optimization

---

## 🚀 Projects I've Built / Currently Building

| Project | What It Is | Tech | Writeup |
| :--- | :--- | :--- | :--- |
| **Serverless URL Shortener** | Event-driven redirect service that handles link generation, Base62 hashing, and auto-expiring links via DynamoDB TTL. | AWS Lambda, API Gateway, DynamoDB, Python | [Read Notes](./projects/aws-serverless-url-shortener.md) |
| **Aegis** | A lightweight security compliance scanner that checks AWS environments against CIS benchmarks and auto-remediates open security groups and public S3 buckets. | Python, Boto3, AWS EventBridge, Terraform | [Read Notes](./projects/aegis.md) |
| **KubeForecast** | A Kubernetes resource optimizer that analyzes Prometheus pod metrics to recommend realistic CPU/memory requests and limits to kill cluster waste. | Kubernetes, Helm, Python, Prometheus | [Read Notes](./projects/kubeforecast.md) |

---

## 📖 Quick Links to My Notes

* **AWS:** [EC2 & Storage](./aws/ec2.md) • [VPC Networking](./aws/vpc.md) • [IAM & Policies](./aws/iam.md) • [S3 Storage & Security](./aws/s3.md)
* **DevOps:** [Terraform Rules of Thumb](./devops/terraform.md) • [Docker & Multi-Stage Builds](./devops/docker.md) • [Kubernetes Basics & Gotchas](./devops/kubernetes.md) • [GitHub Actions & AWS OIDC](./devops/cicd.md)
* **Networking & Security:** [Core Networking](./networking/fundamentals.md) • [My 5-Step Debugging Workflow](./networking/troubleshooting.md) • [Hands-on Labs](./networking/labs.md) • [Security Checklists](./security/labs.md)

---

## 🤝 Connect

If you're also on this journey or have suggestions on how I can improve my architectures, feel free to open an issue or connect with me!
