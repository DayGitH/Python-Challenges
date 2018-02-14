"""
[17-08-21] Challenge #328 [Easy] Latin Squares

https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/

#**Description**
A [Latin square](https://en.wikipedia.org/wiki/Latin_square) is an n × n array filled with n different symbols, each
occurring exactly once in each row and exactly once in each column.
For example:
>1
And,
>1 2
>2 1
Another one, 
>1 2 3 
>3 1 2
>2 3 1
In this challenge, you have to check whether a given array is a Latin square. 
#**Input Description**
Let the user enter the length of the array followed by *n x n* numbers. Fill an array from left to right starting from
above. 
#**Output Description**
If it is a Latin square, then display true. Else, display false. 
#**Challenge Input**
> 5 
> 1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1
> 2
> 1 3 3 4
> 4
> 1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1 
#**Challenge Output**
>  true
> false
> false 
---------
#**Bonus**
A Latin square is said to be reduced if both its first row and its first column are in their natural order.
You can reduce a Latin square by reordering the rows and columns. The example in the description can be reduced to this
>1 2 3
>2 3 1
>3 1 2
If a given array turns out to be a Latin square, then your program should reduce it and display it. 
Edit: /u/tomekanco has pointed out that many solutions which have an error. I shall look into this. Meanwhile, I have
added an extra challenge input-output for you to check. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
