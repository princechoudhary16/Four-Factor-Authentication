import cv2
import face_recognition
from PIL import Image
import os
import time
import numpy as np


print
"def recognize()"

class VideoCamera(object):
    def __init__(self):
        self.known_face_names = []
        db_loc = "C:\\Users\\gopes\\OneDrive\\Desktop\\Four Factor Authentication\\save_image"
        directory = os.fsencode(db_loc)
        self.video = cv2.VideoCapture(0)
        self.known_face_names = []
        for file in os.listdir(directory):
            print("****")
            filename = os.fsdecode(file)
            print(filename,"+++++a+++++++++++++")
            self.known_face_names.append(filename.split('.')[0])
        for j in self.known_face_names:
            print (j,"........................")
        self.known_face_encodings = [face_recognition.face_encodings(face_recognition.load_image_file(db_loc + "/" + i + ".png"))[0] for i in self.known_face_names]


    def get_frame(self):
        ret, self.frame = self.video.read()
        face_names, face_locations = self.know_faces()
        for (top, right, bottom , left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 0, 0), 1)
        ret, jpeg = cv2.imencode('.png', self.frame)
        return (jpeg.tobytes(), face_names)
    
    
    
    def know_faces(self):
        small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            face_distance = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)
        return face_names, face_locations
