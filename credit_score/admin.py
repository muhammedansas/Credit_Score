from django.contrib import admin
from .models import CreditScore,Question,UserResponse

# Register your models here.

admin.site.register(CreditScore),
admin.site.register(Question),
admin.site.register(UserResponse),
