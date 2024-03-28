from datetime import datetime

def backup_file(file_path):
    with open(file_path,"r") as filepointer:
        content=filepointer.read()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name=(f"{file_path}On{timestamp}")
        with open(new_file_name,"w") as new_filepointer:
            new_filepointer.write(content)

backup_file("main.py")