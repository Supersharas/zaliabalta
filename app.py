from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Flask Server</title>
        </head>
        <body>
            <h1>Hello from Flask!</h1>
            <p>My Ubuntu Docker server is working.</p>
        </body>
    </html>
    """

@app.route("/about")
def about():
    return "This is my Flask application running inside Docker!"