from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import serial
import time

arduino = serial.Serial('COM3',9600,timeout=1)

time.sleep(3)


model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

target = input("Enter object to follow: ").strip().lower()

plt.ion()   # interactive mode

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera failed")
        break

    results = model(frame, imgsz=320)

    h, w, _ = frame.shape
    command = ""

    for r in results:
        for box in r.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            name = model.names[cls].lower()

            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 2)
            cv2.putText(frame, name, (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            if name == target:
                centerX = (x1 + x2) // 2

                if centerX < w//3:
                    command = "LEFT"
                elif centerX > 2*w//3:
                    command = "RIGHT"
                else:
                    command = "FORWARD"

    print("Sending:", command)

    if command == "LEFT":

         arduino.write(b'L')

    elif command == "RIGHT":

         arduino.write(b'R')

    elif command == "FORWARD":

         arduino.write(b'F')

    else:

         arduino.write(b'S')

    arduino.flush()

    time.sleep(0.1)


    cv2.putText(frame, command, (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    # 🔥 DISPLAY USING MATPLOTLIB
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("Robot Vision")
    plt.axis('off')
    plt.pause(0.001)
    plt.clf()