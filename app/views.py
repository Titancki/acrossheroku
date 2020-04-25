from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from pprint import pprint
from app.models import Game, Team, MatchHistory
import datetime

def handler404(request, *args, **argv):
    return render(request, "404.html")



def index(request):
    lastMatchs = MatchHistory.objects.all().order_by('-date')[:5]
    tmpemptyMatchs = 5 - lastMatchs.count()
    emptyMatchs = ""
    while tmpemptyMatchs > 0:
        emptyMatchs = emptyMatchs + "."
        tmpemptyMatchs = tmpemptyMatchs - 1

    context = {
        "lastMatchs": lastMatchs,
        "emptyMatchs": emptyMatchs
    }
    return render(request, "index.html", context)
def team(request):
    context = {

    }
    return render(request, "team.html", context)
def staff(request):
    context = {

    }
    return render(request, "staff.html", context)
def affiliate(request):

    context = {

    }
    return render(request, "affiliate.html", context)
def profil(request):
    # Récuperer les donées
    # donées -> mettre a jour la db
    context = {

    }
    return render(request, "profil.html", context)
def contact(request):
    context = {

    }
    return render(request, "contact.html", context)
def auth_logout(request):
    logout(request)
    context = {

    }
    return render(request, "index.html", context)
def admin(request):
    if not request.user.is_staff:
        raise Http404

    allGame = Game.objects.all()
    allTeam = Team.objects.all()
    allMatch = MatchHistory.objects.all()
    context = {
        "allGame": allGame,
        "allTeam": allTeam,
        "allMatch": allMatch,
    }
    return render(request, "admin.html", context)
def add_game(request):
    if not request.user.is_staff:
        raise Http404

    if request.POST.get('gameName'):
        gameName = request.POST.get('gameName')
        game = Game(name=gameName)
        game.save()
    else:
        print("error: Game was not created")

    return redirect('/admin')
def delete_game(request):
    if not request.user.is_staff:
        raise Http404

    if request.GET.get('gamePk'):
        gamePk = request.GET.get('gamePk')
        Game.objects.get(id=gamePk).delete()
    else:
        print("error: Game was not deleted")

    return redirect('/admin')
def add_team(request):
    if not request.user.is_staff:
        raise Http404

    if request.POST.get('teamName'):
        teamName = request.POST.get('teamName')
        teamStructure = request.POST.get('teamStructure')
        teamGame = Game.objects.get(pk=request.POST.get('teamGame'))
        team = Team(name=teamName, structure=teamStructure, game=teamGame)
        team.save()
    else:
        print("error: Team was not created")

    return redirect('/admin')
def delete_team(request):
    if not request.user.is_staff:
        raise Http404

    if request.GET.get('teamPk'):
        teamPk = request.GET.get('teamPk')
        Team.objects.get(id=teamPk).delete()
    else:
        print("error: Team was not deleted")

    return redirect('/admin')
def add_match(request):
    if not request.user.is_staff:
        raise Http404

    if request.POST.get('team1Match'):
        team1Match = Team.objects.get(pk=request.POST.get('team1Match'))
        score1Match = request.POST.get('score1Match')
        team2Match = Team.objects.get(pk=request.POST.get('team2Match'))
        score2Match = request.POST.get('score2Match')
        gameMatch = Game.objects.get(pk=request.POST.get('gameMatch'))
        dateMatch = datetime.datetime.strptime(request.POST.get('dateMatch'),"%d-%m-%Y %H:%M")
        print(dateMatch)

        match = MatchHistory(team1=team1Match, score1=score1Match, team2=team2Match, score2=score2Match, game=gameMatch, date=dateMatch)
        match.save()
    else:
        print("error: Team was not created")

    return redirect('/admin')
def delete_match(request):
    if not request.user.is_staff:
        raise Http404

    if request.GET.get('matchPk'):
        matchPk = request.GET.get('matchPk')
        MatchHistory.objects.get(id=matchPk).delete()
    else:
        print("error: Match was not deleted")

    return redirect('/admin')