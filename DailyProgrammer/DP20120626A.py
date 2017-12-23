"""
title: 'Necessities'
input: ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']

output:

    +---------------+
    |  Necessities  |
    +---------------+
    | fairy         |
    | cakes         |
    | happy         |
    | fish          |
    | disgustipated |
    | melon-balls   |
    +---------------+

Bonus: amend the program so that it can output a two-dimensional table instead of a list. For example, a list of
websites:

titles: ['Name', 'Address', 'Description']
input:  [['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
        ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
        ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']]

output:

    +-----------+------------------+-------------------------------+
    |   Name    |     Address      |          Description          |
    +-----------+------------------+-------------------------------+
    | Reddit    | www.reddit.com   | the frontpage of the internet |
    +-----------+------------------+-------------------------------+
    | Wikipedia | en.wikipedia.net | The Free Encyclopedia         |
    +-----------+------------------+-------------------------------+
    | xkcd      | xkcd.com         | Sudo make me a sandwich       |
    +-----------+------------------+-------------------------------+

    Thanks to Medicalizawhat for suggesting this problem at /r/dailyprogrammer_ideas (a version of this problem was
    originally posted here). If you have a problem you think would be good for us, head over there and post it!

"""


def print_line(sizes, fill='='):
    print('+', end='')
    [print('{}+'.format(fill * (s+2)), end='') for s in sizes]
    print('')


def print_fields(sizes, inputs, just=2,):
    print('|', end='')
    if just == 1:
        [print(' {} |'.format(f[1].ljust(f[0], ' ')), end='') for f in zip(sizes, inputs)]
    elif just == 2:
        [print(' {} |'.format(f[1].center(f[0], ' ')), end='') for f in zip(sizes, inputs)]
    elif just == 3:
        [print(' {} |'.format(f[1].rjust(f[0], ' ')), end='') for f in zip(sizes, inputs)]
    print('')


def main():
    titles = ['Name', 'Address', 'Description']
    inputs = [['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
              ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
              ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']]
    inputs.insert(0, titles)

    sizes = []
    for z in zip(*inputs):
        sizes.append(max(map(len, z)))

    print_line(sizes)
    print_fields(sizes, inputs[0])
    print_line(sizes)

    for i in inputs[1:-1]:
        print_fields(sizes, i, just=1)
        print_line(sizes, '-')

    print_fields(sizes, inputs[-1], just=1)
    print_line(sizes)


if __name__ == "__main__":
    main()
