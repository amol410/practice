import speech_recognition as sr
import threading
import time

def listen_and_transcribe(language='hi-IN'):
    recognizer = sr.Recognizer()

    def callback(recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language=language)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    def listen_in_background():
        # No need to manually handle the Microphone context here
        print(f"Listening continuously in {language}... (Press Ctrl+C to stop)")
        stop_listening = recognizer.listen_in_background(sr.Microphone(), callback)

        try:
            while True:
                time.sleep(0.08)
        except KeyboardInterrupt:
            print("Stopping...")
            stop_listening(wait_for_stop=False)

    # Start listening in a separate thread
    threading.Thread(target=listen_in_background).start()

if __name__ == "__main__":
    listen_and_transcribe()
