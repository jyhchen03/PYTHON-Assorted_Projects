import random

sortnum = []
unsortnum = []

for num in range(100):
    unsortnum.append(random.randrange(101))
print "These are the unsorted numbers: " + "\n" + str(unsortnum) + "\n"
#creates list for later sorted numbers and another for current random numbers

sort = False
while sort == False:
    largenum = 0
#puts program in booleans and loop for as long as numbers are not fully sorted
    if len(unsortnum) != 0:
        for currentnum in unsortnum:
            if currentnum > largenum:
                largenum = currentnum
#if there are still numbers in unsorted list it moves them from one list to the other using following algorithm
        sortnum.append(largenum)
        unsortnum.remove(largenum)
#moves numbers from unsorted list to sorted, and removes those moved numbers
    else:
        sort = True
#while loop and boolean validation stops when numbers are sorted

print "These are the sorted numbers: " + "\n" + str(sortnum)
