import speech_recognition as sr
import pyttsx3
#from to_do import get_tasks
from crypto_updates import get_price_updates, fear_greed
from Entertainment import get_fact, get_joke

# Initialize the recognizer and engine instances
r = sr.Recognizer()
engine = pyttsx3.init()

newVoiceRate = 120
engine.setProperty('rate',newVoiceRate)

# Define a function to speak out the text using the pyttsx3 engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech and return text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Could you please repeat?")
        return recognize_speech()
    except sr.RequestError:
        speak("Sorry, I couldn't connect to the server. Please try again later.")
        return None

# Define the main function to handle user requests
def main():
    speak("Hello! How can I help you today?")
    while True:
        command = recognize_speech().lower()
        if "set reminder" in command:
            # Code to set a reminder
            speak("Reminder set successfully!")
            speak("To-do list created successfully!")
        elif "search the web" in command:
            # Code to search the web
            speak("Here are the search results!")
        elif "crypto updates" in command:
            results = get_price_updates()
            for price in results:
                speak(price)
            break
        elif 'joke' in command:
            joke = get_joke()
            speak(joke)
        elif 'random' in command and 'fact' in command:
            fact = get_fact()
            speak(fact)
        elif 'fear' in command and 'greed' in command:
            advice = fear_greed()
            speak(advice)
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't understand. Could you please try again?")

if __name__ == "__main__":
    main()
