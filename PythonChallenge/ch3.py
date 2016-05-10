import re

if __name__ == '__main__':
    file = open('ch4.txt')
    
    answer = ''
    
    p = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
    for line in file:
        line = line.strip()
        
        mat = p.finditer(line)
        
        for m in mat:
            out = m.group()
            answer += out[4]
            
    print(answer)