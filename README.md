# AI Object Following Robot 🤖

An AI-powered autonomous robot that detects and follows objects in real time using YOLOv8, OpenCV, Python, Arduino, and computer vision techniques.

---

## 📌 Project Overview

This project combines Artificial Intelligence and Robotics to create a smart robot capable of:

- Detecting objects using YOLOv8
- Tracking a selected target object
- Moving automatically based on object position
- Performing real-time object-following using computer vision

The robot uses a camera feed for object detection and an Arduino-controlled motor driver for movement control.

---

## 🚀 Features

- Real-time object detection using YOLOv8
- Autonomous object following
- Live camera feed processing
- Left, right, forward, and stop navigation
- Arduino serial communication
- Computer vision based robotic control

---

## 🛠 Technologies Used

- Python
- OpenCV
- YOLOv8
- Arduino UNO
- L298N Motor Driver
- Serial Communication
- Matplotlib
- Computer Vision
- Artificial Intelligence

---

## ⚙ Hardware Components

- Arduino UNO
- L298N Motor Driver
- DC Motors
- Robot Chassis
- Webcam / USB Camera
- Battery Pack
- Jumper Wires

---

## 💻 Software Requirements

Install required libraries:

bash pip install ultralytics pip install opencv-python pip install matplotlib pip install pyserial 

---

## ▶ How It Works

1. Camera captures live video.
2. YOLOv8 detects objects in the frame.
3. User selects target object.
4. Robot determines object position:
   - Left → Turn Left
   - Right → Turn Right
   - Center → Move Forward
5. Commands are sent to Arduino through serial communication.
6. Arduino controls motors using L298N driver.

---

## 📷 Working Demo

The robot successfully:
- Detects objects in real time
- Tracks target object position
- Moves autonomously toward the object

---

## 📌 Applications

- Surveillance robots
- Smart delivery systems
- Human-following robots
- Industrial automation
- AI-based navigation systems
- Autonomous robotics research

---

## 🔮 Future Scope

- Face recognition integration
- Obstacle avoidance
- Voice assistant support
- SLAM-based navigation
- Drone integration
- Gesture control
- IoT connectivity

---

## 📚 Learning Outcomes

Through this project, I learned:
- AI-based object detection
- Real-time computer vision
- Robotics integration
- Arduino motor control
- Serial communication
- Autonomous navigation concepts

---

## 👨‍💻 Author

Developed as a robotics and AI integration project using computer vision and embedded systems
