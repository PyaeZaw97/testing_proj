from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Info


# Register your models here.
admin.site.site_header='Waaneiza Management System'

class InfoAdmin(admin.ModelAdmin):
    list_display=['customer_name','customer_ph','items','price','branch']
    list_filter=['customer_name','customer_ph','items','price','branch']
    search_fields=['customer_name','customer_ph','items','price','branch']
    

admin.site.register(Info,InfoAdmin)