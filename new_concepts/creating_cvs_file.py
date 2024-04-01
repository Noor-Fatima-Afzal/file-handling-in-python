import csv

data = [
    ['Name', 'Age', 'Country'],
    ['John', 30, 'USA'],
    ['Emily', 25, 'Canada'],
    ['David', 40, 'UK']
]

file_name='data.csv'
with open("data.csv","w",newline="") as file_pointer:
    csv_writer=csv.writer(file_pointer)
    csv_writer.writerows(data)

print(f'csv file named "{file_name}" created successfully! ')

age_lst=[]
with open("data.csv","r", newline="") as file_pointer:
    csv_reader=csv.reader(file_pointer)
    for row in csv_reader:
        print(row[1])
        age_lst.append(row[1])

# typecasting and adding
lst_converted=[int(x) for x in age_lst if x.isdigit()]
print(lst_converted)
total=sum(lst_converted)
print(total)
