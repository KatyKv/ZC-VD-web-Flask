# Файл __init__.py создается Пайчармом автоматически при
# создании пакета Python.
# Это файл настроек Фласка

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'


from app import routes




