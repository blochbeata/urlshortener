from django.contrib import admin


from shortener.models import Link


class LinksAdmin(admin.ModelAdmin):
    list_display = ('short_link', 'httpurl')

admin.site.register(Link, LinksAdmin)
