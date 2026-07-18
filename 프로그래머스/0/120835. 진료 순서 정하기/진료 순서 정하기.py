def solution(emergency):
    dict={}
    for i, num in enumerate(sorted(emergency,reverse=True)):
        dict[num]=i+1
    result=[]
    for i in emergency:
        result.append(dict[i])
    return result
