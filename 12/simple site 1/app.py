from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form_page():
  page_content = """
    <h2> Форма поиска </h2>
    <form action='/search'>
    <input type='text' name='s'>
    <input type='submit' value='Найти'> 
    </form>
    """
  return page_content


@app.route('/search')
def search_page():
  s = request.args['s']
  return f'Вы ввели слово {s}'

app.run()