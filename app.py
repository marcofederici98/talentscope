from flask import Flask, render_template
import functions

questions = ['Lorem ipsum dolor? (1)', 'Lorem ipsum dolor? (2)']
answers = [['a', 'b', 'c'], ['a', 'b', 'c', 'd']]
n = 1

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', question = questions[n], answers = functions.ans_gen(answers[n]))

if __name__ == '__main__':
    app.run(debug=True)