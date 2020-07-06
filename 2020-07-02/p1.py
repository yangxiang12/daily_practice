#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/2 16:25 
# @Author : 杨翔
# @File : p1.py

def solution(s):
    """
    K: 更新重复字符的下标
    res: 保留最大无重复字符长度
    dic: 保留不存在的字符，并且更新重复的字符下标
    :param s:
    :return:
    """
    k, res, dic = -1, 0, dict()
    for idx, val in enumerate(s):
        if val in dic and dic[val] > k:
            k = dic[val]
            dic[val] = idx
        else:
            dic[val] = idx
            res = max(res, idx - k)
    return res


def s(s):
    resp = []
    for index in range(len(s)):
        result = []
        for letter in s[index:]:
            if letter not in result:
                result.append(letter)
            else:
                resp.append(result)
            break
    return max([len(item) for item in resp])


print(s("asdafg"))
