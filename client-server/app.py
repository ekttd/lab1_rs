"""Simple Flask client-server application."""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Process get-request."""
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    """Process post-request."""
    amount = request.form.get('amount')
    amount_int = int(amount)
    if amount_int > 0 and amount_int < 10:
        response = 'котов: ' + amount
    else:
        response = 'неверно заполнено поле'
        amount_int = 0
    return render_template("index.html", message=response,
                           amount_response=amount_int)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
