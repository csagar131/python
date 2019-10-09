f = open("questions.txt",'r')
queslst = [q.strip() for q in f.readlines()]

#print(ques)
count =0
for i in queslst:
    ques  = i.split("=")
    print(ques[0]+"=",end="")
    ans = input()
    if ans == ques[1]:
        count+=1


with open("results.txt",'w') as res:
    k = f'your final score is {count}/{len(queslst)}'
    k = str.format('your final score is '+str(count)+"/"+str(len(queslst)))
    res.write(k)

