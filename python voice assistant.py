import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except:
            print("Sorry, I did not get that")
            return ""

# Main function to run the assistant
def run_assistant():
    while True:
        command = listen().lower()

        if 'stop' in command:
            speak("Goodbye!")
            break
        elif 'hello' in command:
            speak("Hello! How can I help you?")
        elif 'what is your name' in command:
            speak("I am your Python assistant. What can I do for you?")
        else:
            speak("I am not sure how to do that yet.")

if __name__ == "__main__":
    run_assistant()
