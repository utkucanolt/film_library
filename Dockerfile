# 1. Temel imaj
FROM python:3.11-slim

# 2. Çalışma dizini
WORKDIR /app

# 3. Sisteme git, paket listemizi ekle, bağımlılıkları kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Tüm kaynak kodu (app dosyaları + alembic) konteynıra kopyala
COPY . .

# 5. Ortam değişkenleri (Docker Compose içinde de verebilirsin)
ENV DATABASE_URL="postgresql://postgres:12345@db:5432/moviedb"

# 6. Alembic ile migrasyonları uygula, sonra uvicorn ile başlat
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]
