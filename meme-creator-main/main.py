#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')
        textTop = request.form.get("textTop")
        textBottom = request.form.get("textBottom")
        selected_color = request.form.get("selected_color")
        text_top_y = request.form.get("text_top_y")
        text_bottom_y = request.form.get("text_top_y")

        
        

        # Задание №2.Получаем текст
        

        # Задание №3. Получаем расположение текста
       

        # Задание №3. Получаем цвет текста
        

        return render_template('index.html', 
                               # отображаем выбранное изображение
                               selected_image=selected_image,
                               selected_color=selected_color, 

                               # Задание №2. Отображаем текст
                               textTop=textTop,
                               textBottom=textBottom,
                               text_top_y=text_top_y,
                               text_bottom_y=text_bottom_y 

                
                               

                               # Задание №3. Отображаем цвет 
                               
                               
                               #Задание №3. Отоброжаем расположение текста

                             )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
