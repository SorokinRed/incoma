# Пример автотестов

Автотесты написаны на Python3.7 + pytest + selenium
Выполняются в среде selenoid

## Запуск
```
git clone git@github.com:SorokinRed/incoma.git && cd incoma
docker-compose up -d --build
```

## Перезапуск тестов
```
docker-compose start tests
```

## Артефакты
* Отчеты не собираются
* Selenium-логи http://localhost:8080/#/logs
* Запись выполнения тестов http://localhost:8080/#/videos
