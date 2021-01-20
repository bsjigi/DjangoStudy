from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint, sample, choice
from .models import PizzaOrder, Employee

# View들을 모아놓는 파일이기 때문에 views.py라는 이름을 지니고 있다
# Create your views here. (Framework의 특징 : 프로그래머가 어디에 무얼 추가해야 할지 미리 정해놓음)

# View 역할을 하는 함수는 사용자의 요청 정보를 토대로 알맞은 응답을 생성해야 한다
def index(request):
    return HttpResponse("<h1>First App Index Page!</h1>")

def write(request):
    return HttpResponse("<h1 style='color: blue;'>First App Write Page</h1>")

def delete(request):
    return HttpResponse("<h1 style='color: orange;'>First App Delete Page</h1>")

def comic(request):
    return HttpResponse("<a href='http://comic.naver.com'>네이버 웹툰 페이지로</a>")

# localhost:8000/first/layout으로 접속하면 08_레이아웃.html과 같은 화면이 나오도록 만들어보세요
def layout(request):
    # render(req, 'view로 사용할 템플릿 경로', 전달할 데이터 딕셔너리)
    return render(request, 'layout.html')

# localhost:8000/first/table로 접속하면 06_표 출력하기.html과 같은 화면이 나오도록 만들어보세요
# (템플릿과 render() 함수 사용)
def table(request):
    return render(request, 'table.html')

# views의 함수에서는 템플릿으로 데이터를 실어보낼 수 있다
def templatetest(request):
    # 딕셔너리 형태의 데이터만 전달할 수 있다
    a, b, c = 55, 20, 30

    data = {
        'a': a,
        'b': b,
        'c': c,
        'sum': a + b + c,
        'lotto': sample(range(1, 46), 7),  # 랜덤 로또번호 7개를 만들어 템플릿으로 전달해보세요
        'fruit': choice(['apple', 'banana', 'orange', 'kiwi']),
        'lotto2': list(),
        'animals': ('cat', 'dog', 'hawk', 'eagle', 'wolf', 'lion', 'tiger'),
        'odds': {1, 3, 5, 7, 9},
        'welcomeMessage': 'hello! welcome to my homepage!',
        'friends': [],
        'pythonHtmlCode': '<h3 style="color: peru;">파이썬에서 생성된 코드!</h3>',
    }
    # 로또란? 1 ~ 45의 중복없는 숫자 7개
    while len(data['lotto2']) < 7:
        new_num = randint(1, 45)
        if new_num not in data['lotto2']:
            data['lotto2'].append(new_num)

    # 리스트 자체를 if문에 사용하면, 알아서 비어있는 리스트인지 체크를 해준다
    colors = []
    
    if colors:
        print(colors)
    else:
        print('colors가 비어있습니다.')
    
    return render(request, 'template.html', data)


def form(request):
    return render(request, 'test_form.html')

def action(request):
    print(request.GET['name'])
    print(request.GET['age'])
    print(request.GET.getlist('genre'))

    return HttpResponse('Action Test...')

def pizza_order(req):
    return render(req, 'form/pizzashop.html', {
        'toppings': ('supreme', 'vegetarian', 'hawaiian'),
        'sauces': ('tomato', 'tavasco'),
        'extras': (
                        {
                            'name': 'exchez',
                            'desc': 'Extra Cheese'
                        },
                        {
                            'name': 'glufree',
                            'desc': 'Gluten Free Base'
                        },
                        {
                            'name': 'chezcrust',
                            'desc': 'Cheese Crust'
                        }
                  ),
    })

def pizza_payment(req):
    # 사용자로부터 받은 데이터를 DB에 저장하기

    # 1. 모델 객체를 생성한다
    newOrder = PizzaOrder()

    # 2. 사용자가 요청에 실어보낸 데이터를 모델 객체에 채운다
    newOrder.customer_name = req.POST['name']
    newOrder.pizza_topping = req.POST['topping']
    newOrder.pizza_sauce = req.POST['sauce']
    newOrder.optional_extras = '/'.join(req.POST.getlist('extras'))
    newOrder.delivery_instructions = req.POST['instructions']

    # 3. save()
    newOrder.save() # 생성한 데이터를 DB에 저장하는 메서드

    # if req.method == 'GET':
    #     print('------------ 사용자가 주문한 피자 정보 ------------')
    #
    #     print('토핑:', req.GET['topping'])
    #     print('소스:', req.GET['sauce'])
    #     print('추가:', req.GET.getlist('extras'))
    #     print('요구사항:', req.GET['instructions'])
    # elif req.method == 'POST':
    #     print('------------ 사용자가 주문한 피자 정보 ------------')
    #
    #     print('토핑:', req.POST['topping'])
    #     print('소스:', req.POST['sauce'])
    #     print('추가:', req.POST.getlist('extras'))
    #     print('요구사항:', req.POST['instructions'])

    return HttpResponse('<h3>결제중입니다...</h3>')

def static_test(req):
    return render(req, 'static_test.html')

def pizza_list(req):
    # Model.objects.all() : DB에 저장된 모든 데이터를 꺼내오기
    orderlist = PizzaOrder.objects.all()

    return render(req, 'pizzashop/pizza_order_list.html', {
        'orderlist': orderlist,
    })

# <int:id>값을 id라는 이름의 매개변수로 전달받게 된다
def pizza_order_detail(req, id):
    # Model.objects.get(condition) : DB에 저장된 데이터들 중 하나만 꺼내오기
    a_order = PizzaOrder.objects.get(pk=id)

    print('도착한 id값:', id)
    print('해당 id값으로 get()한 주문:', a_order)


    # '/'.join(['apple', 'banana', 'kiwi'])  =>  'apple/banana/kiwi'
    # 'apple/banana/kiwi'.split('/')  =>  ['apple', 'banana', 'kiwi']

    # in : 'eve' in 'hello, everyone' -> True
    #      'exchez' in "['exchez', 'glufree', 'chezcrust']" -> True

    print(a_order.optional_extras.split('/'))

    return render(req, 'pizzashop/pizza_order_detail.html', {
        'a_order': a_order,
        'optional_extra_list': a_order.optional_extras.split('/'),
        'toppings': ('supreme', 'vegetarian', 'hawaiian'),
        'sauces': ('tomato', 'tavasco'),
        'extras': (
            {
                'name': 'exchez',
                'desc': 'Extra Cheese'
            },
            {
                'name': 'glufree',
                'desc': 'Gluten Free Base'
            },
            {
                'name': 'chezcrust',
                'desc': 'Cheese Crust'
            }
        ),
    })

def emp_list(req):
    return render(req, 'org/employee_list.html', {
        'employee_list': Employee.objects.all(),
    })

def pizza_order_modify(req, id):
    # DB의 데이터를 수정하는 방법
    # 1. 이전 데이터를 불러온다
    old_pizza = PizzaOrder.objects.get(pk=id)

    # 2. 이전 데이터의 값을 수정한다
    old_pizza.pizza_topping = req.POST['topping']
    old_pizza.pizza_sauce = req.POST['sauce']
    old_pizza.optional_extras = '/'.join(req.POST.getlist('extras'))
    old_pizza.delivery_instructions = req.POST['instructions']

    # 3. save()
    old_pizza.save()

    # 보여줄 화면을 결정한다
    # redirect: 다른 템플릿으로 보내는 대신, 다른 urls로 보낸다.
    return redirect('pizza_list')


def pizza_order_delete(req, id):
    # DB의 데이터를 삭제하는 방법
    # 1. 모델을 이용해 지워야하는 데이터를 가져온다
    pizza_to_delete = PizzaOrder.objects.get(pk=id)

    # 2. delete()
    pizza_to_delete.delete()

    # 보여줄 화면을 결정한다
    return redirect('pizza_list')



