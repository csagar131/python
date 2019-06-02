from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''


def simple_scrap():
    return simple_soup.find('p').string       #  find('p').string gives the content inside the tag p

def find_list_items():
    return simple_soup.find_all('li')   # find_all give the python list and it contains item inside the list

def print_lst_items(lst):
    for i in range(0,len(lst)):
        print(lst[i].string)

#to find the list of items inside the lst excluding the tag

def print_lst(lst):
    lst1 = [i.string for i in lst]
    return lst1


simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')  # Beautifulsoup is a class , simple_soup is object
print(simple_scrap())

#print(find_list_items())

lst = find_list_items()
print_lst_items(lst)

print('list of list item:',print_lst(lst))



