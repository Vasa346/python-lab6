# Лабораторная работа №6. Модули и пакеты

## Вариант 8

### GUI фреймворк: Tkinter
### Задание: Рецепты (Вок, Бургер, Пицца)

## Условия задач
Создать пакет `recipes` с модулями `wok.py`, `burger.py`, `pizza.py`. Реализовать GUI на Tkinter для расчёта стоимости и калорийности рецептов. Добавить возможность сохранения результатов в Excel. Сохранять результаты расчётов в БД PostgreSQL, запущенной в Docker.

## Описание проделанной работы
- Создан репозиторий `python-lab6` на GitHub.
- Склонирован в `D:\Xlam\python\python-lab6`.
- Создан пакет `recipes` с тремя модулями (Вок, Бургер, Пицца).
- Реализован графический интерфейс на Tkinter (`main.py`).
- Добавлена возможность сохранения отчёта в Excel с помощью `openpyxl`.
- Установлен Docker Desktop и запущен контейнер с PostgreSQL.
- Создана таблица `calculations` и модуль `db_manager.py` для сохранения результатов в БД.
- Интегрировано сохранение в БД при каждом расчёте в GUI.
- Оформлен отчёт.

## Скриншоты результатов

1. Графический интерфейс на Tkinter с расчётом рецепта
<img width="497" height="412" alt="изображение" src="https://github.com/user-attachments/assets/88f9b950-cc6c-4c49-9efa-643565ffb3ab" />

2. Отчёт в Excel с результатами расчёта
<img width="478" height="443" alt="изображение" src="https://github.com/user-attachments/assets/ddf11c02-0069-4e6f-85a9-a39d065b5dc7" />

3. Контейнер PostgreSQL в Docker Desktop
<img width="954" height="487" alt="изображение" src="https://github.com/user-attachments/assets/135767d0-b299-465f-9c78-cb87b5236bf3" />

4. Проверка сохранённых данных в БД
<img width="954" height="124" alt="изображение" src="https://github.com/user-attachments/assets/7ea3ad9a-4c6b-4abe-97c9-1f70e10354f2" />

5. История коммитов (git log --oneline -5)
<img width="946" height="129" alt="изображение" src="https://github.com/user-attachments/assets/21e612be-11fb-40a4-a1cd-9b091f7b8f8f" />

## Ссылки на используемые материалы
- [Официальная документация Python](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [openpyxl Documentation](https://openpyxl.readthedocs.io/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
