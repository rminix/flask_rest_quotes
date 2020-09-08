import os
from app import create_app

app = create_app()


def test_testing_config():
    app.config.from_object('app.config.DevelopmentConfig')
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']