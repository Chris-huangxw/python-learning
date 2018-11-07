__metaclass__ = type
# _*_ coding = UTF-8 _*_


class Person:

    num = 0

    def init(self):
        self.num += 1

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "hello, i'm %s" % self.name

    def __inaccessible(self):
        print "can't see"

    def accessible(self):
        print "can see"
        self.__inaccessible()

class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print "value is ", self.value
class TalkingCalculator(Calculator, Talker):
    pass

m = TalkingCalculator()
m.calculate("(1+2)*3")
m.talk()
