import os,sys
fname=input('Enter the file name')
if os.path.isfile(fname):
    f=open(fname,'r')


lcount=ccount=wcount=0
for i in f:

    lcount=lcount+1
    ccount=ccount+len(i)
    words=i.split()
    print(words)
    wcount=wcount+len(words)
print(lcount)
print(ccount)
print(wcount)