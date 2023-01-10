#HUB del PALAZZO MENTALE ARTIFICIALE
from tkinter import *
from tkinter import *
from tkinter import ttk
import threading



def run_hub():


    root = Tk()

    #settaggio grafico dell'HUB
    #screen_width = root.winfo_screenmmwidth()
    #screen_height = root.winfo_screenheight()
    root.geometry(f"500x50+1300+1300")
    root.title("POTERE- PALAZZO MENTALE ARTIFICIALE")
    buttonPalazzoMentale = ttk.Button(root, text="PALAZZO")
    buttonVision = ttk.Button(root, text="VISION")
    buttonVoce = ttk.Button(root, text="WINSTON")
    buttonPalazzoMentale.grid(row=0, column=1)
    buttonVoce.grid(row=0, column=5)
    buttonVision.grid(row=0, column=2)


    




    
    
    root.mainloop()
    


