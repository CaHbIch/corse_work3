import os.path

from flask import Flask, render_template, request, redirect
# from api.api import api
from classes.bookmarks_class import Bookmarks
from classes.comments_classes import CommentPost
from config import DATA_PATH, COMMAENTS_PATH, BOOKMARKS_PATH
from classes.data_classes import DataPosts

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

data_posts = DataPosts(DATA_PATH)
comment_post = CommentPost(COMMAENTS_PATH)
bookmarks = Bookmarks(BOOKMARKS_PATH)

# app.register_blueprint(api)


@app.route('/')
def post():
    """Реализует ленту до 5 постов"""
    return render_template("index.html",
                           all_post=data_posts.get_posts_all(),
                           count_comment=len(bookmarks.get_bookmarks()))


@app.route("/post/<int:post_id>/")
def view_post(post_id):
    """ Реализует просмотр поста"""
    post = data_posts.tag_replace(post_id)
    return render_template("post.html", posts=comment_post.get_comments_by_post_id(post_id),
                           count_comment=len(comment_post.get_comments_by_post_id(post_id)),
                           post=post)


@app.route("/search/")
def page_search():
    """ Реализует поиск по совпадениям в словах в постах"""
    word = request.args.get('word')
    posts = data_posts.search_for_posts(word)
    return render_template("search.html",
                           posts=posts,
                           count_post=len(posts),
                           word=word)


@app.route("/users/<username>/")
def page_user(username):
    """ Реализует вывод по пользователю """
    return render_template("user-feed.html", user_posts=data_posts.get_posts_by_user(username))


@app.route("/tag/<tagname>")
def page_tag(tagname):
    """ Реализует переход по тегам"""
    tagnames = data_posts.tag_names(tagname)
    return render_template("tag.html", tagnames=tagnames)


@app.route("/bookmarks/add/<post_id>/")
def bookmarks_add_post(post_id):
    """ Добавляет посты в закладки."""
    post_bookmarks = data_posts.get_post_by_pk(post_id)
    bookmarks.add_bookmark(post_bookmarks)
    return redirect("/", code=302)


@app.route('/bookmarks/delete/<int:post_id>')
def page_bookmarks_delete(post_id):
    """  Удаляет посты из закладок"""
    posts = data_posts.get_post_by_pk(post_id)
    bookmarks.del_bookmark(posts)
    return redirect("/", code=302)


@app.route("/bookmarks/")
def all_bookmark():
    bookmark = bookmarks.get_bookmarks()
    """Выводит все закладки"""
    return render_template("bookmarks.html", add_bookmarks=bookmark)


@app.errorhandler(404)
def pageNotFound(error):
    """ Обработчик запросов к несуществующим страницам"""
    return render_template('page404.html', title="Страница не найдена", error=error)


@app.errorhandler(500)
def pageNotFound(error):
    """ Обработчик ошибок, возникших на стороне сервера"""
    return render_template('page500.html', title="Сервер не отвечает", error=error)


if __name__ == "__main__":
    app.run(debug=True)
