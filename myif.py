# 아스키 코드 그림 출력 하기
def print_cat():
    cat_art = r"""
      /\_/\  
     ( o.o ) 
     > ^ <
    """
    print(cat_art)

print_cat()
def print_dog():
    dog_art = r"""
       / \__
      (    @\___
      /         O
     /   (_____/
    /_____/   U
    """
    print(dog_art)

print_dog()
def print_rabbit():
    rabbit_art = r"""
     (\(\ 
     ( -.-)
     o_(")(")
    """
    print(rabbit_art)

print_rabbit()
print("그림 출력 프로그램")
print("===========")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("===========")
n = int(input("선택: "))
# 만약에 1을 입력하면 1번 캐릭터 출력
if n == 1:
    print("고양이")
# 만약에 2를 입력하면 2번 캐릭터 출력
elif n == 2:
    print("강아지")
# 3을 입력하면 3번 캐릭터 출력
elif n == 3:
    print("토끼")
# 잘못 입력하면 잘못 입력했다고 출력
else :
    print("잘못 입력")