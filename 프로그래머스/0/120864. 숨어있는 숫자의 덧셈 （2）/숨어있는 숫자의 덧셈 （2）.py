def solution(my_string):
    temp=''
    num=[]
    for ch in my_string:
        if ch.isdigit():
            temp+=ch
        else:
            if temp:
                num.append(int(temp))
                temp=''
    if temp:
        num.append(int(temp))
        
    if num:
        return sum(num)
    
    else:
        return 0

                