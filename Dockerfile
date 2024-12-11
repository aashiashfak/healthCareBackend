FROM python:3.12-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set the working directory
WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy requirements.txt to the container
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy the Django application to the container
COPY . /app/

# Copy entrypoint.sh to the container and execute it.
COPY ./entrypoint.sh /

# Expose the Django application to serve HTTP requests.
EXPOSE 8000

# Run the Django application.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]