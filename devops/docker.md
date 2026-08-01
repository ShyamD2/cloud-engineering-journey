# Docker Notes & Multi-Stage Builds

Notes on writing clean Dockerfiles, keeping container images tiny, and securing runtimes.

---

## Multi-Stage Build Template (Python FastAPI / Flask)
Don't ship compilers, gcc, and build tools into your production images. Build wheels in a builder stage and copy only clean artifacts into the final stage:

```dockerfile
# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Clean Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app

# Create a non-root user (security best practice)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy installed packages from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:8080/health || exit 1

CMD ["python", "app.py"]
```

---

## Docker Gotchas
* **Running as root:** Default containers run as root UID 0. If there is a container escape bug, the attacker has root on your host. Always add `USER nonroot`.
* **Layer caching:** Put `COPY requirements.txt .` before `COPY . .`. That way, when you change application code, Docker doesn't re-download all your pip packages from scratch.
* **Scan for vulnerabilities:** Run `trivy image my-image:tag` before pushing to Docker Hub or ECR.
