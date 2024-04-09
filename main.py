from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route('/carousel')
def greeting():
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title>Пейзажи Марса</title>
</head>

<body>
    <h1 style='text-align:center'>👽Не фейк! На Марсе нашли инопланетян!👽</h1>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" src="/static/img/image1.png" alt="Первый слайд">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="/static/img/image2.png" alt="Второй слайд">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="/static/img/image3.png" alt="Третий слайд">
        </div>
      </div>
    </div>
</body>

</html>"""
 
 
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
