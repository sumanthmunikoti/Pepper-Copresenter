import qi


class MyFooService:
    def __init__(self, *args, **kwargs):
        # define a signal 'onBang'
        self.onBang = qi.Signal()

    # define a bang method that will trigger the onBang signal

    def bang(self):
        print "bang"
        # trigger the signal with 42 as value
        tts = s.service("ALTextToSpeech")
        motion = s.service("ALMotion")
        sayOp = tts.say("This is a very very very very long sentence.", _async=True)
        moveOp = motion.moveTo(1, 0, 0, _async=True)
        # Wait for both operations to terminate.
        sayOp.wait()
        moveOp.wait()
        self.onBang(42)


app = qi.Application()
app.start()

myfoo = MyFooService()

s = app.session
id = s.registerService("foo", myfoo)

app.run()
