from django.contrib import admin
from techcart import models
  
class StateAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
admin.site.register(models.UserProfile,StateAdmin)
admin.site.register(models.reviews)
admin.site.register(models.product)
admin.site.register(models.catiegorys)
admin.site.register(models.order)
admin.site.register(models.favorite)
admin.site.register(models.cart)
