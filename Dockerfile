# 1. Base image
FROM python:3.11-slim

# 2. Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Working directory
WORKDIR /app

# 4. Copy and install dependencies first
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the project
COPY . .

# 6. Expose the port Render expects
EXPOSE 10000

# 7. Run migrations, collectstatic, create superuser, then start Gunicorn
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    python manage.py shell -c "from django.contrib.auth import get_user_model; \
User=get_user_model(); \
User.objects.create_superuser('sujeet', password='sujeetclinic') \
if not User.objects.filter(username='sujeet').exists() else None" && \
    gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
