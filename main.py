from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    quotes = []
    for _ in range(5):  # Делаем пять запросов
        response = requests.get('https://api.quotable.io/random')
        if response.status_code == 200:
            quote_data = response.json()
            quotes.append({'content': quote_data['content'], 'author': quote_data['author']})
        else:
            quotes.append({'content': "Ошибка при загрузке цитаты", 'author': ""})

    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)