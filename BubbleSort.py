def bubble_sort (mylist):
    last_index = len(mylist) - 1
    for z in range(0, last_index):
        for x in range(0, last_index):
            print(mylist)
            if mylist[x] > mylist [x + 1]:
                mylist[x], mylist [x + 1] = mylist [x + 1], mylist[x]
    return mylist

oldlist = [45, 85, 65,26,58,4,-8,25,63,47]
print( "OLD LIST " + str(oldlist))
newlist = bubble_sort(oldlist).copy()
print("New List" + str(newlist))


