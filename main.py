# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.

n_1 = input('get n_1: ')
try:
    n_1 = int(n_1)
except ValueError:
    print('not int')

n_2 = input('get n_2: ')
try:
    n_2 = int(n_2)
except ValueError:
    print('not int')


def my_f(n_1, n_2, operation_type='+'):
    if type(n_1) is int and type(n_2) is int:
        return n_1 + n_2
    else:
        print('0')


print(my_f(n_1, n_2))


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n]

def a(n):
    sum = 0

    def b(n):
        sum = 0

        def c(n):
            sum = 0
            if not n % 2 == 0:
                sum += 0
            return sum + c(n - 1)

        if n % 2 == 0:
            sum += n
        return sum + b(n - 1)

    if n == 0:
        return 0

        c(n)

    b(n)
    return n + a(n - 1)


print(a(5))




