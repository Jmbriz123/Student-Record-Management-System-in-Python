
def add_student(students):
    new_student = input("Enter the name of the new student: ")
    new_student_id = int(input(f"Enter student id of {new_student}: "))
    new_student_score = int(input(f"Enter score of {new_student}: "))
    # update the dict
    students[new_student] = {"score" : new_student_score, "student_id" : new_student_id}

def display_records(students):
    print("\nStudent Records:")
    print(f"{"Name": <15}{"Score": ^15}{"Student ID": ^15}")
    print("-"*45)

    for i in students:
        print(f"{i:<15}{students[i]["score"]: ^15}{students[i]["student_id"]:^15}")

    

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
        "JM": {"score": 98, "student_id": 202450020},
        "Jemarco": {"score" : 87 , "student_id": 202450021}
    }
    display_menu()
    choice = input("Enter choice: ")

    match choice:
        case 1:
            add_student()
        case 2:
            

main()

