from django.contrib import admin
from .models import MedicineDetails


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id','sku_id', 'product_id', 'sku_name','price',
                    'manufacturer_name','salt_name',
                    'drug_form','Pack_size','strength',
                    'product_banned_flag','unit','price_per_unit')


admin.site.register(MedicineDetails, MedicineAdmin)
