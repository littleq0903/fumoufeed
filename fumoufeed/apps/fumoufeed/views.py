# Create your views here.
from apps.fumoufeed.models import *
from django.views.generic import View
from django.http import HttpResponse
import re
from django.views.decorators.csrf import csrf_exempt

def JsonResponse(data, status=200):
    import json
    data = json.dumps(data)
    return HttpResponse(data, content_type="Content-type: application/json", status=status)


class PeopleApi(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PeopleApi, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        fuid = self.request.path.split('/')[-1]
        people = People.objects.get(fuid=fuid)
        return JsonResponse({'fuid': people.fuid, 'title': people.title})

    def post(self, *args, **kwargs):
        fuid = self.request.REQUEST.get('fuid')
        title = self.request.REQUEST.get('title')
        name = self.request.REQUEST.get('name')
        people = People(fuid=fuid, title=title, name=name)
        people.save()

        return JsonResponse({'success': True})


    def put( self, *args, **kwargs):
        fuid = self.request.path.split('/')[-1]
        title = self.request.REQUEST.get('title')
        name = self.request.REQUEST.get('name')
        people = People.objects.get(fuid=fuid)
        people.title = title
        people.name = name
        people.save()
        
        return JsonResponse({'success': True})


class PostApi(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PostApi, self).dispatch(*args, **kwargs)

    def post( self, *args, **kwargs):
        fuid = self.request.REQUEST.get('fuid')
        fpid = self.request.REQUEST.get('fpid')
        
        people = People.objects.get(fuid=fuid)
    
        try:
            post = Post.objects.get(fpid=fpid)
        except:
            post = Post(fpid=fpid, author=people)
        post.save()

        return JsonResponse({'success': True})

    def delete( self, *args, **kwargs):
        fpid = self.request.path.split('/')[-1]
        post = Post.objects.get(fpid=fpid)
        post.live = False
        post.save()
        return JsonResponse({'success': True})

    @classmethod
    def list(request, *args, **kwargs):
        ps = Post.objects.filter(live=True).order_by('priority', 'create_time')
        data = ps.values('author__fuid', 'fpid', 'author__title', 'author__name')

        return JsonResponse(list(data))

