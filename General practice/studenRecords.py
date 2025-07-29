student_list = []
while True:
    print("01 Enter 1 for new enrollment")
    print("02 Enter 2 to view all records")
    print("03 Enter 3 delete record")
    print("04 Enter 4 to quit the program")

    count = int(input("Enter the Number\n"))
  
    if count == 1:
        name = input("Enter the student name\n")
        classs = input("Enter the class name\n")
        grade = input("Enter the student grade\n")
        print('Student enrolled successfully\n')

        student = (name, classs, grade)
        student_list.append(student)

    elif count == 2:
        print('Students List')
        for idx, student in enumerate(student_list, start=1):
            print(f'Record {idx}')
            print(f'Name   =  {student[0]}')
            print(f'Class  =  {student[1]}')
            print(f'Grade  =  {student[2]}')
            print(" ")

    elif count == 3:
        serial_no = int(input('Enter record no to delete the record\n'))
        print('Press 1 to delete the record and 2 to terminate the program\n')
        confirm = int(input('Enter the confirmation number\n'))
        if confirm == 1:
            del student_list[serial_no-1]
        elif confirm ==2:
            print('Deletion canceled\n')
            continue
        else:
            print('INVALID VALUE ENTERED\n')
            continue
    elif count == 4:
        print('Program terminated')
        break
    else:
        print('INVALID VALUE ENTERED\n')


       


