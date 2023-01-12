#Autentificazione per accedere al PALAZZO MENTALE ARTIFICIALE

#librerie importate
import os,sys
import face_recognition
import cv2
import numpy as np
import math
import time
import HUB
from tkinter import *
from tkinter import *
from tkinter import ttk


#semplice alcoritmo per calcolare la percentuale di accuratezza
def accuratezza(face_distance, face_match_threshold=0.6):
    range=(1.0 - face_match_threshold)
    linear_val=(1.0-face_distance) / (range * 2.0)  
     
    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'

    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val -0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


#algoritmo che utilizza il modulo face_recognition per riconoscere e autentificare il proprietario del PALAZZO MENTALE ARTIFICIALE 

class FaceRecognition:
    face_location = []
    face_encodings= []
    face_name=[]
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True


    def __init__(self):
        self.encode_faces()
    
    #codifica dell'immagine in un numpy array
    def encode_faces(self):
        for image in os.listdir('./POTERE/CAMERE/GALILEO'):
            face_image = face_recognition.load_image_file(f"./POTERE/CAMERE/GALILEO/{image}")
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
  #test      print(self.known_face_names)
    

    def autentificazione(self):
        video_capture = cv2.VideoCapture(0)
        start_time = time.time()

        if not video_capture.isOpened():
            sys.exit('Impossibile aprire la webcam')

        while True:
            accesso =1
            ret, frame = video_capture.read()

        
            if self.process_current_frame:

                #rimpicciolire per migliorare le prestazioni <consiglio
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Riconoscimento visivo
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # attribuire un nome ad un viso non memorizzato
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Volto non memorizzato"
                    confidence = '???'

                    # Calculate the shortest distance to face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    #autentificazione con il proprietario
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        confidence = accuratezza(face_distances[best_match_index])
                        accesso = 2

                    self.face_names.append(f'{name} ({confidence})')
        
            self.process_current_frame = not self.process_current_frame

            #Creazione grafica del bordo intorno al volto
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                

                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                #Frame grafico con il nome
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            # Display
            cv2.imshow('POTERE - AUTENTIFICAZIONE', frame)

            tempo_trascorso= time.time() - start_time

            if accesso == 2 and tempo_trascorso>7:
                if accesso == 2:
                    break
            

            #Uscita utilizzato per testare
            if cv2.waitKey(1) == ord('q'):
                break
        
        # Chiusura webcam e apertura POTERE/HUB
        if accesso==2:
            video_capture.release()
            cv2.destroyAllWindows()
            HUB.run_hub()


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.autentificazione()

