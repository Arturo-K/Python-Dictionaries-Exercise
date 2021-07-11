def add_student(table,new_student):
    '''Add a student to table'''
    table[new_student] = {} #create a new key,value pair in table dictionary
    return table

def delete_student(table,del_student):
    """Delete student from table"""
    table.pop(del_student) #remove student key and corresponding value dictionary
    return table

def delete_course(table,del_course):
    """Delete a course from a table"""
    for key in table:                    #iterating through the dictionary keys
        table[key].pop(del_course, None) # delete course and related grade
    return table

def add_course(table,new_course):
    """Add a course to a table"""
    for name, data in table.items(): #iterate through keys and values of dictionary
        table[name][new_course] = 0  #add course for every student with grade as zero
    return table

def add_grade(table,student,course,grade):
    """Add a grade for a course for a certain student"""
    table[student][course] = grade
    return table

def update_grade(table,student,course,new_grade):
    """Update a grade for a course  for a certain student"""
    table[student][course] = new_grade
    return table

def find_grade(table,student,course):
    """Find the grade of a course for a student"""
    grade = table[student][course]
    print(student.title() + "'s grade in",course,"is",str(grade)+".")

def calc_student_avg(table,student):
    """Calculate average of all course grades for a certain student"""
    total = 0
    num = 0
    for value in table[student].values():   #accessing grades of selected student
        total += value  #setting new total cumulatively
        num += 1    #calculating number of grades

    return round(total/num, 2)  

def avg_allstudents(table,course):
    """Calculate average of all student grades for a certain course"""
    total = 0
    entries = 0
    for value in table.values(): #iterating through the values of the nested dictionary
            #accessing grades of selected course and cumulatively summing values
            total += value[course]
            entries += 1
    
    return round(total/entries, 2)

def highest_student(table, course):
    """Return name of student who achieved highest grade in a course"""
    max_value = 0
    high_student = " "
    for key,value in table.items(): #iterating through the dictionary
        try:
            if value[course] > max_value:   #comparing student grade to highest recorded mark
                max_value = value[course]   #setting new highest value as maximum
                high_student = key  #setting student with highest value iterated
        except KeyError:
            pass
    return high_student

def failed_students(table, course):
    """Return names of students who failed a course"""
    failed = [] #list to store failed students
    for key,value in table.items():
        if value[course] < 60:  #selecting values below 60
            failed.append(key)  #adding failed student to list
    return failed

def display_table(table):
    """Display table"""
    print("\n")
    for key,value in table.items():
        print(key,":",value,"\n")

#def create_nest_dict():
    #pass