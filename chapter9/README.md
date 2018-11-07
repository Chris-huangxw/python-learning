# 构造方法

## super函数

该函数只能在新式类中使用，当前类和对象都可以作为super函数的参数使用，调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法。
```Python
__metaclass = type
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "Aaaah...."
            self.hungry = False
        else:
            print "No, thanks."
#Songbird 继承了 Bird
class SongBird(Bird):  
    def __init__(self):
        super(SongBird, self).__init__()
        #调用超类的构造方法来初始化
        self.sound = "Squawk"
    def sing(self):
        print self.sound
```
即使类已经继承了多个超类，也只需要使用一次super函数
super函数实际返回了一个super对象，这个对象负责进行方法解析。当对其特性进行访问时，它会查找所有超类（以及超类的超类），知道找到所需的特性为止，或者引发一次AttributeError。
