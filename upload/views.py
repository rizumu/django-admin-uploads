from models import FileUpload
from django.shortcuts import render_to_response
from django.template import RequestContext

def all(request):
    files = FileUpload.objects.all().order_by('-upload_date')
    return render_to_response('upload/base.html', {'files': files, 'textarea_id': request.GET['textarea']}, context_instance=RequestContext(request))

def images(request):
    files = FileUpload.objects.filter(content_type = 'image').order_by('-upload_date')
    return render_to_response('upload/base.html', {'files': files, 'textarea_id': request.GET['textarea']}, context_instance=RequestContext(request))
    
def files(request):
    not_files = ['video', 'image']
    files = FileUpload.objects.exclude(content_type__in = not_files).order_by('-upload_date')
    return render_to_response('upload/base.html', {'files': files, 'textarea_id': request.GET['textarea']}, context_instance=RequestContext(request))