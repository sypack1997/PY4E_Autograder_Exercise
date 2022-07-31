num = 0
tot = 0
while True :
    a = input('Enter a number:')
    if a == 'done' :
        break
    try :
        b = float(a)
    except :
        print('Invald input')
        continue

    num = num + 1
    tot = tot + b

print(tot, num, tot/num)
