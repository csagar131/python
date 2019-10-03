my_file = open("data.txt",'r')
data = my_file.read()

my_file.close()
print(data)


my_file1 = open('data.txt','w') # w mode---> this will erase and overwrite content in the file
value = input("ENter data--->> ")
data1 = my_file1.write(value)
my_file1.close()

print(data1)