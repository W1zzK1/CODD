import psycopg2

# Параметры подключения
db_name = "mydatabase"
db_user = "myuser"
db_password = "mypassword"
db_host = "localhost"  # или IP-адрес контейнера, если он не на локальной машине
db_port = "5432"

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        return connection
    except psycopg2.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None