# test the module myFunctions

import myFunctions as mf # importing a module as sth else

# print (mf.factorial(3)) not a good way of testing

print (mf.factorial(-10))
assert mf.factorial(7) == 5040 # test case

print ('All good')