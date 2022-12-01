from perm import Perm


def perms_to_dict(perms, default_value=1):
    d = {}
    for p in perms:
        d[str(p)] = default_value
    return d


def check_dict_by_perm(d, perm):
    if d[str(perm)] < 1:
        return False
    else:
        d[str(perm)] -= 1
        return True


def check_dict_exhaustive(d, check_value=0):
    for k in d:
        if d[k] != check_value:
            return False
    return True


def check_dict_by_list(d, perms):
    for p in perms:
        if not check_dict_by_perm(d, p):
            return False
    if not check_dict_exhaustive(d):
        return False
    return True


def create_n_perm(n):
    return Perm([i+1 for i in range(n)])
