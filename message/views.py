from pusher import Pusher


from django.shortcuts import render

from pusher import Pusher
from django.views.generic import TemplateView
# instantiate pusher
pusher = Pusher(app_id=u'1483810', key=u'3a498a7100788cc8aacb', secret=u'8ce2fd82c540313b2ed4', cluster=u'sa1')


class IndexView(TemplateView):
    template_name = 'index.html'


    def get(self, request, *args, **kwargs):
        print(request.GET)
        if 'inicia' in request.GET:
            print('entrou aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )
            pusher_client.trigger('painel', 'inicia', {'message': 'iniciou'})
        
        if 'pausa' in request.GET:
            print('pausou aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )
            pusher_client.trigger('painel', 'pausa', {'message': 'pausou'})
               
        if 'parar' in request.GET:
            print('pausou aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )
            pusher_client.trigger('painel', 'parar', {'message': 'parou'})

        if 'um' in request.GET:
            print('um aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )
            pusher_client.trigger('painel', 'um', {'message': 'um'})
        
        if 'dois' in request.GET:
            print('dois aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )
            pusher_client.trigger('painel', 'dois', {'message': 'dois'})
        
        if 'tres' in request.GET:
            print('tres aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )   
            pusher_client.trigger('painel', 'tres', {'message': 'tres'})
        
        if 'quatro' in request.GET:
            print('quatro aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )

            pusher_client.trigger('painel', 'quatro', {'message': 'quatro'})

        if 'cinco' in request.GET:
            print('cinco aqui')            
            pusher_client = Pusher(
            app_id='1483810',
            key='3a498a7100788cc8aacb',
            secret='8ce2fd82c540313b2ed4',
            cluster='sa1',
            ssl=True
            )

            pusher_client.trigger('painel', 'cinco', {'message': 'cinco'})

        return super(IndexView,self).get(request, *args, **kwargs)



class UsuarioView(TemplateView):
    template_name = 'usuario.html'