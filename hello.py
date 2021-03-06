from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!!!!!'

@app.route('/new')
def new_page():
    return 'This is another page!'

# Run on Mac
# FLASK_APP=hello.py flask run
# FLASK_APP=twitoff:APP flask shell

# On Windows:
# export FLASK_APP=hello.py (in different terminals may be "set")
# flask run

# if you add this, you can run the flask app as:
# python hello.py
if __name__ == '__main__':
    app.run(debug=True)