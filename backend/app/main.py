import os
import requests
from config import BASE_URL, WB_API_TOKEN

# Заголовки для авторизации
headers = {"Authorization": WB_API_TOKEN}

response = requests.get(f"{BASE_URL}/orders", headers=headers)

if response.status_code == 200:
    print("Подключение к API успешно!")
    print(response.json())  # вывод первых данных
else:
    print("Ошибка подключения:", response.status_code, response.text)
