from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd
import collections


def sort_dict(dict, key_search):
    result = collections.defaultdict(list)
    for item in dict:
        result[item[key_search]].append({'Название': item['Название'], 'Сорт': item['Сорт'], 'Цена': item['Цена'], 'Картинка': item['Картинка'], 'Акция': item['Акция']})
    return result


def get_age_company():
    year_start = datetime.datetime(year=1920, month=1, day=1, hour=0)
    current_year = datetime.datetime.now()
    return current_year.year - year_start.year


age_company = get_age_company()
excel_data_df = pd.read_excel('wine3.xlsx', sheet_name='Лист1', keep_default_na=False).to_dict(orient='records')

sort_data = sort_dict(excel_data_df, 'Категория')

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    years=age_company,
    wines=sort_data
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
