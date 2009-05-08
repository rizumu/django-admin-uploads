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

#. Add the following line to the Admin class on any model you would like to 
	 have uploads available
   Media():
	     js = ('/static/upload_media/jquery.js', '/static/upload_media/model.js')

Configuration
=============

The admin uploads app has one setting that needs to be set in `settings.py`:

#. Required: Set the path to the parent folder of upload_media. In addition
	 to MEDIA_URL also have a plugins folder:

   * UPLOAD_MEDIA_URL = MEDIA_URL + 'plugins/'


TODOs and BUGS
==============
See: http://nothinghere.yet
