from flask import Flask, render_template
import bs4 as bs
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
    sauce = urllib.request.urlopen('https://www.nasdaq.com/symbol/ndaq').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    
    change= float(soup.find('div', id='qwidget_netchange').text)
   
    if change > 0:
        down = False
    else:
        down = True

    return render_template("index.html", down=down)

