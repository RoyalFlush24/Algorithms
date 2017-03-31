#bubble sort program

def bubbleSort(list):
  print "length of list",len(list)
  for passes in range(0, len(list)-1):
    print "pass ------------",passes
    for element in range(0,len(list)-1 - passes):
      print "inner loop",element
      print str(list[element]) + "-"+ str(list[element +1])
      if list[element] > list[element+1]:
        list[element],list[element+1]=list[element+1],list[element]
        print "new values "
        print list[element] 
        print list[element + 1]
        print "new list"
        print list
  return list
  
myList= [34,96,77,3,12,1]
print (bubbleSort(myList))
