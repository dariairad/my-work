# Lab 6.3 - Student Management Program cont. 

# We will now use that function. Create a program that keeps displaying the
# menu until the user picks q. if the user chooses a then call a function called
# doAdd() if the user chooses v then call a function called doView().

def displayMenu ():
    print ('What would you like to do?')
    print ('\t(a) Add new student')
    print ('\t(v) View students')
    print ('\t(q) Quit')
    choice = input ('Type one letter (a/v/q):').strip()

    return choice

def doAdd ():
# to be added
    print ('in adding')
def doView ():
# to be added
    print ('in viewing')

# main program

choice = displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        doAdd ()
    elif choice == 'v':
        doView ()
    elif choice != 'q':
        print ('\n\nplease select either a, v, or q: ')
        choice = displayMenu ()
