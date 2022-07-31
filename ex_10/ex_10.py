fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1


# print(di)

# 가장 큰 값 찾기
#largest = -1
#theword = None
#for k,v in di.items():
    # print (k,v)
    #if v > largest :
        #largest = v
        #theword = k
#print(theword, largest)

# Key, Value 값 변경 및 정렬
tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

# print('Flipped', tmp)
tmp = sorted(tmp, reverse = True)
# print('Sorted', tmp[:5])

for v,k in tmp[:5] :
    print(k,v)
