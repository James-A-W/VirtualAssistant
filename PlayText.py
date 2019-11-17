from gtts import gTTS
import os
import playsound

def PlayText(text):
    print(text)

    try:
        f = open("Preloaded/SOUND_"+text+".mp3","r")
        f.close()
        playsound.playsound("Preloaded/SONG_"+text+".mp3")
    except:
        tts = gTTS(text=text, lang='en')

        try:
            tts.save("NewSounds/sound"+text+".mp3")
        except:
            print("uh oh")
            os.remove("NewSounds/sound"+text+".mp3")
            tts.save("NewSounds/sound"+text+".mp3")
        playsound.playsound("NewSounds/sound"+text+".mp3")
