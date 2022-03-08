# Lecture 4.2 For Loops

# Often used with lists
# Format:

# for elem in list:
    # statements

# for number in range (1,10):
    # statements

boats = ['Sigma', 'Beneteau', 'Swam'] 
for boat in boats:
    print ('I\'d prefer to be out on a '+ boat)
    # if adding int to the list then str(boat)

for number in range (1,10): # 1-9, does not include 10. upwards only
    print ('Hello', number)