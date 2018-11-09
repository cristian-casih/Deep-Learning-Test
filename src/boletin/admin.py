from django.contrib import admin

# Register your models here.
from .models import Registrado
from .forms import RegModelForm

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestramp"]
    form = RegModelForm
    #list_display_links=["nombre"]
    list_filter = ["timestramp"]
    list_editable = ["nombre"]
    seach_fields = ["email", "nombre"]
    #class Meta:

        #model = Registrado

admin.site.register(Registrado, AdminRegistrado)
