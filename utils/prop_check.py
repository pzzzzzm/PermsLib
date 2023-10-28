
DEFAULT_SPLITER = '.'


def _perm_to_str(p, spliter=DEFAULT_SPLITER):
    s_out = ''
    for e in p:
        s_out += str(e) + spliter
    return s_out


def plist_to_dict(plist, default_value=1, spliter=DEFAULT_SPLITER):
    d = {}
    for p in plist:
        d[_perm_to_str(p, spliter)] = default_value
    return d


def check_dict_by_perm(d, perm, spliter=DEFAULT_SPLITER):
    if d[_perm_to_str(perm, spliter)] < 1:
        return False
    else:
        d[_perm_to_str(perm, spliter)] -= 1
        return True


def check_dict_exhaustive(d, check_value=0):
    for k in d.keys():
        if d[k] != check_value:
            return False
    return True


def check_dict_by_plist(d, plist, spliter=DEFAULT_SPLITER):
    if len(d) != len(plist):
        return False
    for p in plist:
        if not check_dict_by_perm(d, p, spliter):
            return False
    if not check_dict_exhaustive(d):
        return False
    return True


def diff(p1, p2):
    assert len(p1) == len(p2)
    d = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            d += 1
    return d


def get_max_diff(plist):
    max_diff = 0
    prev = plist[0]
    for curr in plist:
        max_diff = max(max_diff, diff(prev, curr))
    return max_diff


def filter_plist(plist, f, *args):
    res = []
    for p in plist:
        if f(p, *args):
            res.append(p)
    return res
