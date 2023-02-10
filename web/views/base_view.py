from django.views.generic import TemplateView


class BaseView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = [('/', 'INICIO'),
                           ('quienes-somos', 'QUIENES SOMOS',
                            [('quienes-somos#vision-mision', 'VISION Y MISIÓN'),
                             ('quienes-somos#en-que-creemos', 'EN QUÉ CREEMOS')
                             ]                            
                            ),
                           ('recursos', 'RECURSOS',
                            [('sermones', 'SERMONES'),
                             ('escuela', 'ESCUELA DE FORMACIÓN TEOLÓGICA'),
                             ('confesion', 'CONFESIÓN DE FE'),
                             ('biblia', 'BIBLIA')
                             ]
                            ),
                           ('contacto', 'CONTACTO'),
                           ('eventos', 'EVENTOS'),
                           ('en-vivo', 'EN VIVO'),
                           ('ofrendas', 'OFRENDAS'),
                           ('registro', 'REGISTRO')
                           ]
        return context

