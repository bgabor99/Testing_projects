from enum import Enum

# Define the Building enum
class Building(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    Default = 'Default'

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

def is_sum_over_50(engineering_students, art_science_students):
    return engineering_students + art_science_students > 50

def get_bigger_number(engineering_students, art_science_students):
    # in case of equality return art_science_students, because of the requirement
    if engineering_students > art_science_students:
        return "engineers"
    else:
        return "art_science"

def allocate_1(engineering_students, art_science_students):
    engineer_course = Building.Default
    art_science_course = Building.Default

    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        if engineering_students < 10:
            engineer_course = Building.A
        elif 10 <= engineering_students <= 50:
            engineer_course = Building.B
        elif engineering_students > 50:
            engineer_course = Building.D

    if art_science_course != Building.D:
        if art_science_students < 10:
            art_science_course = Building.B
        elif 10 <= art_science_students <= 50:
            art_science_course = Building.C
        elif art_science_students > 50:
            art_science_course = Building.D
    
    return (engineer_course, art_science_course)


def allocate_1_bad(engineering_students, art_science_students):
    engineer_course = Building.Default
    art_science_course = Building.Default

    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course == Building.D:
        if engineering_students < 10:
            engineer_course = Building.A
        elif 10 <= engineering_students <= 50:
            engineer_course = Building.B
        elif engineering_students > 50:
            engineer_course = Building.D

    if art_science_course != Building.D:
        if art_science_students < 10:
            art_science_course = Building.B
        elif 10 <= art_science_students <= 50:
            art_science_course = Building.C
        elif art_science_students > 50:
            art_science_course = Building.D
    
    return (engineer_course, art_science_course)


def allocate_2(engineering_students, art_science_students):
    engineer_course = Building.Default   
    art_science_course = Building.Default

    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        engineering_students_map = {
            engineering_students < 10: Building.A,
            10 <= engineering_students <= 50: Building.B,
            engineering_students > 50: Building.D,
        }
    
        for condition, building in engineering_students_map.items():
            if condition:
                engineer_course = building
                break

    if art_science_course != Building.D:
        art_science_students_map = {
            art_science_students < 10: Building.B,
            10 <= art_science_students <= 50: Building.C,
            art_science_students > 50: Building.D,
        }

        for condition, building in art_science_students_map.items():
            if condition:
                art_science_course = building
                break

    return (engineer_course, art_science_course)


def allocate_2_bad(engineering_students, art_science_students):
    engineer_course = Building.Default   
    art_science_course = Building.Default

    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(art_science_students, engineering_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        engineering_students_map = {
            engineering_students < 10: Building.A,
            10 <= engineering_students <= 50: Building.B,
            engineering_students > 50: Building.D,
        }
    
        for condition, building in engineering_students_map.items():
            if condition:
                engineer_course = building
                break

    if art_science_course != Building.D:
        art_science_students_map = {
            art_science_students < 10: Building.B,
            10 <= art_science_students <= 50: Building.C,
            art_science_students > 50: Building.D,
        }

        for condition, building in art_science_students_map.items():
            if condition:
                art_science_course = building
                break

    return (engineer_course, art_science_course)


def allocate_3(engineering_students, art_science_students):
    engineer_course = Building.Default   
    art_science_course = Building.Default

    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        engineer_course = (
            Building.A if engineering_students < 10
            else Building.B if 10 <= engineering_students <= 50
            else Building.D
        )

    if art_science_course != Building.D:
        art_science_course = (
            Building.B if art_science_students < 10
            else Building.C if 10 <= art_science_students <= 50
            else Building.D
        )

    return (engineer_course, art_science_course)


def allocate_3_bad(engineering_students, art_science_students):
    engineer_course = Building.Default   
    art_science_course = Building.Default

    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        engineer_course = (
            Building.A if engineering_students < 10
            else Building.B if 10 < engineering_students <= 50
            else Building.D
        )

    if art_science_course != Building.D:
        art_science_course = (
            Building.B if art_science_students < 10
            else Building.C if 10 < art_science_students <= 50
            else Building.D
        )
    return (engineer_course, art_science_course)


def allocate_4(engineering_students, art_science_students):
    def get_building(condition_map):
        for condition, building in condition_map:
            if condition:
                return building
        return Building.Default

    engineer_course = Building.Default   
    art_science_course = Building.Default
    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        engineer_course = get_building([
            (engineering_students < 10, Building.A),
            (10 <= engineering_students <= 50, Building.B),
            (engineering_students > 50, Building.D),
        ])

    if art_science_course != Building.D:
        art_science_course = get_building([
            (art_science_students < 10, Building.B),
            (10 <= art_science_students <= 50, Building.C),
            (art_science_students > 50, Building.D),
        ])

    return (engineer_course, art_science_course)


def allocate_4_bad(engineering_students, art_science_students):
    def get_building(condition_map):
        for condition, building in condition_map:
            if condition:
                return building
        return Building.Default

    engineer_course = Building.Default   
    art_science_course = Building.Default
    if is_sum_over_50(engineering_students, art_science_students):
        bigger_group = get_bigger_number(engineering_students, art_science_students)
        if bigger_group == "engineers":
            engineer_course = Building.D
        if bigger_group == "art_science":
            art_science_course = Building.D

    if engineer_course != Building.D:
        engineer_course = get_building([
            (engineering_students < 10, Building.A),
            (10 <= engineering_students <= 50, Building.B),
            (engineering_students > 50, Building.D),
        ])

    if engineer_course != Building.D:
        art_science_course = get_building([
            (art_science_students < 10, Building.B),
            (10 <= art_science_students <= 50, Building.C),
            (art_science_students > 50, Building.D),
        ])

    return (engineer_course, art_science_course)


'''
# main
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

print("allocate_1: ",allocate_1(ENGINEERING_STUDENTS, ART_AND_SCIENCE_STUDENTS))
print("allocate_2: ",allocate_2(ENGINEERING_STUDENTS, ART_AND_SCIENCE_STUDENTS))
print("allocate_3: ",allocate_3(ENGINEERING_STUDENTS, ART_AND_SCIENCE_STUDENTS))
print("allocate_4: ",allocate_4(ENGINEERING_STUDENTS, ART_AND_SCIENCE_STUDENTS))
'''