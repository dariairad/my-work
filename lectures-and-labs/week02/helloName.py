# Uses a variable to greet
# Author: Daria Sep
name = "Daria" 
print ('Hello ' + name) 

# this won't work > cannot print int with str
age = 30
# print ('Your age is ' + age)
print ('Your age is ' + str(age))
print ('Hello {} \tYour age is {}'.format(name,age))