from django.contrib import admin
from .models import UniwareMaster, UniwareDimension, Inbound
# Register your models here.
@admin.register(UniwareMaster)
class UniwareMasterAdmin(admin.ModelAdmin):
 list_display=['uniware', 'brand', 'headcat', 'subcat','productpic']

@admin.register(UniwareDimension)
class UniwareDimensionAdmin(admin.ModelAdmin):
 list_display=['uniware', 'length', 'width', 'height']

@admin.register(Inbound)
class InboundAdmin(admin.ModelAdmin):
 list_display=['uniware', 'quantity', 'price']

