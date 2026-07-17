def solution(hp):
    total=0
    total+=hp//5
    total+=(hp%5)//3
    total+=(hp%5%3)//1
    return total