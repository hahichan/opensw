##################

  #프로그램명: 성적관리프로그램 v3

  #작성자: 소프트웨어학부 / 2022041041

  #작성일:2025-04-09

  #프로그램 설명: 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램

  ###################
class student():
    
    # 학생들의 학번, 이름, 점수, 총점, 평균, 학점, 등수의 값을 담을 배열 생성
    def __init__(self):
        self.num = []
        self.name = []  
        self.eng = []
        self.c = []
        self.py= []
        self.total= []
        self.ave= []
        self.score=[]
        self.rank= []
        self.n = 0
        self.good = 0

    # 메뉴 출력 함수
    def menu(self): 
        while(True):
            a = 0
            print("1. 학생 추가")
            print("2. 학생 삭제")
            print("3. 학생 검색")
            print("4. 전체 출력")
            print("5. 종료\n")
            a= int(input("입력 : "))
            print("")
            if a == 1:
                self.entry()
            elif a == 2:
                self.delete()
            elif a == 3:
                self.search()
            elif a==4:
                self.out()
            elif a==5:
                input("프로그램이 종료되었습니다.")
                exit()
        
    # 학번, 이름, 점수 입력 함수   
    def entry(self):
        stu_id=input("학번 : ")
        #학번 중복 입력 방지
        if stu_id in self.num:
            print("해당 학번은 이미 존재합니다.")
            return 0
        self.num.append(stu_id)
        self.name.append(input("이름 : "))
        self.eng.append(int(input("영어 : ")))
        self.c.append(int(input("C-언어 : ")))
        self.py.append(int(input("파이썬 : ")))

        #점수의 범위를 벗어난 값 입력시 프로그램 종료
        if(self.eng[-1] > 100 or self.eng[-1] < 0 or self.c[-1] > 100 or self.c[-1] < 0 or self.py[-1] > 100 or self.py[-1] < 0 ):
            print("점수에 오류가 있습니다. ")
            del self.num[-1]
            del self.name[-1]  
            del self.eng[-1]
            del self.c[-1] 
            del self.py[-1]
            return 0

        self.cal()
        self.Score()
        self.count()
        self.n += 1
        print("")
        
    # 총점 및 평균 구하기 함수
    def cal(self):
        self.total.append(self.eng[-1]+self.c[-1]+self.py[-1])
        self.ave.append(self.total[-1]//3) 

    # 학점 계산 함수
    def Score(self):    
        if self.ave[-1] >= 95:
            self.score.append("A+")
        elif self.ave[-1] >= 90:
            self.score.append("A")
        elif self.ave[-1] >= 85:
            self.score.append("B+")
        elif self.ave[-1] >= 80:
            self.score.append("B")
        elif self.ave[-1] >= 75:
            self.score.append("C+")
        elif self.ave[-1] >= 70:
            self.score.append("C")
        elif self.ave[-1] >= 65:
            self.score.append("D+")
        elif self.ave[-1] >= 60:
            self.score.append("D")
        else:
            self.score.append("F")
    
    # 학생 데이터 제거 함수
    def delete(self):
        stu_id=input("삭제할 학생의 학번을 입력하시오 : ")

        if stu_id in self.num:
            d=self.num.index(stu_id)
            if (int(self.ave[d]) >=80):
                self.good -=1
            del self.num[d]
            del self.name[d]  
            del self.eng[d]
            del self.c[d] 
            del self.py[d]
            del self.total[d]
            del self.ave[d]
            del self.score[d]
            self.n -= 1
            print(f"{stu_id}번 삭제되었습니다.\n")
        
        else:
            print(f"{stu_id}번 학생이 존재하지 않습니다.\n")
    
    # 학생 검색 함수
    def search(self):
        stu_id= input("검색하려는 학생의 학번을 입력하시오 : ")
        stu_name = input("검색하려는 학생의 이름을 입력하시오 : ")
        if (stu_id in self.num) and (stu_name in self.name):
            i=self.num.index(stu_id)
            self.ranking()
            print("=============================================================================")
            print("학번          이름       영어   C-언어   파이썬   총점   평균   학점   등수")
            print("=============================================================================")
            print(f"{self.num[i]:<15}{self.name[i]:<10}{self.eng[i]:<8}{self.c[i]:<8}{self.py[i]:<8}{self.total[i]:<7}{self.ave[i]:<7}{self.score[i]:<7}{self.rank[i]:<6}")
            print("")
        else:
            print("해당하는 학생이 없습니다.\n")
            return 0
        
    # 학생들의 총점, 평균, 학점, 등수 출력
    def out(self):
        if self.n == 0:  # 학생 데이터가 없으면 출력하지 않음
            print("학생 데이터가 없습니다.\n")
            return
        
        self.sort()
        self.ranking()
        print("                                성적관리 프로그램 ")
        print("=============================================================================")
        print("학번            이름       영어   C-언어   파이썬   총점   평균   학점   등수")
        print("=============================================================================")
        for i in range(self.n):
            print(f"{self.num[i]:<15}{self.name[i]:<12}{self.eng[i]:<8}{self.c[i]:<8}{self.py[i]:<8}{self.total[i]:<7}{self.ave[i]:<7}{self.score[i]:<7}{self.rank[i]:<6}")
        print(f"80점 이상 학생 수 : {self.good}\n")


    # 등수 구하기 함수
    def ranking(self):
        sorted_scores = sorted(self.total, reverse=True)  
        self.rank = [sorted_scores.index(score) + 1 for score in self.total] 

    # 정렬 함수
    def sort(self):
        # 총점을 중심으로 정렬
        sorted_data = sorted(zip(self.num, self.name, self.eng, self.c, self.py, self.total, self.ave, self.score), key=lambda x: x[5], reverse=True)
        # 정렬된 데이터를 다시 분리
        self.num, self.name, self.eng, self.c, self.py, self.total, self.ave, self.score = map(list, zip(*sorted_data))

    # 80점 이상 학생 카운트 함수
    def count(self):
        if(int(self.ave[-1]) >=80):
            self.good +=1


def main():

    stu = student()
    stu.menu()
    return 0


main()
