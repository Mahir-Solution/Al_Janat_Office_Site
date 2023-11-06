from django.contrib import admin
from .models import Registration
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','fname','study','course','registration_d','contact','address']

admin.site.register(Registration,RegistrationAdmin)
# Register your models here.
