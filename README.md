# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Переменные окружения

- Создайте файл .env
- Пропишите в .env:
```
FILE_PATH=wine.xlsx (или свой путь к файлу)
```

## Запуск

- Скачайте код
- Запустите сайт командой 
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Данные

На вход подаются данные в таблице:

| Категория  | Название            | Сорт            | Цена | Картинка                |  Акция               |
|:----------:|:-------------------:|:---------------:|:----:|:-----------------------:|:--------------------:|
| Белые вина | Белая леди          | Дамский пальчик | 399  |belaya_ledi.png          | Выгодное предложение |
| Напитки    | Коньяк классический |                 | 350  |konyak_klassicheskyi.png |                      |
| Белые вина | Ркацители           | Ркацители       | 499  | rkaciteli.png           |                      |

Формат файла с таблицей должен иметь расширение .xlsx

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
