# Интернет сервис "Старый Рим"
## Описание
Веб-приложение для вымышленной сети пиццерий "Старый Рим".
Позвояет обычным пользователям оформлять заказы и просматривать меню, администратратору добавлять новых работников,
а поварам изменять статус заказа
## Запуск проекта Через Docker
Для запуска проекта через docker-compose введите следующие команды 
```commandline
docker-compose build 
```
```commandline
docker-compose run django python manage.py migrate
```
```commandline
docker-compose up
```