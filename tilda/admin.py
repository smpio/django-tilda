from django.contrib import (admin, messages)
from django.utils.translation import gettext_lazy as _

from . import api
from . import models


class TildaPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'synchronized', 'created', )
    list_filter = ('synchronized', 'created', )
    search_fields = ('title', 'id', )
    change_list_template = 'admin/tilda_page_change_list.html'
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

    def add_view(self, request, form_url='', extra_context=None):
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

        return self.changelist_view(request)

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


class PublishedPageAdmin(admin.ModelAdmin):
    list_display = ('tilda_page', 'path', 'is_enabled', 'note')
    list_filter = ('is_enabled', )
    search_fields = ('path', )


admin.site.register(models.TildaPage, TildaPageAdmin)
admin.site.register(models.PublishedPage, PublishedPageAdmin)
