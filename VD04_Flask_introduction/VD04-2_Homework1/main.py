from datetime import datetime

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index_page():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Текущая дата и время: {current_time}'

if __name__ == '__main__':
    app.run()