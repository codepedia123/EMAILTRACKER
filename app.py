from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/open')
def track_open():
    email_id = request.args.get('id')
    user_ip = request.remote_addr
    timestamp = datetime.now()

    with open("opens.log", "a") as f:
        f.write(f"Email {email_id} opened at {timestamp} from {user_ip}\n")

    return send_file("pixel.gif", mimetype='image/gif')

@app.route('/')
def index():
    return "Tracking pixel server running!"

if __name__ == '__main__':
    app.run()
