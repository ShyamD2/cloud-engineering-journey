# My 5-Step Connectivity Debugging Workflow

Whenever a server can't connect to another server, I run through this checklist in order. It saves me hours of guessing.

---

### Step 1: Check DNS
Is the domain actually resolving to an IP address?
```bash
dig +short api.myservice.com
# Or
nslookup api.myservice.com
```

### Step 2: Check if the Port Is Open (Layer 4)
Can packets reach the port?
```bash
nc -zv -w 3 10.0.10.25 443
# Or with curl:
curl -Iv https://10.0.10.25:443
```
* If it times out: Security Group, NACL, or Route Table issue.
* If connection is refused: Security Group allowed it, but the application isn't running on the server!

### Step 3: Check if the Application is Listening
On the target server:
```bash
ss -tulpn | grep 8080
```
Is the process bound to `0.0.0.0:8080` (all interfaces) or just `127.0.0.1:8080` (localhost only)? If it's bound to `127.0.0.1`, outside traffic cannot reach it.

### Step 4: Check Route Tables
Does the subnet have a route to reach the target?
```bash
ip route show
```
In AWS: Check the subnet's Route Table. Does it have an entry for `0.0.0.0/0 -> igw-xxx` (public) or `0.0.0.0/0 -> nat-xxx` (private)?

### Step 5: Check Ephemeral Ports on NACLs
If you get traffic in but responses drop, check if the subnet's Network ACL allows outbound traffic on ports `1024-65535`.
