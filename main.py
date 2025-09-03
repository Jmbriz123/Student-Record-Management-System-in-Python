
def add_student(students):
    new_student = input("Enter the name of the new student: ")
    new_student_id = int(input(f"Enter student id of {new_student}: "))
    new_student_score = int(input(f"Enter score of {new_student}: "))
    # update the dict
    students[new_student] = {"score" : new_student_score, "student_id" : new_student_id}

def display_records(students):
    print("Name\tScore\tStudent ID")
    print("-"*30)
    for i in students:
        print(i, end="\t")
        print(students[i]["score"], end='\t')
        print(students[i]["student_id"])
    





def display_menu():
    print("Choose action: ")
    print("\t1. Add new student")
    print("\t2. View all students' records")
    print("\t3. Search student by ID")
    print("\t4. Update score of a student")
    print("\t5. Remove a student")
    print("\t6. Show the class average score")

def main():
    students = {
        "student1": {"score": 98, "student_id": 202450020},
        "student2": {"score" : 87 , "student_id": 202450021}
    }
    display_records(students)
    return
    display_menu()
    choice = input("Enter choice: ")
    add_student(students)
    print(students)

main()

