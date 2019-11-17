lis = [
"Sorry, I didn't understand that.",
"I am a hard-coded assistant bot.",
"Hello"
]

from gtts import gTTS
import playsound

def do(s):
    tts = gTTS(text=s,lang="en")
    tts.save("Preloaded/SOUND_"+s+".mp3")

for item in lis:
    do(item)

tts = gTTS(text="I have completed the task",lang="en")
tts.save("Sound1.mp3")
playsound.playsound("Sound1.mp3")
os.remove("Sound1.mp3")
