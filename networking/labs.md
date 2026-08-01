# Networking Labs Notes

## Lab 1: Multi-Subnet VPC with Public & Private Subnets
* Created VPC `10.0.0.0/16`.
* Attached Internet Gateway for public subnets.
* Placed a NAT Gateway in the public subnet so private EC2 instances can run `apt update` without having public IP addresses.

## Lab 2: VPC Peering Connection
* Connected two non-overlapping VPCs (`10.100.0.0/16` and `10.200.0.0/16`).
* **Lesson learned:** VPC Peering is non-transitive. If A peers with B, and B peers with C, A CANNOT talk to C unless you explicitly create a peering link between A and C.
