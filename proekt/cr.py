from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return "Позорищеское учение"


@app.route('/index')
def index():
    return 'Не будьте такими как я. Не будьте позорищами'


@app.route('/promotion')
def promotion():
    promotion_list = [
        "не забывайте зарядку от компа в станкине",
        "комп сдох",
        "и я делаю этот проект чтобы вас предуберечь"
    ]
    return '<br>'.join(promotion_list)


@app.route('/image_pozor')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Позорище</title>
                  </head>
                  <body>
                    <h1>Да, я позорище!</h1>
                    <img src="{url_for('static', filename='img/pozor.png')}" alt="здесь должна была быть картинка, но не нашлась">
                    <p>Но я этим горжусь</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
