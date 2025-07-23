import pandas as pd
import random
from datetime import datetime, timedelta

#number of orders
num_orders = 8000

#list of products and their prices
products = {
    "phone": 400,
    "laptop": 800,
    "ipad": 550,
    "watch": 300,
    "TV": 880,
    "mouse": 50
}

#list of products
products_name = list(products.keys())

#Generate random dates (for the last 180 days)
start_date = datetime.today() - timedelta(days=180)
dates = [start_date + timedelta(days=random.randint(0, 179)) for _ in range(num_orders)]

#Orders generation
data = {
    "order_id": [800 + i for i in range(num_orders)],
    "customer_id": [f"P{random.randint(1, 600):03}" for i in range(num_orders)],
    "order_date": dates,
    "product": [random.choice(products_name) for i in range(num_orders)],
    "quantity": [],
    "price": []
}
# Генерация quantity и price с выбросами
for i in range(num_orders):
    product = data["product"][i]
    base_price = products[product]

    # 8% заказов — выбросы
    if random.random() < 0.08:
        # Выброс в количестве (заказали много штук)
        quantity = random.randint(10, 50)

        # Выброс в цене (например, неверная цена или VIP-продажа)
        price = base_price * random.uniform(2.0, 4.0)
    else:
        quantity = random.randint(1, 5)
        price = base_price * random.uniform(0.95, 1.05)

    data["quantity"].append(quantity)
    data["price"].append(round(price, 2))

#Add price
#data["price"] = [products[i] for i in data["product"]]

#To create DataFrame
df = pd.DataFrame(data)

df.to_csv("order_data.csv", index=False)


print(df)
