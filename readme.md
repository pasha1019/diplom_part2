Привет!
Это вторая часть моей дипломной работы.

Работа с БД:

1. Вывод списка логинов курьеров с количеством их заказов в статусе «В доставке» 
SELECT login, COUNT(ord.id) AS orders
FROM "Couriers" AS cour
LEFT JOIN "Orders" AS ord ON cour.id=ord."courierId"
WHERE ord."inDelivery"='t'
GROUP BY login;

2. Вывод всех трекеров заказов и их статусов

SELECT track, 
CASE
WHEN finished='t' THEN 2
WHEN cancelled='t' THEN -1
WHEN "inDelivery"='t' THEN 1
ELSE 0
END AS status
FROM "Orders";

3. С помощью файлов я автоматизировал проверку, что по треку заказа можно получить данные о заказе
Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.