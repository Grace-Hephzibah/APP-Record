<<<<<<< HEAD
import functools
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis))   
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis))
=======
import functools
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis))   
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis))
>>>>>>> c7462266bf5bbe709727b07d9e164f25601f4cf7
