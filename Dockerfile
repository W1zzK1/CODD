# Используем официальный образ PostgreSQL с поддержкой PostGIS
FROM postgis/postgis:latest

# Устанавливаем переменные окружения для конфигурации базы данных
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Копируем скрипт инициализации в контейнер
COPY init.sql /docker-entrypoint-initdb.d/

# Открываем порт 5432 для доступа к базе данных
EXPOSE 5432