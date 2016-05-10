import re
import urllib.request

nothing = 12345
p = re.compile('\d+')

depth = 1

for i in range(250):  
    URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nothing)
    response = urllib.request.urlopen(URL)
    html = response.read()
    
    print('depth: {}'.format(depth))
    depth += 1
    
    html = html.decode("utf-8")
    print(html)
    
    mat = p.finditer(html)
               
    for m in mat:
        nothing = m.group()
        print(nothing)    
        
    if depth == 86:
        nothing = int(nothing) / 2