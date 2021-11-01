from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader


def new_board(request):
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'board': [
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢'
                            ]
        })
    else:
        return HttpResponseBadRequest


def list_board(request):
    if request.method == 'GET':
        return JsonResponse({
            'list_board': [
                {
                    'game_id': 5,
                    'board': [
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢'
                            ],
                },
                {
                    'game_id': 16,
                    'board': [
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '♙ ▢ ♙ ▢ ♙ ♙ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ♟ ▢ ♟ ▢ ▣ ♟ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢'
                            ],
                },
                {
                    'game_id': 1,
                    'board': [
                                 '▢ ▣ ♗ ♕ ▢ ▣ ♘ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                                 '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                                 '♜ ▢ ▣ ♛ ♚ ▢ ▣ ▢'
                            ],
                }
            ]
        })
    else:
        return HttpResponseBadRequest


def info(request, game_id):
    if request.method == 'GET':
        return JsonResponse({
            'game_id': game_id,
            'player1_id': 156661,
            'player2_id': 156667,
            'turn': 12,
            'winner': None,
            'score': 17.52,
            'engine': 'Stockfish 18.2',
            'board': [
                         '▢ ▣ ♗ ♕ ▢ ▣ ♘ ▣',
                         '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                         '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                         '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                         '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                         '▣ ▢ ▣ ▢ ▣ ▢ ▣ ▢',
                         '▢ ▣ ▢ ▣ ▢ ▣ ▢ ▣',
                         '♜ ▢ ▣ ♛ ♚ ▢ ▣ ▢'
                    ],
        })
    else:
        return HttpResponseBadRequest


def render_board(request):
    if request.method == 'GET':
        return render(request, 'emptyBoard.html')
    else:
        return HttpResponseBadRequest

