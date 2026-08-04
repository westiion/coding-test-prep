def solution(sides):
    sides.sort()
    total=0
    for x in range(1,sides[1]):
        if sides[0] + x > sides[1]:
            total= sides[1]-x
            break
    y=sides[1]+1
    while True:
        if sides[0] + sides[1] == y:
            total+= y-sides[1]
            break
        y+=1    
    return total