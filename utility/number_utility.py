# -*- coding: utf-8 -*-
"""
数字工具类
"""
import random

__author__ = 'l'
__date__ = '2018/5/11'


def get_random_number_list_from_range(num_size, num_range):
    """
    从指定范围内随机获取num_size个数的数据
    :param num_size:
    :param num_range:eg(100,1000)  100<=x<1000
    :return:
    """
    min_range = num_range[0]
    max_range = num_range[1]
    random_list = []
    for i in range(num_size):
        random_list.append(random.randint(min_range, max_range))
    return random_list
