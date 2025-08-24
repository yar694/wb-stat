import requests
import pandas as pd
from config import WB_API_TOKEN, BASE_URL
import os

# Создаём папку data, если её нет
if not os.path.exists("data"):
    os.makedirs("data")

headers = {"Authorization": WB_API_TOKEN}

def get_orders():
    """Получаем заказы"""
    url = f"{BASE_URL}/orders"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orders = response.json().get("orders", [])
        print(f"Загружено заказов: {len(orders)}")
        return orders
    else:
        print("Ошибка при получении заказов:", response.status_code, response.text)
        return []

def get_sales():
    """Получаем продажи"""
    url = f"{BASE_URL}/sales"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sales = response.json().get("sales", [])
        print(f"Загружено продаж: {len(sales)}")
        return sales
    else:
        print("Ошибка при получении продаж:", response.status_code, response.text)
        return []

# Получаем данные
orders = get_orders()
sales = get_sales()

# Сохраняем в DataFrame
df_orders = pd.DataFrame(orders)
df_sales = pd.DataFrame(sales)

# Сохраняем в CSV
df_orders.to_csv("data/orders.csv", index=False)
df_sales.to_csv("data/sales.csv", index=False)

print("Данные сохранены в папке data")
