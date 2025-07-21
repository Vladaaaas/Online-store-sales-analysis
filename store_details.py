import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

#number of orders
num_orders = 5000

#list of products and their prices
products = {
    "phone": 400,
    "laptop": 800,
    "ipad": 550,
    "watch": 300,
    "TV": 880,
}

#list of products
products_name = list(products.keys())

#Generate random dates (for the last 150 days)
start_date = datetime.today() - timedelta(days=150)
dates = [start_date + timedelta(days=random.randint(0, 149)) for _ in range(num_orders)]

#Orders generation
data = {
    "order_id": [800 + i for i in range(num_orders)],
    "customer_id": [f"P{random.randint(1, 400):03}" for i in range(num_orders)],
    "order_date": dates,
    "product": [random.choice(products_name) for i in range(num_orders)],
    "quntity": [random.randint(1, 4) for i in range(num_orders)],
}

#Add price
data["price"] = [products[i] for i in data["product"]]

#To create DataFrame
df = pd.DataFrame(data)

df.to_csv("dales_data.csv", index=False)


print(df.head())
