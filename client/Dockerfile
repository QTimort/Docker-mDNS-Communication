FROM python:3.8

WORKDIR /app

# Install required Python library for mDNS and requests
RUN pip install zeroconf requests

# Copy the client script into the container
COPY client.py .

CMD ["python", "./client.py"]
