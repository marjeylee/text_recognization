# -*- coding: utf-8 -*-
"""
文字处理相关模块,统一以utf8模式进行编码
"""
import re


def is_chinese_character(ch):
    """
    判断该字符是否是汉字,可以使字或者字符串
    :param ch:
    :return:
    """
    pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = pattern.search(ch)
    if match:
        return True
    else:
        return False


def remove_bracket(s):
    """
    移除括号
    :param s:
    :return:
    """
    re_str = '（[\s\S\w\W]*?）'
    pattern = re.compile(re_str)
    match_obj = pattern.findall(s)
    for m in match_obj:
        s = s.replace(m, '')
    return s
