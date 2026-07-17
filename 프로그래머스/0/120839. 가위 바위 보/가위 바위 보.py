def solution(rsp):
    win_rule={'2':'0', '0':'5', '5':'2'}
    win=''
    for hand in str(rsp):
        win+=win_rule[hand]
    return win