# Day 7: Linux Filesystem Hierarchy & OS Diagnostics
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 2A: Linux Internals & OS Diagnostics (Days 7 to 11)**

---

## 🎯 Goal
Understand the Linux Filesystem Hierarchy Standard (FHS), master key directories (`/etc`, `/var`, `/proc`, `/dev`), extract live kernel and hardware telemetry via `/proc`, and solve OverTheWire Bandit Levels 0 through 5.

---

## 📂 Linux Filesystem Hierarchy Standard (FHS) Overview

```text
/ (Root)
├── bin -> usr/bin       # Essential user binaries (ls, cat, cp, mkdir, bash)
├── sbin -> usr/sbin     # Essential system administrator binaries (iptables, fdisk, reboot)
├── etc/                 # System-wide configuration files (nginx.conf, passwd, hosts, fstab)
├── var/                 # Variable data files: logs (/var/log), databases, spool queues
├── proc/                # Virtual pseudo-filesystem: kernel runtime state, processes, RAM, CPU
├── sys/                 # Modern sysfs: kernel device drivers and hardware subsystem knobs
├── dev/                 # Device nodes representing physical/virtual hardware (null, zero, sda)
├── tmp/                 # Volatile temporary scratch space (wiped on reboot)
├── opt/                 # Optional add-on third-party software packages (e.g. /opt/google)
├── home/                # User personal home directories (/home/ubuntu, /home/shyam)
├── root/                # Superuser root personal home directory
└── usr/                 # User utilities, libraries, and documentation
```

### The "Big 4" DevOps Directories

| Directory | What Lives There | Real-World DevOps Incident Example |
| :--- | :--- | :--- |
| **`/etc`** | Configuration files | Misconfigured `/etc/nginx/sites-available/default` causing HTTP 502 bad gateway. |
| **`/var`** | Logs & runtime state | Unrotated logs in `/var/log/syslog` filling root disk to 100%, causing Kubernetes pods to evict. |
| **`/proc`** | Kernel state in RAM | Investigating high CPU steal time via `/proc/stat` or OOM kills in `/proc/meminfo`. |
| **`/dev`** | Device drivers & null sinks | Redirecting noisy cron job outputs to `/dev/null` (`> /dev/null 2>&1`). |

---

## 🛠️ Virtual Filesystem Deep-Dive: `/proc`

The `/proc` directory contains no physical files on disk — it is a virtual pseudo-filesystem generated on-the-fly by the Linux kernel directly from memory.

### 1. `inspect_proc.py`
A cross-platform Linux kernel inspector script:
- Parses `/proc/meminfo` converting raw kB to MB and computing real available memory (subtracting buffers/caches).
- Parses `/proc/cpuinfo` extracting model name and logical core topology.
- Parses `/proc/loadavg` calculating 1-min, 5-min, and 15-min load metrics.

**Usage:**
```bash
# Run diagnostics on Linux / WSL2
python inspect_proc.py

# Run verification test suite
python inspect_proc.py --test
```

---

## 🎮 OverTheWire Bandit Levels 0 → 5 (Command Log)

| Level | Objective | Key Command(s) | Lesson Learned |
| :---: | :--- | :--- | :--- |
| **Bandit 0** | Connect to server via SSH | `ssh bandit0@bandit.labs.overthewire.org -p 2220` | Connecting to remote bastion hosts over custom non-standard ports. |
| **Bandit 0 → 1** | Read password from `readme` | `cat readme` | Basic file viewing with `cat`. |
| **Bandit 1 → 2** | Read file named `-` | `cat ./-` (or `cat < -`) | Leading dash `-` confuses commands into expecting a flag; prefixing `./` anchors relative path. |
| **Bandit 2 → 3** | Read file with spaces in name | `cat "spaces in this filename"` (or with `\ ` escape) | Shell word-splitting requires quotes or backslash escapes. |
| **Bandit 3 → 4** | Read hidden file in `inhere` | `cd inhere && ls -la && cat .hidden` | Dot-files (`.hidden`) are excluded from default `ls`; `ls -la` displays hidden entries. |
| **Bandit 4 → 5** | Find human-readable file in `-fileXX` | `file inhere/* \| grep ASCII` | Using `file` command to determine MIME/encoding without opening binary gibberish. |

---

## 💡 Key Engineering Takeaways
1. **Everything in Linux is a file**: Hard drives (`/dev/sda`), processes (`/proc/1234/`), network sockets, and input streams are accessed via uniform file descriptor abstractions.
2. **MemFree vs MemAvailable**: Never judge Linux memory health by `MemFree` alone. Linux aggressively caches disk blocks into RAM (`Cached`). `MemAvailable` is the true metric of memory immediately reclaimable by applications.
