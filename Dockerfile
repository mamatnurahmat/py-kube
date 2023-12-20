# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable for Kubernetes config file
ENV KUBECONFIG /root/.kube/config

# Make port 80 available to the world outside this container
# EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]
