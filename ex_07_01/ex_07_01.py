man = open('mbox-short.txt')
print(man)

for girl in man:
    boy = girl.rstrip()
    print(boy.upper())
