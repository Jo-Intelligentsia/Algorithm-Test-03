# 1983 조교의 성적 매기기
# 학기가 끝나고, 학생들의 점수로 학점을 계산중이다.
# 학점은 상대평가로 주어지는데, 총 10개의 평점이 있다.
# 학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수가 반영한다.
# 각각 아래 비율로 반영된다.
# 10 개의 평점을 총점이 높은 순서대로 부여하는데, 각각의 평점은 같은 비율로 부여할 수 있다.
# 예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고, 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
# K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
# [제약사항]
# 1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
# 2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
# 3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.
# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
# 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.
# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input()) # 테스트 케이스
for t in range(1,T+1):
    N,M = list(map(int,input().split()))
    dic1 = {}
    dic2 = {} # 순위별로 번호 입력받음
    ls = []

    for i in range(1,N+1):
        a,b,c = list(map(int,input().split()))
        total = a*0.35 + b*0.45 + c*0.2
        dic1[i] = total
    for j in range(1,N+1):
        dic2[j] = (max(dic1, key=dic1.get))
        dic1.pop(max(dic1, key=dic1.get))
    print(dic1)
    print(dic2)
    p = N/10 # 성적당 인원 수
    dic2 = dic2.values()
    for i in dic2:
        ls.append(i)
    # print(dic2)
    # print(ls)
    cnt = 0
    for i in ls:
        cnt += 1
        if i == M:
            break
    print(cnt)
    if cnt <= N/10:
        print(f'#{t} A+')
    elif cnt <= N/10 *2:
        print(f'#{t} A0')
    elif cnt <= N/10 *3:
        print(f'#{t} A-')
    elif cnt <= N/10 *4:
        print(f'#{t} B+')
    elif cnt <= N/10 *5:
        print(f'#{t} B0')
    elif cnt <= N/10 *6:
        print(f'#{t} B-')
    elif cnt <= N/10 *7:
        print(f'#{t} C+')
    elif cnt <= N/10 *8:
        print(f'#{t} C0')
    elif cnt <= N/10 *9:
        print(f'#{t} C-')
    else:
        print(f'#{t} D')
