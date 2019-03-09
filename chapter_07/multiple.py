#for multiple of ten, call with parameeter multiple = 10
def multiple_of(to_check,multiple):
    return not (to_check % multiple)

print(multiple_of(520,5))