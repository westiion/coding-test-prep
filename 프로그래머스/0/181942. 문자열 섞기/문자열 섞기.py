def solution(str1, str2):
    i=0
    result=''
    while i<len(str1):
        result+=str1[i]+str2[i]
        i+=1
    return result
    