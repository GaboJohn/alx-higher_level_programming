#!/usr/bin/python3
def best_score(my_dic):
    return max(my_dic, key=my_dic.get) if my_dic else None
