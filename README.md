## Установка

1. Установка зависимостей:

    ```bash
    pip install -r requirements.txt
    ```

2. Сборка Docker образа для базы данных:

    ```bash
    docker build -t my-postgres-db .
    ```

3. Запуск Docker контейнера для базы данных:

    ```bash
    docker run -d -p 5432:5432 --name my-postgres-container my-postgres-db
    ```

4. Запуск FastAPI приложения:

    ```bash
    uvicorn app.main:app --reload
    ```

