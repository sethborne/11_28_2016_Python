a = [1,2,5,10,255,3]

def ave(arr):
    x = 0;
    for i in range (0,len(arr)):
        x = arr[i] + x
    a = x/len(arr)
    print a

ave(a)
