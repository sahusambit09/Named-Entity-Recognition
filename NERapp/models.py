from django.db import models
class MedicineDetails(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    sku_id = models.CharField(max_length=255, blank=True, null=True)
    product_id = models.CharField(max_length=255 , blank=True, null=False)
    sku_name = models.CharField(max_length=255, blank=True, null=False)
    price = models.CharField(max_length=255, blank=True, null=False)
    manufacturer_name = models.CharField(max_length=255, blank=True, null=False)
    salt_name = models.CharField(max_length=255, blank=True, null=False)
    drug_form = models.CharField(max_length=255, blank=True, null=False)
    Pack_size = models.CharField(max_length=255, blank=True, null=False)
    strength = models.CharField(max_length=255 , blank=True, null=False)
    product_banned_flag = models.CharField(max_length=255, blank=True, null=False)
    unit = models.CharField(max_length=255, blank=True, null=False)
    price_per_unit = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return str(self.sku_name)


