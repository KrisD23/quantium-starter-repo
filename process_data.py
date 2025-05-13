import pandas as pd
import os

# Static constants path
data_folder = "data"
csv_files=["daily_sales_data_0.csv","daily_sales_data_1.csv","daily_sales_data_2.csv"]

# Read data and combine
df_list = [pd.read_csv(os.path.join(data_folder,file)) for file in csv_files]
combined_df = pd.concat(df_list,ignore_index=True)

# Processing data
pink_df = combined_df[combined_df["product"].str.lower() == "pink morsel"].copy()
pink_df["price"] = pink_df["price"].replace('[\$,]', '', regex=True).astype(float)
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# rename columns for required output
output_df = pink_df[["Sales", "date", "region"]]
output_df = output_df.rename(columns={"date": "Date", "region": "Region"})

# Save to CSV
output_df.to_csv("processed.csv", index=False)
print("Done Saved as processed.csv")




