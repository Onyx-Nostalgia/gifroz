from app import create_app


def test_app_creation():
    app = create_app()
    assert app is not None
    assert app.config['DEBUG'] is True


def test_app_with_config_override():
    app = create_app(config_name_override='testing')
    assert app.config['TESTING'] is True
    assert app.config['DEBUG'] is True
