# Обязательное требование Flask! Структура!!!
# В проекте обязательно должны быть категории:
# - temlates - для файлов html (шаблоны страниц)
# - static - для изображений и css файлов

from flask import Flask, render_template

# Переменная app - экземпляр класса Flask, куда передаётся переменная
# __name__ - спец. переменная, которая содержит в себе имя текущего модуля.
# Она помогает фреймоворку находить нужные ресурсы, шаблоны, статические файлы и т.д
app = Flask(__name__)

# Вся более подробная и тестовая информация ниже.
# Здесь сейчас создаем две функции для запуска двух страниц html
@app.route('/')
def films():
    return render_template('films.html')

@app.route('/heroes/')
def heroes():
    return render_template('heroes.html')

# Декоратор - для маршрута (url) к странице. То есть, чтобы функция работала
# с конкретной веб-страницей.
# '/' - главная.
@app.route('/test')
# Вторым декоратором добавим возможность прописать переменную в адрес.
# Переменная пишется в треугольных скобках.
@app.route('/<password>/')
def hello(password=''):
    if password == '1234':
        return 'Доступ разрешен'
    else:
        return 'Доступ запрещен'

# Сейчас на эту страницу сможем заходить по адресу, где к главной странице
# в адресной строке дописано: new/ (можно этот адрес писать даже по-русски)
@app.route('/new/')
def new():
    return 'New page'

# Множественное декорирование: прописываем 3 адреса, но по всем этим
# трем адресам откроется одна страница
@app.route('/newpage/')
@app.route('/новаястраница/')
@app.route('/multinewpage/')
def multi_new():
    return "New page. It's a one page for 3 addresses"

# Запуск html прямо из файла .py
@app.route('/myhtml/')
def start_html():
    html = '''
    <h1> Тестовый запуск локального сервера </h1>
    <p> Этот код html написан прямо в файле main_lesson.py </p>
    '''
    return html

# Запуск html через специальную функцию render_template,
# которая запускает уже созданный html
@app.route('/indexhtml/')
def start_indexhtml():
    return render_template('VD04_index.html')






# Если скрипт запущен напрямую (не импортирован), то запускаем весь
# наш локальный сервер.
if __name__ == '__main__':
    app.run()