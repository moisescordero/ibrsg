from django.conf import settings
from . import BaseView
import os

class Index(BaseView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = os.listdir(os.path.join(settings.STATICFILES_DIRS[0],
                                                    'img',
                                                    'index'
                                                    )
                                       )
        context['images'] = sorted([os.path.join('img', 'index', img) for img in images
                                    if img.split('.')[-1] in ['jpg', 'jpeg', 'png']])
        return context
