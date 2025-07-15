
import pandas as pd
from datetime import datetime
import pytz
import random
import csv

# Step 1: Load and clean the data
df = pd.read_csv("conversions.csv")
df = df.rename(columns={"google_click_id (gclid)": "gclid"})
df_valid = df[(df["gclid"].notnull()) & (df["conversion_value"] > 0)]

# Step 2: Format timestamps
def format_timestamp(ts):
    dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    pst = pytz.timezone("America/Los_Angeles")
    dt = pst.localize(dt)
    return dt.isoformat()

df_valid["formatted_time"] = df_valid["timestamp"].apply(format_timestamp)

# Step 3: Add optional value bucket
df_valid["value_bucket"] = df_valid["conversion_value"].apply(lambda x: "high" if x >= 100 else "low")

# Step 4: Prepare simulated payloads
conversion_action_id = "customers/1234567890/conversionActions/offline_purchase"
currency = "USD"

payloads = []
for _, row in df_valid.iterrows():
    payload = {
        "gclid": row["gclid"],
        "conversion_action": conversion_action_id,
        "conversion_date_time": row["formatted_time"],
        "conversion_value": row["conversion_value"],
        "currency_code": currency
    }
    payloads.append(payload)

# Step 5: Simulate API upload responses
upload_results = []
for record in payloads:
    success = random.random() < 0.9
    result = {
        "gclid": record["gclid"],
        "success": success,
        "error": None if success else "Simulated API failure"
    }
    upload_results.append(result)

# Step 6: Output upload report to CSV
with open("conversion_upload_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["gclid", "success", "error"])
    writer.writeheader()
    for result in upload_results:
        writer.writerow(result)

# Step 7: Print summary stats
total_uploaded = sum(r["success"] for r in upload_results)
total_failed = len(upload_results) - total_uploaded

print(f"Conversion Action Used: {conversion_action_id}")
print(f"Total Uploaded: {total_uploaded}")
print(f"Total Failed: {total_failed}")
