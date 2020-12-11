import cv2
import face_recognition
from decimal import Decimal

 
video_capture = cv2.VideoCapture(0)


face_locations = []

while True:
   
    ret, frame = video_capture.read()

   
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encoding = face_recognition.face_encodings(rgb_frame)
 

    for top, right, bottom, left in face_locations:
        
        img=cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


    cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(face_locations)
print(face_encoding)
res=""
for ind in face_encoding[0]:
    res=res+str(Decimal(ind))
    res=res+":"
l1=res.split(":")
print(type(l1))
print(Decimal(l1[0]))
video_capture.release()
cv2.destroyAllWindows()      

            
              
