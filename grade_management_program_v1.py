#5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여  키보드로부터 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성

## 성적관리 프로그램

#학생의 수의 값을 넣는 상수
N=5

#학점 구하기 함수
def score(n):
    if n>=90 and n<=100:
        return "A"
    elif n>=80 and n<90:
        return "B"
    elif n>=70 and n<60:
        return "C"
    elif n>=60 and n<50:
        return "D"
    else:
        return "F"
    
#등수 구하기 함수
def ranking(arr, s):
    a=1
    for i in range(N):
        if s <arr[i]:
            a+=1
    return a    


    
#메인 함수
def main():

    # 학생들의 점수, 총점, 평균, 학점, 등수의 값을 담을 배열 생성
    eng = [0]*N
    C = [0]*N
    py= [0]*N
    total= [0]*N
    ave= [0]*N
    eng_score= [0]*N
    C_score= [0]*N
    py_score= [0]*N
    rank= [0]*N

    # 학생들의 점수 입력
    print("성적을 입력하십시오. \n")
    for i in range(N):
        print(i+1, "번째 학생의 점수")
        eng[i] = int(input("영어 : "))
        C[i] = int(input("C-언어 : "))
        py[i]= int(input("파이썬 : "))
        
        #점수의 범위를 벗어난 값 입력시 프로그램 종료
        if(eng[i]>100 or eng[i]< 0 or C[i]>100 or C[i]< 0 or py[i]>100 or py[i]< 0  ):
            print("점수에 오류가 있습니다. 프로그램을 종료합니다.")
            input("엔터를 눌러 종료하세요...")
            exit()

        print("")

    # 학생들의 점수 총점 및 평균  구하기

    for i in range(N):
        total[i] = eng[i]+C[i]+py[i]
        ave [i] = format(total[i]/3,".2f") #평균 소숫점 2자리 까지


    #학점 구하기 함수를 사용해 각 과목별 등급 구하기
    for i in range(N):
        eng_score[i] = score(eng[i])
        C_score[i] = score(C[i])
        py_score[i] = score(py[i])
    
    #등수 구하기 함수를 사용해 등수 구하기
    for i in range(N):
        rank[i]= ranking(total, total[i])



    #학생들의 총점, 평균, 학점, 등수 출력
    print("학생 번호    총점    평균    영어  C-언어  파이썬  등수")
    for i in range(N):
        print("    ",i+1,"번   ", total[i],"   ",ave[i], "  ", eng_score[i],"    ",C_score[i],"    ",py_score[i], "    ", rank[i])

    #프로그램 자동 종료 방지 
    print("프로그램이 끝났습니다.")
    input("엔터를 눌러 종료하세요...")


#프로그램 실행
main()
