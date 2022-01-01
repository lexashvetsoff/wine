import datetime
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv


def get_company_age():
    year_founded_winery = 1920
    current_year = datetime.datetime.now()
    return current_year.year - year_founded_winery


def main():
    load_dotenv()
    age_company = get_company_age()
    wines = pd.read_excel(os.getenv('PATH_FILE'), sheet_name='Лист1', keep_default_na=False).to_dict(orient='records')

    wine_by_categories = collections.defaultdict(list)
    for wine in wines:
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


if __name__ == '__main__':
    main()