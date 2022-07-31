name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
di = dict()

for line in fh :
    line = line.rstrip()
    word = line.split()
    if len(word) < 1 or word[0] != 'From':
        continue
    word = word[5]
    # print(word)
    time = word.split(':')
    asd = time[0:1]
    for w in asd:
        di[w] = di.get(w,0) + 1
# print(di)

lst = list()
for key, val in di.items() :
    new = (key, val)
    lst.append(new)
lst = sorted(lst)
# print(lst)

for key, val in lst :
    print(key,val)
