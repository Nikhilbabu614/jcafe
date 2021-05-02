from django.shortcuts import render ,HttpResponse
from food.models import Contact,Orders
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contactu(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        itam1=request.POST.get('itam1')
        contact = Contact(name=name,email=email,itam1=itam1)
        contact.save()
        messages.success(request,"Thanks for your Response")

    #else:
        #  messages.error(request,'form has been declined')

    return render(request,'contact.html')


def Menu(request):
    if request.method == "POST":
        Noodles=request.POST.get('Noodles')
        FriedRice=request.POST.get('FriedRice')
        Manchurian=request.POST.get('Manchurian')
        Chicken65=request.POST.get('Chicken65')
        VegMeal=request.POST.get('VegMeal')
        Coke=request.POST.get('Coke')
        Coffee=request.POST.get('Coffee')
        Tea=request.POST.get('Tea')
        FruitJucies=request.POST.get('FruitJucies')
        Smoothies=request.POST.get('Smoothies')
        Burger=request.POST.get('Burger')
        Roll=request.POST.get('Roll')
        Puffs=request.POST.get('Puffs')
        Chocolate=request.POST.get('Chocolate')
        Paestry=request.POST.get('Paestry')
        Recipent=request.POST.get('Recipent')
        
        det = Orders(Noodles=Noodles,FriedRice=FriedRice,Manchurian=Manchurian,Chicken65=Chicken65,VegMeal=VegMeal,
        Coke=Coke,Coffee=Coffee,Tea=Tea,FruitJucies=FruitJucies,Smoothies=Smoothies,Burger=Burger,
        Roll=Roll,Puffs=Puffs,Chocolate=Chocolate,Paestry=Paestry,Recipent=Recipent)
        det.save()
        messages.success(request,"order has been placed")

    # else:
    #     messages.error(request,'order has been not placed')
    return render(request,"menu.html")


def fastf(request):
    return render(request,"fast.html")

def drinks(request):
    return render(request,"drink.html")

def rollss(request):
    return render(request,"rolls.html")
