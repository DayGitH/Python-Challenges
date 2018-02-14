"""
[2015-06-05] Challenge #217 [Practical Exercise] TeXSCII

https://www.reddit.com/r/dailyprogrammer/comments/38nhgx/20150605_challenge_217_practical_exercise_texscii/

# [](#PEIcon) _(Practical Exercise)_: TeXSCII
LaTeX is a typesetting utility based on the TeX typesetting and macro system which can be used to output mathematical
formulae to display or print. For example, the LaTeX code `\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}` will be transformed into
[this](http://latex.codecogs.com/gif.latex?%5Cdpi%7B200%7D%20%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E%7B2%7D-4ac%7D%7D%7B2a%7D)
when typeset.
The syntax of LaTeX formulae is fairly simple; commands begin with a backslash `\`, followed by the command name,
followed by its arguments in curly braces, such as `\sqrt{-1}` (square-root of -1) or `\frac{1}{3}` (1/3 as a
fraction). Subscript and superscript are also supported, with the `_` and `^` characters respectively, followed by the
script in curly braces - for example, `x^{2}` outputs x^(2). Everything else is output as plain text.
In today's challenge, you'll implement a simplified subset of LaTeX which outputs the resulting formula as ASCII.
# Formal Inputs and Outputs
## Input Specification
You'll be given a LaTeX equation on one line. The commands you need to support are:
* `\frac{top}{bottom}`: A fraction with the given top and bottom pieces
* `\sqrt{content}`: A square-root sign
* `\root{power}{content}`: A root sign with an arbitrary power (eg. cube-root, where the power 3 is at the top-left of
the radical symbol)
* `_{sub}`: Subscript
* `^{sup}`: Superscript
* `_{sub}^{sup}`: Subscript and superscript (one on top of the other)
* `\pi`: Output the greek symbol for pi
Feel free to extend your solution to support any additional structures such as integral signs.
## Output Description
Output the formula with ASCII symbols in the appropriate locations. You're free to pick the output style that looks
most appropriate to you. One possible way might be something like this:
      3_
      √x
    y=--
      3 
# Sample Inputs and Outputs
## Subscripts and Superscripts
### Input
    log_{e}(e^{x})=x
### Output
          x
    log (e )=x
       e
## Stacked Scripts
### Input
    F_{21}^{3}=2^{5}*7^{3}-30
### Output
     3   5  3   
    F  =2 *7 -30
     21         
## Fractions
### Input
    sin^{3}(\frac{1}{3}\pi)=\frac{3}{8}\sqrt{3}
### Output
    
       3 1   3 _
    sin (-π)=-√3
         3   8  
## Quadratic Formula
### Input
    x=\frac{-b+\sqrt{b^{2}-4ac}}{2a}
### Output
           ______
          / 2    
      -b+√ b -4ac
    x=-----------
         2a     
## Cubic Formula
(I hope)
### Input
    x=\frac{\root{3}{-2b^{3}+9abc-27a^{2}d+\sqrt{4(-b^{2}+3ac)^{3}+(-2b^{3}+9abc-27a^{2}d)^{2}}}}{3\root{3}{2}a} -
\frac{b}{3a} -
\frac{\root{3}{2}(-b^{2}+3ac)}{3a\root{3}{-2b^{3}+9abc-27a^{2}d+\sqrt{4(-b^{2}+3ac)^{3}+(-2b^{3}+9abc-27a^{2}d)^{2}}}}
### Output
        3________________________________________________                                                             
        /                  ______________________________                                                             
       /    3         2   /    2     3     3         2  2                             3_   2                          
      √  -2b +9abc-27a d+√ 4(-b +3ac) +(-2b +9abc-27a d)    b                         √2(-b +3ac)                     
    x=--------------------------------------------------- - -- - -----------------------------------------------------
                              3_                            3a       3________________________________________________
                             3√2a                                    /                  ______________________________
                                                                    /    3         2   /    2     3     3         2  2
                                                                 3a√  -2b +9abc-27a d+√ 4(-b +3ac) +(-2b +9abc-27a d) 
# Notes and Further Reading
Solutions have a recommended order of *new* again - feel free to change it back if you prefer *best*. If you want to
play around some with LaTeX, try [this online tool](http://www.codecogs.com/latex/eqneditor.php).
Got any cool challenge ideas? Submit them to /r/DailyProgrammer_Ideas!
"""


def main():
    pass


if __name__ == "__main__":
    main()
