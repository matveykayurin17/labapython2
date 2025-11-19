# Используем официальный Python образ
FROM python:3.12-slim

# Не кешируем pyc, ускоряем контейнер
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем только файлы зависимостей (ускоряет сборку)
COPY requirements.txt pyproject.toml uv.lock ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt || true

# Копируем весь проект внутрь контейнера
COPY . .

# Запуск приложения
CMD ["python", "src/main.py"]