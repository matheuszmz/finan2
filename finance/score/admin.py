from django.contrib import admin
from .models import Account, Accountable, Category, Buy, Score


# Register your models here.
admin.site.register(Account)
admin.site.register(Accountable)
admin.site.register(Category)
admin.site.register(Buy)
admin.site.register(Score)
