import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# # очистить таблицу
# cursor.execute("DELETE FROM admin_page_app_employer")

# # удалить таблицу
# cursor.execute('''DROP TABLE IF EXISTS admin_page_app_order''')

# Создать новую таблицу
# cursor.execute('''CREATE TABLE admin_page_app_order(
#                     id INTEGER PRIMARY KEY,
#                     is_active BOOLEAN DEFAULT TRUE,
#                     category TEXT,
#                     description TEXT,
#                     image TEXT,
#                     location TEXT,
#                     location_link TEXT,
#                     price INTEGER,
#                     owner_id INTEGER
#                     )''')


# conn.commit()

conn.close()