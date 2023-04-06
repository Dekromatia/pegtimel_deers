#импортируем модули
from jinja2 import Environment, FileSystemLoader, Template
from flask import Flask, render_template, url_for, jsonify, render_template_string
import requests
import os
import folium
import folium.plugins as plugins
from folium import IFrame
from matplotlib import image
from matplotlib import pyplot as plt
import json
import base64

fileloader = FileSystemLoader('templates')

env = Environment(loader = fileloader)

TEMPLATE_DIR = os.path.abspath('templates') #задаем пути для запуска файлов во Flask
STATIC_DIR = os.path.abspath('static')

#загрузка книг из файла
# def get_books():
#     with open('library_utf8.json', encoding = "UTF-8") as f:
#         my_table = json.load(f)
#     return my_table

# a = get_books()
# print(a)

#генерация названий книг на странице сайта macros_html
# def index_lib():
#     books_list = get_books()
#     return render_template('macros_books.html', books = books_list)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def homepage():
    # result = requests.get(REST_URL).json()
    return render_template("base.html") #добавить в скобки , result = result

# @app.route("/aboutus")
# def about_us():
#     #result = requests.get(REST_URL).json()
#     return render_template("page4_present.html.j2")

@app.route("/graph2")
def graph():
#     #result = requests.get(REST_URL).json()
    return render_template("graph.html")

@app.route("/resurch")
def resurch():
#     #result = requests.get(REST_URL).json()
    return render_template("research.html")

@app.route("/ch")
def ch():
#     #result = requests.get(REST_URL).json()
    return render_template("chykotka_img.html")

@app.route("/books")
def books():
    return render_template("library.html")

# @app.route("/lib")
# def get_lib():
#     books_list = get_books()
#     return render_template("macros_books.html", books = books_list)

@app.route("/aboutus")
def about_us():
    #result = requests.get(REST_URL).json()
    return render_template("present.html")

# @app.route("/base2")
# def base():
#     #result = requests.get(REST_URL).json()
#     return render_template("base2.html.j2")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    # app.run(debug=True)

# print (TEMPLATE_DIR)