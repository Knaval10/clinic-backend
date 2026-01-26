# Base image
FROM python:3.11-slim

# Prevent pyc files & buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose port for Render
EXPOSE 8000

# Run migrations, collectstatic, create superuser, start server
CMD python -c "from django.contrib.auth import get_user_model; import django, os; \
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); \
User=get_user_model(); User.objects.create_superuser('sujeet', password='sujeetclinic') \
if not User.objects.filter(username='sujeet').exists() else None" && \
python manage.py collectstatic --noinput && \
python manage.py migrate && \
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
