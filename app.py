import os

import morepath
import waitress

from repoze.profile.profiler import AccumulatingProfileMiddleware

class App(morepath.App):
    pass

class Hello(object):
    pass

hello = Hello()

@App.path(model=Hello, path='')
def hello_model():
    return hello

@App.view(model=Hello)
def hello_view(self, request):
    return "hello"

def make_app():
    c = morepath.setup()
    c.scan()
    c.commit()
    return App()

def serve_waitress(app):
    print('serving using waitress')
    waitress.serve(app, host='0.0.0.0', port='8080')

def serve(app):
    serve_waitress(app)

the_app = make_app()

if __name__ == '__main__':
    if not 'NO_PROFILE' in os.environ:
        the_app = AccumulatingProfileMiddleware(
            the_app,
#            cachegrind_filename='cachegrind.out',
            log_filename='wsgi.prof',
            discard_first_request=True,
            flush_at_shutdown=True,
            path='/__profile__'
            )
    serve(the_app)
