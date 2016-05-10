alphabets = 'abcdefghijklmnopqrstuvwxyz'
test = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
url = 'map'

def finder(letter):
    '''Uses binary search to find letter position between 0 and 25.
       If not found, returns the character back'''
    
    lower = 0
    upper = len(alphabets) - 1
    found = False
    letter = letter.lower()
    while lower <= upper and not found:
        mid = (upper + lower) // 2
        if alphabets[mid] < letter:
            lower = mid + 1
        elif alphabets[mid] > letter:
            upper = mid - 1
        else:
            return mid
    return letter
    

def shifter(pos,shift):
    '''Takes position of letter between 0 and 25 and shifts and returns letter'''
    
    new_pos = (pos + shift) % 26
    return alphabets[new_pos]

def string_shift(in_str, num):
    '''Shifts entire string by amount specified'''
    
    answer = ''
    for l in in_str:
        loc = finder(l)
        '''If loc doesn't find the character, that character doesn't get shifted'''
        if type(loc).__name__ != 'str':
            ans = shifter(loc, num)
        else:
            ans = loc
        answer += ans
            
    return answer
    
if __name__ == '__main__':
    print(test)
    print(string_shift(test,2))        
            
    print(url)
    print(string_shift(url,2))
    
