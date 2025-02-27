from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-nobody-knows-key'

from app_form import routes