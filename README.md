# Обрезка ссылок с помощью bit.ly


Файл shorten_url.py берет с командной строки любую ссылку и с помощью [API bit.ly](https://dev.bitly.com/)
возвращает укороченную ссылку, как показано ниже. 

```bash
(.venv) user@host:shorten_url$ python main.py https://replit.com/@NurlanTurganali/shortenurl#main.py
Битлинк bit.ly/3FRajAt

```

Если ссылка является уже укороченной,
то возвращает количество переходов по ссылке.</br>
Например:

```bash
(.venv) user@host:shorten_url$ python main.py https://bit.ly/3FRajAt
По вашей ссылке прошли 8 раз(а)
```


Для быстрой проверки кода, можно перейти в [repl.it](https://replit.com/@NurlanTurganali/shortenurl#main.py)


### Требования к окружению

Операционная система (ОС): `Ubuntu 22.04`, должен работать и в других ОС без проблем.</br>
Версия интерпретатора: `Python 3.10.6`, думаю поддерживается с большинством версий Python3.</br>
Версия пакет менеджера: `pip3 22.3.1`</br>
В проекте нужно создать файл .env, в котором будет храниться переменное окружения BITLY_TOKEN.</br>
Функция load_dotenv() из модуля dotenv, нужно для чтения файла .env и для настройки переменного окружения.
Внимание! Модуль dotenv нужно установить, он не входит в список модулей по умолчанию. Про установку нужных модулей, написано ниже.


### Как установить?

Python3 должен быть уже установлен.</br>
Затем используйте `pip` (или `pip3`, м.б. конфликт с Python2)
для установки зависимостей наберите команду в терминале:
```bash
pip install -r requirements.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.


### Использование

Из терминала (командной строки) набираете следующую команду:

```bash

python3 main.py "url_to_shorten"

```
<<<<<<< HEAD
=======

Если набранный в терминале url не является уже укороченным, получаете вывод похожий ниже:


```bash
(.venv) user@host:shorten_url$ python main.py https://replit.com/@NurlanTurganali/shortenurl#main.py
Битлинк bit.ly/3FRajAt

```

В противном случае, количество переходов через ссылку:

```bash
(.venv) user@host:shorten_url$ python main.py https://bit.ly/3FRajAt
По вашей ссылке прошли 8 раз(а)
```
>>>>>>> 4d58ccee8e5ea6d38f721fada89c36e88496c751


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
