from flask import Flask, request, abort
from gemini_scanner import analyze_video_with_gemini

app = Flask(__name__)

SECRET_TOKEN = "supersonic-boom-boom"


def analyze_video(video_file):
    """
    Current demo-stage pipeline:
    1. Call Gemini scanner to detect 6v6 segments
    2. Return stable placeholder play results for frontend demo
    """
    try:
        segments = analyze_video_with_gemini()
        print("Gemini 6v6 segments:", segments)
    except Exception as e:
        print("Gemini scanner failed:", e)
        segments = []

    # For now, always return demo play results
    # Later this can be replaced with real play classification output
    results = [
        {"ts": "0:03", "type": "Attack", "player": "Player 2"},
        {"ts": "0:11", "type": "Set", "player": "Player 5"},
        {"ts": "0:18", "type": "Dig", "player": "Player 3"},
    ]

    return {
        "status": "success",
        "segments": segments,
        "results": results
    }


@app.route("/process", methods=["POST"])
def process():
    try:
        token = request.headers.get("X-Secret-Token")
        if token != SECRET_TOKEN:
            abort(403)

        video = request.files.get("video")
        if video is None:
            return {"status": "error", "message": "No video uploaded"}, 400

        output = analyze_video(video)
        return output, 200

    except Exception as e:
        print("BACKEND ERROR:", e)
        return {"status": "error", "message": str(e)}, 500


if __name__ == "__main__":
    app.run(port=5000)
