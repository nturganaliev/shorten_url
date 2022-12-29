# Обрезка ссылок с помощью bit.ly



Файл shorten_url.py берет с командной строки любую ссылку и с помощью [API bit.ly](https://dev.bitly.com/)
возвращает укороченную ссылку. Если ссылка является уже укороченной,
то возвращает количество переходов по ссылке.
Если хотите быстро проверить как работает код, можно перейти в [repl.it](https://replit.com/@NurlanTurganali/shortenurl#main.py)


### Как установить?


Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, м.б. конфликт с Python2)
для установки зависимостей:
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


### Цель проекта


Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
