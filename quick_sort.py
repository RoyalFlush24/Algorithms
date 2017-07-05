# quick sort implementation
"""
This algorithm consist of 3 methods:
quickSort() - for sorting the array list according pivot we choose, here I am taking middle element of array as pivot.
swap() - for swapping the left and right references.
partition() - for partition the sub items.
"""
def  quickSort(items, leftIndex, rightIndex):
           """ this method will sort the list"""
           if (len(items) >1):
                      # as long as array has two element , we can partition it.
                      pivotIndex=partition(items,leftIndex,rightIndex)
                      print " The Pivot is : ", pivotIndex

           # if the left reference  hasn't been incremented to
           # reach the pivot yet, we want to keep comparing it
           if (leftIndex < pivotIndex -1):
                      quickSort(items,leftIndex,pivotIndex - 1)

           # if the right reference hasn't been reached to
           # pivot index yet, we keep on comparing yet
           if(pivotIndex < rightIndex):
                      quickSort(items,pivotIndex,rightIndex)

           # return sorted list
           return items

def partition(items,left,right):
           """ The partition method will take list of items, left reference and right
                   reference. Both left and right are indexes  to indicate where
                   the pointers should start. """
           pivot=items[((left+right) / 2)]  # declare the pivot reference (middle one)
           l=left # left mark
           r=right  # right mark
           print " the pivot is under  partition:  ",pivot
           print "left mark is  ",items[left]
           print "right  mark is  ", items[right]

           # once the left mark is greater than right mark
           # we have finished sorting the set of items and we can return
           while (l <= r):
                      # if the left mark is less than pivot , then increment it.
                      # move the pointer to more step (right)
                      while(items[l] <pivot ):
                                 l+=1
                                 print " l is pointing to : ",items[l]
                      # if the right mark is greater than pivot , then decrement it.
                      # move the pointer to left
                      while (items[r] > pivot) :
                                 r -=1
                                 print " r is pointing to : ",items[r]
                                 
                      # if the left mark is greater than pivot, right mark is less then pivot , then
                      # swap the two elements 
                      if (l <= r):
                                 print " now swapping l and r pointers:  ", items[l] ,  items[r]
                                 swap(items, l, r)  # call swap method here
                                 # after swapping , increment left mark pointer and decrement right mark pointer
                                 l +=1   
                                 r -=1
                                 print  "l is pointing to :  ", items[l]
                                 print  "r is pointing to :  ", items[r]
                                 
           # the left mark (l) will be your new pivot 
           return l

def swap(items, leftPointerIndex, rightPointerIndex):
           """ this method will swap the left and right mark elements"""
           # first, create a temporary reference for the left item
           tempReference=items[leftPointerIndex]
           # assign the right mark element to left mark element
           items[leftPointerIndex]=items[rightPointerIndex]
           # assign temporary reference value to right mark 
           items[rightPointerIndex]=tempReference
 
items= [19, 22, 63, 105, 2, 46]   # list for  sorting
print quickSort(items,0,len(items) - 1)   # call quickSort() method
