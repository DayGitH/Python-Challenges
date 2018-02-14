"""
[10/24/2014] Challenge #185 [Intermediate to Hard] Roots of a Polynomial

https://www.reddit.com/r/dailyprogrammer/comments/2k7mnn/10242014_challenge_185_intermediate_to_hard_roots/

# [](#HardIcon) **(Intermediate to Hard)**: Roots of a Polynomial
In mathematics, a polynomial is a form of expression. The type of polynomials we're dealing with today are called
*univariate* polynomials, which means they only have one variable. For this challenge, this variable will be called
`x`. You'll need to dig out your algebra textbooks if you're a bit rusty, though this challenge doesn't require you to
use anything more than high school (A-level) mathematics.
The simplest type of polynomial is this:
    4
Fairly simple, right? Right. A constant value such as `4`, `0` or `-0.2` are polynomials of degree zero.  The next
simplest type looks like this:
    4x+3
The equation for a straight-line graph is a polynomial of degree one. Again, fairly simple to work with. The good thing
about polynomials is that we can visualise them using graphs. [Here is the graph for `y=4x+3`, the polynomial
above](https://www.desmos.com/calculator/llczd44a8i). The next simplest is the quadratic equation, otherwise known as a
polynomial of degree two (notice the pattern yet?). These are similar to linear equations, but they feature a multiple
of x squared bolted onto the front. [Here is the graph of `y=x^2-6x+3`](https://www.desmos.com/calculator/nmzbjtiqmf),
[and here is the graph of `y=(-1/3)x^2-x+8`](https://www.desmos.com/calculator/2vjpjxxgwp).
The cool thing about quadratics is that you can create them by multiplying together two linear polynomials. For
example, `(3x-1)(x+7)` is the same as `3x^2+20x-7`, [as you can see
here](https://www.desmos.com/calculator/si0svfjmcj). If we take a look at the graph of `y=3x-1`, `y=x+7` and
`y=3x^2+20x-7` we notice something interesting. [Here you can see](https://www.desmos.com/calculator/maw5tkik1p) the
quadratic graph crosses the x-axis at the same point as where the linear graphs do. The point where a polynomial
crosses the x=axis are called its *roots* - which is what we will be finding in today's challenge.
You can also do the reverse operation - given an equation, find its roots. For a linear equation, this is simple. A bit
of algebraic jiggery-pokery gives us these steps. Remember, the graph will cross the x-axis where the height (y) is at
zero, so we need to set `y=0`.
    y=ax+b and y=0
    0=ax+b (replace the y in the first equation with 0, as y=0)
    -b=ax (subtract b from both sides)
    -b/a=x (divide both sides by a)
Therefore, we can see that if we have a linear equation `y=ax+b`, it crosses the x=axis at the point where its x value
is `-b/a`. The same can be done for quadratic polynomials via a few methods, including using the [quadratic
formula](https://en.wikipedia.org/wiki/Quadratic_formula) or [completing the
square](https://en.wikipedia.org/wiki/Completing_the_square). If all else fails you can just draw the graph of the
expression to approximate its roots.
What happens when the plotted graph never crosses the x-axis? Simply, it has *no* roots (or no real roots). If you
attempt to use the quadratic formula on an equation such as `x^2+x+4` you will end up square-rooting a negative number,
which we ignore for today's challenge.
Things get a little awkward when you have 3rd-degree polynomials and above. They act the same and are treated the same
as other polynomials but there is no simple formula to find the roots. The Babylonians could find the roots of
quadratic polynomials, but it took mathematicians until the Renaissance to find a one-step formula to get the roots of
a cubic polynomial.
Rather than bothering with the convoluted cubic formula you can instead use what are known as numerical methods. These
methods are approximation methods, and rather than giving you an exact answer immediately they 'home in' on the roots
like a heat-seeking missile. The benefits of these are that they can be used to find roots of almost any mathematical
function, not only polynomils. They can also be used to find roots of very complex polynomials, where a one-step
equation would be huge and ugly. The downsides are that they can often be slow to find the answer, they can only give
you one root at a time and, sometimes, they never even find the root at all! There are several numerical methods to
find polynomial roots, the most commonly used are these:
* [Interval Bisection method](https://en.wikipedia.org/wiki/Bisection_method). This is a simple to understand,
divide-and-conquer algorithm.
* [Newton-Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method). More complex to understand but quicker at
finding a root.
* [Other root finding algorithms](https://en.wikipedia.org/wiki/Root-finding_algorithm#Interpolation_2) such as linear
interpolation are also easy to understand.
Your challenge is, given a polynomial expression of degree no higher than 7, find a root (if it exists) of the
expression where it crosses the x-axis (equal to zero.)
# Formal Inputs and Outputs
## Input Description
You will accept a polynomial in the form used in this challenge description. That is:
* `x` denotes the variable.
* `^...` denotes the exponent of a term.
* A constant denotes the coefficient of a term.
A valid input would be `x^3-5x^2+10x-44` or `-4x^5-7`, but not `2^x+3` (not a polynomial), `x^2+2xy+y^2` (more than one
variable) or `x^11-6x^2-1` (no higher than 7th degree allowed; that is 11th degree).
## Output Description
You are to output a root of the polynomial as a number (or an algebraic expression.. if you're crazy!)
# Sample Inputs and Outputs
Here are some examples to get you going. You can create your own by [typing them in on
Wolfram|Alpha](http://www.wolframalpha.com/input/?i=x^2-7x%2B6), which also plots it and tells you the roots, if any.
## Sample Inputs
1. `4x^2-11x-3`
2. `4x-8`
3. `x^4-2x^3+7x^2-16x+4`
4. `x^2-7x+6`
## Sample Outputs
1. `-0.25` or `3`
2. `2`
3. `2` or `0.2825..`
4. `1` or `6`
# Extension (Hard)
You've found one root of the polynomial - now modify your solution to find *all* of the roots. This will require a
divide-and-conquer algorithm of some sort.
"""


def main():
    pass


if __name__ == "__main__":
    main()
