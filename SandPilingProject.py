#maxFind: takes list of numbers and finds the max of those numbers
#arguments: list, list checked
#returns: current number which is also the max of the list
def maxFind(list): #algorithm talked about in class
    currentnum = list[0]
    for i in list:
        if i > currentnum:
            currentnum = i
    return currentnum

#sandPiling: main algorithm for piling sand, taking into account collapsing
#arguments: grains, number of grains being dropped
#returns: list with the piled sand on table
def sandPiling(grains, place):
    width = len(place)
    for j in range(maxFind(place)):
        for i in range(width-2, -1, -1):
            if place[i] - place[i-1] >= 2:
                place[i] -= 1
                place[i-1] += 1
            elif place[i] - place[i+1] >= 2:
                place[i] -= 1
                place[i+1] += 1
                
    #initial collapse
    for i in range(grains):
        place[width/2] += 1
        for elem in range(width-2, -1, -1):
            if place[elem] - place[elem-1] >= 2:
                place[elem] -= 1
                place[elem-1] += 1
            elif place[elem] - place[elem+1] >= 2:
                place[elem] -= 1
                place[elem+1] += 1
                
    #falling grain collapse  
    for j in range(maxFind(place)):
        for i in range(width-2, -1, -1):
            if place[i] - place[i-1] >= 2:
                place[i] -= 1
                place[i-1] += 1
            elif place[i] - place[i+1] >= 2:
                place[i] -= 1
                place[i+1] += 1
                
    #final collpase
    return place

#program body
tablewidth = int(raw_input("Please enter table length: "))
grainnum = int(raw_input("Please enter number of grains to drop: "))
listtablewidth = []
graincounter = 1

for i in range(tablewidth):
    columnspec = int(raw_input("Please enter number of grains in column " + str(graincounter) + ":" + " "))
    graincounter += 1
    listtablewidth.append(columnspec)
    
print "This is what the table looks like:", '\n', sandPiling(grainnum, listtablewidth)
