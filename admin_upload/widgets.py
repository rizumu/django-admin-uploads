from admin_upload.models import FileUpload
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class WYMEditor(forms.Textarea):
    class Media:
        js = (
            settings.MEDIA_URL + 'admin_upload_media/jquery.js',
            settings.MEDIA_URL + 'admin_upload_media/wymeditor/jquery.wymeditor.pack.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WYMEditor, self).render(name, value, attrs)
        id = 'id_' + name
        wymeditor = mark_safe(u'''<script type="text/javascript">
            $('#%s').wymeditor({
                updateSelector: '.submit-row input[type=submit]',
                updateEvent: 'click',
                lang: '%s',
            });
            </script>''' % (id, self.language))
        return rendered + wymeditor

class WYMEditorUpload(forms.Textarea):
    class Media:
        js = (
            settings.MEDIA_URL + 'admin_upload_media/jquery.js',
            settings.MEDIA_URL + 'admin_upload_media/wymeditor/jquery.wymeditor.pack.js',
            settings.MEDIA_URL + 'admin_upload_media/upload.js'
        )
        css = {
           'all': (settings.MEDIA_URL + 'admin_upload_media/upload.css',)
        }

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditorUpload, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WYMEditorUpload, self).render(name, value, attrs)
        id = 'id_' + name
        wymeditor = mark_safe(u'''<script type="text/javascript">
            $('#%s').wymeditor({
                updateSelector: '.submit-row input[type=submit]',
                updateEvent: 'click',
                lang: '%s',
            });
            </script>''' % (id, self.language))
        files = FileUpload.objects.all().order_by('-upload_date')
        admin_upload_html = render_to_string('admin_upload/base.html', 
            {'files': files, 'textarea_id': id, 'MEDIA_URL': settings.MEDIA_URL })
        return rendered + wymeditor + admin_upload_html
