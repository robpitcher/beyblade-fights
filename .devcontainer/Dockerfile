FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /workspace

# Install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    git \
    && apt-get clean

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code from the src directory
COPY src/ ./src

# Set environment variables for Flask
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose Flask's default port
EXPOSE 5000

# Default command to run Flask app
CMD ["flask", "run"]