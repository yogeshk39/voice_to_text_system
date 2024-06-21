import speech_recognition as sr
import sounddevice as sd
import numpy as np

def recognize_speech_from_mic(recognizer, microphone):
    fs = 44100  # Sample rate
    duration = 5  # Duration of recording

    print("Say something...")
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    audio_data = np.array(recording, dtype=np.int16)

    try:
        print("Recognizing...")
        audio = sr.AudioData(audio_data.tobytes(), fs, 2)
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error during request to Google Speech Recognition service: {e}")
    return None

if __name__ == "__main__":
    recognizer = sr.Recognizer()

    while True:
        try:
            text = recognize_speech_from_mic(recognizer, None)
            if text:
                print(f"Text: {text}")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
