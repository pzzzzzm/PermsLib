from typing import Callable
import copy

DEFAULT_SPLITER = '.'


def perm_to_str(p, spliter=DEFAULT_SPLITER):
    s_out = ''
    for e in p:
        s_out += str(e) + spliter
    return s_out


def plist_to_dict(plist: list[list], default_value=1, spliter=DEFAULT_SPLITER) -> dict:
    d = {}
    for p in plist:
        d[perm_to_str(p, spliter)] = copy.copy(default_value)
    return d


def check_dict_by_perm(d: dict, perm: list, spliter=DEFAULT_SPLITER) -> bool:
    if d[perm_to_str(perm, spliter)] < 1:
        return False
    else:
        d[perm_to_str(perm, spliter)] -= 1
        return True


def check_dict_exhaustive(d: dict, check_value=0) -> bool:
    for k in d.keys():
        if d[k] != check_value:
            return False
    return True


def check_dict_by_plist(d: dict, plist: list[list], spliter=DEFAULT_SPLITER) -> bool:
    if len(d) != len(plist):
        return False
    for p in plist:
        if not check_dict_by_perm(d, p, spliter):
            return False
    if not check_dict_exhaustive(d):
        return False
    return True


def diff(p1: list, p2: list, bit_diff=False) -> int:
    assert len(p1) == len(p2)
    d = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            if bit_diff:
                d += abs(p1[i] - p2[i])
            else:
                d += 1
    return d


def get_max_diff(plist: list, bit_diff=False, cyclic=False) -> int:
    max_diff = 0
    prev = plist[0]
    for curr in plist:
        max_diff = max(max_diff, diff(prev, curr, bit_diff))
        prev = curr

    if cyclic:
        max_diff = max(max_diff, diff(plist[0], plist[-1], bit_diff))

    return max_diff


def filter_plist(plist: list[list], f: Callable[..., bool], *args) -> list[list]:
    res = []
    for p in plist:
        if f(p, *args):
            res.append(p)
    return res
