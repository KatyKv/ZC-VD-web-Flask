from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html', current_page='home')

@app.route('/about/')
def about_page():
    return render_template('about.html', current_page='about')



if __name__ == '__main__':
    app.run()