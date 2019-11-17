import speech_recognition as sr

def RecordSound(time):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=time)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    return ""
