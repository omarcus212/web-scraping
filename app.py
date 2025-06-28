from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def pegar_manchetes():
    url = "https://g1.globo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    manchetes = soup.find_all('a', class_='feed-post-link')

    lista = []
    for m in manchetes:
        titulo = m.text.strip()
        link = m['href']
        lista.append({'titulo': titulo, 'link': link})

    return lista

@app.route('/')
def home():
    manchetes = pegar_manchetes()
    return render_template('index.html', manchetes=manchetes)

if __name__ == "__main__":
    app.run(debug=True)
