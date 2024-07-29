
# Cursor Vision Handfree Computer Control

## Overview
This project focuses on developing a real-time face detection system aimed at enhancing surveillance and access control. Leveraging advanced machine learning algorithms, the system is capable of accurately detecting and recognizing faces in real-time from video feeds.

## Features
- **Real-Time Face Detection:** Detects faces in live video streams with high accuracy.
- **Face Recognition:** Identifies and verifies individuals using a pre-trained facial recognition model.
- **Access Control:** Grants or denies access based on facial recognition results.
- **Surveillance:** Monitors and records video streams for enhanced security.

## Working Actions

Open wide eyes + Mouth Open ==> Left Click

minimize eye + Mouth open ==> Right Click

move your eye sight to move the mouse

Video Explanation



## Acknowledgements




## Authors



## Demo

Insert gif or link to demo


## Deployment

To deploy this project run

```bash
  python run
```


# Hi, I'm Vishnu! 👋


## Lessons Learned
It was my first hackathon. The Problem statement was so interesting that i was stuck to the computer screen straight 24 hrs, No Sleep, No distraction, complete focus...

Key Learnings

    - How the face and other objects are recognized with Mesh Detector

    - We started with 4 members but and at last i was alone left Key learning don't be afraid for errors

    - Always create a separate virtual environment (Very Important)

    - Installing few libraries may be challenging
        - Example Mediapipe requires python 10.5+(62 Bit) where as Autopy works on Python 8.0.0 only it was so hard to find out this later had to choose alternate of Autopy 

    - One of the most important thing I realised is to learn and execute always from command prompt (Importance of Linux)

What challenges did you face and how did you overcome them?

So as mentioned earlier I was constantly getting No Module Error inspite of successfully installing 
    steps to check if you face the same 
    - Always create venv

    - Check if the librari supports current python version

    - Few times you may have installed correct version but wrong bit (i.e.. 32 bit instead of 62 bit)

    - Try to find alternate libraries also 


## Installation

```bash
1. virtual environment
        python -m venv myenv

2. Install requirements from text file
        pip install -r requirements.txt
```
    
## Roadmap

- First
    Use mediapipe and try to locate the mesh for your face

- Second
    After locating the coordinates of eye lids try to find out the ratios of the eye as ratio will be consistent 

- Third 
    Once you have located the movement connect it with mouse with the help of pyautogui

- Fourth 
    Create a front end page for user interaction

- Fifth 
    With the help of Flask connect webpage and the backend


