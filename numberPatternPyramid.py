


x = int(input("Enter a number 0 to 10 : "))
print("First pattern")
# First pattern
#           0
#          010
#         01210
#        0123210
#       012343210

numString = ''
for n in range(x):
    numString = numString + str(n)
    print((x-n)* " " + numString + numString [:-1] [::-1])
    
    
print("Second pattern")
# Second pattern
#           0
#          101
#         12021
#        1230321
#       123404321
numString = ""
for n in range((x)):
    if (n!=0):
        numString = numString + str(n)
    print((x-n)* " " + numString + "0" + numString [::-1]) 
print("Third pattern")
# Third pattern
#           0
#          101
#         21012
#        3210123
#       432101234
numString = ""
for n in range((x)):
    if (n!=0):
        numString = numString + str(n)
    print((x-n)* " " + numString [::-1] + "0" + numString) 
