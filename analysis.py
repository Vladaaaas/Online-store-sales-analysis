import pandas as pd
import numpy as np
from numpy.ma.extras import unique

pd.set_option("display.max_columns", None)
pd.set_option('display.width', None)

data = pd.read_csv("dales_data.csv")

#Converting the column to datetime
data['order_date'] = pd.to_datetime(data['order_date'])
data['order_date'] = data['order_date'].dt.strftime("%Y.%m.%d")

#individual expenses
data['amount'] = data['quantity'] * data['price']


#total revenue - общая выручка
total_rev = sum(data['amount'])

#average receipt
average_receipt = total_rev / len(data)

#number of orders per day
orders_day = data.groupby('order_date')['order_id'].count().reset_index()
orders_day = orders_day.rename(columns={'order_id':'count_orders'})

#unique customers
unique_customers = unique(data['customer_id'])

#cumulative revenue
cum_rev = data['amount'].cumsum()

#top 5 products by sales
prod = data.groupby('product')['amount'].sum().sort_values(ascending=False).reset_index()
top5 = prod['product'].head(5).tolist()

#print(data)
print(f"Total revenue for the last 5 months - {total_rev}\n")
print(f"Average receipt for each purchase - {average_receipt}\n")
print(f"Number of orders per day - {orders_day}\n")
print(f"Unique customers - {unique_customers}\n")
print(f"Сumulative revenue for the last 5 months - {cum_rev}\n")
print(f"Top 5 products by sales - {top5[0]}, {top5[1]}, {top5[2]}, {top5[3]}, {top5[4]}\n")
