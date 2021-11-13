def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor(func):
   