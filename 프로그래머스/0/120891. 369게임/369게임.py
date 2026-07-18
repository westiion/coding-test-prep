def solution(order):
    lst=[x for x in str(order) if x in '369']
    return len(lst)