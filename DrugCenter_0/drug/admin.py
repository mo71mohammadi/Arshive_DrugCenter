from django.contrib import admin
from drug import models



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'BrandName')


admin.site.register(models.Generic)
admin.site.register(models.Molecule)
admin.site.register(models.Doc_inter)
admin.site.register(models.Interaction)
admin.site.register(models.Bime)
admin.site.register(models.Prescription)
admin.site.register(models.Physician)
admin.site.register(models.Patient)
