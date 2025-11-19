FROM python:3.12-slim

# Отключаем лишние .pyc-файлы и включаем прямой вывод
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt pyproject.toml uv.lock ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt || true

# Копируем весь проект
COPY . .

# Запуск проекта как пакета
CMD ["python", "-m", "src.main"]