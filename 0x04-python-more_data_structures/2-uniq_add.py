#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_values = []
    total = 0

    for item in my_list:
        if item not in unique_values:
            unique_values.append(item)
            total += item

    return (total)
