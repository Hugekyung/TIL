"""네이버 부스트캠프 연습문제"""
arr = [1,2,3,3,3,3,4,4]
arr2 = [3,2,4,4,2,5,2,5,5]
arr3 = [3,5,7,9,1,1]

def solution(arr):
    result = []
    _set_arr = set(arr)
    for a in _set_arr:
        cnt = arr.count(a)
        if cnt > 1:
            result.append(cnt)
    
    if not result:
        return [-1]
    
    return result

print(solution(arr3))