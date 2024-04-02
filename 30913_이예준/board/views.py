from django.core.paginator import Paginator

from django.shortcuts import render

from board.models import Board


def main(request):
    board_list = (
        Board.objects
        .all()
    )
    page = request.GET.get('page', 1)
    paginator = Paginator(board_list, 2)
    page_board_list = paginator.get_page(page)

    return render(
        request,
        'main.html',
        context={
            'board_list': page_board_list
        }
    )



















