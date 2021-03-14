from django.shortcuts import render, redirect  # redirect 추가
from user.models import User  # 추가
from .models import Board  # 추가
from .forms import BoardForm  # 추가
from django.http import Http404  # 추가
from django.core.paginator import Paginator  # 추가
from tag.models import Tag  # add

# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split('#')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)

                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')  # -는 역순, 즉 최신순으로 정렬하겠다는 의미
    page = int(request.GET.get('p', 1))  # p라는 변수로 받고 default 값은 1
    paginator = Paginator(all_boards, 10)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})
