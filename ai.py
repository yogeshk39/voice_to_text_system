import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error during request to Google Speech Recognition service: {e}")
    return None

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        try:
            text = recognize_speech_from_mic(recognizer, microphone)
            if text:
                print(f"Text: {text}")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
