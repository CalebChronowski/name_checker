from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)

from forms import NameInput


app = Flask(__name__)

# This is stupid but quick
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=('GET', 'POST'))
def contact():
    form = NameInput()
    print('test')
    if form.validate_on_submit():
        print('validate')
        return redirect(url_for('success'))
    return render_template(
        'index.html',
        form=form
    )

@app.route('/<firstname1>/<lastname1>/<firstname2>/<lastname2>', methods=('Get', 'POST'))
def success():
    print(f"{firstname1} {lastname1} vs. {firstname2} {lastname2}")

if __name__ == '__main__':
   app.run()