import pyttsx3
import time
engine = pyttsx3.init()

engine.say("Welcome!")
engine.say("My name is VATSO")
engine.runAndWait()
print("Short for Virtual Assistant for Text to Speech Operation ;)\n")
time.sleep(3)
engine.say("I will be your assistant for saying on your behalf")
engine.runAndWait()

print("Type what you want to say...\n")

while True:
    x = input("<)) ").lower()

    if x=="bye vatso":
        engine.say("See you later alligator")
        engine.runAndWait()
        break

    engine.say(x)
    engine.runAndWait()