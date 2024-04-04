from PIL import Image, ImageDraw, ImageFont
import telebot
import os

# Инициализация бота
bot = telebot.TeleBot("6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8")

# Функция для создания изображения с текстом
def create_image_with_text(text):
    # Создаем изображение с белым фоном, размером 400x200
    image = Image.new("RGB", (400, 200), "white")

    # Получаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(image)

    # Загружаем шрифт
    font = ImageFont.truetype("arial.ttf", 20)

    # Получаем размеры текста
    text_width, text_height = draw.textsize(text, font=font)

    # Вычисляем координаты для центрирования текста
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2

    # Рисуем текст на изображении
    draw.text((x, y), text, fill="black", font=font)

    return image

# Обработчик команды /send_image
@bot.message_handler(commands=['send_image'])
def handle_send_image(message):
    # Создаем изображение с текстом
    text = "Пример текста на изображении"
    image = create_image_with_text(text)

    # Сохраняем временное изображение
    image_path = "temp_image.png"
    image.save(image_path)

    # Отправляем изображение пользователю
    with open(image_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

    # Удаляем временное изображение
    os.remove(image_path)

# Запуск бота
bot.polling()
