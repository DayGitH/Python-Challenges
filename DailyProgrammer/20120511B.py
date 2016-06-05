"""
Brainf*** is an extremely minimalistic programming language. The memory consists of a large array of bytes, the "tape",
which is manipulated by moving around a single tape pointer. The 8 commands are:
Character	Action
<	move the pointer to the left
>	move the pointer to the right
+	increment the byte the pointer is pointing at (mod 256)
-	decrement the byte the pointer is pointing at (mod 256)
[	if the data which the tape pointer is pointing at is 0, jump forward to the command after the matching square
bracket. Otherwise, just continue to the next command
]	if the data which the tape pointer is pointing at is not 0, jump backwards to the command after the matching square
bracket. Otherwise, just continue to the next command
,	read a character from the input and store it into the current pointer byte
.	output the current pointer byte as an ascii character

Any other character is ignored and treated as a comment

[ ... ] thus make a kind of while loop, equivalent to something like "while(data[pointer] != 0) { ... }". The brackets
match like parentheses usually do, each starting one has a matching ending one. These loops can be nested inside other
loops.

Write a program that reads a brainf*** program and its input, interprets the code, and returns the output.

More information, including a "Hello World" program, can be found on wikipedia.

If you've written your program successfully, try running this and see what pops out:
++++++++++[>>++++++>+++++++++++>++++++++++>+++++++++>+++>+++++>++++>++++++++>+[<
]<-]>>+++++++.>+.-.>+++.<++++.>>+++++++.<<++.+.>+++++.>.<<-.>---.<-----.-.+++++.
\>>>+++.-.<<-.<+..----.>>>>++++++++.>+++++++..<<<<+.>>>>-.<<<<.++++.------.<+++++
.---.>>>>>.<<<++.<<---.>++++++.>>>>+.<<<-.--------.<<+.>>>>>>+++.---.<-.<<<<---.
<.>---.>>>>>>.

Thanks to nooodl for submitting this problem in /r/dailyprogrammer_ideas!
"""

inp = """++++++++++[>>++++++>+++++++++++>++++++++++>+++++++++>+++>+++++>++++>++++++++>+[<""" \
      """]<-]>>+++++++.>+.-.>+++.<++++.>>+++++++.<<++.+.>+++++.>.<<-.>---.<-----.-.+++++.""" \
      """>>>+++.-.<<-.<+..----.>>>>++++++++.>+++++++..<<<<+.>>>>-.<<<<.++++.------.<+++++""" \
      """.---.>>>>>.<<<++.<<---.>++++++.>>>>+.<<<-.--------.<<+.>>>>>>+++.---.<-.<<<<---.""" \
      """<.>---.>>>>>>.
      """


def main():
    l = len(inp)
    w_list = 256*[0]
    w_i = 0
    inp_i = 0
    res = ""

    while inp_i < l:
        cmd = inp[inp_i]

        if cmd == '-':
            w_list[w_i] = (w_list[w_i] - 1) % 256
        elif cmd == '+':
            w_list[w_i] = (w_list[w_i] + 1) % 256
        elif cmd == '>':
            w_i += 1
        elif cmd == '<':
            w_i -= 1
        elif cmd == '[':
            pass
        elif cmd == ']':
            if w_list[w_i]:
                count = 1
                while count:
                    inp_i -= 1
                    if inp[inp_i] == '[':
                        count -= 1
                    elif inp[inp_i] == ']':
                        count += 1
        elif cmd == '.':
            res += chr(w_list[w_i])
        elif cmd == ',':
            inp[inp_i] == ord(input('> '))

        inp_i += 1

    print(res)

if __name__ == "__main__":
    main()
