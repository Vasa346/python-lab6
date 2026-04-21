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
*(Сюда вставить скриншоты через GitHub)*

## Ссылки на используемые материалы
- [Официальная документация Python](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [openpyxl Documentation](https://openpyxl.readthedocs.io/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)