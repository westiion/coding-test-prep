def solution(num_list):
    result=[0,0]
    for num in num_list:
        result[num%2]+=1
    return result
        