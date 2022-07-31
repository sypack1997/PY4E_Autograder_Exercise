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
    word = word[1:2]
    for w in word:
        di[w] = di.get(w,0) + 1
# print(di)

count = -1
mail = None
for k,v in di.items():
    if v > count:
        count = v
        mail = k

print(mail, count)
