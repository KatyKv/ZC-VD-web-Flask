from flask import render_template, request, redirect, url_for

from  app_form import app
from app_form.data_saving import load_data, save_data

users_info = load_data()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        input_name = request.form.get('input_name')
        input_city = request.form.get('input_city')
        input_hobby = request.form.get('input_hobby')
        input_age = request.form.get('input_age')
        
        users_info.append({'name': input_name, 'city': input_city,
                           'hobby': input_hobby, 'age': input_age})
        save_data(users_info)
        return redirect(url_for('index'))
    return render_template('form.html', users_info=users_info)

