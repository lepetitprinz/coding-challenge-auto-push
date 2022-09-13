from itertools import combinations
from collections import Counter

def make_total_order(orders, c):
    total_order = []
    for order in orders:
        order_sorted = [tuple(sorted(o)) for o in list(combinations(order, c))]
        total_order.extend(order_sorted)
        
    return total_order

def count_order(total_order):
    return dict(Counter(total_order))

def filter_order_count(cnt_order):
    new_count_order = {}
    for key, val in cnt_order.items():
        if val != 1:
            new_count_order[key] = val
    
    return new_count_order

def get_max_key(count_order):
    max_val = count_order[max(count_order, key=count_order.get)]
    max_key_list = []
    for key, val in count_order.items():
        if val == max_val:
            max_key_list.append(''.join(key))
    
    return max_key_list

def solution(order, course):
    result = []
    for c in course:
        total_order = make_total_order(order, c)
        if len(total_order) > 0:
            cnt_order = count_order(total_order)
            cnt_order = filter_order_count(cnt_order)
            if len(cnt_order) > 0:
                result.extend(get_max_key(cnt_order))
    
    return sorted(result)