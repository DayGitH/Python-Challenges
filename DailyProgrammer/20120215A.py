'''
Write a program that can translate Morse code in the format of ...---...
A space and a slash will be placed between words. ..- / --.-
For bonus, add the capability of going from a string to Morse code.
Super-bonus if your program can flash or beep the Morse.
This is your Morse to translate:
.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.-
/ --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--
'''

alphanum_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

morse_list = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
              '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---',
              '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

morse_str = '.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / ' \
            '.-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--'

alphanum_str = 'hello daily programmer good luck on the challenges today'

print('Decrypt (D) or Encrypt (E)?')
inp = input('> ')

if inp.upper() == 'D':
    decrypt = True
elif inp.upper() == 'E':
    decrypt = False
else:
    raise AssertionError('Choose the write one next time!!!')

if decrypt:
    answer = ''

    working_list = morse_str.split(' / ')
    for i in range(len(working_list)):
        working_list[i] = working_list[i].split(' ')

    for word in working_list:
        for l in word:
            answer += alphanum_list[morse_list.index(l)]
        answer += ' '
else:
    answer = ''

    working_list = alphanum_str.split(' ')

    for word in working_list:
        for l in word:
            answer += morse_list[alphanum_list.index(l)] + ' '
        answer += ' / '

print(answer)