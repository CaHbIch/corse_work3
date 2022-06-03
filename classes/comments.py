from flask import json
from config import COMMAENTS_PATH


class CommentPost:

    def __init__(self, path=COMMAENTS_PATH):
        self.path = path

    def get_comments(self):
        """Возвращает ВСЕ комментарии к постам"""
        with open(self.path, "r", encoding="UTF-8") as file:
            file = json.load(file)
        return file

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        comments = self.get_comments()
        search_comment = []
        for comment in comments:
            if int(post_id) == comment["post_id"]:
                search_comment.append(comment)
        return search_comment

