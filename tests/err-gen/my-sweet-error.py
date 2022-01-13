import random

def dictErr():
    return {
    ZeroDivisionError: lambda msg: ZeroDivisionError_(msg),
    ValueError: lambda msg: ValueError_(msg),
    NameError: lambda msg: NameError_(msg),
    TypeError: lambda msg: TypeError_(msg),
    }

def error(name=None,errMsg="You shall not pass!"):
    dictErr()[name](errMsg)

def randomErr(errMsg="You shall not pass!"):
    name=random.choice(list(dictErr().keys()))
    dictErr()[name](errMsg)
    
def ZeroDivisionError_(msg):
    print(msg)
    a=0
    a=a/a

def ValueError_(msg):
    print(msg)
    int(";;;")

def NameError_(msg):
    print(msg)
    a=b-x

def TypeError_(msg):
    print(msg)
    f = open(None, "r")
    print(f.read())


