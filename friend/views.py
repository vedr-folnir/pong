from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Friendship
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, "friend/index.html")

def add(request):
    if request.method == 'POST':
        you = request.user
        users = User.objects.filter(username=request.POST.get('username'))
        if len(users) == 0:
            messages.info(request, ("user doesn't exist"))
            return render(request, "friend/add.html")
        new_friend = Friendship.objects.filter(Q(user=you, friend=users[0]) | Q(user=users[0], friend=you))
        if len(new_friend) != 0:
            messages.info(request, ("already friend"))
            return render(request, "friend/work.html", {'friend':users[0], 'you':you, 'n':new_friend})
        new_friend = Friendship(user=you, friend=users[0])
        new_friend.save()
        return render(request, "friend/work.html", {'friend':users[0], 'you':you})
        # Handle the submitted username as needed
        # For example, you can query the User model or process it in other ways
    return render(request, "friend/add.html")
    
def delete_friend(request, id_friendship):
    request = Friendship.objects.get(id=id_friendship)
    request.delete()
    return redirect("friend:list")

def accept(request, id_friendship):
    request = Friendship.objects.get(id=id_friendship)

    request.status = 'accepted'
    request.save()
    return redirect("friend:pending")

def refuse(request, id_friendship):
    request = Friendship.objects.get(id=id_friendship)
    request.status = 'refused'
    request.save()
    return redirect("friend:pending")

def list(request):
    you = request.user
    friends = Friendship.objects.filter(Q(user=you, status='accepted') | Q(friend=you, status='accepted'))
    return render(request, "friend/list.html", {'friends':friends, 'you':you})


def pending(request):
    you = request.user
    friends = Friendship.objects.filter(Q(friend=you, status='pending'))
    return render(request, "friend/pending.html", {'friends':friends, 'you':you})

def refused(request):
    you = request.user
    friends = Friendship.objects.filter(Q(friend=you, status='refused'))
    return render(request, "friend/refused.html", {'friends':friends, 'you':you})
