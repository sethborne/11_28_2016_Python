def odds(x,y):
    for count in range (x,y):
        if (count%2 != 0):
            print count

# odds(1,1001)


def fives(x,y):
    for count in range (x,y):
        if (count%x == 0):
            print count

fives(5,1000001)
