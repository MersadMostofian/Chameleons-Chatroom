
from flask import Flask , render_template , request
from flask_socketio import SocketIO, send
app = Flask(__name__)



@app.route("/")
def start():
    return render_template("start.html")

@app.route("/login")
def login():
    return render_template("login.html")


app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")
@socketio.on('message')
def handle_message(message):
    print("received message: " + message)
    if message != "user connected!":
        send(message , broadcast=True)

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="localhost")