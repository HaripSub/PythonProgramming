from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greet.html', name=name)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
