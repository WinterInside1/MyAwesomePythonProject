from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True, related_name='watched')

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.URLField(max_length=200, blank=True)
    category = models.CharField(max_length=32, blank = True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'User: {self.user} Item: {self.title} Price: {self.price} Date listed: {self.date}'


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Listing: {self.listing} Price: {self.price}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=256)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Date: {self.date} Comment: {self.comment} Listing: {self.listing}'
