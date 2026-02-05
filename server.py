from flask import Flask, render_template, request
from emotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None or text_to_analyze == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
