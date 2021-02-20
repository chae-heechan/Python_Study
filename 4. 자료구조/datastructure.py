# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨는 몇 번째 칸에 타고있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음칸에 탔음
subway.append("하하")   # 맨뒤에 타게된다
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))