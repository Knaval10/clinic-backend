FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies first
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose Render port
EXPOSE 10000

# Run migrations, collect static, create superuser, then start Gunicorn
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then \
        python manage.py createsuperuser --noinput || true; \
    fi && \
    gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
