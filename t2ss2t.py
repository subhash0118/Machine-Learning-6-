import speech_recognition as sr
import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Function to perform Text-to-Speech
def text_to_speech():
    user_input = input("Enter the text you want to convert to speech: ")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Select the first voice
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    print(f"Speaking: {user_input}")
    engine.say(user_input)
    engine.runAndWait()

# Function to perform Speech-to-Text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening... Please speak now.")
        try:
            # Record audio for 5 seconds
            audio_data = recognizer.record(source, duration=5)
            print("Recognizing...")
            # Convert audio to text using Google's Speech-to-Text API
            text = recognizer.recognize_google(audio_data, language="en-US")
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:
        print("\n--- Select an Operation ---")
        print("1. Speech-to-Text (STT)")
        print("2. Text-to-Speech (TTS)")
        print("Any other number to exit.")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\nYou chose Speech-to-Text:")
                speech_to_text()
            elif choice == 2:
                print("\nYou chose Text-to-Speech:")
                text_to_speech()
            else:
                print("Invalid option. Exiting program.")
                break
        except ValueError:
            print("Please enter a valid number. Exiting program.")
            break
