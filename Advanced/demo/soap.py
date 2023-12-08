from wsgiref.simple_server import make_server

from spyne import Application, Integer, Iterable, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield "Hello, %s" % name


# Erstelle eine SOAP-Anwendung
soap_app = Application(
    [HelloWorldService],
    "spyne.examples.hello.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# Erstelle ein WSGI-Server, um die SOAP-Anwendung zu hosten
wsgi_app = WsgiApplication(soap_app)

if __name__ == "__main__":
    server = make_server("0.0.0.0", 5000, wsgi_app)
    print("Listening on http://0.0.0.0:5000")
    server.serve_forever()
