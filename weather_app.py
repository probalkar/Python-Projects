import pyttsx3
import requests
import json

engine = pyttsx3.init()
engine.say("Welcome to my weather app!")
engine.runAndWait()

engine.say("Enter name of your city")
engine.runAndWait()
city = input("Enter name of your city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=6cbfc40927594741a4374206230404&q={city}"

r = requests.get(url)

wDict = json.loads(r.text)
key = list(wDict.keys())

    
value = wDict.values()
for v in value:
    innerKey1 = v.keys()
    break

for w in value:
    innerKey2 = w.keys()

print(f"{key[0]}")
for i in innerKey1:
    print(f"{i} : {wDict[key[0]][i]}")

print(f"{key[1]}")
for j in innerKey2:
    print(f"{j} : {wDict[key[1]][j]}")