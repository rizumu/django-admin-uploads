from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import mimetypes

class FileUpload(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to="media/content")
    title = models.CharField(core=True, maxlength=100)
    description = models.CharField(blank=True, maxlength=200)
    content_type = models.CharField(editable=False, maxlength=100)
    sub_type = models.CharField(editable=False, maxlength=100)

    class Admin:
        list_display = ('title','upload_date','upload', 'mime_type')
        js = ['%s/upload_media/jquery.js' % (settings.MEDIA_URL), '%s/upload_media/photo-edit.js' % (settings.MEDIA_URL)]
    
    class Meta:
        ordering = ['upload_date', 'title']

    def __unicode__(self):
        return self.title
    
    def mime_type(self):
        return '%s/%s' % (self.content_type, self.sub_type)
    
    def type_slug(self):
        return slugify(self.sub_type)
    
    def is_image(self):
        if self.content_type == 'image':
            return True
        else:
            return False
    
    def get_absolute_url(self):
        return '%s/%s' % (settings.MEDIA_URL, self.upload)

    def save(self):
        file_path = '%s%s' % (settings.MEDIA_ROOT, self.upload)
        (mime_type, encoding) = mimetypes.guess_type(file_path)
        try:
            [self.content_type, self.sub_type] = mime_type.split('/')
        except:
            self.content_type = 'text'
            self.sub_type = 'plain'
        super(FileUpload, self).save()
