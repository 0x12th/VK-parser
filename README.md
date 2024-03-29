# VK parser
A simple parser informs users from the community by applying a filter to the received audience.

Простой парсер сообществ, пользователей из сообществ с возможностью применения фильтра на полученную аудиторию.

---

Для реализации интерфейса программы был использован PyQt5 – набор Python библиотек для создания графического интерфейса на базе платформы Qt5. Интерфейс программы стоит из 2 экранных форм: авторизация пользователя, основное окно программы со всем функционалом.



При запуске программы пользователю необходимо авторизоваться, введя логин и пароль. После успешной авторизации программа получает access_token, необходимый для работы многих алгоритмов. Access_token передается в модуль основной программы.

![Screenshot](https://github.com/biryukov12/VK-parser/raw/master/screenshots/auth_form.png)

---

### Структура модуля основной программы:

**- Сообщества.** Для поиска пользователей необходимо указать сообщества (ссылка / ID / заголовок). Также возможен поиск сообществ – необходимо указать фразы для поиска. При поиске сообществ доступен выбор сортировки и количества сообществ на каждую фразу.

**- Критерии активности.** По умолчанию указаны рекомендуемые критерии для поиска целевой аудитории. Но, при необходимости, можно уменьшить или увеличить количество анализируемых публикаций в каждом сообществе. При анализе сообществ можно учитывать лайки / комментарии или лайки и комментарии. Доступно изменение глубины активности пользователей (количество повторяющихся публикаций по лайкам / комментариям на каждого пользователя).

**- Фильтр.** После успешного поиска целевой аудитории пользователь может воспользоваться фильтром. Фильтр следует применять, когда пользователь уверен в выбранных критериях фильтрации, т.к. аудитория со скрытыми полями указанных критериев отсеивается.

**- Сохранение и загрузка полученной аудитории.** Доступен может скопировать полученную аудиторию в буфер обмена или сохранить в отдельном файле. При необходимости, пользователь может загрузить полученную ранее целевую аудиторию для применения фильтра.

![Screenshot](https://github.com/biryukov12/VK-parser/raw/master/screenshots/main_form.png)
