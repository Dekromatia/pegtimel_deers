from jinja2 import Template
import json

with open('csvjson.json', encoding = "UTF-8") as f:
    my_table = json.load(f)

# print(my_table)
# from flask import Flask, render_template, url_for, jsonify

# my_table = [
#   {
#     "name": "Леванова Е. С., Мухарева А. Н., Бове Л. Л. ОБСЛЕДОВАНИЕ НАСКАЛЬНЫХ ИЗОБРАЖЕНИЙ НА РЕКЕ ПЕГТЫМЕЛЬ (ЧУКОТКА) В 2021 ГОДУ: РЕЗУЛЬТАТЫ МОНИТОРИНГА И СОСТОЯНИЕ СОХРАННОСТИ //Ученые записки музея-заповедника «Томская Писаница». – 2022. – №. 15. – С. 59-70.",
#     "url": "https://cyberleninka.ru/article/n/obsledovanie-naskalnyh-izobrazheniy-na-reke-pegtymel-chukotka-v-2021-godu-rezultaty-monitoringa-i-sostoyanie-sohrannosti"
#   },
#   {
#     "name": "Леванова Е. С. и др. Исследование петроглифов на реке Пегтымель в 2022 году.",
#     "url": "http://paeas.ru/x/ru/2022/2022_0606-0612.pdf"
#   },
#   {
#     "name": "Христофорова В. С. Изобразительные и технологические традиции нанесения петроглифов (на примере петроглифов р. Пегтымель) //Научно-практическая реализация творческого потенциала молодежи. – 2021. – С. 263-270.",
#     "url": "https://www.elibrary.ru/item.asp?id=47987672"
#   }]

#шаблон для генерации списка ( html на основе Boostrap )

html = ''' {% macro books_list(list_of_book) -%}
  <ul>
  {% for u in list_of_book -%}
    <li> 
    <a href="{{u.url}}" class="list-group-item">{{u.name}}</a>
    </li>
  {%- endfor %}
  </ul>
{%- endmacro %}

{{ books_list(books)}}
'''
tm = Template(html)

msg = tm.render(books = my_table)

print(msg)