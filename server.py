from flask import Flask
import pythonquiz
app = Flask(__name__)

@app.route("/login")
def login():

    pass

@app.route("/start")
def start():
    
    pass

@app.route("/end")
def end():
    pass

@app.route('/q/<id>')
def question(id):
    
    pass
if __name__ == "__main__":
    app.run(debug=True)
