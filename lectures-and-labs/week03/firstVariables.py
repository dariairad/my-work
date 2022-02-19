# Messing around with variable types

ageOfPatient = {}
age = 3

# We need to convert the type to str so we can concate it to the message
print ('Type ofageOfPatient is: '+ str(type(ageOfPatient)))
print ('Type of age is: ' + str(type(age)))

# Show how to convert int to str and str to int
nextYear = int(age) + 1
print ('Next year you will be ' + str(nextYear))