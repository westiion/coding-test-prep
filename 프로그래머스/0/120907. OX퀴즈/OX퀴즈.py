def solution(quiz):
    answer=[]
    for eq in quiz:
        eq=eq.split()
        if eq[1] == '-':
            eq[2] = -int(eq[2])
        if int(eq[0])+int(eq[2]) == int(eq[4]):
            answer.append('O')
        else:
            answer.append('X')
    return answer