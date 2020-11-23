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

# App settings for development
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/', methods=('GET', 'POST'))
def home():
    form = NameInput()
    print('test')
    if form.validate_on_submit():
        saveNames(form)
        return redirect(url_for('success'))
    return render_template(
        'index.html',
        form=form
    )

@app.route('/compare', methods=('Get', 'POST'))
def success():
    try:
        return (f"{NamesToCompare.first1} {NamesToCompare.last1} vs. {NamesToCompare.first2} {NamesToCompare.last2}")
    except:
        return redirect(url_for('home'))

def saveNames(form):
    global NamesToCompare
    NamesToCompare = Name(form.firstname1, form.lastname1, form.firstname2, form.lastname2)
    print('Names saved')

class Name:
    def __init__(self, fn1, ln1, fn2, ln2):
        self.first1 = fn1._value()
        self.last1 = ln1._value()
        self.first2 = fn2._value()
        self.last2 = ln2._value()

if __name__ == '__main__':
    global NamesToCompare
    app.run()