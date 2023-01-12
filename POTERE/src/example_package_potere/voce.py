import os
from pyttsx3 import init
from tkinter import *
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import datetime
import pygame
import threading
 

class SKYLER():

    root = Tk()
    root.geometry(f"300x50+1700+800")
    root.title("SKYLER")

    engine = init("espeak")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[41].id)

    
    #voce di POTERE
    def voce(audio):
        SKYLER.engine.say(audio)
        SKYLER.engine.runAndWait()


    #input per il riconoscimento testuate del comando (da voce a testo)
    def comandi_vocali():
        x =  sr.Recognizer()

        with sr.Microphone() as source:
            comando = x.listen(source, phrase_time_limit=5)
        
            try:
                richiesta = x.recognize_google(comando, language= 'it-IT')
            
        
            except Exception as e:
                SKYLER.voce("Ripeti comando")
                return "niente"

        return richiesta


    #Settaggio benvenuto
    def benvenuto():
        ora = int(datetime.datetime.now().hour)

        if ora>=0 and ora<5:
            SKYLER.voce("trasformiamo le idee in progetti")

        elif ora>=5 and ora<=7:
            SKYLER.voce("il mattino ha l'oro in bocca e noi siamo pronti")

        elif ora>7 and ora<=9:
            SKYLER.voce("affrontiamo la giornata insieme, valuta i tuoi impegni")
        
        elif ora>9 and ora<13:
            SKYLER.voce("siamo pronti per realizzare qualsiasi idea")

        elif ora>=13 and ora<=15:
            SKYLER.voce("siamo quello che mangiamo")
        
        elif ora>15:
            SKYLER.voce("siamo pronti per realizzare qualsiasi idea")
        
    def Avvio():
        while True:
            permission = SKYLER.comandi_vocali()
            if("attivati" in permission) or ("mi servi" in permission):
                SKYLER.run_winston()
            elif ("disattivati" in permission):
                SKYLER.root.destroy()


        #esecuzioni comandi vocali
    def run_winston():
        c = 2
        SKYLER.benvenuto()
        while True:
            richiesta=SKYLER.comandi_vocali()

            if "test" in richiesta:
                SKYLER.voce("Okay ho appreso il funzionamento delle richieste")
                
            
            elif "presentati" in richiesta:
                SKYLER.voce("siamo pronti")
                #os.system(f'xdg-open "./PRESENTAZIONE/colonna-sonora.mp3"')

                def musica():
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load('./PRESENTAZIONE/colonna-sonora.mp3')
                    pygame.mixer.music.play()

                threading.Thread(target=musica).start()
                
            elif "resta in ascolto" or "fatto" in richiesta:
                break

    root.mainloop()



    

