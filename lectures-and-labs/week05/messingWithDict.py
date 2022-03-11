# Lecture 5.2 Dictionaries


car = {
    'make' : 'Ford',
    'model' : 'Mondeo',
    'year' : 2006,
    'owner' : {
        'name' : 'Andrew',
        'driver-number' : 1123  # dict within a dict
    }
}

# attr = 'make'
# print (car[attr])

print (car['owner'])
print (car ['owner'].get('name'))  
print (type(car ['owner'].get('names')))   # get check is variable is available. if not, doesn't throw an error but gives output none


