import datetime
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler


import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_age_company():
    year_start = datetime.datetime(year=1920, month=1, day=1, hour=0)
    current_year = datetime.datetime.now()
    return current_year.year - year_start.year


age_company = get_age_company()
excel_data_df = pd.read_excel('wine3.xlsx', sheet_name='Лист1', keep_default_na=False).to_dict(orient='records')

wine_by_categories = collections.defaultdict(list)
for wine in excel_data_df:
    wine_by_categories[wine['Категория']].append(wine)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    years=age_company,
    wines=wine_by_categories
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
