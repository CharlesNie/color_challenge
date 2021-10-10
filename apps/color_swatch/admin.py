from django.contrib import admin
from .models import Color, ColorSpace


class ColorAdmin(admin.ModelAdmin):

    fields = ['name', 'min_value', 'max_value']


class ColorInline(admin.TabularInline):
    model = ColorSpace.colors.through
    extra = 1


class ColorSpaceAdmin(admin.ModelAdmin):

    inlines = [ColorInline]
    exclude = ['colors']


admin.site.register(Color, ColorAdmin)
admin.site.register(ColorSpace, ColorSpaceAdmin)
