from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "running",
        "service": "ai-flow-testing"
    }

@app.route("/health")
def health():
    return {
        "healthy": True
    }

if __name__ == "__main__":
    app.run(debug=True)
