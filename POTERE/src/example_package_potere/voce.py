from pyttsx3 import init

def run_voice():
    
    engine = init("espeak")
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[41].id)

    
    engine.say("Bentornato Carlo. Sono nato e sono pronto!")
    engine.runAndWait()


