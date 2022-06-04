class Student: 
    def __init__(self, name, id, age): 
        self.name = name 
        self.id = id 
        self.age = age
        
# creates the object of the class Student 
s = Student("John", 101, 22)

# prints the attribute name of the objects 
print(getattr(s, 'name'))

# reset the value of attribute age to 23 
setattr(s, "age", 23)

# prints the modified value of age 
print(getattr(s, 'age')) 
print(hasattr(s, 'id'))

# deletes the attribute age 
delattr(s, 'age')
