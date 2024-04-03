from .misc import modify_elements_in_plist


def complement_plist(plist: list[list]):
    modify_elements_in_plist(plist, lambda x: 1-x)


def concat(plist1: list[list], plist2: list[list]) -> list[list]:
    if not plist1:
        return plist2
    if not plist2:
        return plist1

    res = []
    for p1 in plist1:
        for p2 in plist2:
            res.append(p1 + p2)
    return res


def rotation(perm: list, step: int, direction='r') -> list:
    assert direction in ['r', 'l']
    step = step % len(perm)
    if direction == 'r':
        step = len(perm) - step
    return perm[step:] + perm[:step]

