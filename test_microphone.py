import speech_recognition as sr

recognizer = sr.Recognizer()

# Test microphone input
def test_microphone():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)  # Listening to the microphone input
        try:
            print("You said: " + recognizer.recognize_google(audio))  # Recognizing the speech
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

test_microphone()
