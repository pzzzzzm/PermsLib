import ops


class Perm:

    def __init__(self, preset=None):
        self.elements = preset

    def __str__(self):
        s = ''
        for e in self.elements:
            s += str(e) if e < 10 else '({})'.format(e)
        return s

    def swap(self, a, b):
        ops.swap(self, a, b, False)

    def flip(self, a, b):
        ops.swap(self, a, b, False)

    def rotate(self, a, b, to_right=True):
        ops.rotate(self, a, b, to_right, False)

    def complement(self):
        ops.complement(self, is_copy=False)

    def copy(self):
        return Perm(self.elements.copy())

