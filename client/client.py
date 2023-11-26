import time
import requests
import socket
from zeroconf import ServiceBrowser, Zeroconf

class MyListener:
    def add_service(self, zeroconf, service_type, name):
        info = zeroconf.get_service_info(service_type, name)
        if info:
            address = socket.inet_ntoa(info.addresses[0])
            url = f"http://{address}:{info.port}/api"
            print(f"Making GET request to {url}")
            try:
                response = requests.get(url)
                print(f"Response from service: {response.json()}")
            except requests.RequestException as e:
                print(f"HTTP request failed: {e}")

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
#browser = ServiceBrowser(zeroconf, "_sila._tcp.local.", listener)

time.sleep(30)
