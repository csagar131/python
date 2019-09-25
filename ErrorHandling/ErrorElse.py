dic = {"name":'sagar', "roll":'745'}
 
try:
    print(dic['name'])
except KeyError:
    print("error founded")
else:
    print("every thing is fine")

'''
when the try block run successfully then only else part will
get executed otherwise else won't work

'''