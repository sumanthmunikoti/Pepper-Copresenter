import time

import qi
import sys

ip = "127.0.0.1"
port = 57581


def onBangCb(i):
    print "bang:", i


def talkNMove(i):
    # foo.bang()
    print "Ok", i


def mycrazydelay(delay, finish_callback):
    time.sleep(delay)
    if finish_callback:
        finish_callback(delay)
    return delay


app = qi.Application()
app.start()
s = app.session
# Getting a service named foo which has been registered at the server
foo = s.service("foo")

# registering onBangCb as the callback on onBang
# foo.onBang.connect(mycrazydelay)

foo.onBang.connect(talkNMove)
foo.bang()
