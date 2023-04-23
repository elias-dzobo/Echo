import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

tasks = []


def get_tasks():
    from main import recognize_speech, speak
    with sr.Microphone() as source:
        print("What tasks would you like to add to your to do lsit")
        audio = r.listen(source)
    try:
        while True:
            task = recognize_speech()
            if 'stop' in task:
                break 
            tasks.append(task) 

        speak("Here is your to do list items for the day")
        for task in tasks:
            speak(task) 
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Could you please repeat?")
        return recognize_speech()
    except sr.RequestError:
        speak("Sorry, I couldn't connect to the server. Please try again later.")
        return None
    
a = get_tasks()
print(a)