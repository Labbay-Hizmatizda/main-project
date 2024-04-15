import requests

# URL, куда отправляется запрос
url = 'https://example.com/api/create_record'

# Значения для полей
data = {
    'name': 'Abdurahmon',
}

# Значение для поля imagefield (URL изображения из базы данных)
image_url = 'https://example.com/path/to/image.jpg'
image_response = requests.get(image_url)

# Проверка статуса ответа на запрос изображения
if image_response.status_code == 200:
    # Параметры формы (изображение и другие поля)
    files = {
        'imagefield': ('image.jpg', image_response.content),  # content содержит содержимое изображения
    }

    # Отправка POST-запроса
    response = requests.post(url, data=data, files=files)

    # Проверка статуса ответа
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code)
else:
    print("Error fetching image:", image_response.status_code)
