from Tkinter import *
from naoqi import ALProxy
import unicodedata
import random
import almath
import math
import motion
import time

class Pepper_For_Cop:

    gestures = ["animations/Stand/Emotions/Negative/Bored_1",
"animations/Stand/Emotions/Neutral/Embarrassed_1",
"animations/Stand/Emotions/Positive/Happy_4",
"animations/Stand/Emotions/Positive/Hysterical_1",
"animations/Stand/Emotions/Positive/Peaceful_1",
"animations/Stand/Gestures/BowShort_1",
"animations/Stand/Gestures/But_1",
"animations/Stand/Gestures/CalmDown_1",
"animations/Stand/Gestures/CalmDown_5",
"animations/Stand/Gestures/CalmDown_6",
"animations/Stand/Gestures/Choice_1",
"animations/Stand/Gestures/Desperate_1",
"animations/Stand/Gestures/Desperate_2",
"animations/Stand/Gestures/Desperate_4",
"animations/Stand/Gestures/Desperate_5",
"animations/Stand/Gestures/Enthusiastic_4",
"animations/Stand/Gestures/Enthusiastic_5",
"animations/Stand/Gestures/Everything_1",
"animations/Stand/Gestures/Everything_2",
"animations/Stand/Gestures/Everything_3",
"animations/Stand/Gestures/Everything_4",
"animations/Stand/Gestures/Excited_1",
"animations/Stand/Gestures/Explain_1",
"animations/Stand/Gestures/Explain_10",
"animations/Stand/Gestures/Explain_11",
"animations/Stand/Gestures/Explain_2",
"animations/Stand/Gestures/Explain_3",
"animations/Stand/Gestures/Explain_4",
"animations/Stand/Gestures/Explain_5",
"animations/Stand/Gestures/Explain_6",
"animations/Stand/Gestures/Explain_7",
"animations/Stand/Gestures/Explain_8",
"animations/Stand/Gestures/Far_1",
"animations/Stand/Gestures/Far_2",
"animations/Stand/Gestures/Far_3",
"animations/Stand/Gestures/Give_3",
"animations/Stand/Gestures/Give_4",
"animations/Stand/Gestures/Give_5",
"animations/Stand/Gestures/Give_6",
"animations/Stand/Gestures/Hey_1",
"animations/Stand/Gestures/Hey_3",
"animations/Stand/Gestures/Hey_4",
"animations/Stand/Gestures/Hey_6",
"animations/Stand/Gestures/IDontKnow_1",
"animations/Stand/Gestures/IDontKnow_2",
"animations/Stand/Gestures/IDontKnow_3",
"animations/Stand/Gestures/Me_1",
"animations/Stand/Gestures/Me_2",
"animations/Stand/Gestures/Me_4",
"animations/Stand/Gestures/Me_7",
"animations/Stand/Gestures/No_1",
"animations/Stand/Gestures/No_2",
"animations/Stand/Gestures/No_3",
"animations/Stand/Gestures/No_8",
"animations/Stand/Gestures/No_9",
"animations/Stand/Gestures/Nothing_2",
"animations/Stand/Gestures/Please_1",
"animations/Stand/Gestures/ShowFloor_1",
"animations/Stand/Gestures/ShowFloor_3",
"animations/Stand/Gestures/ShowFloor_4",
"animations/Stand/Gestures/ShowSky_1",
"animations/Stand/Gestures/ShowSky_11",
"animations/Stand/Gestures/ShowSky_2",
"animations/Stand/Gestures/ShowSky_4",
"animations/Stand/Gestures/ShowSky_5",
"animations/Stand/Gestures/ShowSky_6",
"animations/Stand/Gestures/ShowSky_7",
"animations/Stand/Gestures/ShowSky_8",
"animations/Stand/Gestures/ShowSky_9",
"animations/Stand/Gestures/ShowTablet_2",
"animations/Stand/Gestures/ShowTablet_3",
"animations/Stand/Gestures/Thinking_1",
"animations/Stand/Gestures/Thinking_3",
"animations/Stand/Gestures/Thinking_4",
"animations/Stand/Gestures/Thinking_6",
"animations/Stand/Gestures/Thinking_8",
"animations/Stand/Gestures/Yes_1",
"animations/Stand/Gestures/Yes_2",
"animations/Stand/Gestures/Yes_3",
"animations/Stand/Gestures/YouKnowWhat_1",
"animations/Stand/Gestures/YouKnowWhat_2",
"animations/Stand/Gestures/YouKnowWhat_3",
"animations/Stand/Gestures/YouKnowWhat_5",
"animations/Stand/Gestures/YouKnowWhat_6",
"animations/Stand/Gestures/You_1",
"animations/Stand/Gestures/You_4",
"animations/Stand/Waiting/ShowSky_1",
"animations/Stand/Waiting/ShowSky_2",
"animations/Stand/Waiting/Think_1",
"animations/Stand/Waiting/Think_2",
"animations/Stand/Waiting/Think_3"]

    def __init__(self, master):
        self.speech_list = ["Hi, I'm Pepper. I'm going to talk about Tigers today with the help of my co presenter, Eeeve",
                            "The tiger is the largest extant cat species and a member of the genus Panthera.",
                            "It is most recognisable for its dark vertical stripes on orange-brown fur with a lighter underside.",
                            "It is an apex predator, primarily preying on ungulates such as deer and wild boar."]
        self.current = 0
        self.end = len(self.speech_list)
        self.movement_flag = True
        self.ip = "192.168.1.3"
        # self.ip = "127.0.0.1"
        self.port = 9559
        self.motionProxy = ALProxy("ALMotion", self.ip, self.port)
        self.postureProxy = ALProxy("ALRobotPosture", self.ip, self.port)
        # self.tts = ALProxy("ALTextToSpeech", self.ip, self.port)
        self.tts = ALProxy("ALAnimatedSpeech", self.ip, self.port)
        self.animationService = ALProxy("ALAnimationPlayer", self.ip, self.port)

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

        self.give_turn_button = Button(root, text="Give Turn", command=self.give_turn)
        self.give_turn_button.pack()

        self.take_turn_button = Button(root, text="Take Turn", command=self.take_turn)
        self.take_turn_button.pack()

    def helloCallBack(self):
        for gesture in self.gestures:
            self.animationService.run(gesture)
            print gesture
            time.sleep(7)




        # self.tts.say("It is territorial and generally a solitary but social predator, requiring large contiguous areas of habitat, which support its requirements for prey and rearing of its offspring. Tiger cubs stay with their mother for about two years, before they become independent and leave their mother's home range to establish their own.")
        # u = self.textBox.get("1.0", "end-1c")
        # u = unicodedata.normalize('NFKD', u).encode('ascii', 'ignore')
        # tts.say(u)

    def start(self):
        self.cancel_id = None
        self.head_yaw()

    def head_yaw(self):
        self.motionProxy.setStiffnesses("Head", 1.0)
        names = "HeadYaw"
        rand = random.randrange(10, 60)
        angleLists = [0.0, 5.0, 0.0]
        angleLists = [angle * math.pi / 180.0 for angle in angleLists]
        timeLists = [1.0, 2.0, 2.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, rand * almath.TO_RAD, 1.0, isAbsolute)
        self.motionProxy.angleInterpolation("HeadPitch", angleLists, timeLists, isAbsolute)
        self.cancel_id = self.textBox.after(1000, self.head_yaw)

    def stop(self):
        if self.cancel_id is not None:
            self.textBox.after_cancel(self.cancel_id)
            self.cancel_id = None

    def speak_next(self):
        angleLists = random.randint(10, 35) * almath.TO_RAD
        timeLists = 1.0
        isAbsolute = True
        self.motionProxy.angleInterpolation("HeadYaw", angleLists, timeLists, isAbsolute)
        self.tts.say(self.speech_list[self.current % self.end])
        self.current += 1

    def take_turn(self):
        self.tts.say("Thank you")
        self.motionProxy.angleInterpolation(["HeadYaw", "LShoulderPitch", "LElbowRoll", "LWristYaw"], [[40 * almath.TO_RAD, 0],
                                                                            [40 * almath.TO_RAD, 100 * almath.TO_RAD],
                                                                                          [-40 * almath.TO_RAD, 0],
                                                                                          [40 * almath.TO_RAD, 0]],
                                            [[1.5, 2.0], [1.5, 3.0], [1.5, 2.0], [1.0, 2.0]], True)
        self.motionProxy.moveTo(0.5, 0.5, 0, _async=True)


    def give_turn(self):
        self.motionProxy.angleInterpolation("HeadYaw", 40 * almath.TO_RAD, 1.0, True)
        self.tts.say("Eeve will take over the presentation now")
        self.motionProxy.moveTo(-0.5, -0.5, 0, _async=True)
        self.motionProxy.angleInterpolation("HeadYaw", 10 * almath.TO_RAD, 1.0, True)


        # self.postureProxy.goToPosture("StandInit", 0.5)
        # names = "LElbowRoll"
        # angleLists = -60 * almath.TO_RAD
        # print angleLists
        # timeLists = 1.0
        # isAbsolute = True
        # self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

root = Tk()
Pepper_For_Cop(root)
root.mainloop()