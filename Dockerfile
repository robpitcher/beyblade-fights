# Use the latest Python version
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements.txt first for caching purposes
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY src/ .

# Set environment variables
ENV FLASK_APP=app.py

# Expose the application port
EXPOSE 5000

# Command to run your Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
