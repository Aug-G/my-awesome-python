#coding:utf-8
"""
    快速排序算法
    时间复杂度：O(n**2) 最大
    空间复杂度：O(n**2) 最大
"""


def sort(seq):

    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)