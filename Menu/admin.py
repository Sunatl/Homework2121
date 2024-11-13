from django.contrib import admin
from .models import *


@admin.register(Book)
class Bo(admin.ModelAdmin):
    list_display = ("title","author")
    search_fields = ("title","author")
    list_filter = ("title","author")
    
@admin.register(Borrow)
class Be(admin.ModelAdmin):
    list_display = ["book","borrow_date"]
    search_fields = ["book__title","borrow_date"]
    list_filter = ["book","borrow_date"]
    
        