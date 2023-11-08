

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
