"""
The divisors of a number are those numbers that divide it evenly; for example, the divisors of 60 are 1, 2, 3, 4, 5, 6,
10, 12, 15, 20, 30, and 60. The sum of the divisors of 60 is 168, and the number of divisors of 60 is 12.

The totatives of a number are those numbers less than the given number and coprime to it; two numbers are coprime if
they have no common factors other than 1. The number of totatives of a given number is called its totient. For example,
the totatives of 30 are 1, 7, 11, 13, 17, 19, 23, and 29, and the totient of 30 is 8.

Your task is to write a small library of five functions that compute the divisors of a number, the sum and number of its
divisors, the totatives of a number, and its totient.

    taken from programmingpraxis.com

It seems the number of users giving challenges have been reduced. Since my final exams are going on and its kinda
difficult to think of all the challenges, I kindly request you all to suggest us interesting challenges at
/r/dailyprogrammer_ideas .. Thank you!

"""


def divisors(n):
    divisor_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor_list.append(i)

    return divisor_list


def divisor_sum(n):
    return sum(divisors(n))


def divisor_count(n):
    return len(divisors(n))


def totatives(n):
    n_div = divisors(n)[1:]
    tots = [1]
    for i in range(2, n):
        i_div = divisors(i)[1:]
        if not set(n_div) & set(i_div):
            tots.append(i)
    return tots


def totient(n):
    return len(totatives(n))


def main():
    number = 60
    print(number)
    print(divisors(number))
    print(divisor_sum(number))
    print(divisor_count(number))

    print('\n')

    number = 30
    print(number)
    print(totatives(number))
    print(totient(number))


if __name__ == "__main__":
    main()
