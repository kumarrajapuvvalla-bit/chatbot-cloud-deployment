FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app

# Expose the port that the Flask app listens on
EXPOSE 8080

# Command to run the application
CMD ["python", "app/main.py"]
