from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from service.repositories.menu_repository import MenuRepository
import json


@view_config(renderer='json')
def get_menu(request):
    menu = MenuRepository.get()
    menu_dict = [menu_item.__dict__ for menu_item in menu]
    menu_json = json.dumps(menu_dict)
    response = Response(menu_json)
    response.content_type = 'application/json'
    return response


@view_config(renderer='json')
def get_menu_item(request):
    menu_item_id = request.matchdict['menu_item_id']
    if int(menu_item_id) == 42:
        menu = MenuRepository.get_item(menu_item_id)
        menu_json = json.dumps(menu.__dict__)
        response = Response(menu_json)
        response.content_type = 'application/json'
        return response
    else:
        response =  Response(json.dumps({'error': 404}))
        response.status_int = 404
        response.content_type = 'application/json'
        return response


def create_configuration():
    config = Configurator()
    config.add_route('menu', '/')
    config.add_route('menu_item', '/{menu_item_id}/')
    config.add_view(get_menu, route_name='menu')
    config.add_view(get_menu_item, route_name='menu_item')
    return config


app = create_configuration().make_wsgi_app()
