from easygui import *

#moveDecimal: takes number and moves decimal place until it becomes int for rounding
#arguments: num, number to be moved; spaces, number of spaces shifted
#returns: new int number
def moveDecimal(num, spaces):
	while int(num) != num:
		num *= 10**spaces
	return num
#perfectSquare: takes new int and checks if it is a perfect square
#arguments: num, int in question
#returns: variable - true means it is and false means it isn't
def perfectSquare(num):
    num = int(moveDecimal(num,2))
    for elem in range(num):
        if elem ** 2 == num:
            return True
    return False
#squareRoot: finds square root of number
#arguments: counter, counts how many decimal places square root needs to find; sqrtnum, float being "rooted"
#returns: number if number is square root, or counter if number isn't
def squareRoot(counter, sqrtnum):
    counter = 0
    for i in range(sqrtnum):
        sqrtnum = counter**.5
        counter += 1
    if perfectSquare(sqrtnum):
        return sqrtnum
    else:
        return counter

#program body
sqrtdec_counter = 0
findsqrt = 0
repeat = 'Again!'
#sets all parameters needed in function
while repeat == 'Again!':
    msgbox("Welcome to the Square Root Program!", "Square Root Program")
    replist = ['Again!', 'Leave...']
    findsqrt = enterbox("Please enter a number to find the square root of: ", "Square Root")
    findsqrt = float(findsqrt)
    #changes number into float of number for easier rounding
    sqrtdec = enterbox("Please enter how many numbers to approximate to: ", "Square Root")
    sqrtdec = int(float(sqrtdec))
    #changes number into int(float of number for number to be whole
    textbox("This is the final approximated square root of your number:", "Square Root", str(squareRoot(findsqrt, sqrtdec)))
    #prints result and allows user to repeat
    repeat = buttonbox("Repeat? ", "Resetting", replist)

msgbox("Bye!", "Exit")
