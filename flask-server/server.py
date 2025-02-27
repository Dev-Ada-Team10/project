from flask import Flask

app = Flask(__name__)

@app.route("/languages")
def languages():
    return {"languages": ["English", "Spanish", "Dutch"]}

if __name__ == "__main__":
    app.run(debug=True)