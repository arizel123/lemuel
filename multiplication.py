#ODD NUMBER
for x in range(1,21):
    for y in range(1,21):
        z = x * y

        if z % 5 == 4:
            print("O" , end = "\t")
        else:
            print(x*y , end = "\t")

    print()
print()

#EVEN NUMBER
for x in range(1,21):
    for y in range(1,21):
        z = x * y

        if z % 4 == 3:
            print("E" , end = "\t")
        else:
            print(x*y , end = "\t")

    print()
