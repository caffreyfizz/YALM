from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/list_prof/<type_list>')
def index(type_list):
    list_of_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('training.html', type_list=type_list, profs=list_of_prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')