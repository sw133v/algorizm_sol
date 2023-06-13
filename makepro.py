import sys
sys.stdin = open('made_input.txt', 'r')
file = open('made_output.txt', 'w')

def sol():
    startMember_howManyTurn = list(map(int, input().split()))
    # 시작 멤버, 행해질 턴수 변수를 저장
    graph = list(map(int, input().split()))
    # 각 멤버들이 가리키는 멤버의 인덱스
    graph_len = len(graph)
    dgdg = [0 for _ in range(graph_len)]
    # 당근을 한 횟수를 저장하는 변수
    now_mem = startMember_howManyTurn[0]
    # 처음 시작하는 멤버 초기화

    for _ in range(startMember_howManyTurn[1]):
        now_mem = graph[(now_mem-1)]
        # 인덱스값 조정 및 멤버가 상대를 지목
        dgdg[(now_mem) % graph_len] += 1
        dgdg[(now_mem - 2) % graph_len] += 1
        # 지목받은 상대의 좌우가 당근당근을 함!

    max_data = max(dgdg)
    # 가장 많이 당근당근한 횟수를 구함
    res = [f'{member+1}' for member, dg_max in enumerate(dgdg) if dg_max == max_data]
    # 구해진 횟수를가지고 리스트를 순회하며 횟수가 동일하면 인덱스를 들고옴
    data = ' '.join(res)
    file_data = f'{data}\n'
    file.write(file_data)
    return data

T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')
