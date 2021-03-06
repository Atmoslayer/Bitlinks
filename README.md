# Обрезка ссылок с помощью Битли
Проект предназначен для получения сокращённых ссылок и информации о количестве переходов по сокращённым ссылкам с помощью веб-сервиса Битли. Для получения сокращённой ссылки необходимо ввести ссылку, которую нужно сократить, для получения количества переходов по сокращённой ссылке, нужно вставить её. В обоих случаях после ввода ссылки необходимо ввести токен для взаимодействия с API Bitly. 
### Как установить
Токен необходим для получения доступа к API Bitly, без него любые запросы будут отклонены.
Чтобы получить токен, необходимо зарегестрироваться на сайте [app.bitly.com](https://app.bitly.com), затем перейти в [API в разделе настроек](https://app.bitly.com/settings/api), где после ввода пароля от аккаунта необходимо нажать на кнопку "Generate token", после чего будет получена строка на подобие этой: `25c10e56ad155405125ac1977542fece00231da8` 

В проекте используются переменные окружения для хранения токена, после его получения необходимо добавить его в файл `.env`.
Пример заполненного файла:
```
BITLY_TOKEN = 25c10e56ad155405125ac1977542fece00231da8
```

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей: 
```
pip install -r requirements.txt
```
### Пример запуска
```
>>>https://pixabay.com/ru/images/search/кошка/
Битлинк: https://bit.ly/3HLxjkg
>>>https://bit.ly/3HLxjkg
Количество переходов: 11
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
