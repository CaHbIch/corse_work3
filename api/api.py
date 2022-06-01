# import os
#
# from flask import Blueprint, jsonify
# from classes.data_classes import DataPosts
# import logging
# from config import DATA_PATH
#
# data_posts = DataPosts(DATA_PATH)
#
# path = os.path.join("logs", "api.log")
#
# # Логирование
# logger_api = logging.getLogger("api")  # Создаем логгер
# file_handler = logging.FileHandler(path)  # Записываем логи в файл
#
# logger_api.setLevel("INFO")  # Уровень записи в логи
# formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  # В каком формате будет запись
#
# file_handler.setFormatter(formatter_api)  # применяем формат к логам
# logger_api.addHandler(file_handler)  # записываем в журнал
#
# api = Blueprint('api', __name__)
#
#
# @api.route("/api/posts/", methods=["GET"])
# def page_post_form():
#     """возвращает полный список постов в виде JSON-списка"""
#     logger_api.info("запрос всех постов")
#     all_posts = data_posts.get_posts_all()
#     return jsonify(all_posts)
#
#
# @api.route("/api/posts/<int:post_id>", methods=["GET"])
# def page_post_pk(post_id):
#     """возвращает один пост в виде JSON-словаря."""
#     logger_api.info(f"запрос постов по {post_id}")
#     get_post = data_posts.get_post_by_pk(post_id)
#     return jsonify(get_post)
#
#
