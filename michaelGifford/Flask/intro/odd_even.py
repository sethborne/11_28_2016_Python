def odd_even(x,y):
    for i in range (x,y):
        if (i%2 == 0):
            n = 'even'
        else:
            n = 'odd'
        print 'Number is {}. This is an {} number.'.format(i,n)

odd_even(1,2001)
