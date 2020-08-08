import qi
import sys

# create an application
from MyFooService import MyFooService

app = qi.Application()
app.start()

myfoo = MyFooService()

s = app.session
id = s.registerService("foo", myfoo)

app.run()