data="All Students are STUPIDS"
f=open("asample1.txt","w")
f.write(data)
with open('asample1.txt','r+') as f:
    sm = f.read()
    print(sm)
    print(f.tell())
    f.seek(17)
    print('after the seek count', f.tell())
    f.write('learning python')
    f.seek(0)
    t=f.read()
    print(t)