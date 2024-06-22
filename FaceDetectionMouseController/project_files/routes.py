from project_files import app
from flask import request, render_template
import cv2
import numpy as np
import pyautogui
import time

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/face_mouse')
def face_mouse():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    left_mouse_click = ""
    right_mouse_click = ""

    counter = 0
    left_color = (255, 0, 255)
    right_color = (255, 0, 255)

    screen_w, screen_h = pyautogui.size()

    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            x, y, w, h = faces[0]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            mouse_x = (x + w/2) * screen_w / img.shape[1]
            mouse_y = (y + h/2) * screen_h / img.shape[0]

            try:
                pyautogui.moveTo(mouse_x, mouse_y)
            except:
                pass

            if h > 30:
                if counter == 0:
                    pyautogui.click(button='left')
                    left_mouse_click = "Clicked"
                    time.sleep(1)
                    counter = 1
                    left_color = (0, 200, 0)

                if counter != 0:
                    counter += 1
                    if counter > 10:
                        counter = 0
                        left_color = (255, 0, 255)

        else:
            left_mouse_click = right_mouse_click = ""

        cv2.putText(img, f'left:', (25, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f'{left_mouse_click}', (25, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, left_color, 2)
        cv2.putText(img, f'right:', (450, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f'{right_mouse_click}', (450, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, right_color, 2)

        img = cv2.resize(img, (640, 360))

        cv2.imshow("Webcam", img)
        if cv2.waitKey(25) == ord('q'):
            break

    return ''
