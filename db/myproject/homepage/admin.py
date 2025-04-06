from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "roll",
        "year",
        "class_name",
    )  
    
   
    search_fields = ("name", "email", "roll", "class_name")
    
    # Add filters in the right sidebar
    list_filter = (   "name",
        "email",
        "roll",
        "year",
        "class_name",)
    

    ordering = ("name",)

admin.site.register(UserInfo, UserInfoAdmin)