import pytest
from app import create_app, db


@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config.from_object('app.config.DevelopmentConfig')
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client
        db.drop_all()
