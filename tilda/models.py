# coding: utf-8
import json
import os
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class TildaPage(models.Model):

    id = models.CharField(
        _(u'Page id'),
        max_length=50,
        primary_key=True,
        unique=True
    )

    title = models.CharField(
        _(u'Title'),
        max_length=500
    )

    html = models.TextField(
        _(u'HTML'),
        blank=True
    )

    images = models.TextField(
        _(u'Images'),
        blank=True
    )

    css = models.TextField(
        _(u'CSS'),
        blank=True
    )

    js = models.TextField(
        _(u'JS'),
        blank=True
    )

    synchronized = models.DateTimeField(
        _(u'Synchronized time'),
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        _(u'Created'),
        auto_now_add=True
    )

    class Meta:
        ordering = ('title', )
        verbose_name = _(u'page')
        verbose_name_plural = _(u'Tilda Pages')

    def get_images_list(self):
        if not self.images:
            return []
        data = json.loads(self.images)
        if settings.TILDA_MEDIA_IMAGES:
            return list(map(lambda r: os.path.join('/media/tilda/images', r['to']), data))
        else:
            return list(map(lambda r: r['from'], data))

    def get_css_list(self):
        if not self.css:
            return []
        data = json.loads(self.css)
        if settings.TILDA_MEDIA_CSS:
            return list(map(lambda r: os.path.join('/media/tilda/css', r['to']), data))
        else:
            return list(map(lambda r: r['from'], data))

    def get_js_list(self):
        if not self.js:
            return []
        data = json.loads(self.js)
        if settings.TILDA_MEDIA_JS:
            return list(map(lambda r: os.path.join('/media/tilda/js', r['to']), data))
        else:
            return list(map(lambda r: r['from'], data))

    def _path_images_list(self):
        if self.images:
            return [
                os.path.join(settings.TILDA_MEDIA_IMAGES, r['to'])
                for r in eval(self.images)
            ]
        return []

    def _path_css_list(self):
        if self.css:
            return [
                os.path.join(settings.TILDA_MEDIA_CSS, r['to'])
                for r in eval(self.css)
            ]
        return []

    def _path_js_list(self):
        if self.js:
            return [
                os.path.join(settings.TILDA_MEDIA_JS, r['to'])
                for r in eval(self.js)
            ]
        return []

    def __unicode__(self):
        return '#%s %s' % (self.id, self.title)

    def __str__(self):
        return '#%s %s' % (self.id, self.title)


class PublishedPage(models.Model):
    tilda_page = models.ForeignKey(TildaPage, verbose_name=_(u'Tilda page'),
                                   on_delete=models.CASCADE, null=False)
    path = models.CharField(_(u'Public path to page'), help_text=_(u'E.g.: /my-landing/mobile/'),
                            max_length=200, null=False)
    is_enabled = models.BooleanField(_(u'Is published'),
                                     default=True)
    note = models.TextField(_(u'Note'),
                            null=True, blank=True)

    class Meta:
        unique_together = ('path', 'is_enabled')
