"""
Simple chatbot application.

This Flask application exposes a `/chat` endpoint that accepts user
messages and returns a response.  In a real‑world scenario you could
integrate a natural language processing model here (for example using
the Hugging Face transformers library), but for the purposes of this
demo we keep the logic lightweight and dependency‑free.

To run the application locally you can execute:

```
python app/main.py
```

When containerised the application will listen on port 8080 by
default.  The Dockerfile in this repository sets up the runtime
environment.
"""

import os
from flask import Flask, request, jsonify


app = Flask(__name__)


def generate_reply(message: str) -> str:
    """Generate a reply for the given message.

    For demonstration purposes this function returns a canned
    response.  You could extend it to call a machine learning model
    hosted on AWS SageMaker, Azure OpenAI, or a third‑party API.
    """
    message = message.lower().strip()
    if "hello" in message or "hi" in message:
        return "Hello! How can I assist you today?"
    if "help" in message:
        return "Sure, please tell me what you need help with."
    return "I'm not sure how to respond to that. Could you rephrase?"


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat requests.

    Expected JSON body: {"message": "your message"}
    Returns JSON: {"reply": "bot reply"}
    """
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    reply = generate_reply(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    # When running locally, listen on port 8080 so it matches the
    # container's exposed port.  The host and port can be overridden
    # using environment variables.
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)), debug=False)
