def solution(array):
    count={}
    for num in array:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
            
    lst=list(count.values())
    lst.sort()
    max_num=lst[-1]
    
    cnt=0
    idx=0
    for index, value in count.items():
        if value == max_num:
            idx=index
            cnt+=1
        else:
            continue
    
    if cnt>1:
        result=-1
    else:
        result=idx
    return result
            