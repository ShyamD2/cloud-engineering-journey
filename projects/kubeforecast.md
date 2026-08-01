# Project: KubeForecast — Kubernetes Workload & Cost Optimizer

## Why This Matters
In Kubernetes, developers frequently guess resource requests (e.g. requesting 2 CPUs and 4GB RAM when the app only uses 100m CPU and 200MB). Over a whole cluster, this wastes huge amounts of cloud money on idle worker nodes.

## How It Works
* Collects P95 and P99 CPU and memory metrics from Prometheus.
* Correlates actual pod usage against configured requests and limits.
* Recommends safe, optimized request values to prevent both OOMKills and idle capacity waste.
