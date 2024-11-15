
def test_fib_string_equal(perm: list[int], k: int) -> bool:
    c = 0
    for e in perm:
        if e not in [0, 1]:
            raise Exception('Not a binary word.')
        if e == 0:
            c = 0
        else:
            c += 1
            if c > k:
                return False
    return True

def test_fib_string(perm: list[int], p: int) -> bool:
    c = 0
    for e in perm:
        if e not in [0, 1]:
            raise Exception('Not a binary word.')
        if e == 0:
            c = 0
        else:
            c += 1
            if c >= p:
                return False
    return True


def test_lucas_equal(perm: list[int], k: int) -> bool:
    if not test_fib_string_equal(perm, k):
        return False
    try:
        return k >= (perm.index(0)+perm[-1::-1].index(0))
    except ValueError:
        return k >= len(perm)


def test_lucas(perm: list[int], p: int) -> bool:
    if not test_fib_string(perm, p):
        return False
    try:
        return p > (perm.index(0)+perm[-1::-1].index(0))
    except ValueError:
        return False
    

