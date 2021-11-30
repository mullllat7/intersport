from django.contrib import admin

from applications.order.models import Order, OrderClothes


class OrderClothesInline(admin.TabularInline):
    model = OrderClothes
    extra = 1
    fields = ('clothes', 'quantity', 'total_cost')


class OrderAdminDisplay(admin.ModelAdmin):
    inlines = [OrderClothesInline, ]


admin.site.register(Order, OrderAdminDisplay)
