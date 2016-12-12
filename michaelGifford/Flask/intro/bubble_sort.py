import datetime
from random import randint

def bubbleSort(arr):
    count = 0
    temp = 0
    for i in range(len(arr)-1):
        temp = arr[i+1]
        if arr[i] > temp:
            arr[i+1] = arr[i]
            arr[i] = temp
            count = count + 1
    # print (arr)
    if count == 0:
        print (arr)
        return arr
    else:
        # print (count)
        bubbleSort(arr)


def randList():
    arr = [randint(1,10000) for i in range(101)]
    return arr


t = datetime.datetime.now()
for i in range(1):
    bubbleSort(randList())
print (datetime.datetime.now() - t)

# randList()
