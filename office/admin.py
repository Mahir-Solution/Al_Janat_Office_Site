from django.contrib import admin
from .models import Office
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','contact','message']

admin.site.register(Office,OfficeAdmin)
# Register your models here.
