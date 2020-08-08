from Tkinter import *
from naoqi import ALProxy
import unicodedata
import motion
import random
import almath
import time

# ip = "192.168.1.5"
# port = 9559

speech_list = ["I'm Pepper", "Python rocks", "I rock. Robots are amazing!"]
current = 0;


ip = "127.0.0.1"
port = 64878

root = Tk()

# entry is the input box
entry = Text(root, width=50, bg="blue", fg="white")
entry.pack()


def helloCallBack():
    tts = ALProxy("ALTextToSpeech", ip, port)
    u = entry.get("1.0", "end-1c")
    u = unicodedata.normalize('NFKD', u).encode('ascii', 'ignore')
    tts.say(u)


def move():
    mov = ALProxy("ALMotion", ip, port)
    mov.moveTo(1, 0, 0)


def arm_movement():
    motionProxy = ALProxy("ALMotion", ip, port)
    motionProxy.openHand('LHand')


def head_yaw():
    motionProxy = ALProxy("ALMotion", ip, port)
    motionProxy.setStiffnesses("Head", 1.0)
    names = "HeadYaw"
    rand = random.randrange(10, 60)
    angleLists = rand * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    time.sleep(1.0)
    head_yaw()


button = Button(root, text="Say It", command=helloCallBack)
button.pack()

# moveButton = Button(root, text="Move it", command=arm_movement)
moveButton = Button(root, text="Move it", command=head_yaw)
moveButton.pack()

root.mainloop()
