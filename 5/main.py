import os

dir_path="directory of txt files"
list_of_files=os.listdir(dir_path)
for file in list_of_files:
    file_path=f"{dir_path}/{file}"
    with open(file_path,"r") as filepointer:
        lines=filepointer.readlines()
        for line_number,line in enumerate(lines,0):
            if "noorfatima" in line:
                print(f"noor is present in line no: {line_number+1} of {file}")
                

