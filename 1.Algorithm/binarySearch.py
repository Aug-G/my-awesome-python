#coding:utf-8
#二分查找算法
def binarySearch(l, t):
    low, high = 0, len(l) - 1
    while low < high:
        print low, high
        mid = (low + high) / 2

        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid

    return False

if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print binarySearch(l, 12)
    print binarySearch(l, 1)
    print binarySearch(l, 13)
