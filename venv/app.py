from flask import Flask, render_template, Response
import cv2
import numpy as np
import os  # Add this import
import time  # Add this import
from pygame import mixer

app = Flask(__name__)

# # Get the directory of the current script
# dir_path = os.path.dirname(os.path.realpath(__file__))

# mixer.init()
# sound_file = os.path.join(dir_path, 'sound4.mp3')

# def generate_frames():
#     face_cascade = cv2.CascadeClassifier(os.path.join(dir_path, 'haarcascade_frontalface_default.xml')) 
#     eye_cascade = cv2.CascadeClassifier(os.path.join(dir_path, 'haarcascade_eye.xml')) 

#     cap = cv2.VideoCapture(0) 

#     eyes_closed_start_time = None
#     eyes_closed_duration = 0
#     eyes_closed_threshold = 2  # seconds

#     while True:
#         ret, frame = cap.read() 
#         if not ret:
#             break
        
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

#         face_detected = False
#         eyes_detected = False

#         for (x, y, w, h) in faces:
#             face_detected = True
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray)

#             for (ex, ey, ew, eh) in eyes:
#                 eyes_detected = True
#                 cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#                 print("Eyes are open")  # Print "Eyes detected" when eyes are detected

#         if face_detected:
#             if not eyes_detected:
#                 if eyes_closed_start_time is None:
#                     eyes_closed_start_time = time.time()
#                 eyes_closed_duration = time.time() - eyes_closed_start_time
#                 if eyes_closed_duration >= eyes_closed_threshold:
#                     print("Wake up!")  # Print "Wake up!" if eyes are closed for more than threshold duration
#                     mixer.music.load(sound_file)
#                     mixer.music.play()
#                     eyes_closed_start_time = None  # Reset the timer
#             else:
#                 eyes_closed_start_time = None  # Reset the timer if eyes are detected

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
        
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#         key = cv2.waitKey(1)
#         if key == 27:  
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# @app.route('/')

def index():
    return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run()

