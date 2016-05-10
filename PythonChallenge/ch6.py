import zipfile
import re

zip_file = zipfile.ZipFile('ch6.zip')   # Load zip file
p = re.compile('\d+')                   # Set up regular expression to extract 'nothing'

nothing = 90052
com_list = []

for i in range(909):
    text = zip_file.read(str(nothing) + '.txt')
    comment = zip_file.getinfo(str(nothing) + '.txt').comment # Extract comment from zip file
    com_list.append(comment.decode("utf-8")) # convert comment from byte to string and store to list
    
    text = text.decode("utf-8")

    print(text)
    print(comment)
    
    
    mat = p.finditer(text)
                  
    for m in mat:
        nothing = m.group()   
        
zip_file.close()

''' Print ASCII answer '''
for l in com_list:
    print(l,end='')
    