fileptr = open("input.txt", "w")
line1=input("enter line no 1 : ")
fileptr.write(line1+ '\n')
line2=input("enter line no 2 : ")
fileptr.write(line2+ '\n')
line3=input("enter line no 3 : ")
fileptr.write(line3+ '\n')
line4=input("enter line no 4 : ")
fileptr.write(line4+ '\n')
line5=input("enter line no 5 : ")
fileptr.write(line5+ '\n')
fileptr.close()
fileptr = open("input.txt","r")
content=fileptr.read()
reverseline1=line1[::-1]
reverseline2=line2[::-1]
reverseline3=line3[::-1]
reverseline4=line4[::-1]
reverseline5=line5[::-1]
fileptr = open("output.txt","w")
fileptr.write("line1 : "+reverseline1+"\n")
fileptr.write("line2 : "+reverseline2+"\n")
fileptr.write("line3 : "+reverseline3+"\n")
fileptr.write("line4 : "+reverseline4+"\n")
fileptr.write("line5 : "+reverseline5+"\n")
fileptr.close()