# Crawler
#### Реализован класс Crawler:
+ Чтобы запустить краулер в консоли, запустите crawler.py 
и в качестве первого аргумента укажите начальный URL,
 в качестве второго аргумента максимально допустимое
  число сохраненных страниц (необязательный параметр, по умолчанию 10).
+ Конструктор принимает два аргумента: 
    + Начальный URL
    + Максимально допустимое количество сохраненных страниц
+ Метод crawl() запускает процесс обработки html страниц
+ Метод reboot() возвращает краулер к первоначальному состоянию до первого запуска.
#### Работа с сетью реализована в файле networking.py
#### Сохранение html страниц реализовано в save.py
#### Генерация хэша в hash_work.py