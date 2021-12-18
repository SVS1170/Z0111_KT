from aiohttp import web


def mnk(x1=1, y1=2, x2=2, y2=4, x3=3, y3=9, x4=4, y4=11, x5=5, y5=13, x6=6, y6=19,x7=7 , y7=25, x8=8, y8=26, x9=9, y9=30):
    n = 9
    xs = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
    ys = y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9
    xys = (x1 * y1) + (x2 * y2) + (x3 * y3) + (x4 * y4) + (x5 * y5) + (x6 * y6) + (x7 * y7) + (x8 * y8) + (x9 * y9)
    a = (n * xys - xs * ys) / (n * xys - xs**2)
    b = (ys * xys - xs * xys) / (n * xys - xs**2)
    data1 = "Коэффициэнты a и b уравнния y = a * x + b"
    data2 = "a = " + str(a) + " b = " + str(b)
    data3 = "Уравнение прямой: "
    data4 = "y = " + str(a) + " * x + " + str(b)
    return data1, data2, data3, data4


async def handle(request: web.Request) -> web.StreamResponse:
    css = """<style>
         body {
        background-color: #87ceeb
        }
        h1 {
          color: White;
          text-align: center
        } 
        h2 {
          color: black;
          text-align: center
        } 
        </style>
        </head>
        <body>"""
    text = f'''<!DOCTYPE html>
    <html>
    {css}
    <h1>"Выберите задачу"<h1/>
    <form action="/mnk" target="_blank">
       <button>Расчет mnk</button>
    </form>

    </html>'''

    return web.Response(text=text, content_type='text/html')


async def wmnk(request: web.Request) -> web.StreamResponse:
    css = """<style>
    body {
      background-color: white;
    }
    h1 {
      color: red;
      text-align: center
    } 
    h2 {
      color: black;
      text-align: center
    } 
    </style>
    </head>
    <body>"""
    text = f'''<!DOCTYPE html>
<html>
<form action="/mnk" method="POST">
   Пожалуйста, введите исходные данные:<br>
   <input type="text" name="d1" value="" placeholder="x1" required><br>
   <input type="text" name="d2" value="" placeholder="y1" required><br>
   <input type="text" name="d3" value="" placeholder="x2" required><br>
   <input type="text" name="d4" value="" placeholder="y2" required><br>
   <input type="text" name="d5" value="" placeholder="x3" required><br>
   <input type="text" name="d6" value="" placeholder="y3" required><br>
   <input type="text" name="d7" value="" placeholder="x4" required><br>
   <input type="text" name="d8" value="" placeholder="y4" required><br>
   <input type="text" name="d9" value="" placeholder="x5" required><br>
   <input type="text" name="d10" value="" placeholder="y5" required><br>
   <input type="text" name="d11" value="" placeholder="x6" required><br>
   <input type="text" name="d12" value="" placeholder="y6" required><br>
   <input type="text" name="d13" value="" placeholder="x7" required><br>
   <input type="text" name="d14" value="" placeholder="y7" required><br>
   <input type="text" name="d15" value="" placeholder="x8" required><br>
   <input type="text" name="d16" value="" placeholder="y8" required><br>
   <input type="text" name="d17" value="" placeholder="x9" required><br>
   <input type="text" name="d18" value="" placeholder="y9" required><br>
   
   <input type="submit" value="Вычислить">
</form>
</html>'''

    return web.Response(text=text, content_type='text/html')


async def wmnk1(request) -> web.StreamResponse:
    a = await request.post()
    # print(a)

    x1 = int(a["d1"])
    y1 = int(a["d2"])
    x2 = int(a["d3"])
    y2 = int(a["d4"])
    x3 = int(a["d5"])
    y3 = int(a["d6"])
    x4 = int(a["d7"])
    y4 = int(a["d8"])
    x5 = int(a["d9"])
    y5 = int(a["d10"])
    x6 = int(a["d11"])
    y6 = int(a["d12"])
    x7 = int(a["d13"])
    y7 = int(a["d14"])
    x8 = int(a["d15"])
    y8 = int(a["d16"])
    x9 = int(a["d17"])
    y9 = int(a["d18"])

    print(x1)
    data = mnk(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6,x7 , y7, x8, y8, x9, y9)
    css = """<style>
    body {
      background-color: white;
    }
    h1 {
      color: red;
      text-align: center
    } 
    h2 {
      color: black;
      text-align: center
    } 
    </style>
    </head>
    <body>"""
    text = f'''<!DOCTYPE html>
<html>
<h1>{data}<h1/>
<form action="/" target="_blank">
   <button>Переход по ссылке</button>
</form>
</html>'''

    return web.Response(text=text, content_type='text/html')


app = web.Application()
app.add_routes(
    [web.get("/", handle), web.get("/mnk", wmnk),
     web.post("/mnk", wmnk1),
     web.get("/{name}", handle)])
