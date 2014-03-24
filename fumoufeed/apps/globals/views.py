from django.views.generic.base import TemplateView


from conf import settings


class IndexView(TemplateView):

    template_name = "globals/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        context['FACEBOOK_APP_ID'] = settings.FACEBOOK_APP_ID
        return context
