

from threading import *
def dispaly():
    for i in range(1,11):
        print('child thread')
t=Thread(target=dispaly)