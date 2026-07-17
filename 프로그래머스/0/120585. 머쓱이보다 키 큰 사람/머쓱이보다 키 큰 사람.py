def solution(array, height):
    array.sort(reverse=True)
    cnt=0
    for num in array:
        if height<num:
            cnt+=1
        else:
            break
    return cnt
            