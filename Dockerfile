# ---------- BASE IMAGE ----------
FROM python:3.12-slim

# ---------- ENVIRONMENT VARIABLES ----------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---------- WORKING DIRECTORY ----------
WORKDIR /app

# ---------- SYSTEM DEPENDENCIES ----------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# ---------- PYTHON DEPENDENCIES ----------
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ---------- COPY PROJECT ----------
COPY . /app/

# ---------- EXPOSE PORT ----------
# Render injects $PORT at runtime
EXPOSE 10000

# ---------- RUN DJANGO SERVER ----------
# Collect static files at runtime, then start Gunicorn
CMD bash -c "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
