
# Google Ads Conversion Upload Script (Simulated)

## Overview
This Python script simulates uploading offline conversions to Google Ads. It reads a CSV, processes and enriches the data, and generates a report of simulated successes and failures.

---

## Features
- Reads `conversions.csv` and filters valid rows (`gclid` present and `conversion_value > 0`)
- Formats timestamps to Google Ads-compatible format
- Adds a value bucket (`high` if ≥ $100, `low` otherwise)
- Simulates API upload (90% success rate)
- Outputs a detailed success/failure report as CSV
- Prints summary stats to terminal

---

## Files Included
| File                          | Description                                     |
|-------------------------------|-------------------------------------------------|
| `script.py`                   | Main Python script                             |
| `cleaned_conversions.csv`     | Output of cleaned + enriched data              |
| `conversion_upload_report.csv`| Simulated API response log                     |
| `README.md`                   | This readme file                               |

---

## How to Run

Make sure Python 3 and `pandas` are installed. Then:

```bash
python script.py
```

Place `conversions.csv` in the same folder before running.

---

## Output
- `conversion_upload_report.csv`: Log of simulated success/failure
- Summary printed to console:
  ```
  Conversion Action Used: customers/1234567890/conversionActions/offline_purchase
  Total Uploaded: 4
  Total Failed: 1
  ```

---

## Note
This script simulates Google Ads API behavior only. It does not use a real developer token or OAuth. To use in production:
- Replace the simulated upload block with `google-ads` API client code
- Add a `google-ads.yaml` config with your credentials

---

## Next Steps (for real-world usage)
- Enable the Google Ads API in Google Cloud
- Authenticate via OAuth2 to get a refresh token
- Replace the simulated response with `ConversionUploadService`
