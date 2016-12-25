#!/usr/bin/env python
# -*- coding: utf-8 -*-

def stdQuicksort(L):
    qsort(L, 0, len(L) - 1)

def qsort(L, first, last):
    if first < last:
        split = partition(L, first, last)
        qsort(L, first, split - 1)
        qsort(L, split + 1, last)

def partition(L, first, last):
    # 选取列表中的第一个元素作为划分元素
    pivot = L[first]

    leftmark = first + 1
    rightmark = last

    while True:
        while L[leftmark] <= pivot: # 如果列表中存在与划分元素pivot相等的元素，让它位于left部分
            # 以下检测用于划分元素pivot是列表中的最大元素时，防止leftmark越界
            if leftmark == rightmark:
                break
            leftmark += 1

        while L[rightmark] > pivot:
            # 这里不需要检测，划分元素pivot是列表中的最小元素时，rightmark会自动停在first处
            rightmark -= 1

        if leftmark < rightmark:
            # 此时，leftmark处的元素大于pivot，而rightmark处的元素小于等于pivot，交换二者
            L[leftmark], L[rightmark] = L[rightmark], L[leftmark]
        else:
            break

    # 交换first处的划分元素与rightmark处的元素
    L[first], L[rightmark] = L[rightmark], L[first]

    # 返回划分元素pivot的最终位置
    return rightmark

def pycQuicksort(L):
    if len(L) <= 1: return L
    return pycQuicksort([x for x in L if x < L[0]]) + \
           [x for x in L if x == L[0]] + \
           pycQuicksort([x for x in L if x > L[0]])
