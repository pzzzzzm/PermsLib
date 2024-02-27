from typing import Callable


def print_p(p: list, splitter='', ge10_check=False) -> str:
    p_str = ''
    for i in range(len(p)):

        p_str += '(' + str(p[i]) + ')' if ge10_check and type(p[i]) is int and p[i] >= 10 else str(p[i])
        # p_str += str(p[i])
        if i != len(p) - 1:
            p_str += splitter
    print(p_str)
    return p_str


def print_plist(plist: list[list], splitter='', ge10_check=False):
    for p in plist:
        print_p(p, splitter, ge10_check)


def modify_elements_in_plist(plist: list[list], f: Callable, *args):
    for i in range(len(plist)):
        for j in range(len(plist[i])):
            plist[i][j] = f(plist[i][j], *args)

