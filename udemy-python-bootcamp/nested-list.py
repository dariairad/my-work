# nesting a list and indexing a nested list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

matrix = [list1, list2, list3] # list nested under snother list
print (matrix)

list4 = [10, 11, 12]

matrix.append(list4) # add/nest another list at the end of the existing list
print (matrix) 

matrix.pop(0) # remove nested list in postion [0]
print (matrix)

a = matrix[0][0] # 1st object from list1
print (a)


# list comprehension
# grabbing the first element of every row in the matrix object. 

firsts = [row[0] for row in matrix]
print (firsts)