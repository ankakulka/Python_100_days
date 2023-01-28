# SCOPE

# Global scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
def myfunc():
  global x
  x = 300

# Local scope
# A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.


# Naming Variables
# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope (outside the function)
#  and one available in the local scope (inside the function):

# NOTE: There is no block scope in Python:
# for, while, if etc. don't count as a local scope in Python
# local scope only works for namespaces - variables and functions