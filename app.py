from re import DEBUG

from flask import Flask, render_template

#https://www.youtube.com/watch?v=yBDHkveJUf4


app = Flask(__name__)

FILE_SOURCE = [
    {'id': '1',
     'company': 'IDEAL',
     'start_line': '5',
     'product_column': '3',
     'base_price_column': '9',
     'list_price_column': '12',
     'replacement_cost_column': '24',
     'last_forign_cost_column': '24'},
     {'id': '2',
     'company': 'Hoffman Canada',
     'start_line': '5',
     'product_column': '3',
     'base_price_column': '9',
     'list_price_column': '12',
     'replacement_cost_column': '24',
     'last_forign_cost_column': '24'}
    ]

@app.route('/')
def hello_world():

    return render_template('home.html', list_of_sources=FILE_SOURCE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
