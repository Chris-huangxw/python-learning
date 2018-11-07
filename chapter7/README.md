python中将方法或者特性变为私有（无法从外部访问），只需要在名字前面加上双下划线即可。
'''
class Seretive:
    def __inaccessible(self):
        print "can't see"

    def accessible(self):
        print "can see"
        self.__inaccessible()
'''

现在的__inaccessible从外界无法访问，但是在内部还能使用.

输出结果如下：
can see
can't see
Traceback (most recent call last):
  File "New_Class.py", line 25, in <module>
    pro = Person().__inaccessible()
AttributeError: 'Person' object has no attribute '__inaccessible'

但是其实还是可以在外部访问私有方法__inaccessible()的，因为在类内部所有双下划线开始的名字都被翻译成了类名加单下划线的形式Seretive_inaccessible()，可以通过这个访问到私有方法。
如果实在不想让其他对象访问内部数据，那么可以是用单下划线。所有前面有单下划线的名字都不会被带星号的import语句导入

# 多个超类
'''
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print "value is ", self.value
class TalkingCalculator(Calculator, Talker):
    pass
'''
子类不做任何事情，从自己的超类继承所有的行为。这个被称为多重继承，但是尽量避免使用。
当使用多重继承的时候，如果一个方法从多个超类继承（就是有两个具有相同名字的不同方法），那么要注意超类的顺序，先继承的类会重写后继承的类中的方法。

# 总结
## 对象
对象包括特性和方法。特性只是作为对象的一部分变量；方法是存储在对象内部的函数。（绑定）方法和其他函数的区别在于方法总是将对象作为自己的第一个参数（self）。

## 类
类代表对象的集合，每一个对象（实例）都有一个类。类的主要任务是定义它的实例会用到的方法。

## 多态
多态是实现将不同类型和类的对象进行同样对待的特性---不需要知道对象属于哪个类就可以调用。

## 封装
对象可以将内部状态隐藏（封装）起来。

## 继承
一个类可以是一个或者多个类的子类。子类从超类继承所有方法。可以使用多个超类。普通的实现方式是使用核心的超类和一个或者多个混合的超类
