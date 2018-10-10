#==============BUBBLE SORT===============
import random

sortnum = []

for nums in range(100):
    sortnum.append(random.randrange(101))
#generates 1000 random whole numbers from 0-100
print "This is the unsorted list: " + "\n" + str(sortnum) + "\n"

changed = False
while changed == False:
    changed = True
#sets boolean to false, and allows following code to loop until fully sorted
    for numindex in range(len(sortnum)-1):
        if sortnum[numindex] < sortnum[numindex + 1]:
            changed = False
#takes length of one less than current number and sets boolean to false if number is less than one more than the number
            swapnum = sortnum[numindex]
            sortnum[numindex] = sortnum[numindex + 1]
            sortnum[numindex + 1] = swapnum
#makes dummy variable for current number, and makes each number equal to following number

print "This is the sorted list: " + "\n" + str(sortnum)

#==============INSERTION SORT==============
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
