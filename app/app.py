from flask import Flask
import socket
import os

app = Flask(__name__)

# Replace with your actual bucket name and region
S3_BUCKET = "sna-static-files"
S3_REGION = "us-east-1"
S3_IMAGE_URL = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/logo.png"

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>Flask App on AWS ECS Fargate</h1>
    <p><b>Served by Pod:</b> {hostname}</p>
    <p><b>Environment:</b> AWS ECS + S3</p>
    <img src="{S3_IMAGE_URL}" alt="Logo from S3" width="200"/>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
