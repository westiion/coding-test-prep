def solution(spell, dic):
    spell=sorted(''.join(spell))
    answer=2
    for word in dic:
        if spell == sorted(word):
            answer = 1
    return answer