cabinet = {3:"유재석", 100:"김태호"}  # {key:data}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])       error 뜨고 끝남
print(cabinet.get(5))       #None 리턴 후 이어짐
print(cabinet.get(5, "사용 가능"))
print("hi")


print(3 in cabinet)     # 있으면 True, 없으면 False
print(5 in cabinet)

box = {"A-3":"유재석", "B-100":"김태호"}
print(box["A-3"])
print(box["B-100"])

# 새 손님
print(box)
box["A-3"] = "김종국"
box["C-20"] = "조세호"
print(box)

# 간 손님
del box["A-3"]
print(box)

# key들만 출력
print(box.keys())

# value들만 출력
print(box.values())

# key, value 둘다 출력
print(box.items())

# 목묙탕 폐점
box.clear()
print(box)