# Google Ads Conversion Upload Script (Simulated)

## 📝 Overview
This Python script simulates uploading offline conversions to Google Ads. It reads a CSV, processes and enriches the data, and generates a report of simulated successes and failures.

---

## 🚀 Features
- Reads `conversions.csv` and filters valid rows (`gclid` present and `conversion_value > 0`)
- Formats timestamps to Google Ads-compatible format
- Adds a value bucket (`high` if ≥ $100, `low` otherwise)
- Simulates API upload (90% success rate)
- Outputs a detailed success/failure report as CSV
- Prints summary stats to terminal

---

## 📁 Files Included
| File                          | Description                                     |
|-------------------------------|-------------------------------------------------|
| `script.py`                   | Main Python script                             |
| `cleaned_conversions.csv`     | Output of cleaned + enriched data              |
| `conversion_upload_report.csv`| Simulated API response log                     |
| `README.md`                   | This readme file                               |

---

## ▶️ How to Run

Make sure Python 3 and `pandas` are installed. Then:

```bash
python script.py
