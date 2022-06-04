from typing import NewType
 
# Create a new user type called 'StudentID' that consists of
# an integer
StudentID = NewType('StudentID', int)
sample_id = StudentID(100)
from typing import NewType
# Create a new user type called 'StudentID'
StudentID = NewType('StudentID', int)
def get_student_name(stud_id: StudentID) -> str:
    return str(input(f'Enter username for ID #{stud_id}:\n'))
stud_a = get_student_name(StudentID(100))
print(stud_a)
stud_b = get_student_name(-1)
print(stud_b)
