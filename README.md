### Запуск
1. Установить виртуальное окружение `python3 -m venv venv`
2. Зайти в окружение `source venv/bin/activate`
3. Установить зависимости `pip3 install -r requirements.txt`
4. Запустить celery `./celery.sh` (внутри указывается количество изначальных и максимальных воркеров -autoscale=n,m)
5. Запустить веб-сервис `python3 main.py`
### Задача
Написать web-сервис для подсчёта MD5-суммы произвольного документа.
### Вводная
Сервис должен предоставлять функционал подсчета MD5-суммы
произвольного документа, доступного по URL. Скачивание и вычисление суммы
должно происходить в “фоновом” процессе.
Необходимо реализовать очередь задач, где поставщиком является RESTful
приложение, а обработчиком фоновые процессы. Количество фоновых процессов
должно масштабироваться динамически, с целью эффективной параллельной
обработки поступающих запросов. Максимальное число процессов задается
константой. В системе не должно быть большое количество простаивающих
процессов.
Запуск расчета MD5 осуществляется путем отправки POST-запроса
приложению, где указывается URL файла, который можно скачать. В ответ
приложение возвращает GUID задачи.
Пользователь выполняет GET-запрос, указав GUID задачи, и в ответ получает
либо сумму, либо ему сообщается, что задача еще не завершена. В случае сбоя в
фоновых заданиях возвращается причина ошибки.