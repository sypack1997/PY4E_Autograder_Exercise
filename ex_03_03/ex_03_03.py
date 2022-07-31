gr = input("Grade: ")
try :
    sc = float(gr)
    sc >= 0.0
    sc <= 1.0
except :
    print ("Error, please enters a value out of range")
    quit()

if sc >= 0.9 :
    print("A")
elif sc >= 0.8 :
	print("B")
elif sc >= 0.7 :
	print("C")
elif sc >= 0.6 :
	print("D")
else :
	print("F")
