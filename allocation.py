from enum import Enum

# Define the Building enum
class Building(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

# Define the number of registered students for each faculty
ENGINEERING_STUDENTS = 0
ART_AND_SCIENCE_STUDENTS = 0

def get_engineering_students_number(default_value):
    engineering_students_input = input("Enter the number of students in the Engineering faculty: ")
    if engineering_students_input:
        return int(engineering_students_input)
    else:
        return default_value

def get_art_and_science_students_number(default_value):
    art_and_science_students_input = input("Enter the number of students in the Art and Science faculty: ")
    if art_and_science_students_input:
        return int(art_and_science_students_input)
    else:
        return default_value

def allocate_1(engineering_students, art_science_students):
    if engineering_students < 10:
        return Building.A
    elif 10 <= engineering_students <= 50:
        return Building.B
    elif art_science_students < 10:
        return Building.B
    elif 10 <= art_science_students <= 50:
        return Building.C
    else:
        return Building.D

'''
ENGINEERING_STUDENTS = get_engineering_students_number(20)
ART_AND_SCIENCE_STUDENTS = get_art_and_science_students_number(40)
# Handle negative engineering_students
if ENGINEERING_STUDENTS < 0:
    raise ValueError("Number of engineering students cannot be negative or above ")
# Handle negative engineering_students
if ART_AND_SCIENCE_STUDENTS < 0:
    raise ValueError("Number of Art and Science students cannot be negative")

print("ENGINEERING_STUDENTS: ", ENGINEERING_STUDENTS)
print("ART_AND_SCIENCE_STUDENTS: ", ART_AND_SCIENCE_STUDENTS)

print(allocate_1(ENGINEERING_STUDENTS, ART_AND_SCIENCE_STUDENTS))
'''