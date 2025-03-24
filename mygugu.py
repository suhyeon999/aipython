# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력 하는 프로그램을 만들어 보자
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 사칙연산 수행 및 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# 나눗셈의 경우 0으로 나누는 상황 처리
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print(f"{num1} / {num2} = 오류 (0으로 나눌 수 없습니다)")