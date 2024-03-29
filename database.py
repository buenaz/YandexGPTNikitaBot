import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="log_file.txt",
    filemode="w",
)

def create_connection():
    logging.info("Соединение с БД")
    connection = None
    try:
        connection = sqlite3.connect('users.db')
        logging.info("Подключение к базе данных успешно установлено")
    except Error as e:
        logging.info(f"Ошибка при подключении к базе данных: {e}")
    return connection


def close_connection(connection):
    logging.info("Разрыв соединения с БД")
    if connection:
        connection.close()
        logging.info("Подключение к базе данных закрыто")


def create_table():
    logging.info("Создание таблицы")
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS users (
                text TEXT,
                answer TEXT
            )
            """
            cursor.execute(query)
            connection.commit()
            logging.info("Таблица успешно создана")
        except Error as e:
            logging.info(f"Ошибка при создании таблицы: {e}")
        finally:
            cursor.close()
            close_connection(connection)


def create(text, answer):
    logging.info("Создание записи в БД")
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users VALUES (?, ?)"
            values = (text, answer)
            cursor.execute(query, values)
            connection.commit()
            logging.info("Запись успешно записана")
            return cursor.lastrowid
        except Error as e:
            logging.info(f"Ошибка при создании таблицы: {e}")
        finally:
            cursor.close()
            close_connection(connection)

create_table()