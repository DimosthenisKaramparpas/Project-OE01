from flask import Flask
from flask import render_template
app = Flask(__name__)
name="Katerina"
repliess={"Uno":0, "Due":0, "Tre":1, "Quatro":0}
score=0
@app.route('/')
def quiz():
    return render_template('main_page.html', user_name=name, replies=repliess.keys(), answer=score)
