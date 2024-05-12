# Проект по тестированию [REST API](https://reqres.in/)


![image](/images/site.PNG)

#### Список проверок, реализованных в авто-тестах

- [x] Регистрация пользователя с некорректным email (POST)
- [x] Создание пользователя (POST)
- [x] Получение списка пользователей (GET)
- [x] Успешная регистрация пользователя (POST)
- [x] Обновление данных пользователя (UPDATE)
- [x] Запрос не существующего пользователя (GET)
- [x] Удаление пользователя (DELETE)


#### Параметры сборки
Данные параметры не обязательны для заполнения.

* `ENVIRONMENT` - параметр определяет окружение для запуска тестов, по умолчанию DEV
* `COMMENT` - комментарий к сборке

### Запуск автотестов в Jenkins

#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/project-rest-api/">проект</a>

![This is an image](/images/Jenkins.PNG)

#### 2. Выбрать пункт **Build with Parameters**

#### 3. Внести изменения в конфигурации сборки, при необходимости

#### 4. Нажать **Build**

#### 5. Результат запуска сборки можно посмотреть в классическом формате Allure Results

![This is an image](/images/allure.PNG)

![This is an image](/images/allure_2.PNG)

#### 6. Проект также имеет интеграцию с Allure TestOps

![This is an image](/images/allure_testops.PNG)

#### 8. Также проект имеет интеграцию с Jira

![This is an image](/images/jira.png)

#### 7. Информация о результатах прогона сборки будет отправлена в telegram канал

![This is an image](/images/telegram.PNG)


## Запуск авто-тестов локально

1. Склонировать репозиторий
2. Перейти в папку с проектом
3. Создать виртуальное окружение
4. Активировать виртуальное окружение
5. Установить зависимости
6. Запустить тесты

Пример команд для терминала:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -vv -s .
```

Создание локального отчета:

```bash
allure serve allure-results
```
