import os

def manue():
    manue_choice = int(input("\n What do you want to do ? \n 1.register student \n 2. mark attendance\n 3. check eligibility "))
    return manue_choice

manue()

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
        att=name_count[name_of_student]
        print(att)
        try:
            percentage=(att/count_att)*100
        except Exception as e:
            print(e)
            percentage=(att/1)*100
        if percentage>75:
            print(f"comgratulations ! {name_of_student} is eligible to sit in exam! ")
        else:
            print(f"Alas ! {name_of_student} is not eligible to sit in exam! ")

if os.path.exists("count_att.txt"):
    with open("count_att","r") as filepointer:
        count_att=int(filepointer.read())
else:
    count_att = 0

while True:
    choice = manue()
    if choice == 1:
        register_student()
    elif choice == 2:
        mark_attendance()
        count_att += 1
        with open("count_att.txt","w") as filepointer:
            filepointer.write(str(count_att))
        count_att()
    elif choice == 3:
        name_of_student = input("Enter the name of the student: ")
        check_eligibility(name_of_student)
    else:
        print("Please choose option within the menu ! ")
