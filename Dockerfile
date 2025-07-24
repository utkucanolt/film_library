# Python 3.11 image
FROM python:3.11

# Çalışma dizini
WORKDIR /code

# Gerekli dosyaları kopyala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Tüm kodu ekle
COPY . .

# Başlangıç komutu (manual başlatma yaparsın)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
