
def _check_qab(q, a, b):
    return a == 0 or q*a > b


def check_q_decreasing(perm: list[int], q: float) -> bool:
    a, b, prev = 0, 0, 0
    for e in perm:
        if e not in [0, 1]:
            raise Exception('Not a binary word.')
        if prev == 0:
            if e == 0:
                a += 1
            else:
                b += 1
                prev = 1
        else:
            if e == 1:
                b += 1
            else:
                if _check_qab(q, a, b):
                    a, b, prev = 1, 0, 0
                else:
                    return False
    return _check_qab(q, a, b)
