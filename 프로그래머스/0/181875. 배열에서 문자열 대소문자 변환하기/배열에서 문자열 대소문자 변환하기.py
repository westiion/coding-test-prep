def solution(strArr):
    for i,string in enumerate(strArr):
        if i%2==1:
            strArr[i]=''.join([x.upper() for x in string])
        else:
            strArr[i]=''.join([x.lower() for x in string])
    return strArr