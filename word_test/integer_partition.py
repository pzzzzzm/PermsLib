
def test_integer_partition(perm: list[int], s: int) -> bool:
    c = 0
    b = perm[0]
    for p in perm:
        if b >= p:
            c += p
        else:
            return False
    return c == s
