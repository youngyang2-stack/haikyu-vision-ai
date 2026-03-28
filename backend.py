from flask import Flask, request, abort
import requests

app = Flask(__name__)

SECRET_TOKEN = "supersonic-boom-boom"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1486061326337052837/6v3xoqoALk3cAL5oLyLxv0XZLxT0PmPDRG_Hrq7zODnAxbyXkpI5PP9UVJ5YG-qcfG5Y"

@app.route("/process", methods=["POST"])
def process():
    token = request.headers.get("X-Secret-Token")
    if token != SECRET_TOKEN:
        abort(403)
    requests.post(DISCORD_WEBHOOK, json={"content": "Video payload received!"})
    return {
    "status": "success",
    "results": [
        {"ts": "0:03", "type": "Attack", "player": "Player 2"},
        {"ts": "0:11", "type": "Set", "player": "Player 5"},
        {"ts": "0:18", "type": "Dig", "player": "Player 3"}
    ]
}, 200

if __name__ == "__main__":
    app.run(port=5000)
