# Lecture 7 - Files

# messing with os module

import os

filename = 'test.txt'
if os.path.exists(filename):
    print (filename, "already exists")
else:
    print(filename, "does not exist do you want to create it?")

# os.remove (filename) # to delete existing file