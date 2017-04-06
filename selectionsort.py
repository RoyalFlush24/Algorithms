def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       print "fillslot value-",fillslot
       positionOfMax=0
       for location in range(1,fillslot+1):
            print "alist second position", alist[location]
            print " alist of positionOfMax",alist[positionOfMax]
            if alist[location]>alist[positionOfMax]:
               positionOfMax = location
               print "positionOfMax",positionOfMax
               print "location is ",location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77]
selectionSort(alist)
print(alist)
