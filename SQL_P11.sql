--Работа с базой данных
--Задание 1
SELECT c.login, 
	COUNT(o.id) AS count_orders 
From "Couriers" As c 
INNER JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" = true 
GROUP BY c.login;
     
--Задание 2
SELECT track,
CASE 
   WHEN finished = true THEN 2
   WHEN cancelled = true THEN -1
   WHEN "inDelivery" = true THEN 1
   ELSE 0
   END 
   FROM "Orders";
