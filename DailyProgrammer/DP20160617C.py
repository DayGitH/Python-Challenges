"""
[2016-06-17] Challenge #271 [Hard] Formatting J code

https://www.reddit.com/r/dailyprogrammer/comments/4ojbgq/20160617_challenge_271_hard_formatting_j_code/

J code can be written like basic/pascal/fortran.
Challenge today is to convert between 2 or 4 format styles for one J routine.  the last 2 are optional bonuses.  
Your program should autodetect any current format, and output the target format from any state.
The program should return text/arrays of lines instead of making "sideeffect print statements"
#J control word rules
This challenge is almost entirely about adding and replacing linefeeds and leading spaces.  [reference to all j control
words, you likely don't need to read](http://www.jsoftware.com/help/dictionary/ctrl.htm)
A control word is a string of letters and underscores that is at least 2 letters long and ends with a `.`  For the sake
of this challenge the only control words that are used are:
`for_varname. if. do. else. end. label_.`  (these are case sensitive)
you may (or not) assume that an end-of_word boundary occurs after the control word but a space or linefeed isn't
strictly necessary for J's parser.  A begining of word boundary is necessary for J to parse correctly, but can be
ignored.
 
All control words have implied linefeeds that follow and precede them, and so all multiline code can be converted to a
single line by converting "essential linefeeds" (those that separate (LF terminated) statements that do not have
intervening control words) into the "dummy control word separator:" `label_.`
The `end.` control word terminates an `if.` or `for.` structure.  
The `do.` control word acts as `THEN` (for if.) and as "middle separator" for all other control words.
The sample code here is taken from http://rosettacode.org/wiki/Levenshtein_distance#J
#inputs
all of the following sections contain inputs ( and the first 4 are target outputs).  The challenge inputs are "messed
up" but still valid J code, that can be formatted into one of the first 4 inputs/outputs.
Your function should take the described inputs, and an additional parameter that is the desired output format.  The
number of spaces or tabs that are leading spaces is your choice and may be a global paramater.
#1. Basic format
The following  as input must also be able to output itself.   
    
      D=. x +/&i.&>:&# y
      for_i. 1+i.#x do.
        for_j. 1+i.#y do.
          if. ((<:i){x)=(<:j){y do.
            D=.(D {~<<:i,j) (<i,j)} D
          else.
            min=. 1+<./D{~(i,j) <@:-"1#:1 2 3
            D=. min (<i,j)} D
          end.
        end.
      end.
      {:{:D
#2 linear format
This has linefeeds removed, and the 2 statements inside the `else.` clause are separated by a `label_.` clause.
This is likely the most useful "starting format" to convert to and from all others.  If you do just 2 parts of this
challege, convert from this format to `1.`, and also convert from `1.` to `1.` unchanged.
    D=. x +/&i.&>:&# y for_i. 1+i.#x do. for_j. 1+i.#y do. if. ((<:i) (x)=(<:j){y do. D=.(D {~<<:i,j) (<i,j)} D else.
min=. 1+<./D{~(i,j) <@:-"1#:1 2 3 label_. D=. min (<i,j)} D end. end. end. {:{:D
#3. python layout format
like `1.` but with `end.`s terminating the last line of their sections.
      D=. x +/&i.&>:&# y
      for_i. 1+i.#x do.
        for_j. 1+i.#y do.
          if. ((<:i){x)=(<:j){y do.
            D=.(D {~<<:i,j) (<i,j)} D
          else.
            min=. 1+<./D{~(i,j) <@:-"1#:1 2 3
            D=. min (<i,j)} D end. end. end.
      {:{:D
#4. implied python format
this is the only format that is not valid J code.  Its a simple modification to `3.` in that `do.` and `end.` control
words are removed.  Where this is challenging is if this is the input for other outputs, and this format must be
detected and `do` and ` end` keywords must be added.
      D=. x +/&i.&>:&# y
      for_i. 1+i.#x 
        for_j. 1+i.#y 
          if. ((<:i){x)=(<:j){y 
            D=.(D {~<<:i,j) (<i,j)} D
          else.
            min=. 1+<./D{~(i,j) <@:-"1#:1 2 3
            D=. min (<i,j)} D 
      {:{:D
#challenge input 1
this is valid J code.
    
    D=. x +/&i.&>:&# y 
    for_i.
    1+i.#x 
    do. for_j. 1+i.#y 
    do. 
    
    if. ((<:i) (x)=(<:j){y do. D=.(D {~<<:i,j) (<i,j)} D else. min=. 1+<./D{~(i,j) <@:-"1#:1 2 3 
    D=. min (<i,j)} D 
    label_.  end. end. end. {:{:D
#challenge input 2
Very hard:  partially implied python format, and partially "free form"
      D=. x +/&i.&>:&# y for_i. 1+i.#x 
        for_j. 1+i.#y do. 
          if. ((<:i){x)=(<:j){y 
            D=.(D {~<<:i,j) (<i,j)} D
          else.
            min=. 1+<./D{~(i,j) <@:-"1#:1 2 3
            D=. min (<i,j)} D end. 
      {:{:D
(missing (implied) end. statement.  Some implied do. statements)
____
To cut down on output, converting challenge `1.` to output `4.` likely requires exercising all of your code, in such a
way that it works.
"""


def main():
    pass


if __name__ == "__main__":
    main()
