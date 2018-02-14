"""
[2017-06-21] Challenge #320 [Intermediate] War (card game)

https://www.reddit.com/r/dailyprogrammer/comments/6ilyfi/20170621_challenge_320_intermediate_war_card_game/

# Description
You will be implementing the classic card game [War](https://en.wikipedia.org/wiki/War_(card_game\)).
### Gameplay
This two player game is played using a standard 52-card deck. The objective of the game is to win all the cards. The
deck is divided evenly among the players, giving each a deck of face-down cards. In unison, each player reveals the top
card of their deck – this is a battle – and the player with the higher card adds both cards to the bottom of their
deck. If the cards are of equal value, it's war!
This process is repeated until one player runs out of cards, at which point the other player is declared the winner.
### War
Both players place their next three cards face down, then a card face-up. The owner of the higher face-up card wins the
war and adds all cards on the table to the bottom of their deck. If the face-up cards are again equal then the war
repeats with another set of face-down/up cards, until one player's face-up card is higher than their opponent's, or
both players run out of cards
If, when a war begins
* either player does not have enough cards for the war, both players reduce the number of cards to allow the war to
complete (e.g. if P2 has only three cards remaining, both players play two cards down and one card up. If P2 has only
one card remaining, no cards are played face-down and each player only plays one card up). 
* either player has no cards remaining, the other player wins. 
* both players have no cards remaining, the game is a draw (this is exceptionally rare in random games). 
### Post-battle/war
For consistency (so we all end up with the same result for the same input), cards used in a battle or war should be
added to the bottom of the winner's deck in a particular order.
After a battle, the winner's card is added to the bottom the winner's deck first, then the loser's card. 
After a war or wars, cards used in the war(s) are added to the deck first, followed by the two tying cards. "Cards used
in the war(s)" is defined as follows:
0. Cards from any sub-wars (recursive, using this ordering)
1. Winner's face-down cards (in the order they were drawn, first card draw is first added to bottom, etc)
2. Winner's face-up card
3. Loser's face-down cards (in the order they were drawn, first card draw is first added to bottom, etc)
4. Loser's face-up card
# Input
Input will consist of two lines of space-separated integers in [1..13]. In a standard game, the two lines will each
contain 26 numbers, and will be composed of four of each integer in [1..13]. However, your program should be able to
handle decks of any size and composition. The first number on a line represents the top card in the deck, last number
is the bottom.
### Challenge inputs
    5 1 13 10 11 3 2 10 4 12 5 11 10 5 7 6 6 11 9 6 3 13 6 1 8 1 
    9 12 8 3 11 10 1 4 2 4 7 9 13 8 2 13 7 4 2 8 9 12 3 12 7 5 
#
    3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1 
    9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5 
#
    1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13 
    1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13 
# Output
Output "1" if P1 wins, "2" if P2 wins, and "0" if P1 and P2 tied.
### Challenge outputs
    1
#
    2
#
    0
#Finally
Have a good challenge idea, like /u/lpreams did?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
