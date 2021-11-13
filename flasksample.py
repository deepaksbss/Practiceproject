# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def smartlogic(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner
@smartlogic
def div(a,b):
    print(a/b)


div(2,4)