from django.db import models
from user.models import User 
from product.models import Product 

# Review Model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 

    SCORE_CHOICES = [
        ('very_good','Very Good'),
        ('good','Good'),
        ('average','Average'),
        ('bad','Bad'),
        ('very_bad','Very Bad')
    ]
    score = models.CharField(max_length=100, choices=SCORE_CHOICES) 
    comment = models.TextField(null = True, blank=True)

    def __str__(self):
        return f'Review of {self.product.name} by {self.user.username}'