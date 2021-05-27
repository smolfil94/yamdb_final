# api_yamdb
![Django-app workflow](https://github.com/nikismol94/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Описание сервиса
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы»,
«Музыка».

# Установка сервиса
1. Скопируйте проект к себе на компютер 
  ```git clone https://github.com/Lookin44/infra_sp2.git```
3. Создайте файл .env со значениями: 
  ```DB_NAME=postgres```
  ```POSTGRES_USER=postgres```
  ```POSTGRES_PASSWORD=postgres```
  ```DB_HOST=db```
  ```DB_PORT=5432```
  ```EMAIL_HOST_PASSWORD=<Ваш пароль от почты>```
3. Запустите Docker: 
  ```sudo docker-compose up```
5. Выполните миграции внутри докера 
  ```sudo docker-compose exec web python manage.py migrate --noinput```
7. Создайте суперюзера внутри докера 
  ```sudo docker-compose exec web python manage.py createsuperuser```
9. Соберите всю статику внутри докера 
  ```sudo docker-compose exec web python manage.py collectstatic --no-input```
11. Загрузите тестовые данные 
  ```sudo docker-compose exec web python manage.py loaddata fixtures.json```

# Алгоритм регистрации пользователей
1. Пользователь отправляет запрос с параметром email и username на ```/auth/email/```.
3. **YaMDB** отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .
4. Пользователь отправляет запрос с параметрами email, username и confirmation_code на ```/auth/token/```, в ответе на запрос ему приходит token (JWT-токен).
5. При желании пользователь отправляет PATCH-запрос на ```/users/me/``` и заполняет поля в своём профайле (описание полей — в документации).

# Пользовательские роли
* Аноним — может просматривать описания произведений, читать отзывы и комментарии.
* Аутентифицированный пользователь — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.
* Модератор — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
* Администратор — полные права на управление проектом и всем его содержимым. Может создавать и удалять категории и произведения. Может назначать роли пользователям.
* Администратор Django — те же права, что и у роли Администратор.

# Информация по запросам
1. Запустите сервер
2. Перейдите на http://localhost:8000/redoc/

#### Проект разработан командой:
* [Александр Маскалев](https://github.com/maskalev)
  - Роль: TL, Developer; develop: приложение Api : модели, вьюхи, пермишены, сериалайзеры, эндпоинты для Category, Genre, Title
* [Галина Чернышаева](https://github.com/chgala)
  - Роль: Developer; develop: приложение Api: модели, вьюхи, пермишены, сериалайзеры, эндпоинты для Category, Genre, Title
* [Никита Филипенков](https://github.com/smolfil94)
  - Роль: Developer; develop: приложение Users
