# https://doi.org/10.1007/978-3-031-34347-6_23

from utils import rotation


def semi_meander(n: int, stamp=False) -> list[list[int]]:
    perms = []
    q = [1 for _ in range(n)]

    def gen_meander(p, t):
        i, j = 1, 0
        while i <= t:
            if t >= n:
                perms.append(p)
            else:
                if q[t]:
                    gen_meander(p + [t+1], t+1)
                else:
                    gen_meander([t+1] + p, t+1)
                q[t] = 1 - q[t]

            if i == t:
                break

            j = 1 if t >= n and stamp else _next_semi_meander(p, t, q[t-1])
            p = rotation(p, j, 'l') if q[t-1] else rotation(p, j)

            i += j

    gen_meander([1], 1)

    return perms


def stamp_folding(n: int) -> list[list[int]]:
    return semi_meander(n, True)


def _next_semi_meander(p, t, d):
    j = p[0] if d else p[t-1]

    if j == 1 and not t%2:
        return 1
    elif j%2 == t%2:
        return p.index(j + 1) + 1 if d else t - p.index(j + 1)
    else:
        return p.index(j - 1) + 1 if d else t - p.index(j - 1)


