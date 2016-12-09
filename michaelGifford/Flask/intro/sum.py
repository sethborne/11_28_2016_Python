a = [1,2,5,10,255,3]

def sum(arr):
    x = 0;
    for i in range (0,len(arr)):
        x = arr[i] + x
    print x

sum(a)
