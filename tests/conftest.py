import pytest
import views


# создаем фикстуру для тестирования всех вьюшек
@pytest.fixture()
def test_client():
    app = views.app
    return app.test_client()
