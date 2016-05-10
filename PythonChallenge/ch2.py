if __name__ == '__main__':
    file = open('ch3.txt')
    
    answer = ''
    char_list = {}
    for line in file:
        for word in line:
            try:
                char_list[word] += 1
            except:
                char_list[word] = 1
                '''Use unicode to see if it is letter
                   unicode(a)=97 and unicode(z) = 122'''
                if 97 <= ord(word.lower()) <= 122:
                    answer += word
                
    print(answer)
    file.close()