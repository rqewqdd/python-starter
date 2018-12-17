class coreClass:
    def onBegin(self):
        print('Begin')
    def onAction(self):
        return True
    def onSuccess(self):
        print('Success')
    def onFail(self,message):
        print(message)

class eventPage(coreClass):
    def __init__(self):
        self.onBegin()
        if self.onAction():
            self.onSuccess()
        else :
            message = 'Fail'
            self.onFail(message)

test = eventPage()
