# Используем минимальный Python 3.12 образ
FROM python:3.12-slim

# Настройки Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория в контейнере
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.in requirements.in

# Устанавливаем pip-tools, генерируем requirements.txt и ставим зависимости
RUN pip install --no-cache-dir pip-tools && \
    pip-compile requirements.in --output-file requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Команда запуска приложения
CMD ["python", "-m", "src.main"]