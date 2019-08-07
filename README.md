Тестовое задание

**Структура проекта: \**
[test] \
-test_f1.py содержит кейсы с наборами тестовых данных \
[docker] \
-docker-entrypoint.sh скрипт выполняемый при запуске докер-контейнера \
[allure-2.12.1] бинарная сборка аллюра для генерации тест-отчета \
[/] \
-conftest.py - содержит реализации этапов взаимодействия с веб-формами \
-Dockerfile - инструкция с установкой firefox и всех необходимых зависимостей для запуска тестов в headless режиме \
-geckodriver - драйвер для запуска firefox новых версий
-requirements.txt - файл с библиотеками-зависимостими для установки через pip  

**Для работы через докер: \**
(Требуется установленный docker актуальной версии) \
1.сбилдить проект \
``` docker build -t dialog-test .``` \
2.запустить образ \
```docker run -v [path-to-project]/allure-report:/tests/allure-report dialog-test``` \
3.для просмотр отчета открыть в браузере(предпочтительно Firefox) файл: \
```[path-to-project]/allure-report/index.html``` \
или если через аллюр(Для открытия тест-отчета через аллюр необходима java 1.8+ ): \
```/allure-2.12.1/bin/allure open ./tests/allure-report/```

**При запуске тестов из проекта: \**
Тестам необходим интерпретатор Python-3.7 и выше, \
python-pytest, \
(```sudo apt install python-pytest```)
зависимости указаные в requirements.txt \
(```pip3 install --trusted-host pypi.python.org -r requirements.txt)``` \
присутствие в PATH пути до geckodriver \
(```/home/[USER]/PycharmProjects/dialog/geckodriver```)  \


1.Для запуска тестов выполнить команду: \
```pytest ./test/test_f1.py --alluredir=./tests/allure``` \

2.Запуск генерации(Для генерации тест-отчета через аллюр необходима java 1.8+): \
```./allure-2.12.1/bin/allure generate ./tests/allure ./tests/allure-report --clean``` \
3.Для просмотр отчета открыть в браузере(предпочтительно Firefox) файл: \
```./tests/allure-report/index.html``` \
или если через аллюр(Для открытия тест-отчета через аллюр необходима java 1.8+): \
```/allure-2.12.1/bin/allure open ./tests/allure-report/```



