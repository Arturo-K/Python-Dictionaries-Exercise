from functions import *

print("== Python Program to access and modify student grades ==\n")

#================data============================
#need to be able to import from file/database
#initiate a nested dictionary to store table data
table = {
    "Ali":{
        "SWE225":90,
        "SWE371":89,
        "SWE346":10,
        "SWE245":59,
    },
    "Mohammed":{
        "SWE225":60,
        "SWE371":76,
        "SWE346":90,
        "SWE245":70,
    },
    "Saed":{
        "SWE225":50,
        "SWE371":90,
        "SWE346":86,
        "SWE245":100,
    },
    "John":{
        "SWE225":77,
        "SWE371":65,
        "SWE346":67,
        "SWE245":90,
    },
    "Mike":{
        "SWE225":45,
        "SWE371":98,
        "SWE346":93,
        "SWE245":80,
    },
    }

#===========================Simple User Interface=======
#Create GUI that displays table and gives options
#Use Tkinter
display_table(table)
while True:
    print("\nOptions:",
        "\n1. Add a student to the table.",
        "\n2. Delete a student from a table.",
        "\n3. Delete a course from a table.",
        "\n4. Add a course to the table.",
        "\n5. Add a grade for a course for a certain student.",
        "\n6. Update a grade for a course for a certain student.",
        "\n7. Find the grade of a course for a student.",
        "\n8. Calculate the average of all course grades for a certain student.",
        "\n9. Calculate the average of all course grades for a certain student.",
        "\n10. The name of the student who achieved the highest grade in a course.",
        "\n11. The names of students who failed a course (failure is a grade below 60).",
        "\n12. Display table."
        "\n0. exit."
        )
    choice = int(input("Pick an action to execute: "))

    if choice == 1:
        new_student = input("Enter student name : ")
        table = add_student(table,new_student)

    elif choice == 2:
        del_student = input("Enter student to delete : ").title()
        table = delete_student(table,del_student)

    elif choice == 3:
        del_course = input("Enter course to delete : ").upper()
        table = delete_course(table,del_course)

    elif choice == 4:
        new_course = input("Enter code for new course : ").upper()
        table = add_course(table,new_course)
        

    elif choice == 5:
        student = input("Enter student name : ").title()
        course = input("Enter course code : ").upper()
        grade = int(input("Enter grade : "))
        table = add_grade(table,student,course,grade)

    elif choice == 6:
        student = input("Enter student name : ").title()
        course = input("Enter course code : ").upper()
        new_grade = int(input("Enter new grade : "))
        update_grade(table,student,course,new_grade)

    elif choice == 7:
        student = input("Enter student name : ").title()
        course = input("Enter course code : ").upper()
        find_grade(table, student, course)

    elif choice == 8:
        student = input("Enter student name : ").title()
        print("Average grade for",student,"is", str(calc_student_avg(table,student)))

    elif choice == 9:
        course = input("Enter course code :").upper()
        print("Average grade for",course,"is",
            str(avg_allstudents(table,course)))

    elif choice == 10:
        course = input("Enter course code :").upper()
        print("The highest student in",course,"is",highest_student(table,course))

    elif choice == 11:
        course = input("Enter course code :").upper()
        print("The students who failed", course, "are",failed_students(table,course))

    elif choice == 12:
        #function call after conditional
        pass
    elif choice == 0:
        break
    else:
        print("Invalid Option, try again.")

    #display data to show any changes
    display_table(table)
        