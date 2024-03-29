def register_student():
    student=input("Enter name of student: ")
    with open("students.txt","a") as filepointer:
        filepointer.write(student+"\n")

def mark_attendance():
    with open("students.txt","r") as filepointer:
        lines=filepointer.readlines()
        for line in lines:
            line=line.strip()
            if line:
                att=input(f"{line} is present or absent? P/A ").capitalize()
                if att=="P":
                    with open("attendace.txt","a") as filepointer:
                        filepointer.write(line+"\n")

name_count={}

def count_attendance():
    with open("attendace.txt","r") as filepointer:
        lines=filepointer.readlines()
        for line in lines:
            line=line.strip()
            if line in name_count:
                name_count[line]+=1
            else:
                name_count[line]=1

def check_eligibility(name_of_student):
    if name_of_student in name_count:
        att = name_count[name_of_student]
        print(att)
        try:
            percentage=(att/count_att)*100
        except Exception as e:
            print(e)
            percentage=(att/1)*100
        if percentage>75:
            print(f"Congratulations! {name_of_student} is eligible to sit in the exam!")
        else:
            print(f"Alas! {name_of_student} is not eligible to sit in the exam!")
    else:
        print(f"No attendance records found for {name_of_student}.")

manue = int(input("\n What do you want to do ? \n 1. Register student \n 2. Mark attendance\n 3. Check eligibility \n 0. Do nothing\n"))

count_att=0

while True:
    if manue == 1:
        register_student()
    elif manue == 2:
        mark_attendance()
        count_att += 1
        with open("count_att.txt", "a") as filepointer:
            filepointer.write(str(count_att))
        count_attendance()
    elif manue == 3:
        check_eligibility(input("Enter name of student: "))
    elif manue == 0:
        break
    else:
        print("Invalid choice")
    
    manue = int(input("\n What do you want to do ? \n 1. Register student \n 2. Mark attendance\n 3. Check eligibility \n 0. Do nothing\n"))