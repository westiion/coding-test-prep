def solution(array, n):
    array.append(n)
    array.sort()
    idx=array.index(n)
    if idx==0:
        return array[idx+1]
    elif idx==len(array)-1:
        return array[idx-1]
    else:
        gap1=array[idx]-array[idx-1]
        gap2=array[idx+1]-array[idx]
        if gap1==gap2:
            return array[idx-1]
        else:
            if gap1<gap2:
                return array[idx-1]
            else:
                return array[idx+1]
    