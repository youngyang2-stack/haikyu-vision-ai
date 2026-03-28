from flask import Flask, request, abort
import requests

app = Flask(__name__)

SECRET_TOKEN = "supersonic-boom-boom"
DISCORD_WEBHOOK = "YOUR_WEBHOOK_HERE"

def analyze_video(video_file):
    # 暂时先返回假数据
    return [
        {"ts": "0:03", "type": "Attack", "player": "Player 2"},
        {"ts": "0:11", "type": "Set", "player": "Player 5"},
        {"ts": "0:18", "type": "Dig", "player": "Player 3"},
    ]

@app.route("/process", methods=["POST"])
def process():
    token = request.headers.get("X-Secret-Token")
    if token != SECRET_TOKEN:
        abort(403)

    video = request.files.get("video")
    if video is None:
        return {"status": "error", "message": "No video uploaded"}, 400

    requests.post(DISCORD_WEBHOOK, json={"content": "Video payload received!"})

    results = analyze_video(video)

    return {
        "status": "success",
        "results": results
    }, 200

if __name__ == "__main__":
    app.run(port=5000)
