my_file = open("people.txt",'r')
people = []

for i in my_file:
    i = i.rstrip()
    people.append(i)

my_file.close()

print("people is ",people)

print("Enter the name of nearby people")
nearby = input().rstrip().split()
print("nearby is",nearby)
print("---------writing to nearby_friends file---------------")

for i in nearby:
    print(i)
    if i in people:
        f = open("nearby_friends.txt",'a')
        f.write(i+"\n")
        f.close()


#print(lst)