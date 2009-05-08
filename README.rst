====================
Django Admin Uploads
====================

File/media browser for Django admin interface. Designed to insert images and 
files into textareas in the admin interface with a simple GUI interface.

Currently, the following features have been written and are working:

- Django 1.1 support
- TinyMCE support (probably but not sure, still need to test)
- WYMeditor support

Installation
============

#. Add the `admin_upload` directory to your Python path.

#. Add `admin_upload` to your `INSTALLED_APPS` setting so Django can find the
   template files associated with the Admin Uploads.
   
   Alternatively, add the path to the admin uploads templates
   (``'path/to/django_admin_uploads/templates'`` to your ``TEMPLATE_DIRS`` setting.)

#. Create uploads folder in your MEDIA_ROOT

Configuration
=============

See Janis Leidel's blogpost for more comprehensive instructions on the
WYMeditor integration process in Django:
http://jannisleidel.com/2008/11/wysiwym-editor-widget-django-admin-interface/ 


#. Create a forms.py for any model that has a textfield for which you would like to apply either WYMEditor or WYMEditorUpload (with upload image capability)


		from django import forms
		from django.db.models import get_model
		from admin_upload.widgets import WYMEditor, WYMEditorUpload
		from jwa.news.models import NewsEntry

		class NewsEntryAdminModelForm(forms.ModelForm):
		    body = forms.CharField(required=False, widget=WYMEditorUpload())
		    notes = forms.CharField(required=False, widget=WYMEditor())

		    class Meta:
		        model = get_model('news', 'newsentry')


#. In your admin.py, import your form class, and register the model with the admin using get_model to avoid extra imports.


		from django.contrib import admin
		from django.db.models import get_model
		from myapp.news.models import NewsEntry
		from myapp.news.forms import NewsEntryAdminModelForm


		class NewsEntryAdmin(admin.ModelAdmin):
		    form = NewsEntryAdminModelForm
		    list_display = ( 'title', 'status', 'on_sites')
		    prepopulated_fields = {'slug': ('title',)}

		admin.site.register(get_model('news', 'newsentry'), NewsEntryAdmin)



TODOs and BUGS
==============
#. Test Cross Browser
#. Test TinyMCE (I've only yet tested WYMeditor)
#. Add setting to choose if Flickr, YouTube, options available
#. on delete, remove deleted file/image from DOM
#. get request variable in widgets.py
#. use image icon on wymeditor & TinyMCEfor uploading? (easier way to use default WYM settings)
#. Add way to manage WYMeditor & TinyMCE options

BUG
#. Doen't insert when multiple WYMeditors on same admin.
