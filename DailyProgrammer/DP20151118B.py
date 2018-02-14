"""
[2015-11-18] Challenge # 242 [Intermediate] VHS recording problem

https://www.reddit.com/r/dailyprogrammer/comments/3u6o56/20151118_challenge_242_intermediate_vhs_recording/

**Description**
All nineties kids will remember the problem of having to program their vhs recorder to tape all their favorite shows.
Especially when 2 shows are aired at the same time, which show do we record?
Today we are going to program the recorder, so that we have a maximum amount of tv shows on one tape.
*Input*
    1530 1600
    1555 1645
    1600 1630
    1635 1715
*Output*
    3
**Input description**
You recieve a timetable with when the shows start and when it ends. All times are in Military time.
**Output description**
You return the maximum number of shows you can record.
We can switch between channels instantaneously, so if a shows start on the same time a other one stops, you can record
them.
**Inputs**
*Set 1*
    1530 1600
    1605 1630
    1645 1725
    1700 1730
    1700 1745
    1705 1745
    1720 1815
    1725 1810
*Set 2*
    1555 1630
    1600 1635
    1600 1640
    1610 1640
    1625 1720
    1635 1720
    1645 1740
    1650 1720
    1710 1730
    1715 1810
    1720 1740
    1725 1810
**Bonus 1**
We want to know what shows we have recorded, so instead of showing the number of shows, show the names of the shows we
recorded.
*Input*
    1535 1610 Pokémon
    1610 1705 Law & Order
    1615 1635 ER
    1615 1635 Ellen
    1615 1705 Family Matters
    1725 1810 The Fresh Prince of Bel-Air
*Output*
    Pokémon
    Law & Order
    The Fresh Prince of Bel-Air
**Bonus 2**
Now the first line will be a **must see** show. We don't care if we don't max out the number of shows, but we sure want
to have our favorite recorded.
*Input*
    The Fresh Prince of Bel-Air
    1530 1555 3rd Rock from the Sun
    1550 1615 The Fresh Prince of Bel-Air
    1555 1615 Mad About You
    1615 1650 Ellen
    1655 1735 Quantum Leap
*Output*
    The Fresh Prince of Bel-Air
    Ellen
    Quantum Leap
If you want to generate more, I got a dotnetfiddle for:
 - [Challenge](https://dotnetfiddle.net/xjXHl9)
 - [Bonus 1](https://dotnetfiddle.net/bn5QrS)
 - [Bonus 2](https://dotnetfiddle.net/6dwkGl)
**Finally**
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[2015-11-18] Challenge # 241 [intermediate] ascii Bitmap Chess

https://www.reddit.com/r/dailyprogrammer/comments/3t9lar/20151118_challenge_241_intermediate_ascii_bitmap/

# 1. unicode sucks
From Monday's challenge,
      toascii '1r3rk1/1pnnq1bR/p1pp2B1/P2P1p2/1PP1pP2/2B3P1/5PK1/2Q4R'
    .r...rk.
    .pnnq.bR
    p.pp..B.
    P..P.p..
    .PP.pP..
    ..B...P.
    .....PK.
    ..Q....R
make something like this:
    ┌─┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
    │8│     │X...X│     │.....│     │X...X│  X  │.....│
    │ │     │XXXXX│     │.....│     │XXXXX│XXXXX│.....│
    │ │     │.XXX.│     │.....│     │.XXX.│ XXX │.....│
    │ │     │.XXX.│     │.....│     │.XXX.│XXXXX│.....│
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │7│.....│     │.XXX.│ XXX │X.X.X│     │..X..│O   O│
    │ │.....│  X  │XXXX.│XXXX │XXXXX│     │.XXX.│OOOOO│
    │ │.....│  X  │..X..│  X  │.XXX.│     │..X..│ OOO │
    │ │.....│ XXX │XXXX.│XXXX │X...X│     │..X..│ OOO │
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │6│     │.....│     │.....│     │.....│  O  │.....│
    │ │  X  │.....│  X  │..X..│     │.....│ OOO │.....│
    │ │  X  │.....│  X  │..X..│     │.....│  O  │.....│
    │ │ XXX │.....│ XXX │.XXX.│     │.....│  O  │.....│
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │5│.....│     │.....│     │.....│     │.....│     │
    │ │..O..│     │.....│  O  │.....│  X  │.....│     │
    │ │..O..│     │.....│  O  │.....│  X  │.....│     │
    │ │.OOO.│     │.....│ OOO │.....│ XXX │.....│     │
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │4│     │.....│     │.....│     │.....│     │.....│
    │ │     │..O..│  O  │.....│  X  │..O..│     │.....│
    │ │     │..O..│  O  │.....│  X  │..O..│     │.....│
    │ │     │.OOO.│ OOO │.....│ XXX │.OOO.│     │.....│
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │3│.....│     │..O..│     │.....│     │.....│     │
    │ │.....│     │.OOO.│     │.....│     │..O..│     │
    │ │.....│     │..O..│     │.....│     │..O..│     │
    │ │.....│     │..O..│     │.....│     │.OOO.│     │
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │2│     │.....│     │.....│     │.....│  O  │.....│
    │ │     │.....│     │.....│     │..O..│OOOOO│.....│
    │ │     │.....│     │.....│     │..O..│ OOO │.....│
    │ │     │.....│     │.....│     │.OOO.│OOOOO│.....│
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │1│.....│     │O.O.O│     │.....│     │.....│O   O│
    │ │.....│     │OOOOO│     │.....│     │.....│OOOOO│
    │ │.....│     │.OOO.│     │.....│     │.....│ OOO │
    │ │.....│     │O...O│     │.....│     │.....│ OOO │
    ├─┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
    │ │a    │b    │c    │d    │e    │f    │g    │h    │
    └─┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
Here are some 4x5 crappy bitmaps to get started
    O...O
    OOOOO
    .OOO.
    .OOO.
    ;
    .OOO.
    OOOO.
    ..O..
    OOOO.
    ;
    ..O..
    .OOO.
    ..O..
    ..O..
    ;
    O.O.O
    OOOOO
    .OOO.
    O...O
    ;
    ..O..
    OOOOO
    .OOO.
    OOOOO
    ;
    .....
    ..O..
    ..O..
    .OOO.
    ;
    .....
    ..O..
    .O.O.
    .....
the last one is that ghost square from Monday's challenge.  Bitmaps differences for Starting, Regular, and Ghost Rooks
is encouraged, as is code generating as much as possible of the variations.
# 2. Is the black king in check
[how chess pieces can move](https://en.wikipedia.org/wiki/Chess#Movement)
The black king (k) is in a check position if
1. He pretends he is a bishop(b), and can capture a B or Q(ueen)
2. He pretends he is a rook(r), and can capture a R or Q(ueen)
3. He pretends he is a knight(n), and can capture a N 
4. He pretends he is a pawn(p), and can capture a P
(note that pieces are blocked by other friend and foe pieces from "checking" the king)
For output, list all squares that have a piece that is holding the black king in check.
** sample input **
1r3rk1/1pnnq1bR/p1pp2B1/P2P1p2/1PP1pP2/2B3P1/5PK1/2Q4R
** sample output **
empty - no checks.
** challenge input **
'1r3kR1/4P3/6NB/8/8/Q7/8/4KR2'
"""


def main():
    pass


if __name__ == "__main__":
    main()
