from webtest import TestApp
from service.controllers.application_controller import app


def test_get_menu():
    test_app = TestApp(app)
    res = test_app.get('/', status=200)
    assert res.body == b'[{"id": 42, "name": "Spam & Eggs", "price": 15.0}]'


def test_get_menu_item():
    test_app = TestApp(app)
    res = test_app.get('/42/', status=200)
    assert res.body == b'{"id": 42, "name": "Spam & Eggs", "price": 15.0}'


def test_get_menu_item_not_found():
    test_app = TestApp(app)
    res = test_app.get('/43/', status=404)
    assert res.body == b'{"error": 404}'
    assert res.status_code == 404
