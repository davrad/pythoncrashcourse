ordinals = [i for i in range(1,10)]
for ordinal in ordinals:
    if ordinal == 1:
        print("1st")
    elif ordinal == 2:
        print("2nd")
    elif ordinal == 3:
        print("3rd")
    else:
        print(str(ordinal)+"th")