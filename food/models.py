from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField( max_length=254)
    itam1 = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Orders(models.Model):
    Noodles = models.CharField(max_length=100)
    FriedRice = models.CharField(max_length=100)
    Manchurian = models.CharField(max_length=100)
    Chicken65 = models.CharField(max_length=100)
    VegMeal = models.CharField(max_length=100)
    Coke = models.CharField(max_length=100)
    Coffee = models.CharField(max_length=100)
    Tea = models.CharField(max_length=100)
    FruitJucies = models.CharField(max_length=100)
    Smoothies = models.CharField(max_length=100)
    Burger = models.CharField(max_length=100)
    Roll = models.CharField(max_length=100)
    Puffs = models.CharField(max_length=100)
    Chocolate = models.CharField(max_length=100)
    Paestry = models.CharField(max_length=100)
    Recipent = models.CharField(max_length=100 , default="none")


    
    def __str__(self):
         return self.Recipent
    

