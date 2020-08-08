from Tkinter import *
from naoqi import ALProxy
import unicodedata
import random
import almath
import time

class Pepper_For_Cop:

    def __init__(self, master):
        self.speech_list = ["I'm Pepper", "Python rocks", "I rock. Robots are amazing!"]
        self.current = 0
        self.end = len(self.speech_list)
        self.movement_flag = True
        self.ip = "127.0.0.1"
        self.port = 64878
        self.motionProxy = ALProxy("ALMotion", self.ip, self.port)
        self.tts = ALProxy("ALTextToSpeech", self.ip, self.port)

        self.textBox = Text(master, width=50, bg="blue", fg="white")
        self.textBox.pack()

        self.button = Button(master, text="Say It", command=self.helloCallBack)
        self.button.pack()

        self.startButton = Button(master, text='Start Head Rotation', command=self.start)
        self.startButton.pack()

        self.stopButton = Button(master, text='Stop Head Rotation', command=self.stop)
        self.stopButton.pack()

        self.speak_button = Button(root, text="Speak Next", command=self.speak_next)
        self.speak_button.pack()

    def helloCallBack(self):
        tts = ALProxy("ALTextToSpeech", self.ip, self.port)
        u = self.textBox.get("1.0", "end-1c")
        u = unicodedata.normalize('NFKD', u).encode('ascii', 'ignore')
        tts.say(u)

    def start(self):
        self.cancel_id = None
        self.head_yaw()

    def head_yaw(self):
        self.motionProxy.setStiffnesses("Head", 1.0)
        names = "HeadYaw"
        rand = random.randrange(10, 60)
        angleLists = rand * almath.TO_RAD
        timeLists = 1.0
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        self.cancel_id = self.textBox.after(1000, self.head_yaw)

    def stop(self):
        if self.cancel_id is not None:
            self.textBox.after_cancel(self.cancel_id)
            self.cancel_id = None

    def speak_next(self):
        angleLists = 10 * almath.TO_RAD
        timeLists = 1.0
        isAbsolute = True
        self.motionProxy.angleInterpolation("HeadYaw", angleLists, timeLists, isAbsolute)
        self.tts.say(self.speech_list[self.current % self.end])
        self.current += 1


root = Tk()
Pepper_For_Cop(root)
root.mainloop()