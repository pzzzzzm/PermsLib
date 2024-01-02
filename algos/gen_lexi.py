from math import ceil


def _gen_perms_recur(n, length, vd, cnt, limit, prev, perms):
    # if 0 < limit <= cnt:
    #     return cnt
    if len(prev) == length:
        perms.append(prev.copy())
        cnt += 1
        return cnt
    for i in vd.keys():
        if vd[i] > 0:
            prev.append(i)
            vd[i] -= 1
            cnt = _gen_perms_recur(n, length, vd, cnt, limit, prev, perms)
            if 0 < limit <= cnt:
                return cnt
            prev.pop()
            vd[i] += 1
    return cnt


def gen_perms(n: int, limit=-1, multiset_dict=None) -> list[list[int]]:
    perms = []
    first_perm = []
    cnt = 0
    length = n
    volume_dict = {}
    for i in range(1, n+1):
        volume_dict[i] = 1
    if multiset_dict is not None:
        for k in multiset_dict:
            volume_dict[k] = multiset_dict[k]
            length += multiset_dict[k] - 1

    _gen_perms_recur(n, length, volume_dict, cnt, limit, first_perm, perms)
    return perms


def gen_binary(n: int, limit=-1) -> list[list[int]]:
    perms = []
    first_perm = []
    cnt = 0
    length = n
    volume_dict = {0: n, 1: n}
    _gen_perms_recur(n, length, volume_dict, cnt, limit, first_perm, perms)
    return perms


# def _gen_all_perms_recur(n, l, limit=-1):
#     if l <= 1:
#         return [[i] for i in range(1, n+1)]
#     sub_perms = _gen_all_perms_recur(n, l-1, limit)
#     perms = []
#     for i in range(1, n+1):
#         for sp in sub_perms:
#             if not (0 < limit <= len(perms)):
#                 perms.append([i]+sp)
#     return perms
#
#
# def gen_all_perms(n: int, limit=-1) -> list[list[int]]:
#     return _gen_all_perms_recur(n, n, limit)


def _gen_integer_partition_lexi(n, l, prev_max, limit=-1):
    if l == 1:
        return [[n]]
    perms = []
    for i in range(ceil(n/l), min(prev_max+1, n-l+2)):
        sub_perms = _gen_integer_partition_lexi(n-i, l-1, i, limit)
        for sp in sub_perms:
            if not (0 < limit <= len(perms)):
                perms.append([i]+sp)
            else:
                return perms
    return perms


def gen_integer_partition_lexi(n: int, l: int, limit=-1) -> list[list[int]]:
    return _gen_integer_partition_lexi(n, l, n, limit)

