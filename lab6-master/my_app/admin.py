from django.contrib import admin
from.models import *
# Register your models here.

class CountrysAdmin(admin.ModelAdmin):
    fields = ('cnt_name', 'hotel_name',)
    list_filter = ('cnt_name', 'hotel_name')
    list_display = ('cnt_name', 'hotel_name')
    search_fields = ('cnt_name', 'hotel_name')
    list_per_page = 10


class NomersAdmin(admin.ModelAdmin):
    fields = ('id_nomera', 'kod_nomera', 'hotell')
    list_filter = ('id_nomera', 'kod_nomera', 'hotell')
    list_display = ('id_nomera', 'kod_nomera')
    search_fields = ('id_nomera', 'kod_nomera', 'hotell')
    list_per_page = 10

class HotelsAdmin(admin.ModelAdmin):
    fields = ('id_hotel', 'hotel_name','photo')
    list_filter = ('id_hotel', 'hotel_name','photo')
    list_display = ('id_hotel', 'hotel_name','photo')
    search_fields = ('id_hotel', 'hotel_name','photo')
    list_per_page = 10


class RegistrsAdmin(admin.ModelAdmin):
    fields = ('code_registr', 'nomer_registr')
    list_filter = ('code_registr', 'nomer_registr')
    list_display = ('code_registr', 'nomer_registr')
    search_fields = ('code_registr', 'nomer_registr')
    list_per_page = 10


class HumansAdmin(admin.ModelAdmin):
    fields = ('fio', 'registr_code')
    list_filter = ('fio', ('registr_code', admin.RelatedOnlyFieldListFilter))
    list_display = ('fio', 'registr_code')
    search_fields = ('fio', 'registr_code')
    list_per_page = 10


admin.site.register(Hotel)
admin.site.register(Country, CountrysAdmin)
admin.site.register(Human)
#admin.site.register(Human, HumansAdmin)
admin.site.register(Nomer)
admin.site.register(Registr, RegistrsAdmin)