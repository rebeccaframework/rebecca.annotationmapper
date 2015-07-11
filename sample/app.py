import waitress
from zope.interface import Interface
from pyramid.config import Configurator
from rebecca.annotationmapper.annotations import FromMatchDict


class FromService(object):
    def __init__(self, iface):
        self.iface = iface

    def __call__(self, name):
        def annotate(request):
            return request.find_service(self.iface, name=name)
        return annotate


class Greeter(object):
    def __init__(self, message):
        self.message = message

    def greet(self, name):
        return "{message}, {name}".format(message=self.message, name=name)


class IGreeter(Interface):
    def greet(name):
        """ greeting to name """


def index(context, request, name: FromMatchDict, greeter: FromService(IGreeter)):
    # request.response.text = "Hello, {name}".format(name=name)
    request.response.text = greeter.greet(name)
    return request.response


def main():
    config = Configurator()
    config.include('pyramid_services')
    config.include('rebecca.annotationmapper')
    config.add_route("hello", "/hello/{name}")
    config.add_view(index, route_name="hello")
    config.register_service(Greeter("Hello Greeter"), IGreeter, name="greeter")
    app = config.make_wsgi_app()
    waitress.serve(app)

if __name__ == '__main__':
    main()