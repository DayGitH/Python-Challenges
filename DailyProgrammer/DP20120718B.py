"""
Working on planning a large event (like a wedding or graduation) is often really difficult, and requires a large number
of dependant tasks. However, doing all the tasks linearly isn't always the most efficient use of your time. Especially
if you have multiple individuals helping, sometimes multiple people could do some tasks in parallel.

We are going to define an input set of tasks as follows. The input file will contain a number of lines, where each line
has a task name followed by a colon, followed by any number of dependencies on that task. A task is an alphanumeric
string with underscores and no whitespace

For example, lets say we have to eat dinner. Eating dinner depends on dinner being made and the table being set. Dinner
being made depends on having milk, meat and veggies. Having milk depends on going to the fridge, but meat and veggies
depend on buying them at the store. buying them at the store depends on having money, which depends on depositing ones
paycheck.... this scenario would be described in the following input file. Note task definitions can appear in any order
and do not have to be defined before they are used.

eat_dinner: make_dinner set_table
make_dinner: get_milk get_meat get_veggies
get_meat: buy_food
buy_food: get_money
get_veggies: buy_food
get_money: deposit_paycheck

Write a program that can read an input file in this syntax and output all the tasks you have to do, in an ordering that
no task happens before one of its dependencies.
"""


class Node:
    def __init__(self, value, above=None, below=None):
        self.value = value
        self.above = set()
        self.below = set()

        if above:
            self.add_above(above)
        if below:
            self.add_below(below)

    def add_above(self, value):
        self.above.add(value)

    def remove_above(self, value):
        self.above.remove(value)

    def add_below(self, value):
        self.below.add(value)


def work_list(inp):
    node_list = {}
    working_list = inp.split('\n')

    for w in working_list:
        head, tails = w.split(': ')

        if head not in node_list:
            node_list[head] = Node(head)

        for t in tails.split(' '):
            if t not in node_list:
                node_list[t] = Node(t, below=head)
            else:
                node_list[t].add_below(head)
            node_list[head].add_above(t)

    res = []
    while node_list:
        hold = [n for n in node_list.keys() if not node_list[n].above]
        res += hold
        for h in hold:
            node_list = remove_node(h, node_list)
    return res


def remove_node(node, node_list):
    node_list.pop(node)
    for n in node_list:
        if node in node_list[n].above:
            node_list[n].remove_above(node)
    return node_list


def main():
    inp = ("eat_dinner: make_dinner set_table\n"
           "make_dinner: get_milk get_meat get_veggies\n"
           "get_meat: buy_food\n"
           "buy_food: get_money\n"
           "get_veggies: buy_food\n"
           "get_money: deposit_paycheck")

    print(work_list(inp))


if __name__ == "__main__":
    main()
