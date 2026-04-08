# Imagen pesada (completa)
FROM python:3.10

WORKDIR /app

# Copiamos todo de un solo golpe
COPY . .

# Instalamos sin optimizar
RUN pip install -r requirements.txt

CMD ["python", "script.py"]
