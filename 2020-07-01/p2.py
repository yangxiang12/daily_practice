#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/1 18:32 
# @Author : 杨翔
# @File : p2.py 

"""
根据target进行左右排序
"""


def solution(nums, target):
    if target not in nums:
        return []

    stack = [target]
    mid = nums.index(target)

    length = len(nums)
    left, right = mid, mid
    for _ in range(length):
        left -= 1
        right += 1

        if left >= 0:
            stack.append(nums[left])

        if right < length:
            stack.append(nums[right])

    return stack


s = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
