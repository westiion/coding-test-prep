def solution(todo_list, finished):
    return [work for work in todo_list if not finished[todo_list.index(work)] ]
