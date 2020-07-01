#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/1 16:40 
# @Author : 杨翔
# @File : p1.py
# 题目两数之和
"""
遍历查询，先生成一个空的dict(),然后将每次val和idx添加到字典中，然后等待下次查询，
[target - vla]存在在字典中，那么就取出他们的下标即可
"""


# 解题1
def two_nums(nums, target):
    dic = {}
    for idx, val in enumerate(nums):
        if dic.get(target - val):
            return [idx, dic[target - val]]
        dic[val] = idx


# 解题2


def add(nums, target):
    if len(nums) < 2:
        return []

    # 首先排序一哈子
    nums1 = sorted(nums)
    first, last = 0, len(nums1) - 1
    while first < last:
        if nums1[first] + nums1[last] == target:
            break
        elif nums1[first] + nums1[last] > target:
            last -= 1
        elif nums1[first] + nums1[last] < target:
            first += 1
        else:
            return []
    return [nums.index(nums1[first]), nums.index(nums1[last])]
