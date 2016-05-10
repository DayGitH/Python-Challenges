"""
Tower of Hanoi [http://en.wikipedia.org/wiki/Tower_of_Hanoi] is a famous problem.

the challenge today is a very famous one where you are to write a function to calculate the total number of moves to
solve the tower in fastest way possible
"""


class Hanoi:
    def __init__(self, n):
        self.A = [i for i in range(n)]
        self.B = []
        self.C = []
        self.hist = {i: '' for i in range(n)}
        self.prev = -1

    def recursive(self, num, frm, to):
        # get spare list name
        spr = self.get_spare(frm, to)

        if num > len(self.get_col(frm)):
            print('invalid num value')
            return

        if num != 1:
            self.recursive(num-1, frm, spr)
        self.move_pin(num-1, frm, to)
        if num != 1:
            self.recursive(num -1, spr, to)

    def iterative(self, frm, to):
        # get tower lists based on labels
        f = self.get_col(frm)
        t = self.get_col(to)
        spr = self.get_spare(frm, to)
        s = self.get_col(spr)

        # first move based on size of starting column
        if len(f) % 2 == 0:
            self.move_pin(0, frm, spr)
            self.hist[0] = frm
        else:
            self.move_pin(0, frm, to)
            self.hist[0] = frm

        success = False
        while f or s:
            # while from and spare list have elements present
            for a in [frm, spr, to]:
                for b in [frm, spr, to]:
                    success = False
                    if a == b:
                        # ignore if same list in both for loops
                        continue
                    try:
                        # get element for moving
                        smallest = self.get_smallest(self.get_col(a))

                        # hist_check to stop moving back into previous position
                        # prev check to stop moving recently moved element twice in a row
                        if self.hist_check(smallest, b) and smallest != self.prev:
                            self.move_pin(smallest, a, b)
                            self.prev = smallest
                            self.hist[smallest] = frm if a == frm else to if a == to else spr
                            success = True
                            # print('\n{} > {} success\n'.format(a, b))
                    except:
                        pass
                        # print('f>t failed')

                    if success:
                        break
                if success:
                    break

    def move_pin(self, n, frm, to):
        f = self.get_col(frm)
        t = self.get_col(to)
        if self.check_smallest(n, f) and self.can_recieve(n, t):
            t.append(f.pop(f.index(n)))
            t.sort()
        else:
            raise Exception('impossible')

        print(self.A, self.B, self.C)

    def hist_check(self, n, to):
        return not self.hist[n] == to

    def get_col(self, col):
        if col == 'A':
            return self.A
        elif col == 'B':
            return self.B
        elif col == 'C':
            return self.C
        else:
            print('error in get_col')

    def get_spare(self, frm, to):
        l = ['A', 'B', 'C']
        l.remove(frm)
        l.remove(to)

        return l[0]

    def check_smallest(self, n, frm):
        # print(frm[0])
        return frm[0] == n
        # if frm[0] == n:
        #     return True
        # else:
        #     return False

    def get_smallest(self, frm):
        return frm[0]

    def can_recieve(self, n, to):
        try:
            return to[0] > n
        except IndexError:
            return True
        # if to[0] > n:
        #     return False
        # else:
        #     return True

if __name__ == '__main__':
    h = Hanoi(7)

    # h.iterative('A', 'C')
    h.recursive(7, 'A', 'C')
