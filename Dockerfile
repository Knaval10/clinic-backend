# Use official Python slim image
FROM python:3.11-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependencies first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Automatically create superuser without email
RUN python -c "from django.contrib.auth import get_user_model; import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings'); django.setup(); User=get_user_model(); \
User.objects.create_superuser('sujeet', password='sujeetclinic') if not User.objects.filter(username='sujeet').exists() else None"

# Expose port (Render uses $PORT)
EXPOSE 8000

# Start Gunicorn server
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
