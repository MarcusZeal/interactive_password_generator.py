# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
# RUN pip install -r requirements.txt

# Default to running the interactive script
CMD ["python", "interactive_password_generator.py"]
