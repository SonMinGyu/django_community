from django.shortcuts import render, redirect  # redirect 추가
from .models import User  # 추가
from django.http import HttpResponse  # 추가
from django.contrib.auth.hashers import make_password, check_password  # 추가
from .forms import LoginForm  # 추가

# Create your views here.

# 함수를 url에 연결하면 요청정보가 request 변수로 들어옴
# 비니지스 로직


def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    # django form 생성 version
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id

            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

    # html에 form 생성 version
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = "입력하지 않은 칸이 있습니다."
    #     else:
    #         # 입력한 아이디가 등록된 아이디 인가 검사
    #         id_exist = False
    #         id_search = User.objects.values()
    #         for i in range(len(id_search)):
    #             if username in id_search[i].values():
    #                 id_exist = True

    #         if not id_exist:
    #             res_data['error'] = "등록된 아이디가 없습니다."
    #             return render(request, 'login.html', res_data)

    #         # 입력한 이름의 유저 정보를 가져옴
    #         user = User.objects.get(username=username)
    #         print(user.username)
    #         print("input password {}".format(password))
    #         print("user password {}".format(user.password))

    #         if check_password(password, user.password):
    #             print("hi")
    #             # 비밀번호가 같을 경우 처리

    #             # 세션
    #             request.session['user'] = user.id

    #             # redirect
    #             return redirect('/')
    #         else:
    #             res_data['error'] = "비밀번호가 틀렸습니다."
    # return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        userEmail = request.POST.get('userEmail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)  # POSt는 dict 임

        res_data = {}

        if not (username and userEmail and password and re_password):
            res_data["error"] = '빈칸을 채워주세요!'
        elif password != re_password:
            res_data["error"] = '비밀번호가 다릅니다!'
        else:
            user = User(
                username=username,
                userEmail=userEmail,
                password=make_password(password)  # 비밀번호 암호화
            )

            user.save()

        return render(request, 'register.html', res_data)
