from django.contrib import admin
from .models import Item

# Register your models here.
#방법1
# admin.site.register(Item)

# 방법2
# class ItemAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Item, ItemAdmin)

# 방법3
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']
    list_filter = ['is_publish']
    search_fields = ['name'] #검색  UI

    def short_desc(self, item):
        return item.desc[:20]