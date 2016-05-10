"""
Write a program that draws a square spiral [http://10binary.deviantart.com/art/square-spiral-203786602] . You can print
out this spiral in ASCII text, but using a graphics library would produce a more pleasant output.
Bonus: Now draw a normal spiral. Some samples of spirals can be found here [Broken link] .
"""

def unshared_copy(inList):
    ''' Copies cascaded lists'''
    if isinstance(inList, list):
        return list( map(unshared_copy, inList) )
    return inList


def fill(array, pos_x, pos_y, clockwise, axis_increment, positive_increment):
    ''' Fills one line'''
    x = pos_x
    y = pos_y
    working_set = unshared_copy(array)

    while True:
        working_set[y][x] = '#'

        # Check axis and direction of line
        if axis_increment == 'x' and positive_increment:
            try:
                # check two positions ahead to see if we need to stop increasing
                if working_set[y][x + 2] == '#':
                    break
            except IndexError:
                pass
            try:
                # check if increasing will cause index error
                if working_set[y][x + 1] == ' ':
                    x += 1
            except IndexError:
                break
        elif axis_increment == 'x' and not positive_increment:
            try:
                # check two positions ahead to see if we need to stop increasing
                if x - 2 < 0:
                    raise IndexError
                if working_set[y][x - 2] == '#':
                    break
            except IndexError:
                pass
            try:
                # check if increasing will cause index error
                if x - 1 < 0:
                    raise IndexError
                if working_set[y][x - 1] == ' ':
                    x -= 1
            except IndexError:
                break
        elif axis_increment == 'y' and positive_increment:
            try:
                # check two positions ahead to see if we need to stop increasing
                if working_set[y + 2][x] == '#':
                    break
            except IndexError:
                pass
            try:
                # check if increasing will cause index error
                if working_set[y + 1][x] == ' ':
                    y += 1
            except IndexError:
                break
        elif axis_increment == 'y' and not positive_increment:
            try:
                # check two positions ahead to see if we need to stop increasing
                if y - 2 < 0:
                    raise IndexError
                if working_set[y - 2][x] == '#':
                    break
            except IndexError:
                pass
            try:
                # check if increasing will cause index error
                if y - 1 < 0:
                    raise IndexError
                if working_set[y - 1][x] == ' ':
                    y -= 1
            except IndexError:
                break

    return working_set, x, y


def flip_increments(clockwise, axis_increment, positive_increment):
    ''' flips the axis and positive increment depending on requirement'''
    return_axis = axis_increment
    if axis_increment == 'x':
        return_axis = 'y'
    elif axis_increment == 'y':
        return_axis = 'x'

    return_pos = positive_increment
    if clockwise and axis_increment == 'y':
        return_pos = not positive_increment
    elif not clockwise and axis_increment == 'x':
        return_pos = not positive_increment

    return return_axis, return_pos


size = 101
pos_x = 0
pos_y = 0
positive_increment = True
axis_increment = 'x'
clockwise = True

array = [[' ' for a in range(size)] for b in range(size)]

# print(array)

distance = size

while True:
    old_x, old_y = pos_x, pos_y
    array, pos_x, pos_y = fill(array, pos_x, pos_y, clockwise, axis_increment, positive_increment)
    axis_increment, positive_increment = flip_increments(clockwise, axis_increment, positive_increment)

    if old_x == pos_x and old_y == pos_y:
        break

for a in array:
    print(' '.join(a))