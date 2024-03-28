import json
import requests

# Заполнение массива данных:
data = [
    {"phone": "NUMBER", "text": "TEXT"},
    {"phone": "NUMBER", "text": "TEXT"}
]

# Разбиение массива на пакеты по 50 элементов:
chunks = [data[i:i + 50] for i in range(0, len(data), 50)]

# Адрес сервера OperSMS:
base_url = "http://83.69.139.182:8080/"

# Логин и пароль:
login = "LOGIN"
password = "PASSWORD"

for chunk in chunks:
    # Отправка запроса на сервер OperSMS:
    response = requests.post(base_url, data={
        "login": login,
        "password": password,
        "data": json.dumps(chunk)
    })

    # Получение ответа в формате JSON:
    result = response.json()

    # Извлечение request_id:
    request_id = result[0]['request_id']

    # Получение статуса отправленного сообщения:
    status_url = "http://83.69.139.182:8081/status"
    status_response = requests.post(status_url, data={
        "login": login,
        "password": password,
        "data": json.dumps([{"request_id": request_id}])
    })

    # Извлечение интересующих данных из ответа:
    status_result = status_response.json()
    state = status_result[0]['delivery-notification']['status'][0]['$']['state']

    """
    Кроме "state" (string) массив также содержит другую полезную информацию:
    "code" (integer),
    "delivered-date" (date Y-m-d H:i:s),
    "description" (string),
    "message-count" (integer),
    "ordinal" (integer)
    """
