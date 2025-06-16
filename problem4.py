file = open("students.txt",'r')
details = {}


for line in file:
    name,score = line.split(',')
    print(name,score)
    details[name] = int(score)

file.close()


for key,value in details.items():
    value+=5
    details[key]=value
    print(key,value)

file = open("updated_students.txt",'w')
for key,value in details.items():
    new_str = str(key) + "," + str(value) + "\n"
    file.write(new_str)
    

file.close()