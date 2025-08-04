FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY vendor /vendor
RUN pip install --no-cache-dir --no-index --find-links=/vendor -r requirements.txt

COPY . .

CMD ["python", "app.py"]