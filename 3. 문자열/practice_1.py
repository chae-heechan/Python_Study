python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java")) 

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))  # 없을 경우 return -1
# print(python.index("Java")) # 없을 경우 error 띄우고 종료
print("hi")

print(python.count("n"))