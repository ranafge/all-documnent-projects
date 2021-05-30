import os
import random
import re
import sys
from itertools import groupby
from collections import Counter

# socks = input().strip().split()
# # print(socks)
# # p = 0
# # for e in set(socks):
# #     p += socks.count(e) // 2
# # print(p)
# socks = Counter(map(int, input().strip().split()))
# for e in socks:
#     print(e,socks[e]//2 )

# lst = [1, 2, 3, 3, 6, 8, 8, 10, 2, 5, 7, 7]
# result = []
#
# for k, g in groupby(lst):
#     group = list(g)
#     if k > 6 and len(group)>1:
#         result.append(group)
#     else:
#         result.extend(group)
# print(result)
#
# a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
#
# for k, v in groupby(a):
#     print(k, list(v))
#     print((len(list(v)), k), end=' ')
#
# print([(v,k) for k, v in Counter(a).items()])
# print(Counter(a).items())
# print(Counter(a).values())

# things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"], \
#           ["vehicle", "speed boat"], ["vehicle", "school bus"]]
# dic ={}
n = 9
ls = list(map(int, input().strip().split()))[:n]
f = lambda x: x
ans = 0
for x in [len(list(g)) for k, g in groupby(sorted(ls, key=f), f)]:
    ans += x // 2
print(ans)

height = 0
prev_height = 0
cnt = 0
n = input()
s = input().strip()
for i in range(len(s)):
    if (s[i] == 'U'):
        height += 1
    elif s[i] == 'D':
        height -= 1
    if height == 0 and prev_height < 0:
        cnt += 1
    prev_height = height
print(cnt)
