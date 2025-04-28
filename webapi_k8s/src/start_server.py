from flask import Flask
from redis import Redis
import socket  # importiert das Modul für den Hostnamen

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def hello_world():
    count = redis.incr('hits')
    hostname = socket.gethostname()  # Holt den Hostnamen des Pods
    return 'Hello World! I have been seen {} times. You are visiting pod: {}.\n'.format(count, hostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
