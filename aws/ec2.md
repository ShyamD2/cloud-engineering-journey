# Amazon EC2 Notes & Cheat Sheet

These are my personal operational notes for EC2 instances, EBS storage, and secure server access.

---

## 1. Things I Never Do in Production Anymore
* **Opening port 22 to 0.0.0.0/0**: Just don't. Use **AWS Systems Manager (SSM) Session Manager** instead. Attach the `AmazonSSMManagedInstanceCore` policy to the instance IAM role, keep port 22 closed, and run:
  ```bash
  aws ssm start-session --target i-0123456789abcdef0
  ```
  No SSH keys to lose, no bastions to maintain, and full audit logs in CloudWatch.

* **Using IMDSv1**: IMDSv1 is vulnerable to SSRF (Server-Side Request Forgery). Always enforce IMDSv2:
  ```bash
  aws ec2 modify-instance-metadata-options \
      --instance-id i-0123456789abcdef0 \
      --http-tokens required \
      --http-endpoint enabled
  ```

---

## 2. EBS gp3 vs io2 (Mental Model)
* **gp3 is the default choice**: You get baseline 3,000 IOPS and 125 MB/s throughput included for free regardless of size. With gp2, you had to buy huge 1TB disks just to get 3,000 IOPS.
* **io2 is for heavy relational databases**: Consistent sub-millisecond latency and high 99.999% durability.

---

## 3. How to Expand an EBS Volume Without Any Downtime
When an attached disk runs out of space:
1. Increase the size in AWS Console or CLI:
   ```bash
   aws ec2 modify-volume --volume-id vol-xxxx --size 50
   ```
2. Wait a minute for the EBS status to move to `optimizing`.
3. SSH / SSM into the box and check disk layout:
   ```bash
   lsblk
   ```
4. Grow the partition:
   ```bash
   sudo growpart /dev/xvda 1
   ```
5. Resize the actual filesystem (check with `df -T` first):
   ```bash
   # If XFS:
   sudo xfs_growfs -d /

   # If ext4:
   sudo resize2fs /dev/xvda1
   ```
*Zero reboots, zero service restarts.*
