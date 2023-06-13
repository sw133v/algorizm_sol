import random
file = open('madeinput.txt', 'w')
how_many = 10
file.write(f'{how_many}\n')

for _ in range(how_many):
    people = random.randrange(4, 11)
    start_mem = random.randrange(1, people+1)
    turn = random.randrange(1, 51)
    direction = [0 for _ in range(people)]
    # 인원, 시작멤버, 행해질 횟수를 랜덤으로 뽑고
    # 각 멤버들의 방향을 저장할 변수를 초기화

    for i in range(people):
        # 해당 인원에 맞게 
        direct = random.randrange(1, people + 1)
        # 조정된 인덱스 값으로 방향을 랜덤으로 뽑고
        while i+1 == direct:
            direct = random.randrange(1, people + 1)
        # 랜덤으로 뽑힌 값이 자기 자신을 가리키지 않는다면
        direction[i] = f'{direct}'
        # 멤버들의 방향을 저장     

    data = f'{start_mem} {turn}\n'
    file.write(data)
    data = ' '.join(direction)
    data = f'{data}\n'
    file.write(data)
