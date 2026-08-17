def solution(num_list):
    if len(num_list)>=11:
        return sum(num_list)
    else:
        i=1
        for n in num_list:
            i*=n
        return i