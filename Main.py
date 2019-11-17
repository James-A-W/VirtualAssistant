from PlayText import PlayText
from Calculate import Calculate
import Listen
import playsound
import os
def gthh(data):
    tosay = ""
    dd = data.split(" ")
    for item in dd:
        print(item)
        print(dd[0])
        if item == dd[0]:
            pass
        else:
            tosay = tosay + item
            tosay = tosay + " "
    tosay = tosay[:len(tosay)-1]
    return tosay
os.system("cls")
PlayText("Hello there, welcome back.")
global run
run = True
def Scarl(data):
    data = data.lower()
    if data.startswith("play") or data.startswith("start") or data.startswith("song"):
        data = data.split(" ")
        try:
            playsound.playsound(gthh(data)+".mp3")
        except:
            PlayText("You did not tell me what mp3 file to play")
            
    elif data.startswith("say"):
        PlayText("You asked me to say: "+gthh(data))
    
    elif data.startswith("shut down") or data.startswith("turn off") or data.startswith("off"):
        PlayText("Okay, I will shutdown now. Goodbye.")
        run = False
        print(run)

    elif data.startswith("calculate") or data.startswith("what's") or data.startswith("do"):
        PlayText("Calculating")
        t = gthh(data)
        print(t)
        summed = Calculate(t)
        PlayText(t+" = "+str(summed))

    elif data.startswith("hi"):
        PlayText("Hello")

    elif data.startswith("what are you"):
        PlayText("I am a hard-coded assistant bot.")

    elif data.startswith("clear space"):
        PlayText("Clearing Space.")
        for name in os.listdir("NewSounds"):
            os.remove("NewSounds/"+name)
    
    else:
        PlayText("Sorry, I didn't understand that.")

while run == True:
    if run == False:
        break
    PlayText("What is your command")
    Command = Listen.RecordSound(4)
    if Command != None:
        Command = Command.lower()
        if Command.startswith("shut down") or Command.startswith("turn off"):
            PlayText("Okay, I am shutting down now. Goodbye James.")
            break
        PlayText("Processing your command")
        Scarl(Command)
