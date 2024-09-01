"""Import modules from the package flask ."""

from flask import Flask, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    """Returns the emotions detected for a given string and the dominant emotion """
    text_to_analyze = request.args["text_to_analyze"]
    emotion = emotion_detection.emotion_detector(text_to_analyze)
    dominant_emotion = emotion["dominant_emotion"]
    if dominant_emotion is None:
        return {
            "error_message": "Invalid text! Please try again!."
        }, 400

    anger_score = emotion["anger"]
    fear_score = emotion["fear"]
    disgust_score = emotion["disgust"]
    joy_score = emotion["joy"]
    sadness_score = emotion["sadness"]

    emotion_expr = f"For the given statement, the system response \
is 'anger': {anger_score}, 'disgust': {disgust_score}, \
'fear': {fear_score}, 'joy': {joy_score} and \
'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

    return {
        "message": emotion_expr
    }

if __name__ == "__main__":
    app.run(debug=True)
