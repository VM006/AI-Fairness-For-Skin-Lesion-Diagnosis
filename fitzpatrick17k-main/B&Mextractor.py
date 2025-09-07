# Code for extracting benign and malignant samples from fitzpatrick17k.csv
# 07/09/2025

import pandas as pd

# Read the CSV file
df = pd.read_csv('fitzpatrick17k.csv')

# Filter rows where nine_partition_label contains 'benign' or 'malignant'
filtered_df = df[df['nine_partition_label'].str.contains('benign|malignant', case=False, na=False)]

# Save the filtered data to a new CSV if needed
filtered_df.to_csv('fitzpatrick17k_B&Monly.csv', index=False)

# Display the first few rows
print(f"Found {len(filtered_df)} rows with benign or malignant labels")
print(filtered_df.head())