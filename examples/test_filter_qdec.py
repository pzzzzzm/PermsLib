import sys
sys.path.append('.')
from algos.gen_lexi import gen_binary
from word_test import check_q_decreasing
from utils import *

n = 7
q = 1
plist = gen_binary(n)

qdecs = []
for p in plist:
    qdecs.append(p) if check_q_decreasing(p, q) else qdecs

print_plist(qdecs)
print("Total: {}".format(len(qdecs)))

