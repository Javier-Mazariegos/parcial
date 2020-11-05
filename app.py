from flask import Flask, url_for, request,redirect
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    my_data =[]
    if request.method == 'POST':
        palabra = request.form['palabra']
        reverse = palabra[::-1]
        tamaño = len(palabra)
        for i in "aeiou":
            vowel = palabra.lower().count(i)
        for i2 in "bdfghjklmnñpqrstvxyz":
            consonants = palabra.lower().count(i2)
        mayuscula = palabra.upper()
        minuscula = palabra.lower()
        updown = ""
        for i3 in range(len(palabra)):
            if(i3%2 == 0):
                updown += palabra[i3].upper()
            else:
                updown += palabra[i3].lower()
        naive = ""
        naive= palabra.replace("a","@")
        naive= palabra.replace("e", "3")
        naive= palabra.replace("i", "!")
        naive= palabra.replace("o", "0")
        naive= palabra.replace("u", ")")
        my_data = [palabra,reverse,tamaño,vowel,consonants,mayuscula,minuscula,updown,naive]
        return redirect(url_for('index'))
    template = env.get_template('index.html')
    image_file = url_for('static',  filename ='avatar.jpg')
    return template.render(my_data=my_data,image_file= image_file)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)