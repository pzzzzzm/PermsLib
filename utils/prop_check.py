def _perm_to_str(p, spliter='.'):
    s_out = ''
    for e in p:
        s_out += str(e) + spliter
    return s_out


def plist_to_dict(plist, default_value=1, spliter='.'):
    d = {}
    for p in plist:
        d[_perm_to_str(p, spliter)] = default_value
    return d


def _check_dict_by_perm(d, perm, spliter='.'):
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


def check_dict_by_plist(d, plist, spliter='.'):
    if len(d) != len(plist):
        return False
    for p in plist:
        if not _check_dict_by_perm(d, p, spliter):
            return False
    if not check_dict_exhaustive(d):
        return False
    return True


def _cal_diff(p1, p2):
    assert len(p1) == len(p2)
    diff = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            diff += 1
    return diff


def get_max_diff(plist):
    max_diff = 0
    prev = plist[0]
    for curr in plist:
        max_diff = max(max_diff, _cal_diff(prev, curr))
    return max_diff


def filter_plist(plist, f, *args):
    res = []
    for p in plist:
        if f(p, *args):
            res.append(p)
    return res
