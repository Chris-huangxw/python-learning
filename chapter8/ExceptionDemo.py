# _*_ coding = UTF-8 _*_

try:
    x = input('enter a number:')
    y = input('enter a number:')
    print int(x)/int(y)
except (ZeroDivisionError, TypeError), e:
    print e
    print 'error'
