import sys
sys.path.append('.')
from algos.gen_lexi import gen_binary
from word_test import check_q_decreasing
from utils import *

n = 7
q = 1

# generate all binary permutation
plist = gen_binary(n)

# filter out the permutations which are not q-deceasing words
qdecs = filter_plist(plist, check_q_decreasing, q)

print_plist(qdecs)
print("Total: {}".format(len(qdecs)))

