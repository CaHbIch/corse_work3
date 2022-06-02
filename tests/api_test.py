from views import app
import pytest

class TestApi:

    def test_status_code_all_post(self):
        response = app.test_client().get('/api/posts/', follow_redirects=True)
        """ Возвращает список"""
        assert response.status_code == 200, "Статус код (/api/posts) не верный"
        assert type(response.json) == list, "Это не список!"
    #
    # def test_element_key(self):
    #     """Тест название ключей и количества имен"""
    #     posts_keys_names = {"poster_name", "poster_avatar",
    #                         "pic", "content", "views_count",
    #                         "likes_count", "pk"}
    #     resp = app.test_client().get('/api/posts/', follow_redirects=True)
    #     assert len(resp.json.keys()) == len(posts_keys_names), "Ошибка в кол-ве ключей"
    #     assert set(resp.json.keys()) == posts_keys_names, "Ошибка в названии ключей!"
    #
    # def test_api_one_post(self):
    #     resp = app.test_client().get('/api/posts/1', follow_redirects=True)
    #     assert resp.status_code == 200, "Статус код (/api/posts/1) не верный"
    #     assert type(resp.json) == dict, "Это не словарь!"
