# Use official Python slim image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev libjpeg-dev zlib1g-dev libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files at runtime instead of build
# Render recommends running collectstatic as a start command

# Expose port
EXPOSE 10000  # Render uses $PORT variable, we will use CMD below

# Run server
CMD bash -c "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
