from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD pipeline"

# This is the important part
if __name__ == "__main__":
    # 0.0.0.0 means "listen to all network interfaces"
    # port=5000 means Flask runs on port 5000 inside the container
    app.run(host="0.0.0.0", port=5000)
