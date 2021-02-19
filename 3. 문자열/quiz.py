inputValue = "http://naver.com"
password = inputValue.replace("http://", "")
password = password[:password.index(".")]
outputValue = password[:3] + str(len(password)) + str(password.count("e")) + "!"


print(f"{inputValue}의 비밀번호는 {outputValue}입니다.")