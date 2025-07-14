"""
Flask web server for Emotion Detection.
Serves a web interface and an API endpoint for emotion analysis.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Serve the main HTML page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handle emotion detection requests.
    Returns formatted string response or error message.
    """
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
