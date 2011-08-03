from django.contrib import admin

from admin_upload.models import FileUpload


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ("title", "upload_date", "upload", "mime_type")


admin.site.register(FileUpload, FileUploadAdmin)
