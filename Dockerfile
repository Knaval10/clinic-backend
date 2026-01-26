# Use official Python slim image
FROM python:3.11-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose port (Render uses $PORT)
EXPOSE 8000

# Entrypoint script to handle migrations, static files, superuser, and start server
CMD python -c "from django.contrib.auth import get_user_model; import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); \
User=get_user_model(); User.objects.create_superuser('sujeet', password='sujeetclinic') if not User.objects.filter(username='sujeet').exists() else None" && \
python manage.py collectstatic --noinput && \
python manage.py migrate && \
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
