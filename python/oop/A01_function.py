# A01_function.py

# 함수 (function)
#   - 영어 뒤에 ()를 붙여서 사용하는 모든 것
#   - 기능들을 묶어서 이름 붙여 놓는 것
#   - 매개변수
#   - 리턴


# 3줄 짜리 명령어를 묶어서 하나로 정의해놓았다 (함수를 정의했다)
def printRabbit():
    print(' /)/)')  # by python 제작자
    print('(  ..)')
    print('(  >♡')

# 함수는 나중에 실컷 사용할 기능을 미리 정의해 놓는 문법이다
printRabbit()
printRabbit()
printRabbit()


# 매개변수가 있는 함수
def printInfo(name='기본이름', age=123, gender='unknown'):
    print(f'이름: {name}\n나이: {age}\n성별: {gender}\n')

# 매개변수가 있는 함수를 사용할 때는 값을 전달해야 한다
printInfo('철수', 10, 'male')
printInfo('영희', 15, 'female')
printInfo(*['민수', 20, 'mail'])  # 리스트의 내용을 풀어서 매개변수로 전달할 수도 있다
printInfo()  # 매개변수에 기본값이 있는 함수는 그냥 호출할 수도 있다
printInfo(age=11, gender='femail', name='채윤')  # 매개 변수명을 입력하면 위치를 지키지 않아도 된다


# 리턴이 있는 함수
def getInfo(name, age, gender):
    return f'이름: {name}\n나이: {age}\n성별: {gender}\n'

# 리턴이 있는 함수는 모든 내용을 처리한 뒤에 결과를 함수를 호출한 곳에 반환한다
result = getInfo('대현', 20, 'male')
print(result)
print(getInfo('대현', 20, 'male'))


