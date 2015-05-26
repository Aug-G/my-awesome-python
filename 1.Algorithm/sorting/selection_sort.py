#coding:utf-8
"""
 选择排序
 时间复杂度：O(n**2)
 空间复杂度：O(1)
"""

def sort(seq):

    for i in range(0, len(seq)):
        iMin = i
        for j in range(i+1, len(seq)):
            if seq[iMin] > seq[j]:
                iMin = j
        if i != iMin:
            seq[i], seq[iMin] = seq[iMin], seq[i]

    return seq