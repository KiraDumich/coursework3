from flask import Flask, render_template, request
from utils import get_posts_all, get_comments_by_post_id, get_comments_count, search_for_posts
from utils import get_posts_by_user


app = Flask(__name__)


@app.route('/')
def index_page():
    """Главная страница"""
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def post_page(postid):
    """Станица с постом по id"""
    comments = get_comments_by_post_id(postid)
    posts = get_posts_all()
    count_comments = get_comments_count(postid)
    return render_template('post.html', posts=posts, comments=comments, pk=postid, count_comments=count_comments)


@app.route('/search/')
def search_page():
    """Страница поиска"""
    query = request.args["s"]
    found_posts = search_for_posts(query)
    count_posts = len(found_posts)
    print(found_posts)
    return render_template('search.html', count_posts=count_posts, posts=found_posts, query=query)


@app.route('/user/<username>')
def user_page(username):
    """Страница с постами конкретного пользователя"""
    posts_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user, username=username)


@app.errorhandler(404)
def page_not_found(error):
    """Страница с ошибкой 404"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(error):
    """Страница с ошибкой 500"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(port=5001)

