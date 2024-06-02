# Official slim base image
FROM python:3.12-slim

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the contents of the folder we are currently working in to our container
COPY . .

# Expose the port the web app runs on
EXPOSE 5000

# Run our app
CMD ["python", "app.py"]