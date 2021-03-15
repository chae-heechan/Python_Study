# import sys
# print("Python", "Java", "JavaScript", sep=" vs ")
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재미있을까요?")

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep=":")

# 은행 순번표
for number in range(1,21):
    print("대기번호 : " + str(number).zfill(3))

# 항상 문자열
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은" + answer + "입니다.")