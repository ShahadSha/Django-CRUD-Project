from django.shortcuts import render
from .models import Destination, table, cards

# Create your views here.
def index(request):
    

    dests = Destination.objects.all()

    tb1 = table()
    tb1.firstn = "shahad"
    tb1.lastn = 'sha'

    tb2 = table()
    tb2.firstn = "Rahul"
    tb2.lastn = 'P'

    tb3 = table()
    tb3.firstn = "vignesh"
    tb3.lastn = 'D'

    tbs = [tb1,tb2,tb3]

    cards1 = cards()
    cards1.title = "card 1"
    cards1.img = 'img-5.png'
    cards1.desc = "ok bye 1"

    cards2 = cards()
    cards2.title = "card 2"
    cards2.img = 'img-3.png'
    cards2.desc = "ok bye 2"

    cards3 = cards()
    cards3.title = "card 3"
    cards3.img = 'img-4.png'
    cards3.desc = "ok bye 3"

    cardss = [cards1,cards2,cards3]


    return render(request, 'index.html', {'dests' : dests, 'tbs' : tbs, 'cardss' : cardss})