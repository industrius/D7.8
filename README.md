D7.8 Домашнее задание

Функционал реализует:
- добавление/удаление книги;
- учет количества экземпляров книги;
- добавление/удаление автора;
- добваление/удаление издателя;
- процедуру передачи книги читателю и возврат в библиотеку;
- регистрацию, авторизацию и удаление читателей;
- модель разграничения доступа на основании привилегий.

Внимание! 
В проекте использована БД Postgres и пакеты для публикации на Heroku.
Данные для подключения к БД Postgres указаны в settings.py.
Для работы с локальной БД необходимо закомментировать раздел "БД Heroku" и раскомментировать раздел "БД Postgres".
Настройки локальной БД Postgres указана в пункте 6.


Для проверки задания локально:

1. Создать новый катог виртуального окружения:

python -m venv <Имя каталога виртуального окружения>

2. Стянуть репозиторий к себе, распаковать в каталог проекта - <Имя каталога проекта> и скопировать его в каталог виртуального окружения - <Имя каталога виртуального окружения>.

3. Активировать виртуальное окружение!

4. Перейти в каталог проекта:

cd <Имя каталога проекта>

5. Установить зависимости из requirements.txt:

pip install -r requirements.txt

6. Создать в БД Postgres базу с именем "bookshelf", пользователя с именем "app" и паролем "P@ssw0rd".

7. Выполнить миграции БД:

python manage.py migrate

8. Импортировать в БД данные книг, авторов, издателей и тестовых пользователей:

python manage.py loaddata data.xml

9. Запустить сервер:

python manage.py runserver

10. Открыть URL:

http://127.0.0.1:8000/

11. Первоначальное предоставление права библиотекаря:

В верхнем меню выбрать пункт "Читатель" и войти под учтной записью администратора.

Имя пользователя: admin

Пароль: admin

В верхнем меню выбрать пункт "Библиотекарь".
В списке читателей найти Библиотекаря и в его строке нажать кнопку "Библиотекарь".

Для входа под учетной записью библиотекаря используйте:

Имя пользователя: biblio

Пароль: P@ssw0rd1

Пользователю "Библиотекарь" будут предоставлены права:
- добавление/удаление книги;
- учет количества экземпляров книги;
- добавление/удаление автора;
- добваление/удаление издателя;
- процедура передачи книги читателю и возврат в библиотеку;
- регистрацию и удаление читателей.

12. Вход под тестовой учетной записью читателя:

В верхнем меню выберите пункт "Читатель".

Для входа под учетной записью тестового читателя используйте:

Имя пользователя: reader

Пароль: P@ssw0rd1

Пользователь "Читатель" имеет право:
- процедура передачи книги читателю и возврат в библиотеку.

13. Регистрация нового читателя:

Доступно только не авторизованным пользователям!
В верхнем меню выбрать пункт "Читатель".
В появившейся форме входа нажать кнопнку "Регистрация".
Заполнить форму и сохранить.