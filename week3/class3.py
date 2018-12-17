class cal:
    def __init__(self):
        self.result = 0
    def add(self, num1,num2):
        self.result = num1 + num2
        return self.result
    def sub(self, num1,num2):
        self.result = num1 - num2
        return  self.result

class moreGoodCal(cal):
    def mul(self, num1,num2):
        self.result = num1 * num2
        return  self.result

calTest = moreGoodCal()
print(calTest.add(3,4))
print(calTest.sub(3,4))
print(calTest.mul(3,4))
