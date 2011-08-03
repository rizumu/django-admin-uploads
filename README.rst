====================
Django Admin Uploads
====================

File/media browser for Django admin interface. Designed to insert
images and files into textareas in the admin interface with a simple
GUI interface.

Currently, the following features have been written and are working:

- Django 1.3 support
- WYMeditor 0.5 rc2 bundled
- TinyMCE support (probably but not sure, still need to test)

Installation
============

#. Add the `admin_upload` directory to your Python path.

#. Add `admin_upload` to your `INSTALLED_APPS` setting so Django can
find the template files and staticfiles associated with the Admin
Uploads application.

#. Create an empty uploads folder in your MEDIA_ROOT where images will
 be saved.

Configuration
=============

See Janis Leidel's blogpost for more comprehensive instructions on the
WYMeditor integration process in Django:
http://jannisleidel.com/2008/11/wysiwym-editor-widget-django-admin-interface/


#. Create a admin.py for any model that has a textfield for which you
would like to apply either WYMEditor or WYMEditorUpload (with upload
image capability). Then set the form in your Admin class, and register the model
with the admin::

    from django import forms
    from django.db.models import get_model

    from django.contrib import admin

    from admin_upload.widgets import WYMEditor, WYMEditorUpload

    from my_news_app.models import NewsEntry


    class NewsEntryAdminModelForm(forms.ModelForm):
        body = forms.CharField(required=False, widget=WYMEditorUpload())
        notes = forms.CharField(required=False, widget=WYMEditor())

        class Meta:
            model = NewsEntry


    class NewsEntryAdmin(admin.ModelAdmin):
        form = NewsEntryAdminModelForm
        list_display = ( "title", "status", "on_sites")
        prepopulated_fields = {"slug": ("title",)}


    admin.site.register(NewsEntry, NewsEntryAdmin)


TODOs and BUGS (out of date)
============================
#. Test Cross Browser
#. Test TinyMCE (I've only yet tested WYMeditor)
#. Add setting to choose if Flickr, YouTube, options available
#. on delete, remove deleted file/image from DOM
#. get request variable in widgets.py
#. use image icon on wymeditor & TinyMCEfor uploading? (easier way to use default WYM settings)
#. Add way to manage WYMeditor & TinyMCE options

BUG
#. Doesn't insert when multiple WYMeditors on same admin.
