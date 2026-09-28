# Day 8: Linux Permissions, Ownership & Security Auditing
> **DevOps & Cloud Engineer 36-Day Master Plan — Candidate: Shyam Kumar D**  
> **Phase 2A: Linux Internals & OS Diagnostics (Days 7 to 11)**

---

## 🎯 Goal
Master the Linux discretionary access control (DAC) model, calculate octal permission math (`755`, `644`, `600`), enforce least-privilege file ownership with `chmod` and `chown`, audit systems for dangerous world-writable permissions, and solve OverTheWire Bandit Levels 6 through 10.

---

## 🔐 The Linux Permission Model

Every file and directory has 3 distinct entity scopes and 3 permission bits:

```text
-  rwx  r-x  r--   1 ubuntu devops 4096 Sep 28 10:00 deploy.sh
│  ───  ───  ───
│   │    │    │
│   │    │    └── Other (World) Permissions: r-- (Read Only)
│   │    └─────── Group (devops) Permissions: r-x (Read & Execute)
│   └──────────── User (Owner: ubuntu) Permissions: rwx (Read, Write, Execute)
└──────────────── File Type: '-' = regular file, 'd' = directory, 'l' = symlink
```

### Octal Binary Math Matrix

| Permission | Symbol | Binary Bit | Decimal Value | Meaning for Files | Meaning for Directories |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **Read** | `r` | `100` | **4** | View file contents (`cat`) | List directory contents (`ls`) |
| **Write** | `w` | `010` | **2** | Modify/overwrite file | Create, delete, or rename files within directory |
| **Execute** | `x` | `001` | **1** | Run as binary/script | Enter/traverse directory (`cd`) |

### Common Production Permission Patterns

| Octal | Permissions | Common DevOps Use Case |
| :---: | :---: | :--- |
| **`600`** | `rw-------` | SSH private keys (`~/.ssh/id_rsa`), AWS `.pem` keys, production `.env` secrets. |
| **`644`** | `rw-r--r--` | Standard public configuration files (`nginx.conf`), static assets, logs. |
| **`700`** | `rwx------` | User's private `~/.ssh` directory, root home directory `/root`. |
| **`755`** | `rwxr-xr-x` | Executable bash/python scripts (`/usr/local/bin`), public web root directories. |
| **`777`** | `rwxrwxrwx` | **SECURITY RED FLAG**: Anyone can read, overwrite, or delete. Never permitted in production! |

---

## 🛠️ Security Audit Utility: `perm_auditor.py`

Audits directory trees for compliance against zero-trust DevOps security baselines:
- **World-Writable Detection**: Flags files with `mode & 0o002` (vulnerable to tampering).
- **Credential Exposure**: Ensures SSH keys (`id_rsa`, `.pem`) and `.env` files are locked down to `600` or stricter.
- **Config Sanity**: Flags executable bits erroneously set on static configs or markdown notes.

**Usage:**
```bash
# Audit target directory
python perm_auditor.py --dir /opt/myapp

# Run verification tests
python perm_auditor.py --test
```

---

## 🎮 OverTheWire Bandit Levels 6 → 10 (Command Log)

| Level | Objective | Key Command(s) | Lesson Learned |
| :---: | :--- | :--- | :--- |
| **Bandit 6 → 7** | Find file owned by `bandit7`, group `bandit6`, size 33 bytes | `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` | Using `find` with user, group, size filters and discarding stderr permission errors (`2>/dev/null`). |
| **Bandit 7 → 8** | Find password next to word `millionth` | `grep "millionth" data.txt` | Fast text extraction from large data files using `grep`. |
| **Bandit 8 → 9** | Find only line that occurs once | `sort data.txt \| uniq -u` | `uniq` requires sorted input (`sort`) to find unique unrepeated lines. |
| **Bandit 9 → 10** | Extract human-readable string preceded by `=` | `strings data.txt \| grep "===="` | Extracting ASCII strings from compiled/binary files using `strings`. |
| **Bandit 10 → 11** | Decode Base64 encoded password | `base64 -d data.txt` | Decoding base64 encoded credentials in terminal. |

---

## 💡 Key Engineering Takeaways
1. **Directory execute bit (`x`) is traversal**: Without the execute bit on a directory (`chmod -x mydir`), users cannot `cd` into it or access any file inside, even if individual files have `644` read permissions.
2. **Discarding Permission Denied with `2>/dev/null`**: Searching the root filesystem (`find /`) as non-root floods stderr with hundreds of `Permission denied` lines. Redirecting descriptor 2 to `/dev/null` silences errors and leaves clean actionable output.
3. **SSH Client Permission Refusal**: OpenSSH actively refuses to connect (`Permissions 0644 for 'id_rsa' are too open`) if private keys have group or world permissions. They must always be `chmod 600 id_rsa`.
