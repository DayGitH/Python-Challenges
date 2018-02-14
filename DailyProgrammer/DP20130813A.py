"""
[08/13/13] Challenge #137 [Easy] String Transposition

https://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/

# [](#EasyIcon) *(Easy)*: String Transposition
It can be helpful sometimes to rotate a string 90-degrees, like a big vertical "SALES" poster or your business name on
vertical neon lights, like [this image from Las Vegas](http://imgur.com/766x8uM). Your goal is to write a program that
does this, but for multiples lines of text. This is very similar to a [Matrix
Transposition](http://en.wikipedia.org/wiki/Transpose), since the order we want returned is not a true 90-degree
rotation of text.
*Author:* nint22
# Formal Inputs & Outputs
## Input Description
You will first be given an integer N which is the number of strings that follows. N will range inclusively from 1 to
16. Each line of text will have at most 256 characters, including the new-line (so at most 255 printable-characters,
with the last being the new-line or carriage-return).
## Output Description
Simply print the given lines top-to-bottom. The first given line should be the left-most vertical line.
# Sample Inputs & Outputs
## Sample Input 1
    1
    Hello, World!
## Sample Output 1
    H
    e
    l
    l
    o
    ,
    
    W
    o
    r
    l
    d
    !
    
## Sample Input 2
    5
    Kernel
    Microcontroller
    Register
    Memory
    Operator
## Sample Output 2
    KMRMO
    eieep
    rcgme
    nrior
    eosra
    lctyt
     oe o
     nr r
     t
     r
     o
     l
     l
     e
     r
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[08/13/13] Challenge #136 [Easy] Student Management

https://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/

# [](#EasyIcon) *(Easy)*: Student Management
You are a computer science professor at South Harmon Institute of Technology, and are in dire need of automatic
grading! The good news is you have all of your student's assignments in an easy-to-read format, making automation easy!
You will be given a list of unique student names, and then a list of their assignment grades. All assignments are based
on 20 points and are scored in whole-numbers (integers). All students have received the same number of assignments, so
you don't have to worry about managing [jagged arrays](http://en.wikipedia.org/wiki/Iliffe_vector).
*Author:* nint22
# Formal Inputs & Outputs
## Input Description
On standard console input, you will be given two space-delimited integers N and M: N is the number of students (which
ranges from 1 to 60, inclusive), and M is the number of assignments (which ranges from 4 to 100, inclusive). This will
be followed by N lines of text, each starting with an upper-case unique string being is your students name. This is
then followed by M integers, which are the grades ranging from 0 to 20, inclusively.
## Output Description
On the first line of output, print the class' average grade. Then, for each student, print their name and average grade
(up to two decimal points precision).
# Sample Inputs & Outputs
## Sample Input 1
    3 5
    JON 19 14 15 15 16
    JEREMY 15 11 10 15 16
    JESSE 19 17 20 19 18
## Sample Output 1
    15.93
    JON 15.80
    JEREMY 13.40
    JESSE 18.60
    
## Sample Input 2
    10 10
    ABIGAIL 11 3 5 20 4 2 8 17 4 5
    ALEXANDER 2 12 20 0 6 10 3 4 9 7
    AVA 11 15 2 19 14 5 16 18 15 19
    ETHAN 6 12 0 0 5 11 0 11 12 15
    ISABELLA 16 0 10 7 20 20 7 2 0 1
    JACOB 2 14 17 7 1 11 16 14 14 7
    JAYDEN 10 10 3 16 15 16 8 17 15 3
    MADISON 10 11 19 4 12 15 7 4 18 13
    SOPHIA 5 17 14 7 1 17 18 8 1 2
    WILLIAM 12 12 19 9 4 3 0 4 13 14
## Sample Output 2
    9.50
    ABIGAIL	7.90
    ALEXANDER 7.30
    AVA	13.40
    ETHAN 7.20
    ISABELLA 8.30
    JACOB 10.30
    JAYDEN 11.30
    MADISON 11.30
    SOPHIA 9.00
    WILLIAM 9.00
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[08/13/13] Challenge #135 [Easy] Arithmetic Equations

https://www.reddit.com/r/dailyprogrammer/comments/1k7s7p/081313_challenge_135_easy_arithmetic_equations/

# [](#EasyIcon) *(Easy)*: Arithmetic Equations
[Unix](http://en.wikipedia.org/wiki/Unix), the famous multitasking and multi-user operating system, has several
standards that defines Unix commands, system calls, subroutines, files, etc. Specifically within [Version
7](http://en.wikipedia.org/wiki/Version_7_Unix) (though this is included in many other Unix standards), there is a game
called "arithmetic". To quote the [Man Page](http://en.wikipedia.org/wiki/Man_page):
    Arithmetic types out simple arithmetic problems, and waits for an answer to be typed in. If the answer
    is correct, it types back "Right!", and a new problem. If the answer is wrong, it replies "What?", and
    waits for another answer. Every twenty problems, it publishes statistics on correctness and the time
    required to answer.
Your goal is to implement this game, with some slight changes, to make this an [Easy]-level challenge. You will only
have to use three arithmetic operators (addition, subtraction, multiplication) with four integers. An example equation
you are to generate is "2 x 4 + 2 - 5".
*Author:* nint22
# Formal Inputs & Outputs
## Input Description
The first line of input will always be two integers representing an inclusive range of integers you are to pick from
when filling out the constants of your equation. After that, you are to print off a single equation and wait for the
user to respond. The user may either try to solve the equation by writing the integer result into the console, or the
user may type the letters 'q' or 'Q' to quit the application.
## Output Description
If the user's answer is correct, print "Correct!" and randomly generate another equation to show to the user. Otherwise
print "Try Again" and ask the same equation again. Note that all equations must randomly pick and place the operators,
as well as randomly pick the equation's constants (integers) from the given range. You are allowed to repeat constants
and operators. You may use either the star '*' or the letter 'x' characters to represent multiplication.
# Sample Inputs & Outputs
## Sample Input / Output
*Since this is an interactive application, lines that start with '>' are there to signify a statement from the console
to the user, while any other lines are from the user to the console.*
    0 10
    > 3 * 2 + 5 * 2
    16
    > Correct!
    > 0 - 10 + 9 + 2
    2
    > Incorrect...
    > 0 - 10 + 9 + 2
    3
    > Incorrect...
    > 0 - 10 + 9 + 2
    1
    > Correct!
    > 2 * 0 * 4 * 2
    0
    > Correct!
    q
"""


def main():
    pass


if __name__ == "__main__":
    main()
