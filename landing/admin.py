from django.contrib import admin
from .models import Newuser

# Register your models here.
@admin.register(Newuser)
class useradmin(admin.ModelAdmin):
    list_display= ('username', 'first_name', 'last_name', 'profilepic','email', 'address','password')
