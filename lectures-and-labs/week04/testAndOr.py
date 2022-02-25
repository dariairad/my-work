# Lecture 04 - Ands and Ors

number = -1
if (number >=0) and (number <= 100):
    print ('valid')

# can't be 'and' > will result in true + false = false
if number <=0 or number >= 100: 
    isBad = True
    print ('stop')
else: 
    isBad = False
    print ('go')