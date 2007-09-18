from models import FileUpload
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
import urllib, urlparse, datetime

def all(request):
    if not request.user.is_staff:
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    files = FileUpload.objects.all().order_by('-upload_date')
    return render_to_response('upload/base.html', {'files': files, 'textarea_id': request.GET['textarea']}, context_instance=RequestContext(request))

def images(request):
    if not request.user.is_staff:
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    files = FileUpload.objects.filter(content_type = 'image').order_by('-upload_date')
    return render_to_response('upload/base.html', {'files': files, 'textarea_id': request.GET['textarea']}, context_instance=RequestContext(request))
    
def files(request):
    if not request.user.is_staff:
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    not_files = ['video', 'image']
    files = FileUpload.objects.exclude(content_type__in = not_files).order_by('-upload_date')
    return render_to_response('upload/base.html', {'files': files, 'textarea_id': request.GET['textarea']}, context_instance=RequestContext(request))
    
def youtube(request):
    import elementtree.ElementTree as ET
    user = 'NBC'
    needs_user_setting = True
    gdata_feed = "http://gdata.youtube.com/feeds/videos?author=%s&orderby=updated" % (user,)
    root = ET.parse(urllib.urlopen(gdata_feed)).getroot()
    videos = []
    for e in root.findall('{http://www.w3.org/2005/Atom}entry'):
        video = {}
        video['title'] = e.findtext('{http://www.w3.org/2005/Atom}title')
        date = e.findtext('{http://www.w3.org/2005/Atom}published').split('T')[0]
        video['upload_date'] = date
        media = e.find('{http://search.yahoo.com/mrss/}group')
        video['description'] = media.findtext('{http://search.yahoo.com/mrss/}description')
        video['thumb'] = media.find('{http://search.yahoo.com/mrss/}thumbnail').attrib['url']
        video['url'] = media.find('{http://search.yahoo.com/mrss/}player').attrib['url']
        videos.append(video)
    return render_to_response('upload/youtube.html', {'videos': videos, 'textarea_id': request.GET['textarea'], 'needs_user_setting': needs_user_setting}, context_instance=RequestContext(request))
    
def download(request):
    if not request.user.is_staff:
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    if request.method == 'GET':
        f = FileUpload();
        f.title = request.GET['title'] or 'untitled'
        print f.title
        f.description = request.GET['description']
        print f.description
        url = urllib.unquote(request.GET['photo'])
        file_content = urllib.urlopen(url).read()
        file_name = url.split('/')[-1]
        f.save_upload_file(file_name, file_content)
        print f.upload
        f.save()
        return HttpResponse('%s' % (f.id))