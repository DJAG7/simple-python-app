# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Define the environment variable (this will be set in Kubernetes)
ENV OPENWEATHER_API_KEY=""

# Define the command to run the app
CMD ["python", "app.py"]
