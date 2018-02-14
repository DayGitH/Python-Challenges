"""
[2017-12-06] Challenge #343 [Intermediate] Mozart's Musical Dice

https://www.reddit.com/r/dailyprogrammer/comments/7i1ib1/20171206_challenge_343_intermediate_mozarts/

In 1787 the famous composer Wolfgang Amadeus Mozart devised a *Musikalisches Würfelspiel* (musical dice game) that lets
you "compose without the least knowledge of music".  Obviously, this is a very loose definition of "compose", but it
does produce pieces of music that have probably never been written down or played before. We'll be playing his game
today (with some simplifications so you don't need to know musical notation).
Today's challenge may seem a little harder than typical at first, but it's actually not bad once you get the idea. I've
tried to make the instructions as clear and complete as possible, but please ask for help if you have any trouble
understanding them.
## The starting composition
[Start by downloading the *starting composition*
here.](https://gist.githubusercontent.com/cosmologicon/708fefa9793753ed4f075aaf781f3d67/raw/f08364a6056691215b99f705b4836f3d131ff6eb/mozart-dice-starting.txt)
Each line in this file gives the note name, starting time, and duration for one note in the starting composition, e.g.:
    D3 281.5 0.5
"D3" is the name of the note, which you don't need to understand for this game. The starting time and duration of the
note are given in units of *beats*, where beat 0 is the start of the song. This line means to play note D3 for 0.5
beats, starting at beat 281.5, and ending at beat 282.
The starting composition is 528 beats long, and consists of 176 *measures*, each of which is 3 beats long. Measure 1
goes from beat 0 to beat 3, measure 2 goes from beat 3 to beat 6, etc., up to measure 176, which goes from beat 525 to
528.
## Building your composition
The game consists of selecting 16 of the 176 measures from the starting composition, rearranging them to be measures 1
through 16 of a shorter, 48-beat composition, and outputting this shorter composition in the same format as the
starting composition.
For instance, the first measure you select might be measure 3. Measure 3 goes from beat 6 to beat 9, which means it's
all lines that start on or after beat 6, and before beat 9:
    C3 6 2
    E3 6 2
    G5 6 1
    C5 7 1
    E5 8 1
You need to change the starting times of each note in this measure so that it's measure 1 in your new composition. In
this case that means to subtract 6 from each of the starting times. The note names and the durations will stay the
same. The measure will then look like this:
    C3 0 2
    E3 0 2
    G5 0 1
    C5 1 1
    E5 2 1
The second measure you select from the starting composition might be measure 22, which is these notes:
    C3 63 2
    E5 63 1
    C5 64 1
    G4 65 1
You would then change the starting times of each note in measure 22 of the starting composition so that it's measure 2
in your new composition:
    C3 3 2
    E5 3 1
    C5 4 1
    G4 5 1
And so on. Once you've changed the starting times of each note in all 16 of your selected measures, just output all the
notes in your new composition.
## Measure selection
If you just randomly choose 16 measures from the starting composition, it won't sound very good, so you need to use
Mozart's system for selecting the measures. For each of your 16 measures, there are 11 possible selections from the
starting composition, and you choose each one by rolling two six-sided dice and taking their total (2 through 12),
using this table:
	96 32 69 40 148 104 152 119 98 3 54
	22 6 95 17 74 157 60 84 142 87 130
	141 128 158 113 163 27 171 114 42 165 10
	41 63 13 85 45 167 53 50 156 61 103
	105 146 153 161 80 154 99 140 75 135 28
	122 46 55 2 97 68 133 86 129 47 37
	11 134 110 159 36 118 21 169 62 147 106
	30 81 24 100 107 91 127 94 123 33 5
	70 117 66 90 25 138 16 120 65 102 35
	121 39 136 176 143 71 155 88 77 4 20
	26 126 15 7 64 150 57 48 19 31 108
	9 56 132 34 125 29 175 166 82 164 92
	112 174 73 67 76 101 43 51 137 144 12
	49 18 58 160 136 162 168 115 38 59 124
	109 116 145 52 1 23 89 72 149 173 44
	14 83 79 170 93 151 172 111 8 78 131
For each of the 16 rows in this table, select one of the numbers from the row depending on the roll of two dice. If you
roll 2, take the first number in the row, if you roll 3, take the second number, etc. For example, if your first roll
is a 7, you would take the sixth number from the first row (104). Then if your second roll is a 6, you would take the
fifth number from the second row (74). Continuing to all 16 rows, you might get this sequence:
	104 74 163 85 146 129 169 91 138 77 48 29 137 160 89 131
These are, in order, the 16 measures that you take from the starting composition to make your composition. So for this
example, measure 104 from the starting composition will become measure 1, measure 74 will become measure 2, and so on,
with measure 131 from the starting composition becoming measure 16. [Here is the result for this
example.](https://gist.githubusercontent.com/cosmologicon/add771c183866539d5a68c2d9771ed49/raw/4d3d207d0bce3a87ea089c0920b95473316381be/mozart-dice-example-solution.txt
## Listening to your composition
I threw together [a JavaScript page that converts the format used here into generated
sounds](http://ufx.space/stuff/mozart-dice/). Try it out by pasting your output into the text box and hitting play.
If you're feeling extra ambitious, use a library in the language of your choice to convert your text file into a
playable music file, such as MP3 or MIDI.
# Acknowledgements
*Mozart's dice game is in the public domain. [A PDF can be found
here.](http://hz.imslp.info/files/imglnks/usimg/b/bc/IMSLP20432-PMLP47543-mozart_-_dice_waltz.pdf) I used the
MIT-licensed [mozart-dice-game npm package by timmydoza](https://github.com/timmydoza/mozart-dice-game) to generate the
starting composition file.*
*Thanks to composer Mary Bichner for music theory consultation on writing this challenge.*
"""


def main():
    pass


if __name__ == "__main__":
    main()
