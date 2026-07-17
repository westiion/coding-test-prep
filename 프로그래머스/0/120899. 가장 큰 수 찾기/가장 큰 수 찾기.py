def solution(array):
    max=sorted(array)[-1]
    idx=array.index(max)
    return [max,idx]