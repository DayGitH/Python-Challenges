"""
[2017-12-08] Challenge #343 [Hard] Procedural music generation

https://www.reddit.com/r/dailyprogrammer/comments/7ifbd5/20171208_challenge_343_hard_procedural_music/

Today we have an open-ended challenge: write a program to generate music. The goal, like [this week's Intermediate
challenge](https://www.reddit.com/r/dailyprogrammer/comments/7i1ib1/20171206_challenge_343_intermediate_mozarts), is to
create a piece of music that has never been written down or heard before, but taking it to the next level. Knowledge of
music theory can be applied to this challenge, but it is not required.
You can use whatever methods you want, including using existing music as training data or input. But you should not
just apply straightforward manipulations to existing music like with this week's Intermediate challenge. One common
technique is to [train a Markov chain model on existing music](https://en.wikipedia.org/wiki/Markov_chain#Music). Other
techniques are perfectly valid too, such as [cellular automata](http://tones.wolfram.com) or [neural
networks](http://www.cs.colorado.edu/~mozer/Research/Selected%20Publications/music.html).
Make it as short or as long as you like. Even 16 beats is not easy.
# Training/input data
For your convenience I've converted a few pieces of music into an easy-to-use format, which you can listen to using the
tool below. You don't have to use these pieces: you can use other pieces, or no inputs at all.
* [Mozart: Rondo Alla
Turca](https://gist.githubusercontent.com/cosmologicon/310dfe3aa8a5b9b8f558caa995e0ee68/raw/baa3c343d69295dba226610362bc321a2e36ffc9/rondo.txt
* [Mozart: Eine Kleine
Nachtmusik](https://gist.githubusercontent.com/cosmologicon/f0ec10d86346af3a23762464741a0a03/raw/9f3812b56e53d63c22c11729394c8513b257265a/eine-kleine.txt
* [Debussy: Clair de
Lune](https://gist.githubusercontent.com/cosmologicon/eb532ac6bf58ddb12cfe6d2840ad1fe5/raw/ace3acac23267d7d1bb3d209505ad9c69c2570a4/clair-de-lune.txt
* [Beethoven: Für
Elise](https://gist.githubusercontent.com/cosmologicon/5d0b86abe51a9ee572dc0f57718ef83d/raw/d57da806d33cdd1187aac7a103dec7f21d17ddcb/elise.txt
Each line in this format specifies a note with three values: pitch, starting time, and duration. The pitch number is
the [MIDI note
number](http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm), where
middle C = 60. The starting time and duration are both in units of beats. For example, the line:
    37 8.5 0.5
means to play the note C#3 (corresponding to a pitch number of 37) for 0.5 beats, starting at beat 8.5.
You can use this format for your output too, or use any other format you like (including audio formats). Of course,
it's more fun if you can listen to it one way or another!
# Listening and sharing
I threw together [this JavaScript page that converts the above format into generated
sounds](http://ufx.space/stuff/procmusic/). If you use the same format, paste your output there and hit play to listen.
Share the URL with us so we can listen too!
# Ideas
There are many tweaks you can make to change the sound of your output. One simple way to try to improve the sound is to
select notes only from a certain scale. (If you don't know what a scale is, you can learn by doing [this week's Easy
challenge](https://www.reddit.com/r/dailyprogrammer/comments/7hhyin/20171204_challenge_343_easy_major_scales/).) Of
course you may apply any other music theory knowledge you have.
You might also consider, instead of randomly choosing notes, basing your selection of notes on real-world scientific
data. (This idea comes from my favorite novel, Dirk Gently.)
If you have any musically-inclined friends, see if they can tell the difference between output based on Mozart and
output based on Beethoven.
Good luck!
"""


def main():
    pass


if __name__ == "__main__":
    main()
