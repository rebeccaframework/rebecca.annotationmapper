===============================
rebecca.annotationmapper
===============================

``rebecca.annotationmapper`` is viewmapper for pyramid web application.
That processes annotations of view arguments.

INSTALL
===============================

::

  $ pip install rebecca.annotationmapper

``rebecca.annotationmapper`` provides include fook.

USAGE
===============================

::

  config.include('rebecca.annotationmapper')

Annotate arguments using ``rebecca.annotationmapper.annotations``

::

   def hello(context, request, nane: FromMatchDict):
       request.response.text = "Hello, {name}".format(name=name)
       return request.response

   config.add_route("hello", "/hello/{name}")
   config.add_view(hello, route_name="hello")

The argument ``name`` annotated by ``FromMatchDict`` is
given value from ``request.matchdict['name']`` by ``rebecca.annotationmapper.AnnotationViewMapper``.

For example, you access 'http://localhost/hello/aodag' and you get message 'Hello, aodag'.

Annotations
===============================

FromMatchDict
-------------------------------

FromParam
-------------------------------

FromSession
-------------------------------

FromHeader
-------------------------------

FromAttr
---------------------------------