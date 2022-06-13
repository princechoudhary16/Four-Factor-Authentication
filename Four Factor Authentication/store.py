import cv2


class VideoCameraSave(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier('C:\\Users\\gopes\\OneDrive\\Desktop\\Four Factor Authentication\\haarcascade_frontalface_default.xml')

    def newMember(self, get_name):
        ret, frame = self.video.read()
        img_counter = 0
        name = get_name
        img_name = name + ".png".format(img_counter)
        faces = self.face_cascade.detectMultiScale(frame, 1.3, 5)
        flag = 1
        while True:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (67, 67, 67), 1) 
                detected_face = frame[int(y):int(y+h), int(x):int(x+w)] 
                detected_face = cv2.resize(detected_face, (160, 160)) 
                flag = 0
            if flag == 0:
                cv2.imwrite("C:\\Users\\gopes\\OneDrive\\Desktop\\Four Factor Authentication\\save_image\\" + img_name, detected_face)
                print("{} written!".format(img_name))
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
    
