
from django.urls import path
from . import views

# localhost:8000/first/로 요청한 모든 요청은 이곳에 도착하게 된다
# 이후의 주소에 따라 어떤 함수를 사용할지를 이곳에서 설정할 수 있다
urlpatterns = [
    path('iiindex', views.index, name='index'),
    path('wwwwwwwwwwwwrite/', views.write, name='write'),
    path('deeeeelete/', views.delete, name='delete'),
    path('commmmic/', views.comic, name='comic'),
    path('layyyyout', views.layout, name='layout'),
    path('table', views.table, name='table'),
    path('templatetest', views.templatetest, name='test'),
    path('form/', views.form, name='form'),
    path('action', views.action, name='action'),
    path('pizza/order/', views.pizza_order, name='pizza_order'),
    path('pizza/order/list', views.pizza_list, name='pizza_list'),
    path('pizza/order/<int:id>/detail/', views.pizza_order_detail, name='pizza_detail'),
    path('pizza/order/<int:id>/detail/modify', views.pizza_order_modify, name='pizza_modify'),
    path('pizza/order/<int:id>/detail/delete', views.pizza_order_delete, name='pizza_delete'),
    path('pizza/order/payment', views.pizza_payment, name='pizza_payment'),
    path('static_test', views.static_test, name='static_test'),
    path('org/employee/list', views.emp_list, name='emp_list'),
]