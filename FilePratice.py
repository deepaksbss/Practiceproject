import csv
def searchName():
    scr=input('enter the name of the employee to retrive the record')
    f=open('afilecsv.csv','r+')
    out=csv.reader(f)
    for line in out:
        if scr == line[1]:
            print(line)

def searchsalary():
    scr= input('enter the employe salary')
    f = open('afilecsv.csv', 'r+')
    out = csv.reader(f)
    for line in out:
        if scr == line[1]:
            print(line)
    
print('please enter 1 for retrive the name')
print('please enter 2 for retrive the salary')
scr =int(input('Enter the name option press 1'))

if scr == 1:
    searchName()
elif scr == 2:
    searchsalary()
else:
    print('please provide the valuable option')
