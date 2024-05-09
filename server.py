# Imports
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        ans = str({"anger":anger, "disgust":disgust, "fear":fear, "joy":joy, 
        "sadness":sadness, "dominant_emotion":dominant_emotion})
        return "For the given statement, the system response is  " + ans

# Rendering Home Page
@app.route("/")
def render_index_page():
    return render_template('index.html')

# Running application on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)