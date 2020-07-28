from array import *

numbers = array('i', [13, 14, 11, 20, 17, 20, 21, 50, 90, 60])

def linearsearch (num):
    
    matchfound = False
    
    for number in numbers:
        
        if (number==num):
            matchfound = True; 
            break
     
    if(matchfound):
        print("Match found for: " + str(num))     
    else:
        print("Match not found for: " + str(num))

num = int(input("Input a number to search: "))

linearsearch(num)