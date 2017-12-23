# coding=utf-8

from collections import Counter

c = Counter()
for ch in ['589', '589', '611', '711']:
    c[ch] += 1

if __name__ == '__main__':
    # 列表出现次数最多的元素求法
    print c
    c = dict(c)
    count = max(c.values())
    count_index = c.values().index(count)
    print c.keys()[count_index]