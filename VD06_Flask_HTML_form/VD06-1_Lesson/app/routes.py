from datetime import datetime

# render_template: для рендеринга HTML-шаблонов.
# request: для работы с данными HTTP-запросов.
# redirect и url_for: для перенаправления пользователей
# и создания URL по имени функции.
from flask import render_template, request, redirect, url_for

from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # использует метод POST, так как информация будет отправляться.
    # Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if title and content:
            posts.append({'title': title, 'content': content, 'timestamp': timestamp})
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)

