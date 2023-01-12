#HUB del PALAZZO MENTALE ARTIFICIALE
from tkinter import *
from tkinter import *
from tkinter import ttk
from voce import *
from PALAZZO import *
from vision import *
import threading
import subprocess



def run_hub():

    root = Tk()

    #settaggio grafico dell'HUB
    #screen_width = root.winfo_screenmmwidth()
    #screen_height = root.winfo_screenheight()
    root.geometry(f"500x50+1300+1300")
    root.title("POTERE- PALAZZO MENTALE ARTIFICIALE")

    def palazzo():
        run_PalazzoMentale()

    buttonPalazzoMentale = ttk.Button(root, text="PALAZZO",  command=lambda: threading.Thread(target=palazzo).start())

    def vision():
        os.chdir("./POTERE/src/example_package_potere")
        subprocess.run(["python", "vision.py"])
        
        
    buttonVision = ttk.Button(root, text="VISION", command=lambda: threading.Thread(target=vision).start())

    def assistente():
        SKYLER.Avvio()

    buttonVoce = ttk.Button(root, text="SKYLER", command=lambda: threading.Thread(target=assistente).start())

    buttonPalazzoMentale.grid(row=0, column=1)
    buttonVoce.grid(row=0, column=5)
    buttonVision.grid(row=0, column=2)


    root.mainloop()
    


