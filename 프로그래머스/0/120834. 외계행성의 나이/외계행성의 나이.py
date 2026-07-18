def solution(age):
    dict={}
    for i, chr in enumerate('abcdefghij'):
        dict[i]=chr
        
    result=''
    for num in str(age):
        result+=dict[int(num)]
        
    return result
        