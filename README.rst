====================
Django Admin Uploads
====================

File/media browser for Django admin interface. Designed to insert images and 
files into textareas in the admin interface with a simple GUI interface.

Currently, the following features have been written and are working:

- Django 1.1 support
- TinyMCE support
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

#. Create a forms.py for any model that has a textfield for which you would like to 
		apply either WYMEditor or WYMEditorUpload (with upload image capability)

		from django import forms
		from django.db.models import get_model
		from admin_upload.widgets import WYMEditor, WYMEditorUpload
		from jwa.portfolio.models import Project, Category


		class ProjectAdminModelForm(forms.ModelForm):
		    full_description = forms.CharField(required=False, widget=WYMEditor())
		    brief_description = forms.CharField(required=False, widget=WYMEditor())
		    recent_project_text = forms.CharField(required=False, widget=WYMEditor())
		    notes = forms.CharField(required=False, widget=WYMEditor())

		    class Meta:
		        model = get_model('portfolio', 'project')

		class CategoryAdminModelForm(forms.ModelForm):
		    category_description = forms.CharField(required=False, widget=WYMEditorUpload())

		    class Meta:
		        model = get_model('portfolio', 'category')


TODOs and BUGS
==============
See: http://nothinghere.yet
