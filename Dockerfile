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
    python manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.create_superuser('sujeet', password='sujeetclinic') \
if not User.objects.filter(username='sujeet').exists() else None" && \
    gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
