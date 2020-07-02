#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/2 16:25 
# @Author : 杨翔
# @File : p1.py


def length_Longest_substring(s):
    k, res, c_dict = -1, 0, {}
    for i, c in enumerate(s):
        if c in c_dict and c_dict[c] > k:
            k = c_dict[c]
            c_dict[c] = i
        else:
            c_dict[c] = i
            res = max(res, i - k)
    return res


a = length_Longest_substring("qwertttqiolq")

