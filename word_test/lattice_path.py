from typing import Callable


def test_lattice_path(perm: list[int], flaw: int, step_map=None) -> bool:
    if not step_map:
        # step_map = {
        #     1: 1,
        #     0: -1
        # }
        step_map = lambda x: {
            1: 1,
            0: -1
        }[x]
    assert isinstance(step_map, Callable)
    h = 0
    fcnt = 0
    for p in perm:
        h += step_map(p)
        if h < 0:
            fcnt += 1

    return h == 0 and fcnt <= flaw


def test_dyck_path(perm: list[int], step_map=None) -> bool:
    return test_lattice_path(perm, 0, step_map)


def test_dyck_ap(perm: list[int], step_map=None) -> bool:
    if not step_map:
        step_map = lambda x: x
    return test_lattice_path(perm, 0, step_map)
