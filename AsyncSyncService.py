import qi


class AsyncSyncService:
    def __init__(self, *args, **kwargs):
        self.onBang = qi.Signal()


app = qi.Application()
app.start()
myAsyncService = AsyncSyncService()
s = app.session
id = s.registerService("asyncfoo", myAsyncService)
app.run()
