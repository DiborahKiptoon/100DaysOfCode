#Implementing read write operations etc
#we shall perform 3 different case studies within today's lesson


#case study 1 = read mode
'''var_name = open ("file1.txt", "r")
for each in var_name:
    print(each)'''



#Read mode method 2
file_read = open("file1.txt", "r")
print(file_read.read())


#Read mode method 3
with open("file1.txt") as file_read:
    text = file_read.read()
    print(text)

# Split operation on txt file
with open("file1.txt") as data:
    data_1 = data.readlines()
    for line in data_1:
        var = line.split()
        print(var)