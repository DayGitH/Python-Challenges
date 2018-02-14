"""
[2016-07-29] Challenge #277 [Hard] Trippy Julia fractals

https://www.reddit.com/r/dailyprogrammer/comments/4v5h3u/20160729_challenge_277_hard_trippy_julia_fractals/

#Description
You’re making a music video for an acid rock band. Far out man! Of course they want visual effects with fractals,
because they’ve googled fractals, and they’re [super
trippy](https://www.google.com/search?q=fractal&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjljOT9l7nNAhXIKo8KHct2CckQ_AUICCgB&biw=1920&bih=1014).
Of course, they don’t know the mad programming needed to make these fractals. But you do, and that’s why they pay you
money.
A [Julia set](http://wikipedia.org/wiki/julia_set) is made by applying a function to the complex numbers repeatedly and
keeping track of when the resulting numbers reach a threshold value. One number may take 200 iterations to achieve and
absolute value over a certain threshold, value while an *almost* identical one might only take 10 iterations.
Here, we’re interested in Julia sets because you can make [pretty
pictures](https://en.wikipedia.org/wiki/Julia_set#/media/File:Julia_-0.8_0.156.png) with them if you map each complex
input number to a pixel on the screen. The task today is to write a program that does all the math necessary for your
computer to draw one of these beautiful pictures. In addition to making a buck from the band, you can also make a set
of nice wallpapers for your desktop!
##How to make a picture from a Julia set
*1 – Pick your function*
Pick a function f which maps from a complex number z to another complex number. In our case we will use f(x) = z^2 –
0.221 – 0.713 i, because that makes a particularly pretty picture. To customize your own picture you can change the
constant – 0.221 – 0.713 i to something else if you want.
The threshold value for this function is 2.
*2 – Make a set of complex numbers*
The only complex numbers which are interesting for the Julia set are the ones where both the real and the imaginary
part is between -1 and 1.  That’s because, if the absolute value of an input number exceeds the threshold value, it
will keep increasing or decreasing without bounds when you keep applying your function. So your program needs to keep a
whole bunch of these small complex numbers in memory – one number for each pixel in your final image.
*3 - Apply f to that set of complex numbers iteratively*
Your program needs to check *how many times you can apply the function f to each of the complex numbers above before
its absolute value crosses the threshold value*. So for each of your complex numbers, you get number of iterations, I.
*4 – Map the values of I to pixels in a picture*
You can do this in many ways, but an easier way, which I recommend, is that the real and imaginary parts of the complex
numbers are the positions of the pixel on the X- and Y-axis, respectively, and I is the intensity of the pixel. You
might want to set some cutoff to prevent specific pixels from iterating thousands of times.
##Illustrative example
Say I want to make a 3x3 pixel image. I use the function f(z) = z^2 – 0.221 – 0.713 i. I map the complex numbers with
both real and imaginary parts in the interval [-1, 1] to the nine pixels, giving nine input complex numbers (pixels):
(-1 + 1\*i) (0 + 1\*i) (1 + 1\*i)
(-1 + 0\*i) (0 + 0\*i) (1 + 0\*i)
(-1 - 1\*i) (0 - 1\*i) (1 - 1\*i)
I calculate how many times I need to apply f to each pixel before its absolute value crosses the threshold value 2:
(1) (5) (2)
(3) (112) (3)
(2) (5) (1)
Finally I convert it to a 3x3 pixel image with the intensities above (not shown).
#Formal Inputs & Outputs
##Input description
The desired resolution in pixels written as X Y for example:
500 400
##Output description
A Julia set with the desired resolution, in this case:
[A link to the output picture](http://imgur.com/4nVcHVk)
#Bonuses
##Bonus #1
The band needs to upload in HD. Make your program fast enough to make wallpaper-sized pictures of 1920 x 1080 pixels
with a reasonable iteration depth (128 or above).
##Bonus #2
Make your program accept an arbitrary function, f, instead of just f(x) = z^2 – 0.221 – 0.713 i. The right function can
really make the shapes crazy!
##Bonus #3
Because neighboring pixels can vary a lot in intensity (this is a property of the Julia sets!), the result looks a
little pixelated. Implement some kind of [anti-alialising](https://en.wikipedia.org/wiki/Spatial_anti-aliasing) to make
it look prettier.
##Bonus #4
The problem is [embarrasingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel). There’s a lot of speed
to gain by parallising your code!
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
This challenge is posted by /u/Gobbedyret . All credits go to him/her
"""


def main():
    pass


if __name__ == "__main__":
    main()
