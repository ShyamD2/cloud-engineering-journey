# Kubernetes Notes & Core Concepts

Kubernetes can feel overwhelming at first. Here is the mental model that helped me make sense of it.

---

## The Core Mental Model
* **Pod:** The smallest unit. Runs one or more containers sharing network and storage.
* **Deployment:** Manages Pod replicas, handles rolling updates, and automatically replaces dead pods.
* **Service:** Gives pods a stable IP address and handles load balancing across replicas (because Pod IPs change every time they restart).
* **Ingress:** The front door. Routes external HTTP/HTTPS traffic to the right Service based on domain name or path.

---

## Always Set Requests and Limits
If you don't specify resource requests and limits, one runaway pod can consume all memory on a node and cause Kubernetes to kill other critical services:

```yaml
resources:
  requests:
    cpu: "100m"     # 0.1 CPU core
    memory: "128Mi"
  limits:
    cpu: "500m"     # 0.5 CPU core
    memory: "256Mi" # Will be OOMKilled if it exceeds this
```

---

## Probes You Need to Know
* `livenessProbe`: "Is my app dead?" If this fails, Kubernetes restarts the pod.
* `readinessProbe`: "Is my app ready for traffic?" If this fails, Kubernetes removes the pod from the Service load balancer so users don't get 502/503 errors while it's warming up.
