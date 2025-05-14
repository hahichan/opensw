##################

  #프로그램명: 성적관리프로그램 v4

  #작성자: 소프트웨어학부 / 2022041041

  #작성일:2025-05-14

  #프로그램 설명: 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램

  ###################


import pymysql


class StudentDB:
    #데이터베이스
    def __init__(self):
        # 1. 먼저 DB 서버에 접속 (데이터베이스 지정 안함)
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='00000000',
            charset='utf8',
            autocommit=True  # DB 생성 후 바로 사용
        )
        self.cur = self.conn.cursor()
        
        # 2. 데이터베이스 생성 (없을 경우만)
        self.cur.execute("CREATE DATABASE IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8")
        
        # 3. 생성된 DB로 다시 연결
        self.conn.select_db('mydb')
        
        # 4. students 테이블 생성 (없을 경우만)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id VARCHAR(20) PRIMARY KEY,
                name VARCHAR(20) NOT NULL,
                eng INT CHECK (eng BETWEEN 0 AND 100),
                c INT CHECK (c BETWEEN 0 AND 100),
                py INT CHECK (py BETWEEN 0 AND 100),
                total INT,
                average FLOAT,
                grade VARCHAR(3)
            )
        """)

    #DB 종료 함수
    def close(self):
        self.cur.close()
        self.conn.close()
    
    #메뉴 출력 함수
    def menu(self):
        while True:
            print("\n1. 학생 추가\n2. 학생 삭제\n3. 학생 검색\n4. 전체 출력\n5. 종료\n")
            choice = input("입력 : ")
            if choice == '1':
                self.entry()
            elif choice == '2':
                self.delete()
            elif choice == '3':
                self.search()
            elif choice == '4':
                self.out()
            elif choice == '5':
                print("프로그램이 종료되었습니다.")
                self.close()
                break

    #입력 함수
    def entry(self):
        stu_id = input("학번 : ")
        self.cur.execute("SELECT id FROM students WHERE id=%s", (stu_id,))
        if self.cur.fetchone():
            print("해당 학번은 이미 존재합니다.")
            return
        name = input("이름 : ")
        eng = int(input("영어 : "))
        c = int(input("C-언어 : "))
        py = int(input("파이썬 : "))

        #점수의 범위를 벗어난 값 입력시 프로그램 종료
        if not all(0 <= s <= 100 for s in (eng, c, py)):
            print("점수에 오류가 있습니다.")
            return

        total = eng + c + py
        avg = total / 3
        grade = self.calculate_grade(avg)

        self.cur.execute("""
            INSERT INTO students (id, name, eng, c, py, total, average, grade)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (stu_id, name, eng, c, py, total, avg, grade))
        self.conn.commit()
        print("학생이 추가되었습니다.")

    #삭제 함수
    def delete(self):
        stu_id = input("삭제할 학번 : ")
        self.cur.execute("DELETE FROM students WHERE id=%s", (stu_id,))
        self.conn.commit()
        print("삭제 완료")

    #검색 함수
    def search(self):
        stu_id = input("학번 : ")
        name = input("이름 : ")
        self.cur.execute("SELECT * FROM students WHERE id=%s AND name=%s", (stu_id, name))
        student = self.cur.fetchone()
        if student:
            self.print_header()
            self.print_student(student, self.get_rank(student[5]))
        else:
            print("해당 학생 없음")
    #검색 결과 출력 함수
    def out(self):
        self.cur.execute("SELECT * FROM students ORDER BY total DESC")
        students = self.cur.fetchall()
        if not students:
            print("학생 데이터가 없습니다.")
            return

        self.print_header()
        for rank, student in enumerate(students, start=1):
            self.print_student(student, rank)

        self.cur.execute("SELECT COUNT(*) FROM students WHERE average >= 80")
        count = self.cur.fetchone()[0]
        print(f"\n80점 이상 학생 수 : {count}")

    #학점 계산 함수
    def calculate_grade(self, avg):
        if avg >= 95: return "A+"
        elif avg >= 90: return "A"
        elif avg >= 85: return "B+"
        elif avg >= 80: return "B"
        elif avg >= 75: return "C+"
        elif avg >= 70: return "C"
        elif avg >= 65: return "D+"
        elif avg >= 60: return "D"
        else: return "F"

    #랭킹 계산 함수
    def get_rank(self, total_score):
        self.cur.execute("SELECT COUNT(*) FROM students WHERE total > %s", (total_score,))
        higher_count = self.cur.fetchone()[0]
        return higher_count + 1

    #학생 정보 목록 출력 함수
    def print_header(self):
        print("="*80)
        print("학번        이름     영어   C-언어   파이썬   총점   평균   학점   등수")
        print("="*80)

    #학생 정보 출력 함수
    def print_student(self, s, rank):
        print(f"{s[0]:<12}{s[1]:<8}{s[2]:<8}{s[3]:<8}{s[4]:<8}{s[5]:<8}{s[6]:<8.1f}{s[7]:<6}{rank}")

def main():
    app = StudentDB()
    app.menu()

main()