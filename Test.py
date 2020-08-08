import qi
import sys
from pprint import pprint

class Test:

    def bar(self):
        print("bar")

if __name__ == "__main__":

    app = qi.Application()
    # start the session
    app.start()
    session = app.session
    tts = session.service("ALTextToSpeech")
    motion = session.service("ALMotion")
    sayOp = tts.say("This is a very very very very long sentence.", _async=True)
    moveOp = motion.moveTo(1, 0, 0, _async=True)
    # Wait for both operations to terminate.
    sayOp.wait()
    moveOp.wait()

# if __name__ == "__main__":
#     app = qi.Application(sys.argv)
#
#     # start the eventloop
#     app.start()
#
#     almemory = app.session.service("ALMemory")
#     pprint(almemory.getDataListName())

# from naoqi import ALProxy
#
# ip = "127.0.0.1"
# port = 52629
#
# tts = ALProxy("ALTextToSpeech", ip, port)
# tts.say("Hello from PyCharm!")
# python MyClient.py --qi-url=tcp://127.0.0.1:57341
