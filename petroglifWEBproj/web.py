from jinja2 import Environment, FileSystemLoader
# Template
from flask import Flask, render_template, redirect
# url_for, jsonify, render_template_string
import os
import json
# import requests
# import folium 
# import folium.plugins as plugins
# from folium import IFrame
# from matplotlib import image
# from matplotlib import pyplot as plt
# import base64
# pixplot_url = os.environ.get('PIX_URL', 'http://localhost:4000')
flask_url = os.environ.get('FL_URL', 'http://localhost:5000')

fileloader = FileSystemLoader('templates')
env = Environment(loader = fileloader)
TEMPLATE_DIR = os.path.abspath('templates') #задаем пути для запуска файлов во Flask
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def homepage():
    return render_template("base.html") #добавить в скобки , result = result

@app.route("/pixplot")
def graph():
    result = redirect(PIX_URL)
    # result = redirect(f'http://127.0.0.1:4000')
    return result

@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/ch")
def ch():
    return render_template("chykotka.html")

@app.route("/books")
def books():
    return render_template("library.html")

@app.route("/aboutus")
def about_us():
    return render_template("present.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")