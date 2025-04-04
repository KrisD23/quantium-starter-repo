import pandas as pd

# List of actual CSV filenames
files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']


df = pd.concat(
    [
        pd.read_csv(file)
        .query("product.str.lower() == 'pink morsel'")  
        .assign(
            price=lambda x: x["price"].str.replace("$", "", regex=False).astype(float),  
            sales=lambda x: x["quantity"] * x["price"]  
        )[['sales', 'date', 'region']]  
        for file in files
    ],
    ignore_index=True
)


df.to_csv('clean_data.csv', index=False)

print("File created successfully")



