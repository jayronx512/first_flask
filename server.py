# from flask import Flask
# app = Flask(__name__)

# @app.route("/") # Revisit decorators if you unclear of this syntax
# def index():
#     return '<h1>Why so easy</h1>'

# if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
#    app.run()

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return '<h1>Why so easy</h1>'


# @app.route("/another")
# def show():
#     return '<h1>Yo</h1>'

# if __name__ == '__main__':
#     app.run()

# from flask import Flask
# app = Flask(__name__)

# @app.route('/user/<username>')
# def show(username):
#     return f"Hi {username[5]}"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def index(name):
    name = name.upper()
    return render_template('index.html', name=name) # by default looks for index.html inside a templates folder in the same directory as this script.

if __name__ == '__main__':
    app.run()
