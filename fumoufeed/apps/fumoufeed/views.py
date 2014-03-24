# Create your views here.
from apps.fumoufeed.models import *
from django.views.generic import View

class PeopleApi(View):
    def get(self, fuid):
        pass

    def post(self):
        pass

    def put(self, fuid):
        pass


class PostApi(View):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self, fpid):
        pass

    @classmethod
    def list(request, *args, **kwargs):
        pass

