# Lab 4.1.4 - Extra

# Program from Lab 4.1.1 (lab4.1.1-isEven.py) modified so it keeps prompting the user for a number until the user enters -1

# Author: Daria Sep

while True: #loop
    number = int (input ('Enter number -1: '))
    if number == -1:
        print ('Thank you')
        break
    else:
        print ('Input incorrect. Please try again. ')
        continue #continues and prompts input request again


# ref: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

    
    
    
    