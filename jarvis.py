import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

# keep global instruction like your original code
instruction = ""
last_song = ""

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower().strip()

            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', " ").strip()
                print("Command:", instruction)

            print("Heard:", instruction)

    except:
        pass
    return instruction

def play_Jarvis():
    global last_song
    global instruction

    instruction = input_instruction()
    if not instruction:
        return

    print("Processing:", instruction)

    if "play" in instruction:
        song = instruction.replace("play", "").strip()
        if song and song != last_song:
            talk("Playing " + song)
            pywhatkit.playonyt(song)
            last_song = song
            return  # prevent multiple tabs
        elif song == last_song:
            talk("Song is already playing")
            return

    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        talk('Current time ' + current_time)

    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date " + current_date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you')

    elif 'what is your name' in instruction:
        talk('I am Jarvis, What can I do for you')

    elif 'who is' in instruction:
        human = instruction.replace('who is', "").strip()
        if human == "":
            human = instruction
        try:
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        except:
            talk("Sorry I could not find information")

    else:
        talk('Please Repeat')

    time.sleep(0.5)  # small pause to prevent repeated loops

# continuously listen
while True:
    play_Jarvis()