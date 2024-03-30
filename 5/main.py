import os

try:
    dir=input("Enter the directory path to search: ")
    file_names_list=os.listdir(dir)
    keyword=input("Enter the keyword or pattern to search for: ")
    for file in file_names_list:
        if file.endswith(".txt"):
            file_path=os.path.join(dir,file)    
            with open(file_path,"r") as filepointer:
                lines=filepointer.readlines()
                line_num=0
                for line in lines:
                    line_num+=1
                    if keyword in line:
                        print(f" on Line {line_num} Keyword '{keyword}' found in file: {file}")
except FileNotFoundError:
    print("Directory not found.")