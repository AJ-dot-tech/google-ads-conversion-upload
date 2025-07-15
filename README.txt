
# Google Ads Conversion Upload Script (Simulated)

## Overview
This Python script simulates uploading offline conversions to Google Ads using cleaned data from a CSV.

## What It Does
1. Reads a `conversions.csv` file with GCLIDs, values, and timestamps.
2. Filters valid rows (non-null GCLID and value > 0).
3. Formats timestamps to the required Google Ads format.
4. Buckets conversions by value (e.g., high vs low).
5. Simulates the upload to Google Ads (random success/failure).
6. Outputs a detailed report of which conversions succeeded or failed.
7. Prints summary stats and conversion action ID used.

## How to Run
```bash
python script.py
```

Make sure `conversions.csv` is in the same folder.

## Notes
- The upload step is simulated — no real API calls are made.
- A real integration would replace the simulation block with an authenticated `google-ads` API client.

## Output
- `conversion_upload_report.csv`: a CSV log of each upload attempt (success or error)
- Terminal output with summary stats
