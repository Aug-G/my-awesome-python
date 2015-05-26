#coding:utf-8
"""
    冒泡排序
    时间复杂度：O(n ** 2)
    空间复杂度：O(1)
"""

def sort(seq):
    L = len(seq)
    for _ in range(L):
        for n in range(1, L):
            if seq[n] < seq[n - 1]:
                seq[n - 1], seq[n] = seq[n], seq[n - 1]
    return seq