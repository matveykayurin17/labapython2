FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt pyproject.toml uv.lock ./


RUN pip install --no-cache-dir -r requirements.txt || true


COPY . .


CMD ["python", "-m", "src.main"]