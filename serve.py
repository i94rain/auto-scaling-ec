from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST"])
def start_cpu_stress():
    subprocess.Popen(["python", "stress_cpu.py"])
    return "CPU stress started."

@app.route("/", methods=["GET"])
def get_private_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return f"Private IP address: {private_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
