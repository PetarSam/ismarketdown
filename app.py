from flask import Flask, render_template
import bs4 as bs
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
    sauce = urllib.request.urlopen('https://www.marketscreener.com/NASDAQ-COMP-4944/').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    result = soup.find('td', id='zbjsfv_pf').text[0]
   
    if result == "-":
        down = True
    else:
        down = False

    return render_template("index.html", down=down)

if __name__ == 'main':
    app.run()