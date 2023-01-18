from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def main_page():
  return f'Главная страница'



@app.route('/search')
def search_page():
  s = request.args['s']
  return f'Вы ввели слово {s}'


@app.route('/filter')
def filter_page():
  from_value = request.args['from']
  to_value = request.args['to']
  return f'Ищем в диапазоне от {from_value} до {to_value}'

@app.route('/get-data')
def data_page():

  start_with = request.args.get("startwith")
  end_with = request.args.get("endwith")
  return f'Начинаем с {start_with} Заканчиваем на {end_with}'


app.run()