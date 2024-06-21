from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

def recognize_speech_from_audio_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"Error during request to Google Speech Recognition service: {e}"

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
