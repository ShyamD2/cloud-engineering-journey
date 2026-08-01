# AWS IAM Notes & Security Playbook

IAM is the foundation of everything in AWS. If your IAM setup is messy, your security is messy.

---

## The Rule of Least Privilege
I never attach `AdministratorAccess` to an EC2 instance or developer role. Give only the exact actions needed:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadOnly",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-app-assets",
        "arn:aws:s3:::my-app-assets/*"
      ]
    }
  ]
}
```

---

## Users vs Roles vs Instance Profiles
* **IAM User:** A person or a legacy service with static access keys (avoid these whenever possible).
* **IAM Role:** An identity with temporary credentials. Used by AWS services, Lambda functions, or external tools via STS AssumeRole.
* **Instance Profile:** A container that passes an IAM role to an EC2 instance so your code can call AWS APIs without embedding access keys on the server.

---

## Troubleshooting IAM Denials
When AWS says `AccessDenied`, I check in this order:
1. Is there an **Explicit Deny** anywhere? (Explicit deny always wins).
2. Is there an **SCP** (Service Control Policy) at the AWS Organizations level blocking this?
3. Is there a **Permissions Boundary** attached to the user/role that leaves out this action?
4. If accessing S3 or KMS, does the **Bucket Policy** or **KMS Key Policy** allow the caller?
