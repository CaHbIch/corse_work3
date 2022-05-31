import json

from config import DATA_PATH


class DataPosts:

    def __init__(self, path=DATA_PATH):
        self.path = path

    def get_posts_all(self):
        """Возвращает все посты"""
        with open(self.path, "r", encoding="UTF-8") as file:
            file = json.load(file)
            return file

    def get_posts_by_user(self, poster_name):
        """ Возвращает посты определенного пользователя по имени"""
        search_posts = []
        for post in self.get_posts_all():
            if poster_name in post["poster_name"]:
                search_posts.append(post)
        return search_posts

    def search_for_posts(self, content):
        """ Возвращает список постов по ключевому слову"""
        search_content = []
        for get_content in self.get_posts_all():
            if str(content).lower() in get_content["content"].lower().split(' '):
                search_content.append(get_content)
        return search_content

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору"""
        for post in self.get_posts_all():
            if int(pk) == post["pk"]:
                return post

