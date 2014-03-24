# Create your views here.
from apps.fumoufeed.models import *
from django.views.generic import View
from django.http import HttpResponse

def JsonResponse(data, status=200):
    import json
    data = json.dumps(data)
    return HttpResponse(data, content_type="Content-type: application/json", status=status)


class PeopleApi(View):
    def get(self, fuid):
        people = People.objects.get(fuid=fuid)
        return JsonResponse({'fuid': people.fuid, 'title': people.title})

    def post(self):
        fuid = self.request.REQUEST.get('fuid')
        title = self.request.REQUEST.get('title')
        people = People(fuid=fuid, title=title)
        people.save()

        return JsonResponse({'success': True})


    def put(self, fuid):
        title = self.request.REQUEST.get('title')
        people = People.objects.get(fuid=fuid)
        people.title = title
        people.save()
        
        return JsonResponse({'success': True})


class PostApi(View):
    def post(self):
        fuid = self.request.REQUEST.get('fuid')
        fpid = self.request.REQUEST.get('fpid')
        
        people = People.objects.get(fuid=fuid)
    
        try:
            post = Post.objects.get(fpid=fpid)
        except:
            post = Post(fpid=fpid, author=people)
        post.save()

        return JsonResponse({'success': True})

    def delete(self, fpid):
        post = Post.objects.get(feed_id=fpid)
        post.live = False
        post.save()
        return JsonResponse({'success': True})

    @classmethod
    def list(request, *args, **kwargs):
        ps = Post.objects.filter(live=True).order_by('priority', 'create_time')
        data = ps.values('author__fuid', 'fpid', 'author__title')

        return JsonResponse(list(data))

