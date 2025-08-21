# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Download the model during the build process
# This ensures the model is included in the final container
RUN python training/download_model.py

# Tell the container to run app.py when it starts
# Gunicorn is a production-ready web server
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]