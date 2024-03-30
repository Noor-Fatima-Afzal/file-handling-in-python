with open("Input.txt", "w") as filepointer:
    for i in range(1,6):
        line = input(f"Enter line # {i}: ")
        filepointer.write(line + "\n")

with open("Input.txt", "r") as filepointer:
    lines = filepointer.readlines()
    reverseline1 = lines[0][::-1]
    reverseline2 = lines[1][::-1]
    reverseline3 = lines[2][::-1]
    reverseline4 = lines[3][::-1]
    reverseline5 = lines[4][::-1]

with open("Output.txt", "w") as filepointer:
    filepointer.write("line1 : "+reverseline1+"\n")
    filepointer.write("line2 : "+reverseline2+"\n")
    filepointer.write("line3 : "+reverseline3+"\n")
    filepointer.write("line4 : "+reverseline4+"\n")
    filepointer.write("line5 : "+reverseline5+"\n")