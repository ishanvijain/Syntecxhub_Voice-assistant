import speech_recognition as sr
from gtts import gTTS
import pyautogui
import webbrowser
import playsound
import time
def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print(response_text)
    filename = f"response_{int(time.time())}.mp3"
    tts = gTTS(text=response_text, lang='en')
    tts.save(filename)
    playsound.playsound(filename)
    
tasks = []
listeningToTask = False

def main():
    global tasks
    global listeningToTask
    # respond("Hello, Jake. I hope you're having a nice day today.")
    while True:
        command = listen_for_command()

        triggerKeyword = ""

        
        if command and triggerKeyword in command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + " currently in your list.")
            elif "add a task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
            elif "open chrome" in command:
                respond("Opening Chrome.")
                webbrowser.open("https://www.youtube.com/")
            elif "exit" in command:
                respond("Goodbye!")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")

if __name__ == "__main__":
    # print(listen_for_command())
    respond("Assistant Started")
    main()
