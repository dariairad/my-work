# Lab 6.4 - Student Management Program Cont.

# We can now write the function doAdd(students). So we need to think what we want this to do.
#   a. Read in the student’s name (that is straightforward)
#   b. Read in the module names and grades (this is a bit more complicated
#      so let’s put this in separate function and think about it by itself, see 5. below)
#   c. Test this function, it creates a student dict, we can print that out.
#   d. We should add the student dict to list (pass this list in)
#   e. Test this.

students = []

def readModules ():
    return []
def doAdd (students):
    currentStudent = {}
    currentStudent ['name'] = input ('Enter name: ')
    currentStudent ['modules'] = readModules ()

    students.append(currentStudent)

# test

doAdd (students)
doAdd (students)
print (students)