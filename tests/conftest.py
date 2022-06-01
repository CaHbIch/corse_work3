import pytest
import views

# создаем фикстуру для тестирования всех вьюшек API
from classes.data_classes import DataPosts


# @pytest.fixture()
# def test_client():
#     app = views.app
#     return app.test_client()
#
#
# @pytest.fixture()
# def test_client():
#     data_posts = DataPosts("./data/data.json")
#     return data_posts
