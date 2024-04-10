from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/distribution')
def index():
    peoples = [
            'Ридли Скотт',
            "Энди Уир",
            "Марк Уотни",
            "Венката Капур",
            "Тедди Сандерс",
            "Шон Бин"
        ]
    return render_template('training.html', profs=peoples)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')