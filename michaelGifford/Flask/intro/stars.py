def draw_stars(arr):
    for i in range(len(arr)):
        if type(arr[i]) is int:
            print ('*'*arr[i])
        elif type(arr[i]) is str:
            print (arr[i][0].lower()*len(arr[i]))

x = [4,6,1,3,5,7,25,'Michael','Rodenel','Bernie','Amy']
draw_stars(x)
