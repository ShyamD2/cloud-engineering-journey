# CI/CD Notes: GitHub Actions & AWS OIDC

How to build automated pipelines and authenticate to AWS without storing permanent API keys in GitHub.

---

## Why OIDC Beats Static Access Keys
In the old days, people put `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` into GitHub Secrets.
The problem? Those keys never expire. If someone leaks a secret or has repo access, they have access to your AWS account forever until you revoke it.

With **OpenID Connect (OIDC)**:
1. GitHub Actions asks GitHub for a signed JWT token.
2. The runner hands that token to AWS STS.
3. AWS checks the repository name and branch. If it matches your IAM Trust Policy, it gives back **temporary credentials valid for 1 hour**.
4. Zero static keys stored anywhere.

---

## Sample Workflow
```yaml
name: Deploy Infra
on:
  push:
    branches: [ main ]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS Credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::197550036081:role/GitHubActionsDeployRole
          aws-region: ap-south-1

      - name: Verify Authentication
        run: aws sts get-caller-identity
```
