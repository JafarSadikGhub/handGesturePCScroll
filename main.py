import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

red_lower = np.array([0,120,70])
red_upper = np.array([10,255,255])
prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('space')
            else:
                print('doing nothing')
            prev_y = y
            #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
            #print(area)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
