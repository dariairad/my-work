# Lab 7 - Jason
# Write a function that will store a simple Dict to a file as JSON. TEST IT

import json

filename = 'testdict.json'
sample = dict (name = 'fred', age = 31, grades = [1, 34, 55])

def writeDict (obj) :
    with open (filename, 'wt') as f:
        json.dump (obj, f, indent = 1)

writeDict (sample)


# dump ()
# indent 
# https://www.geeksforgeeks.org/json-dump-in-python/