import os
from pyttsx3 import init
from tkinter import *
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import datetime
import pygame

def run_voice():

    
    root = Tk()

    root.geometry(f"300x50+1700+800")
    root.title("WINSTON")


    engine = init("espeak")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[41].id)
       
    #voce di POTERE
    def voce(audio):
        engine.say(audio)
        engine.runAndWait()



    #input per il riconoscimento testuate del comando (da voce a testo)
    def comandi_vocali():
        x =  sr.Recognizer()

        with sr.Microphone() as source:
            comando = x.listen(source, phrase_time_limit=5)
        
        try:
            richiesta = x.recognize_google(comando, language= 'it-IT')
        
        except Exception as e:
            voce("Ripeti comando")
            return "niente"

        return richiesta


    #Settaggio benvenuto
    def benvenuto():
        ora = int(datetime.datetime.now().hour)

        if ora>=0 and ora<5:
            voce("trasformiamo le idee in progetti")

        elif ora>=5 and ora<=7:
            voce("il mattino ha l'oro in bocca e noi siamo pronti")

        elif ora>7 and ora<=9:
            voce("affrontiamo la giornata insieme, valuta i tuoi impegni")
        
        elif ora>9 and ora<13:
            voce("siamo pronti per realizzare qualsiasi idea")

        elif ora>=13 and ora<=15:
            voce("siamo quello che mangiamo")
        
        elif ora>15:
            voce("siamo pronti per realizzare qualsiasi idea")


    com=1
    while com==1:

        benvenuto()
        richiesta=comandi_vocali()

        if "test" in richiesta:
            voce("Okay ho appreso il funzionamento delle richieste")
            com=2
        
        elif "presentati" in richiesta:
            voce("siamo pronti")
            #os.system(f'xdg-open "./PRESENTAZIONE/colonna-sonora.mp3"')

            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('./PRESENTAZIONE/colonna-sonora.mp3')
            pygame.mixer.music.play()
            com=2
    
    root.mainloop()

    

