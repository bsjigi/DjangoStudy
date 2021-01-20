from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(req):
    return HttpResponse('<p>두 번째 앱의 메인 페이지</p>'
                        '<a href="./news/">뉴스 메인</a><br>'
                        '<a href="./news/article1">기사1</a><br>'
                        '<a href="./news/article2">기사2</a><br>')

def news_main(req):
    return HttpResponse('<h3>뉴스 메인 페이지</h3>')

def article1(req):
    return HttpResponse('<p>[속보] 코로나 확진 1097명 또 최다...닷새째 1000명대</p>')

def article2(req):
    return HttpResponse('<p>오늘 확진자 또 최대 기록 경신… 3단계 격상 기로</p>')