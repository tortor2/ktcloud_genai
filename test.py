str ="hello"

print(str)

num =1

print(num)

name = "kevin"
age = 25
print("이름:", name, "나이:", age)

num = int(input("숫자 입력: "))
if num > 0:
    print("양수입니다")
elif num < 0:
    print("음수입니다")
else:
    print("0입니다")




for i in range(5):
    print("안녕하세요", i+1, "번째")



fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(fruit)

def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("kevin"))

person = {"이름": "tor", "나이": 25, "직업": "학생"}
print("이름:", person["이름"])
print("나이:", person["나이"])


count = 0
while count < 5:
    print("카운트:", count)
    count += 1