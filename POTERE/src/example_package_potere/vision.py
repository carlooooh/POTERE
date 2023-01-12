#POTERE-VISION
#CAMERA DI DESTINAZIONE: GALILEO

#FUNZIONI DA IMPLEMENTARE:
#SALVATAGGIO 'VOLTI AMICI' CON ATTRIBUTI


import os,sys
import face_recognition
import cv2
import numpy as np
import threading





class FaceRecognition2:
    face_loction = []
    face_encodings= []
    face_name=[]
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True
    


    def __init__(self):
        self.encode_faces()

    
    def encode_faces(self):
        for image in os.listdir('./POTERE/CAMERE/GALILEO'):
            face_image = face_recognition.load_image_file(f"./POTERE/CAMERE/GALILEO/{image}")
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
        print(self.known_face_names)
    

    def run_recognition(self):
        
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')
        

        while True:
            
            ret, frame = video_capture.read()

            
            if self.process_current_frame:
            
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                
                rgb_small_frame = small_frame[:, :, ::-1]

                
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Strunzzz"
                    

                    
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        
                            
                    self.face_names.append(f'{name}')

            self.process_current_frame = not self.process_current_frame

            
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
            
            cv2.imshow('POTERE', frame)

            if cv2.waitKay(1) == ord('q'):
                break
        
        video_capture.release()
        cv2.destroyAllWindows()
                
                
            
def avvio():

    def run():
        fr=FaceRecognition2()
        fr.run_recognition()
    
    threading.Thread(target=run).start()
    
    


        




