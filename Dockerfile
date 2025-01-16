# auth_service/Dockerfile

FROM python:3.10-slim

# Set a working directory in the container
WORKDIR /app

# Copy requirements into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual application code
COPY app /app/app

# Expose port 8001 if you want (optional, but good for clarity)
EXPOSE 8001

# Command to run the service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
