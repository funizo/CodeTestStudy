def solution(n):
    arr = [[0] * n for _ in range(n)]  # n x n 크기의 0으로 초기화된 이차원 배열 생성
    
    for i in range(n):
        arr[i][i] = 1  # 대각선 상에 있는 원소들을 1로 설정
    
    return arr