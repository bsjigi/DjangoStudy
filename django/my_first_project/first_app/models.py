from django.db import models

# models.py에 현재 앱에서 사용할 데이터의 형태를 정의한다.
# Django는 이곳에 정의한 클래스를 바탕으로 테이블을 자동으로 생성해준다.

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(primary_key=True, max_length=200)
    address = models.CharField(max_length=500)

class Employee(models.Model):
    # 모델에는 각 컬럼을 정의하고, 각 컬럼의 데이터 타입을 지정해야 한다

    # models.IntegerField() : 정수만 저장할 수 있는 컬럼을 생성한다. (컬럼을 필드라고 하기도 한다)
    emp_id = models.IntegerField(primary_key=True)
    # models.CharField() : 문자열을 저장할 수 있는 컬럼을 생성한다. max_length를 반드시 설정해야 한다.
    ename = models.CharField(max_length=50)
    # models.FloatField() : 소수를 저장할 수 있는 필드를 생성한다. 파이썬의 float타입을 사용한다.
    salary = models.FloatField(null=False)
    # models.ForeignKey()
    #   : 외래키 필드를 생성한다. 어떤 모델을 참조할지 설정해야 한다.
    #     on_delete를 반드시 설정해야 한다.
    department_name = models.ForeignKey(Department, on_delete=models.PROTECT)

# 연습문제: 아까 작성한 테이블을 보면서 모델을 정의 해보세요

class PizzaOrder(models.Model):
    # ※ 모델에 PK를 생략하고 마이그레이션을 진행하면
    #   자동으로 id라는 이름의 PK를 하나 생성해준다.
    customer_name = models.CharField(max_length=50)
    pizza_topping = models.CharField(max_length=20)
    pizza_sauce = models.CharField(max_length=20)
    optional_extras = models.CharField(max_length=200)
    delivery_instructions = models.TextField()





