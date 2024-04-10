from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/training/<prof>')
def index(prof):
    proffession = prof.lower()
    return render_template('training.html', prof=proffession)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')