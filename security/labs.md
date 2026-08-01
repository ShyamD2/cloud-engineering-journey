# Cloud Security & Hardening Checklist

Things I check to make sure an AWS account and Linux servers are hardened against common attacks:

---

## AWS Account Baselines
- [ ] Root account has MFA enabled and has zero access keys created.
- [ ] AWS CloudTrail is turned on across all regions with log file validation enabled.
- [ ] AWS EBS encryption by default is enabled for the account.
- [ ] S3 Block Public Access is enabled at the account level.
- [ ] Zero Security Groups have port 22 (SSH) or port 3389 (RDP) open to `0.0.0.0/0`.

---

## Linux Server Baselines
- [ ] Password authentication disabled in `/etc/ssh/sshd_config` (`PasswordAuthentication no`).
- [ ] Root login via SSH disabled (`PermitRootLogin no`).
- [ ] Dedicated service accounts with `/usr/sbin/nologin` for daemons.
- [ ] Firewall (UFW / iptables) enabled with default deny on incoming traffic.
