# Terraform Rules of Thumb

My notes on structuring clean, maintainable Terraform code and avoiding state file disasters.

---

## 1. Never Store State Locally
Local `terraform.tfstate` files on your laptop get deleted, conflict with teammates, and contain secrets in plaintext. Always use a remote backend:

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "shyam-tf-state-ap-south-1"
    key            = "prod/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```
* S3 holds the state file with encryption and versioning.
* DynamoDB handles locking so two people can't apply changes simultaneously.

---

## 2. My Standard File Layout
```text
├── main.tf           # Resources
├── variables.tf      # Inputs with descriptions and types
├── outputs.tf        # IDs and endpoints to share
├── terraform.tfvars  # The actual values (ignored in .gitignore if sensitive)
└── versions.tf       # Provider locks
```

---

## 3. Useful Commands I Run Regularly
```bash
terraform fmt -recursive      # Clean up formatting automatically
terraform validate            # Catch syntax errors before touching AWS
terraform plan -out=tfplan    # Save the plan so apply does exactly what you reviewed
terraform apply tfplan
```
