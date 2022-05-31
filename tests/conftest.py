import pytest
import api


# создаем фикстуру для тестирования всех вьюшек
@pytest.fixture()
def test_client():
    app = api.app
    return app.test_client()
