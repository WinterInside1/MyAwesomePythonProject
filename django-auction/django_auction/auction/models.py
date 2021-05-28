from django.db import models


class Client(models.Model):
    id = models.CharField(max_length=10)
    # role = Role - переделать с django choices
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    balance = models.FloatField
    ad_flag = models.BooleanField
<<<<<<< HEAD
    # карта?r
=======
    # карта?
>>>>>>> 56e1310e552f60ca550d0e429e122e4b740026b5


class Advertisement(models.Model):
    id = models.CharField(max_length=10)
    text = models.TextField


class Item(models.Model):
    id = models.CharField(max_length=10)
    name = models.TextField
    price = models.FloatField
    # check for on_delete and primary_key fields
<<<<<<< HEAD
    owner = models.OneToOneField(Client, on_delete=models.CASCADE())
=======
    owner = models.OneToOneField(Client, on_delete=models.CASCADE(), foreign_key)
>>>>>>> 56e1310e552f60ca550d0e429e122e4b740026b5
    # id аукциона


class Auction(models.Model):
    id = models.CharField(max_length=10)
    # type = AuctionType - сделать с django choices
    description = models.TextField
    time = models.TimeField
<<<<<<< HEAD
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    owner = models.OneToOneField(Client, on_delete=models.CASCADE)
    ads = models.ForeignKey(Advertisement, on_delete=models.SET_NULL)
=======
    item = models.OneToOneField(Item, on_delete=models.CASCADE, foreign_key)
    owner = models.OneToOneField(Client, on_delete=models.CASCADE, foreign_key)
    ads = models.ForeignKey(Advertisement, on_delete=models.SET_NULL, foreign_key)
>>>>>>> 56e1310e552f60ca550d0e429e122e4b740026b5


# TODO:
# 1. Объединить оплату и доставку в транзакцию
# 2. Проверить правильность выставленных связей и on_delete событий
class Transaction(models.Model):
    id = models.CharField(max_length=10)
<<<<<<< HEAD
    auction = models.OneToOneField(Auction, on_delete=models.SET_NULL)
=======
    auction = models.OneToOneField(Auction, on_delete=models.SET_NULL, foreign_key)
>>>>>>> 56e1310e552f60ca550d0e429e122e4b740026b5
