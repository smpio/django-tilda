from django.contrib import (admin, messages)
from django.utils.translation import ugettext as _

from . import api
from . import models


class TildaPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'synchronized', 'created', )
    list_filter = ('synchronized', 'created', )
    search_fields = ('title', 'id', )
    readonly_fields = (
        'id',
        'title',
        'html',
        'images',
        'css',
        'js',
        'synchronized',
        'created',
    )

    def has_add_permission(self, request):
        return False

    def fetch_pages(modeladmin, request, queryset):
        if api.api_getpageslist():
            messages.add_message(
                request,
                messages.SUCCESS,
                _(u'Pages successfuly fetched from Tilda')
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                _(u'Nothing fetched. Perharps wrong settings')
            )
    fetch_pages.label = _(u'Fetch pages')

    def synchronize_pages(self, request, queryset):
        for obj in queryset:
            if api.api_getpageexport(obj.id):
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _(u'Page «{}» successfuly synced from Tilda'.format(obj.title))
                )
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    _(u'Something wrong...')
                )
    synchronize_pages.label = _(u'Synchronize')

    actions = ('fetch_pages', 'synchronize_pages')


admin.site.register(models.TildaPage, TildaPageAdmin)
