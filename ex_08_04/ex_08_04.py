fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh :
    line = line.rstrip()
    asd = line.split()
    for dd in asd :
        if dd not in lst :
            lst.append(dd)

lst.sort()
print(lst)
