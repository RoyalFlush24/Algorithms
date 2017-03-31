def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        print "length of list"+ str(len(alist))
        print "middle of list",mid
        lefthalf = alist[:mid]
        print lefthalf
        righthalf = alist[mid:]
        print righthalf
        print "%%%%%%%%%%%%%%%%%%%%"

        mergeSort(lefthalf)
        print "left----- half --------done"
        mergeSort(righthalf)
        print "right----- half --------done"

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                print "lefthalf" + str(lefthalf[i])
                print "righthalf" + str(righthalf[j])
                alist[k]=lefthalf[i]
                print "K List = " + str(alist[k])       
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            print alist[k]

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
