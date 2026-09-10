# Day 7 — Mini Build #1: Retail ETL Pipeline

Today's mini build turned into a full standalone project rather than a quick daily script, so it lives in its own repository instead of this folder.

**Full project, code, and documentation:**
👉 [github.com/akash3461/retail-etl-pipeline](https://github.com/akash3461/retail-etl-pipeline)

## What it does

Takes a raw 541,909-row retail transactions dataset and turns it into clean, validated, memory-optimized Parquet output — the full pipeline: Extract → Inspect → Clean → Transform → Validate → Optimize → Load.

## Highlights

- 536,639 final rows (5,268 duplicates + 2 invalid price records removed)
- Memory optimized through dtype downcasting and categorical encoding
- Structured logging throughout the pipeline run
- Data validated *after* cleaning, not just before

See the [project README](https://github.com/akash3461/retail-etl-pipeline#readme) for the full architecture, benchmarks, and how to run it.

---

*Part of the [100 Days of Data Engineering](../README.md) challenge — Day 7 of 100.*