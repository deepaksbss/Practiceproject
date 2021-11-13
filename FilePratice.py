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


if scr == 1:
    searchName()

