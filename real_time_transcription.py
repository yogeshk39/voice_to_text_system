# real_time_transcription.py

import speech_recognition as sr

def recognize_speech_from_stream(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_stream = recognizer.listen(source)
        return audio_stream

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        while True:
            audio_stream = recognize_speech_from_stream(recognizer, microphone)
            print("Recognizing...")
            transcription = recognizer.recognize_google(audio_stream)
            print(f"Transcription: {transcription}")
    except KeyboardInterrupt:
        print("Stopping the transcription.")
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

if __name__ == "__main__":
    main()
