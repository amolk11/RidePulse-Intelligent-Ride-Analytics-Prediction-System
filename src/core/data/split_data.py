import pandas as pd
import os

# Load dataset
df = pd.read_csv("dataset/raw/ncr_ride_bookings.csv")

# Sort by time
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
df = df.sort_values(by='Datetime')

# Drop date and time columns
df = df.drop(columns=['Date', 'Time'])

# Split
train = df.iloc[:100000]
test = df.iloc[100000:110000]
retrain = df.iloc[110000:]

# Create output folder
os.makedirs("dataset/processed", exist_ok=True)

# Save
train.to_csv("dataset/processed/train.csv", index=False)
test.to_csv("dataset/processed/test.csv", index=False)
retrain.to_csv("dataset/processed/retrain.csv", index=False)

print("Data split completed!")