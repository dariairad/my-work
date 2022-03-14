def displayMenu ():
    print ('What would you like to do?')
    print ('\t(a) Add new student')
    print ('\t(v) View students')
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
    print ('\tName \tGrade')
    for module in modules:
        print("\t{} \t{}".format(module['name'], module['grade'])) 

def doView(students):
    for currentStudent in students:
        print(currentStudent['name'])
        displayModules(currentStudent['modules'])

def doView (students):
    print ('', students)