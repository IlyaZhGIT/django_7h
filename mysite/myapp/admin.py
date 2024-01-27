from django.contrib import admin

from .models import Product

# Register your models here.

admin.site.site_header = "My Porsche shop header"
admin.site.site_title = "My Porsche shop title"
admin.site.index_title = "index title"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ("name",)
    list_editable = ("description",)
    actions = ("make_zero",)

    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)
