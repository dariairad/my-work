# Lecture 4.2 While Loops

# Format:

# while condition
    # statements

count = 0 # need to initialise
while count < 10:
    print (count)
    count +=1 # variable must change otherwise the loop will be infinite

count = 10 
while count >= 0:
    print (count)
    count -= 1  
print ('Blast Off') 

val = input ('Enter something (q to quit):')
while val != 'q':
    print ('you said: ' + val)
    val = input ('q to quit:')
print ('Goodbye')

