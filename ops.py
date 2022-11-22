
def swap(p, a, b):
    temp = p.elements[a]
    p.elements[a] = p.elements[b]
    p.elements[b] = temp


def flip(p, a, b):
    while a < b:
        swap(p, a, b)
        a += 1
        b -= 1


def rotate(p, a, b, to_right=True):
    if to_right:
        while b != a:
            swap(p, b-1, b)
            b -= 1
    else:
        while a != b:
            swap(p, a, a+1)
            a += 1

