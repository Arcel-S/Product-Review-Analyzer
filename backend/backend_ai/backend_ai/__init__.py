from pyramid.config import Configurator
from pyramid.events import NewRequest

# Fungsi Manual CORS
def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        })
    event.request.add_response_callback(cors_headers)

def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        
        # Pasang CORS
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)
        config.add_route('cors_options', '/{catch_all:.*}', request_method='OPTIONS')
        config.add_view(lambda r: '', route_name='cors_options', renderer='string')

        config.scan()
    return config.make_wsgi_app()