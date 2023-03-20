FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Set Django environment variables
ENV DJANGO_SETTINGS_MODULE=placementManagement.settings.production

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate

# Expose port
EXPOSE 8000

# Start the application
CMD ["gunicorn", "app/placementManagement.wsgi", "-b", "0.0.0.0:8000"]
