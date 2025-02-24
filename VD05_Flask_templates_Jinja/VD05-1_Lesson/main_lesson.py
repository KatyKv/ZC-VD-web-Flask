from lib2to3.fixes.fix_input import context

from flask import Flask, render_template

app = Flask(__name__)


# Jinja - шаблонизатор. Используется для генерации HTML, XML и
# других текстовых форматов из шаблонов.


# Начнем с переменных шаблонизатора.
# Например, функция render_template кроме самого шаблона, т.е.
# файла html может на вход принять множество аргументов,
# и эти аргументы функция будет пробрасывать в заданный шаблон.
# Создадим копию функции films с другим адресом, а сам
# html-документ не меняем.
# А в films.html вместо заголовка запишем переменную caption
# {{...}} - вывод (print). А в функции её передаём.
# Теперь при запуске главной и /shablon увидим разный title,
# а переменная link задает разный текст на кнопках


@app.route('/films/')
def films():
    return render_template('films.html', caption='Фильмы', link='Wiki')


# Но много переменных неудобно задавать в параметрах функции,
# удобнее распаковать словарь

@app.route('/films1/')
def films1():
    context = {
        'caption': 'Кино',
        'link': 'Перейти в Википедию'
    }
# Распаковка словаря через **
    return render_template('films.html', **context)


# Работа с условиями в jinja
# В файле shablon.html используем if:
# {% if %}
# ...
# {% elif %}
# ...
# {% endif %}

# И цикл for:
# {% for user in users %}
#         {{user}}
#         {% endfor %}
@app.route('/if-for')
def ifs():
    context = {
        'number': 6,
        'users': ['Anna', 'Den', 'Maks'],
        'poem': ['Константин Симонов',
                'Жди меня, и я вернусь…',
                '',
                'Жди меня, и я вернусь.',
                'Только очень жди,',
                'Жди, когда наводят грусть',
                'Желтые дожди,',
                'Жди, когда снега метут,',
                'Жди, когда жара,',
                'Жди, когда других не ждут,',
                'Позабыв вчера.',
                'Жди, когда из дальних мест',
                'Писем не придет,',
                'Жди, когда уж надоест',
                'Всем, кто вместе ждет.'
                 ]
    }

    return render_template('shablon.html', **context)

# Для использования шаблона html добавляем в нем блоки, которые
# необходимо будет заполнить разной информацией:
#       {% block title %}
#
#       {% endblock %}
# Создали шаблон films_template.html. В нем шапка и футер.

@app.route('/')
def mainpage():
    context = {
        'link': 'Перейти в Википедию'
    }
    return render_template('films.html', **context)


@app.route('/heroes/')
def heroes():
    return render_template('heroes.html')

if __name__ == '__main__':
    app.run()