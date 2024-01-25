from flask import Flask, request, jsonify, make_response
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Start the stress_cpu.py script without waiting for it to finish.
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify(message="CPU stress test started"), 202

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return make_response(private_ip, 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
