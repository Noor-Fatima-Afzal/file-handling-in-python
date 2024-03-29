from datetime import datetime

def backup_file(file_path):
    with open(file_path,"r") as filepointer:
        print("File opened successfully in read mode")
        content=filepointer.read()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name=(f"{file_path}On{timestamp}")
        with open(new_file_name,"w") as new_filepointer:
            print("File opened successfully in write mode")
            new_filepointer.write(content)
            print(f"Backup of {file_path} is created with name {new_file_name}")
backup_file("main.py")