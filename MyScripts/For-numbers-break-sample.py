for number in [2, 3, 4, 5, 6, 7, 8, 9]:
    if number % 2 == 0:
        print("%s is even number" % number)
    elif number > 7:
        break
    else:
        continue
    print("You can't see me, cause I'm odd number")