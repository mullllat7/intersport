from django.contrib import admin

from applications.clothes.models import Clothes, ClothesImage


class InlineClothesImage(admin.TabularInline):
    model = ClothesImage
    extra = 1
    fields = ['image', ]


class ClothesAdminDisplay(admin.ModelAdmin):
    inlines = [InlineClothesImage, ]


admin.site.register(Clothes, ClothesAdminDisplay)
