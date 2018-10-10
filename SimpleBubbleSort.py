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
