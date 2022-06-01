from os import path

import data as data

from views import app
import pytest
from classes.data_classes import DataPosts

dp = DataPosts()

@pytest.fixture()
def test_client():
    data_posts = DataPosts(path)
    return data_posts

class TestApi:

    def test_status_code_all_post(self, test_client):
        # response = test_client('/api/posts/', follow_redirects=True)
        """ Возвращает список"""
        all_posts = dp.get_posts_all()
        assert all_posts.status_code == 200, "Статус код (/api/posts) не верный"
        # assert type(all_posts) == list, "Это не список!"

    # def test_element_key(self):
    #     """Тест название ключей и количества имен"""
    #     posts_keys_names = {"poster_name", "poster_avatar",
    #                         "pic", "content", "views_count",
    #                         "likes_count", "pk"}
    #     resp = app.test_client().get('/api/posts/', follow_redirects=True)
    #     item = resp.json[0]  # <<< Вот тут ключевое отличие!
    #     assert len(resp.json.keys()) == len(posts_keys_names), "Ошибка в кол-ве ключей"
    #     assert set(resp.json.keys()) == posts_keys_names, "Ошибка в названии ключей!"

    # def test_api_one_post(self):
    #     resp = app.test_client().get('/api/posts/1', follow_redirects=True)
    #     assert resp.status_code == 200, "Статус код (/api/posts/1) не верный"
    #     assert type(resp.json) == dict, "Это не словарь!"
