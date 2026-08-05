def solution(polynomial):
    x_sum = 0
    num_sum = 0

    for term in polynomial.split(' + '):
        if 'x' in term:
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term[:-1])
        else:
            num_sum += int(term)

    answer = []

    if x_sum > 0:
        if x_sum == 1:
            answer.append('x')
        else:
            answer.append(str(x_sum) + 'x')

    if num_sum > 0:
        answer.append(str(num_sum))

    return ' + '.join(answer)