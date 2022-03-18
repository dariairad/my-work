# Lab 7.5 - 7.7

# Lab 6.5 - Student Management Program cont.



import json
students = []
filename="studentData.json"
sample= dict(name='fred', age=31, grades=[1,34,55])
# writeDict () - lab 7.6
def writeDict (obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)
# readDict () - lab 7.7
def readDict():
    with open(filename) as f:
        return json.load(f)

def displayMenu ():
    print ('What would you like to do?')
    print ('\t(a) Add new student')
    print ('\t(v) View students')
    print ('\t(s)Save students')  # new item - lab 7.6
    print('\t(l) load students') # new item - lab 7.7
    print ('\t(q) Quit')
    choice = input ('Type one letter (a/v/q):').strip()
    return choice

def doAdd (students):
    student = {}
    student ['name'] =  input ('Enter name: ')
    student ['modules'] = readModules ()
    students.append (student)
                
def readModules ():
    modules = []
    moduleName = input ('\tEnter the first Module name (blank to quit): ').strip()

    while moduleName != '':
        module = {}
        module ['name'] = moduleName 
        module ['grade'] = int (input ('\t\tEnter grade: '))
        modules.append (module)
        moduleName = input ('\tEnter next module name (blank to quit): ').strip()

    return modules

def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print("\t{}  \t{}".format(module["name"], module["grade"]))   

def doView(students):
    for currentStudent in students:
        print(currentStudent['name'])
        displayModules(currentStudent['modules'])
# doSave - lab7.6
def doSave (students):
    writeDict (students)
    print("students saved")
# doLoad - lab7.7
def doLoad():
    global students 
    students = readDict()
    print ('students loaded')

# students = []
choice = displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        doAdd ()
    elif choice == 'v':
        doView ()
    elif choice == 's':
        doSave ()
    elif choice == 'l':
        doLoad ()
    elif choice != 'q':
        print ('\n\nplease select either a, v, s or q: ')
    choice = displayMenu ()

