import json

from config import BOOKMARKS_PATH


class Bookmarks:

    def __init__(self, path=BOOKMARKS_PATH):
        self.path = path

    def get_bookmarks(self):
        """Возращает все закладки"""
        with open(self.path, "r", encoding="utf-8") as file:
            file = json.load(file)
        return file

    def add_bookmark(self, post_id):
        """ Добавляет закладку"""
        get_bookmark = self.get_bookmarks()
        if post_id in get_bookmark or not post_id:
            return
        get_bookmark.append(post_id)
        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(get_bookmark, file, ensure_ascii=False, indent=2)

    def del_bookmark(self, post_id):
        """ Удаляет закладку"""
        get_bookmark = self.get_bookmarks()
        if post_id not in get_bookmark or not post_id:
            return
        get_bookmark.remove(post_id)
        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(get_bookmark, file, ensure_ascii=False, indent=2)
