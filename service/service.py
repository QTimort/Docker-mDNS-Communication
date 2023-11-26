from flask import Flask
from zeroconf import ServiceInfo, Zeroconf
import socket
import threading

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def handle_request():
    return {"message": "Hello from mDNS API service!"}, 200

def run_flask_app():
    app.run(host='0.0.0.0', port=3000, debug=False)

def register_mdns_service():
    desc = {'path': '/api'}
    info = ServiceInfo("_http._tcp.local.",
                       "My MDNS Service._http._tcp.local.",
                       # todo this should be an argument such as we can provide the IP through docker
                       addresses=[socket.inet_aton("192.168.200.2")],
                       port=3000,
                       properties={})
    zeroconf = Zeroconf()
    print("Registering mDNS service...")
    zeroconf.register_service(info)
    try:
        # Run indefinitely
        while True:
            pass
    finally:
        zeroconf.unregister_service(info)
        zeroconf.close()

if __name__ == '__main__':
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Register mDNS service
    register_mdns_service()