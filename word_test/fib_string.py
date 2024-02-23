
def test_fib_string(perm: list[int], k: int) -> bool:
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


def test_lucas(perm: list[int], k: int) -> bool:
    if not test_fib_string(perm, k):
        return False
    try:
        return k >= (perm.index(0)+perm[-1::-1].index(0))
    except ValueError:
        return k >= len(perm)
    

