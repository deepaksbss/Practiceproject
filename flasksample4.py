fname = input('Enter the name of the file')
letter = input('enter the letter value')
k=0
with open(fname, 'r') as f:
    for line in f:
        print(line)
        words = line.split()
        for val in words:

            for i in val:
                if(letter == i):
                    k=k+1;

print(k)