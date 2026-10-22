import pandas as pd
import numpy as np

# Load the logistics dataset
try:
    df = pd.read_csv('swiftexpress_deliveries.csv')
    print("Dataset loaded successfully from file.")
except FileNotFoundError:
    print("CSV file not found. Creating a sample dataset for demonstration.")
    sample_data = {
        'order_id': [101, 102, 103, 104, 105],
        'dispatch_time': ['2026-10-01 08:00:00', '2026-10-01 09:30:00', '2026-10-01 10:15:00', '2026-10-01 11:00:00', '2026-10-01 12:30:00'],
        'delivered_time': ['2026-10-01 09:10:00', '2026-10-01 11:00:00', '2026-10-01 11:45:00', '2026-10-01 13:15:00', '2026-10-01 13:30:00'],
        'delivery_delay_mins': [10, -5, 25, 0, 15]
    }
    df = pd.DataFrame(sample_data)

# Step 1: Check for missing values and fill them with the median delay
print("\n--- Step 1: Data Cleaning ---")
print("Checking missing values:")
print(df.isnull().sum())

median_delay = df['delivery_delay_mins'].median()
df['delivery_delay_mins'] = df['delivery_delay_mins'].fillna(median_delay)

# Step 2: Convert date columns to datetime and calculate actual transit time in minutes
print("\n--- Step 2: Feature Engineering ---")
df['dispatch_time'] = pd.to_datetime(df['dispatch_time'])
df['delivered_time'] = pd.to_datetime(df['delivered_time'])

# Calculate transit time duration
df['actual_transit_mins'] = (df['delivered_time'] - df['dispatch_time']).dt.total_seconds() / 60

# Step 3: Compute key performance indicators (KPIs)
print("\n--- Step 3: KPI Calculations ---")
average_delay = df['delivery_delay_mins'].mean()

# On-Time Delivery Rate: percentage of orders with delay <= 0 minutes
on_time_count = (df['delivery_delay_mins'] <= 0).sum()
total_orders = len(df)
otdr_percentage = (on_time_count / total_orders) * 100

# Display final summary results
print("========================================")
print("      LOGISTICS PERFORMANCE SUMMARY     ")
print("========================================")
print(f"Average Transit Delay        : {average_delay:.2f} mins")
print(f"On-Time Delivery Rate (OTDR) : {otdr_percentage:.2f}%")
print("========================================")

# Step 4: Save the cleaned data to a new CSV file for export
output_filename = 'cleaned_logistics_data.csv'
df.to_csv(output_filename, index=False)
print(f"\nCleaned data successfully saved as '{output_filename}'. Ready to download!")
