#импортируем модули
from jinja2 import Environment, FileSystemLoader, Template
from flask import Flask, render_template, url_for, jsonify, render_template_string, redirect
import requests
import os
import json

fileloader = FileSystemLoader('templates')

env = Environment(loader = fileloader)

TEMPLATE_DIR = os.path.abspath('templates') #задаем пути для запуска файлов во Flask
STATIC_DIR = os.path.abspath('static')

with open('macros/csvjson.json', encoding = "UTF-8") as f:
    my_table = json.load(f)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def homepage():
    # result = requests.get(REST_URL).json()
    return render_template("base.html") #добавить в скобки , result = result

# @app.route("/aboutus")
# def about_us():
#     #result = requests.get(REST_URL).json()
#     return render_template("page4_present.html.j2")

@app.route("/graph")
def graph():
    result = redirect(f"http://127.0.0.1:4000")
    return result

@app.route("/research")
def research():
#     #result = requests.get(REST_URL).json()
    return render_template("research.html")

@app.route("/ch")
def ch():
#     #result = requests.get(REST_URL).json()
    return render_template("chykotka.html")

@app.route("/books")
def books():
    return render_template("library.html")

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