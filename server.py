from flask import Flask, request
from shared import message_queue

app = Flask(__name__)

@app.route("/")
def home(error=""):
    return f"""
    <style> 
        body {{
            font-family: Arial, sans-serif;
            background-color: #111;
            color: white;

            min-height: 100vh;
            margin: 0;

            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

            textarea {{
                width: 90%;
                height: 150px;
                font-size: 24px;
                padding: 15px;
            }}

            button {{
                width: 90%;
                padding: 18px;
                margin-top: 15px;
                font-size: 22px;
                font-weight: bold;
                cursor: pointer;
                background-color: blue;
            }}

            .status {{
                font-size: 18px;
                margin-bottom: 20px;
                text-align: center;
            }}

            .container {{
                width: 90%;
                max-width: 500px;
                text-align: center;
            }}

            h1 {{
                margin-bottom: 20px;
            }}

    </style>
    <div class="container">
        <h1>Home Messenger</h1>
        <p class="status">{error}</p>

        <form action="/send" method="POST">
            <textarea name="message" placeholder="Type your message..."></textarea>
            <button type="submit">Send Message</button>
        </form>
    </div>
    """


@app.route("/send", methods=["POST"])
def send():
    message = request.form.get("message")

    if not message:
        return home("Message cannot be empty")

    message_queue.put(message)    
    return home("Message received")


def run_server():
    app.run(host="0.0.0.0", port=5050)
