def solution(num_list):
    result=[]
    for num in num_list:
        if num < 0:
            result.append(num_list.index(num))
        else:
            pass
    if result:
        return result[0]
    else:
        return -1