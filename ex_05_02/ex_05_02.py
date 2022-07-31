largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        str = int(num)
        if smallest is None:
            smallest = str
        elif str < smallest:
            smallest = str

        if largest is None:
            largest = str
        elif str > largest:
            largest = str
            
    except:
        print('Invalid input')
        continue



print("Maximum is", largest)
print("Minimum is", smallest)
