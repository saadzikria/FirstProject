# Pull Base Image
FROM python:3.9.18-slim

# Copy Requirements File and Script File
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install all dependencies
RUN pip install -r requirements.txt

# Expose port 80
EXPOSE 80

ENTRYPOINT [ "python", "app.py" ]
