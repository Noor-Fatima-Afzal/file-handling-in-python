# Write a Python program that searches for a specific keyword or pattern in a
# directory of text files and displays the file names and line numbers where the
# keyword or pattern is found.

import os

list_of_files=os.listdir("directory of txt files")
for file in list_of_files:
    with open(file,"r") as filepointer:
        lines=filepointer.readlines()
        for line in lines:
            for word in line:
                if word=="noor":
                    
