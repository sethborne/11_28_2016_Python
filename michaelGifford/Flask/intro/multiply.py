arr = [10,20,50,80]

def multiplyBy(arr,y):
    newarr = []
    for i in range(0,len(arr)):
        newarr.append(arr[i] * y)
    print newarr

multiplyBy(arr,5)
