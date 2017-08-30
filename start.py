from service.controllers.application_controller import app
from wsgiref.simple_server import make_server


if __name__ == '__main__':
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
