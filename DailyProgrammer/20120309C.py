"""
We'd like to write a list of people, ordered so that no one appears in the list before anyone he or she is less smart
than.

The input will be a list of pairs of names, one pair per line, where the first element in a pair names a person smarter
than the person named by the second element of the pair. That is, each input line looks like:
smarter-person : less-smart-person

For example:
Einstein : Feynmann
Feynmann : Gell-Mann
Gell-Mann : Thorne
Einstein : Lorentz
Lorentz : Planck
Hilbert : Noether
Poincare : Noether

There is no limit to the number of lines of input. Your output should be a list of all the distinct input names,
without duplicates, one per line, ordered as described above. For example, given the input shown above, one valid
output would be:
Einstein
Feynmann
Gell-Mann
Thorne
Lorentz
Planck
Hilbert
Poincare
Noether

Note that the "smarter than" relation supplied as input will not, in general, specify a total order that would allow us
to write out the desired list in strictly decreasing order of smartness. For example, the following output is also
valid for the input shown above:
Hilbert
Einstein
Feynmann
Gell-Mann
Poincare
Thorne
Lorentz
Planck
Noether

from a programming contest
"""

inp = '''Einstein : Feynmann\n''' \
      '''Feynmann : Gell-Mann\n''' \
      '''Gell-Mann : Thorne\n''' \
      '''Einstein : Lorentz\n''' \
      '''Lorentz : Planck\n''' \
      '''Hilbert : Noether\n''' \
      '''Poincare : Noether'''

final = []
work = inp.split('\n')
workingflg = False

while True:
    for w in work:
        up, down = w[:w.index(' :')], w[w.index(': ') + 2:]

        if up not in final:
            final.append(up)
        if down not in final:
            final.append(down)

        i_up = final.index(up)
        i_dn = final.index(down)
        if i_dn < i_up:
            final.insert(i_dn, final.pop(i_up))
            workingflg = True

    if workingflg:
        workingflg = False
    else:
        break

print(final)
