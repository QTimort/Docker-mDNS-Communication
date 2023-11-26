FROM python:3.8

WORKDIR /app

# Install required Python library for mDNS and Flask
RUN pip install zeroconf Flask

# Copy the service script into the container
COPY service.py .

CMD ["python", "./service.py"]