# Amazon VPC Notes & Networking Blueprint

A VPC is your private slice of AWS. Here is how I set mine up properly and how I troubleshoot when things refuse to connect.

---

## My Standard 3-Tier Subnet Layout
Whenever I design a VPC for an app, I divide `10.0.0.0/16` like this:

```text
10.0.0.0/16 (VPC)
├── Public Subnets (For ALBs & NAT Gateways only)
│   ├── ap-south-1a: 10.0.1.0/24
│   └── ap-south-1b: 10.0.2.0/24
├── Private App Subnets (For EC2 instances, ECS, EKS)
│   ├── ap-south-1a: 10.0.10.0/24
│   └── ap-south-1b: 10.0.11.0/24
└── Isolated Database Subnets (RDS, Redis — NO internet route at all)
    ├── ap-south-1a: 10.0.20.0/24
    └── ap-south-1b: 10.0.21.0/24
```

> **Remember:** AWS reserves 5 IP addresses per subnet (.0 network, .1 router, .2 DNS, .3 future, .255 broadcast). A `/24` gives you 251 usable IPs, not 256.

---

## Security Groups vs NACLs (The Gotcha That Bit Me)
* **Security Groups** are **stateful**. If inbound port 443 is allowed, the response traffic is automatically allowed back out.
* **Network ACLs** are **stateless**. If you allow inbound 443, you **MUST** also have an outbound rule allowing ephemeral ports (`1024-65535`). If you forget this, curl will hang forever.

---

## Save Money on NAT Gateways with VPC Gateway Endpoints
NAT Gateways cost around ~$32/month plus $0.045 per GB transferred.
If your private EC2 instances download or upload files to S3, you do **not** need to route that through the NAT Gateway!
* Create an **S3 Gateway Endpoint** (it is 100% free).
* Point your private route table to the endpoint.
* All S3 traffic now stays on AWS's internal network at zero data transfer cost.
