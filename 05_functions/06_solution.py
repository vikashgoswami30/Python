
def fact(value):
    if value==0:
        return 1
    else:
        return value * fact(value-1)


print(fact(5))
 