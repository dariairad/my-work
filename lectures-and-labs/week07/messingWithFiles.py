# Lecture 7 - Files

# Creating a file: 

filename = 'text.txt'
with open (filename, 'wt') as f:
    f.write ('Hello World')

# reading a file one line at a time:

with open ('messingWithFiles.py', 'rt') as f:
    for line in f:
        # print ('line :', line [:-1])
        print (line, end = '')