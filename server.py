"""Flask app for emotion detection using Watson NLP"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the homepage with the input form"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """Analyze the emotion from the provided text and return the formatted result or error"""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

if __name__ == "__main__":
    app.run(debug=True)
