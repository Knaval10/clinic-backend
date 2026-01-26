FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Entrypoint: run migrations, collectstatic, create superuser, start Gunicorn
CMD python -c "import os, django; from django.contrib.auth import get_user_model; \
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); \
User=get_user_model(); \
User.objects.create_superuser('sujeet', password='sujeetclinic') if not User.objects.filter(username='sujeet').exists() else None" && \
python manage.py migrate && \
python manage.py collectstatic --noinput && \
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
