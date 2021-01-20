
# 클래스
#   - 설계도
#   - 클래스는 정의한 시점에서는 실체가 없다
#   - 생성자를 통해 실체를 생성해야 하며, 생성된 실체를 인스턴스라고 부른다

# 인스턴스
#   - 클래스의 생성자를 호출하고 나면 생성되는 실체
#   - 클래스의 멤버 변수는 인스턴스마다 각각 다른 값을 지닐 수 있다

# self
#   - 각 인스턴스 마다 가지고 있는 영역
#   - 멤버 변수들이 저장되는 공간
#   - self 영역의 값을 이용하는 메서드를 인스턴스 메서드라고 부른다

class Human:
    def __init__(self, name, age):
        # 멤버 변수, 필드, 속성 (property, attribute)
        self.name = name
        self.age = age

    def introduce(self):
        # 멤버 변수는 self. 영역에서 꺼내어 사용해야 한다
        if self.age < 15:
            print(f'안녕! 내 이름은 {self.name}. 나이는 {self.age}살 이야.')
        else:
            print(f'안녕하세요! 제 이름은 {self.name}입니다. 나이는 {self.age}살 입니다.')

# 사람마다 이름이 다르고 나이가 다르다
# 멤버 변수는 인스턴스마다 다른 값을 지닐 수 있다
human1 = Human('홍길동', 10)   # Human 클래스의 인스턴스 1
human2 = Human('임꺽정', 11)   # Human 클래스의 인스턴스 2
human3 = Human('김철수', 33)

# 인스턴스 메서드는 각 인스턴스가 가지고 있는 값을 이용해 동작하게 된다.
# 메서드를 한번만 만들어 놔도 각 인스턴스가 가지고 있는 값을 이용해 다르게 동작한다.
human1.introduce()
human2.introduce()
human3.introduce()

class Burger:
    # 클래스의 생성자
    #   - 클래스에서 사용할 멤버 변수를 정의하는 용도로 사용하는 함수
    def __init__(self, meat, sauce, name):
        self.meat = meat
        self.sauce = sauce
        self.name = name

# Burger 클래스의 인스턴스들
b1 = Burger('불고기', '불고기 소스', '불고기 버거')
b2 = Burger('약간 매운 치킨', '흰색 소스', '상하이 스파이시 버거')


#####################################################################

# 연습문제. 직접 클래스를 하나 설계하고 테스트 해보세요 (멤버 변수 2개 이상, 메서드 1개 이상)
from random import randint

class Lotto:
    def __init__(self):
        self.numbers = self.new_lotto()

    def new_lotto(self):
        new_numbers = []
        while len(new_numbers) != 6:
            num = randint(1, 45)

            if num not in new_numbers:
                new_numbers.append(num)
        return new_numbers

lotto = Lotto()

for i in range(10):
    print(lotto.new_lotto())











