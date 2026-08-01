# Project: Serverless URL Shortener on AWS

## Why I Built This
I wanted to build a practical serverless application on AWS to understand how API Gateway, Lambda, and DynamoDB interact without relying on bloated frameworks.

---

## Architecture
```text
Client ──► API Gateway (HTTP API) ──► Lambda (Python 3.11) ──► DynamoDB
```

1. **Shorten URL (`POST /shorten`):**
   * Receives long URL.
   * Generates a 7-character Base62 hash.
   * Writes to DynamoDB with a TTL timestamp (e.g. expires in 30 days).
   * Returns short URL.

2. **Redirect (`GET /{short_code}`):**
   * Looks up the short code in DynamoDB.
   * Increments the click counter atomically.
   * Returns `HTTP 302 Found` with `Location: <long_url>`.

---

## Big Takeaways
* **HTTP 302 vs 301:** I initially used HTTP 301, but browsers cached the redirect, so repeated clicks never hit my Lambda and didn't count in analytics! Switched to 302 with `Cache-Control: no-cache`.
* **DynamoDB TTL:** Native TTL deletes old records automatically for free without running any cleanup cron jobs.
