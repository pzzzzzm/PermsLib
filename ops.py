import perm


def swap(p, a, b, is_copy=True):
    if is_copy:
        p = p.copy()
    temp = p.elements[a]
    p.elements[a] = p.elements[b]
    p.elements[b] = temp
    return p


def flip(p, a, b, is_copy=True):
    if is_copy:
        p = p.copy()
    while a < b:
        swap(p, a, b, False)
        a += 1
        b -= 1
    return p


def rotate(p, a, b, to_right=True, is_copy=True):
    if is_copy:
        p = p.copy()
    if to_right:
        while b != a:
            swap(p, b-1, b, False)
            b -= 1
    else:
        while a != b:
            swap(p, a, a+1, False)
            a += 1
    return p


def complement(p, is_copy=True):
    if is_copy:
        p = p.copy()
    c = max(p.elements)+1
    for i in range(len(p.elements)):
        p.elements[i] = c - p.elements[i]
    return p


def index_repr(p):
    index_list = [0 for _ in range(len(p.elements))]
    for i in range(1, len(p.elements)+1):
        e = p.elements[i-1]
        index_list[e-1] = i
    return perm.Perm(index_list)

