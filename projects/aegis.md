# Project: Aegis — Cloud Security & Governance Engine

## The Problem
In cloud environments, developers sometimes accidentally create public S3 buckets or open port 22 in a security group to test something quickly and forget to close it.

## What Aegis Does
Aegis is an automated event-driven compliance tool I built using Python, Boto3, and AWS EventBridge.
* Listens to AWS CloudTrail API events via EventBridge.
* When a new Security Group rule opens port 22 or 3389 to `0.0.0.0/0`, Aegis revokes the rule immediately and sends a notification.
* When a new S3 bucket is created without Block Public Access, Aegis enables Block Public Access automatically.

It turns passive security guidelines into active real-time guardrails.
