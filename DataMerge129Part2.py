import csv


data=[]

with open('Project127.csv',encoding='utf8') as f:
    reader=csv.reader(f)
    for row in reader:
        data.append(row)


header1=data[0]
data1=data[1:]

data=[]

with open('Project129Part1.csv',encoding='utf8') as f:
    reader=csv.reader(f)
    for row in reader:
        data.append(row)


header2=data[0]
data2=data[1:]

header=header1+header2

data=[]

for i in data1:
    data.append(i)

for i in data2:
    data.append(i)


with open('total_stars.csv','w',newline='',encoding='utf8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)