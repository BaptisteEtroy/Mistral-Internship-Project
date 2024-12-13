# Start from a slim Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create a non-root user for security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "Mistral:app", "--host", "0.0.0.0", "--port", "8000"]