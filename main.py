'''
Problema  10
Calculează combinări de n luate câte k (n și k date).
'''


def get_n_choose_k(n, k):
    '''
    :param n: primul parametru
    :param k: al doilea parametru
    :return:  combinări de n luate câte k
    '''
    nfactorial = 1
    kfactorial = 1
    diferentafactorial = 1
    diferenta = n - k
    while (n):
        nfactorial = nfactorial * n
        n = n - 1
    while (k):
        kfactorial = kfactorial * k
        k = k - 1
    while (diferenta):
        diferentafactorial = diferentafactorial * diferenta
        diferenta = diferenta - 1
    rez = (nfactorial // (kfactorial * diferentafactorial))
    return rez


def test_get_n_choose_k():
    '''

    :return: Verifica get_n_choose_k()
    '''
    assert get_n_choose_k(10, 8) == 45
    assert get_n_choose_k(10, 1) == 10
    assert get_n_choose_k(32, 28) == 35960


'''
Problema 1
Găsește ultimul număr prim mai mic decât un număr dat.
'''


def prim(a):
    '''

    :param a: primul parametru
    :return: daca 'a' este numar prim
    '''
    if a == 1:
        return False
    else:
        for i in range(2, int(a / 2), 1):
            if a % i == 0:
                return False
        return True


def get_largest_prime_below(n):
    '''

    :param n: primul parametru
    :return: cel mai mare numar prim mai mic decat parametrul n
    '''
    for i in range(n, 2, -1):
        if prim(i) == True:
            return i


def test_get_largest_prime_below():
    '''

    :return: Verifica get_largest_prime_below()
    '''
    assert get_largest_prime_below(111) == 109
    assert get_largest_prime_below(500) == 499
    assert get_largest_prime_below(50) == 47


'''
problema 5
Determină dacă un număr dat este palindrom.
'''


def is_palindrome(n):
    '''

    :param n: numarul verificat
    :return: daca n este palindrom
    '''

    ogl = 0;
    aux = n
    while n > 0:
        ogl = ogl * 10 + n % 10
        n = n // 10
    if aux == ogl:
        return True
    else:
        return False


def test_is_palindrome():
    '''
    Verifica is_palindrom()
    '''

    assert is_palindrome(12321) == True
    assert is_palindrome(123) == False
    assert is_palindrome(5) == True


def teste():
    test_get_largest_prime_below()
    test_get_n_choose_k()
    test_is_palindrome()


def main():
    teste()
    while True:
        print("1.Comb de n luate k.")
        print("2.Găsește ultimul număr prim mai mic decât un număr dat.")
        print("3.Verifica daca n este palindrom.")
        print("-1.Inchide Programul.")
        optiune = input("Insereaza un numar: ")
        if optiune == "1":
            n = int(input("Introduceti n: "))
            k = int(input("Introduceti k: "))

            print(get_n_choose_k(n, k))
        elif optiune == "2":
            n = int(input("Introduceti n: "))
            print(get_largest_prime_below(n))
        elif optiune == "3":
            n=int(input("Introduceti n: "))
            print(is_palindrome(n))
        elif optiune == "-1":
            print("Inchidere program!")
            break
        else:
            print("Insereaza alt numar: ")


if __name__ == '__main__':
    main()
