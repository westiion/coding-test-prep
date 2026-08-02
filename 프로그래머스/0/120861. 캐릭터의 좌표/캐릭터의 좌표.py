def solution(keyinput, board):
    result=[0,0]
    dict={'left':-1, 'right':1, 'up':1, 'down':-1}
    limit_v=(board[0]-1)//2
    limit_h=(board[1]-1)//2
    
    for point in keyinput:
        if point in ['left','right']:
            result[0]+=dict[point]
            if abs(result[0]) > limit_v:
                result[0]-=dict[point]
        else:
            result[1]+=dict[point] 
            if abs(result[1]) > limit_h:
                result[1]-=dict[point]
    return result