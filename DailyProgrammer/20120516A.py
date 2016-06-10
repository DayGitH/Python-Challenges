"""
Write a function that given two sorted lists, returns a list whith the two lists merged together into one sorted list.
So, for instance, for inputs [1,5,7,8] and [2,3,4,7,9] it should return [1,2,3,4,5,7,7,8,9].
Try and make your code as efficient as possible.
"""


def main():
    inp1 = [1, 5, 7, 8]
    inp2 = [1, 2, 3, 4, 5, 7, 7, 8, 9]

    res = []
    while inp1 or inp2:
        if inp1 and inp2:
            if inp1[0] <= inp2[0]:
                res.append(inp1.pop(0))
            else:
                res.append(inp2.pop(0))
        elif inp1:
            res.append(inp1.pop(0))
        elif inp2:
            res.append(inp2.pop(0))

    print(res)

if __name__ == "__main__":
    main()
