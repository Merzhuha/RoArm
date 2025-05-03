# Robotic Arm Crane Controller for Object Manipulation
A Python-based control system for a servo-powered robotic crane arm that allows real-time manual control through keyboard inputs. This project enables users to move the arm along X, Y, Z axes and control the gripper (claw) for lifting, transporting, and placing objects.

Developed as part of the Introduction to Robotics course at KBTU.

## Features
Real-time control of robotic arm with keyboard

Move joints along X, Y, Z axes

Open/close the gripper (claw)

Simple, expandable Python codebase

USB serial communication with the robotic arm

JSON-based command formatting

Manual precision control with feedback delay management

## Hardware Requirements
Servo-controlled robotic arm (e.g., RoArm M2 or equivalent)

USB connection to host PC (e.g., /dev/ttyUSB0 or COMx)

Lightweight test objects (e.g., boxes, paperclips)

Software Requirements
Python 3.7+

Required libraries:

pyserial

keyboard

json

time

## Install dependencies using:

pip install pyserial keyboard
How It Works
1. Serial Communication
The robotic arm receives JSON-formatted commands through a serial port. Example:

json
{"X": 120, "Y": 60, "Z": 30, "T": 1041, "t": 45}
2. Keyboard Control
The Python script maps specific keypresses to robotic arm actions:

Key	Action
W/S	Move arm forward/back
A/D	Move left/right
Q/E	Move up/down (Z-axis)
R/F	Open/close claw
Z	Toggle joints
X	Exit program

3. Feedback Loop
Each key input updates the position dictionary, formats it into JSON, and sends it over the serial connection with a short delay to prevent command flooding.

Experimental Results
![image](https://github.com/user-attachments/assets/7de61d9d-fa99-492c-9ba9-389781a48053)

Smooth and responsive manual control

Accurate object picking and placement

Stable joint switching and grip function

Minor lag resolved using small delays (time.sleep(0.1))

Reliable for repeated use in test scenarios

Limitations and Future Work
No sensor feedback or autonomous behavior

Fully manual; no path planning or inverse kinematics

Future improvements may include:

Vision-based object tracking (OpenCV integration)

Gesture or voice-based control via AI

Smarter movement using inverse kinematics

Sensor feedback for error correction

Developed By
Robotics Students, KBTU

Torebek Tanirbergen

Zulpukhar Merzhan

Aubekerov Anuar

Contact:
t_torebek@kbtu.kz
m_zulpukhar@kbtu.kz
an_aubekerov@kbtu.kz

Acknowledgements
We thank the Robotics Lab instructors and course supervisors for their continuous support and feedback throughout this project.

## References
PySerial Documentation

Arduino Serial Basics

RoArm M2 Documentation

Keyboard Python Module

Forward Kinematics - Wikipedia
