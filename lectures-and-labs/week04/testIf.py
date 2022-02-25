# Lecture 04 - if statement

if True:
    #statements
    print ('condition is true')

a = 2
if a == 3:
    print ('yes, the world is sane')
else:
    print ('3 is not equal to 2')


aNumber = 5
if (aNumber % 2) == 0: # brackets for clarity only
    print (aNumber, 'is even')
elif (aNumber % 3) == 0:
    print (aNumber, 'is divisable by 3')
else:
    print (aNumber, 'is not even or divisable by 3')
