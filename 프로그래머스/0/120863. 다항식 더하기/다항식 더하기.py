def solution(polynomial):
    result=[0,0]
    poly=polynomial.split(' + ')
    for term in poly:
        if 'x' in term:
            if term == 'x':
                result[0]+=1
            else:
                result[0]+=int(term[:-1])
        else:
            result[1]+=int(term)
            
    if result[0]:
        if result[0]==1:
            result[0]=''
            
        if result[1]:
            return f'{result[0]}x + {result[1]}'
        else:
            return f'{result[0]}x'
    else:
        if result[1]:
            return f'{result[1]}'
        else:
            pass
        
        
            
            