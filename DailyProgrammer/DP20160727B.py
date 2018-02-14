"""
[2016-07-27] Challenge #277 [Intermediate] Fake coins

https://www.reddit.com/r/dailyprogrammer/comments/4utlaz/20160727_challenge_277_intermediate_fake_coins/

#Description
Their are some false golden coins, wich are lighter then others, in the treasure chest. The assistant has weighed the
coins, but can not figure out which are false and which are not.
#Formal Inputs & Outputs
##Input description
Each coin is labeled with a letter, and is put on the scale in groups or by itself.
The input consist of the coins on the left side, the coins on the right side and the way the scale tipped. This can be
`left`, `right` or `equal` when the two sides wheigt the same. 
###Input 1
    a b left
    a c equal
###Input 2
    a c equal
    
###Input 3
    a c equal
    a b equal
    c b left
##Output description
You must determine which coins are lighter then the others.
###Output 1
    b is lighter
    
It is possible that you can't determine this because you have not in enough info.
###Output 2
    no fake coins detected
    
And it is possible that the provided data has been inconsistent.
###Output 3
    data is inconsistent
#Notes/Hints
`left` means that the left side is heavier. Same goes for `right`...
#Challenge input
##1
    ab xy left
    b x equal
    a b equal
    
##2
    a x equal
    b x equal
    y a left
   
##3
    abcd efgh equal
    abci efjk left
    abij efgl equal
    mnopqrs tuvwxyz equal
##4
    abc efg equal
    a e left
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
#Edit Notes
You can assume that there is only 1 fake coin, if not, the data is inconsistent.
If your solution worked without this assumption, you can leave it like that.
And all real coins weight the same, just like the fake coins. But no real weight is necessary to complete the challenge
"""


def main():
    pass


if __name__ == "__main__":
    main()
