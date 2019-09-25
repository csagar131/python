dic = {"name":'sagar', "roll":'745'}
 
try:
    print(dic['name1'])
except KeyError:
    print("error founded")
    raise
else:
    print("every thing is fine")