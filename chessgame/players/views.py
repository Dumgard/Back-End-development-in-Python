from django.http import JsonResponse, HttpResponseNotAllowed
from players.models import Player
from datetime import datetime
from django.shortcuts import render


def create(request):
    if request.method == 'POST':
        u = Player()
        p = request.POST
        u.password = p.get("password")
        u.email = p.get("email")
        u.is_superuser = False
        u.username = p.get("username")
        u.first_name = p.get("first_name")
        u.last_name = p.get("last_name")
        u.is_staff = False
        u.is_active = True
        u.date_joined = datetime.now().date()
        u.nickname = p.get("username")
        u.rating = 1200
        u.history = None
        u.save()
        return render(request, 'create.html')
    else:
        return HttpResponseNotAllowed


def info(request, player_id):
    if request.method == 'GET':
        u = Player.objects.get(id=player_id)
        return JsonResponse({
            "Id": player_id,
            "Last time online": u.last_login,
            "Username": u.username,
            "First name": u.first_name,
            "Last name": u.last_name,
            "Is active": u.is_active,
            "Date joined": u.date_joined,
            "Nickname": u.nickname,
            "E-mail": u.email,
            "Rating": u.rating,
        })
    else:
        return HttpResponseNotAllowed


def ratings(request):
    if request.method == 'GET':
        ps = Player.objects.order_by('-rating')
        res = {}
        for p in ps:
            res[p.id] = f"Rating: {p.rating}            Nickname: {p.nickname}"
        return JsonResponse(res)
    else:
        return HttpResponseNotAllowed


def update(request):
    if request.method == 'POST':
        p = request.POST
        u = Player.objects.get(id=p.get('id'))
        if 'password' in p and p.get('password') is not None:
            u.password = p.get('password')
        if 'first_name' in p and p.get('first_name') is not None:
            u.first_name = p.get('first_name')
        if 'last_name' in p and p.get('last_name') is not None:
            u.last_name = p.get('last_name')
        if p.get('nickname') is not None:
            u.nickname = p.get('nickname')
        u.save()
        return render(request, 'update.html')
    else:
        return HttpResponseNotAllowed


def delete(request):
    if request.method == 'POST':
        Player.objects.filter(id=request.POST.get("id")).delete()
        return render(request, 'deletion.html')
    else:
        return HttpResponseNotAllowed

# Create your views here.
