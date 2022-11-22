import ops


class Perm:

    def __init__(self, n, preset=None):
        self.n = n
        if preset is None:
            self.elements = [i for i in range(1, n+1)]
        else:
            if len(preset) != n:
                raise Exception('Inconsistent length of init array.')
            else:
                self.elements = preset

    def __str__(self):
        s = ''
        for e in self.elements:
            s += str(e) if e < 10 else '({})'.format(e)
        return s

    def swap(self, a, b):
        ops.swap(self, a, b)

    def flip(self, a, b):
        ops.swap(self, a, b)

    def rotate(self, a, b, to_right=True):
        ops.rotate(self, a, b, to_right)

    def copy(self):
        return Perm(self.n, self.elements.copy())

