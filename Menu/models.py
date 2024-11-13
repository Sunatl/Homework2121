from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    
    class Meta:
        default_permissions = ('add', 'change', 'delete') 
        permissions = (
            ('view_order', 'Can view order'),
        )

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title}"
