# 사용자에게 몇 단을 출력할지 입력받기
dan = int(input("몇 단을 출력할까요? "))

# 구구단 출력
print(f"== {dan}단 ==")
for i in range(1, 10):
    result = dan * i
    print(f"{dan} × {i} = {result}")