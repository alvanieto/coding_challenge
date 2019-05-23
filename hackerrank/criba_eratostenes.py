import typing


def criba_eratostenes(max_: int) -> typing.List[int]:
    not_prime = set()
    prime = []
    for i in range(2, max_ + 1):
        if i not in not_prime:
            prime.append(i)
            not_prime.update(range(i * i, max_ + 1, i))
    return prime
