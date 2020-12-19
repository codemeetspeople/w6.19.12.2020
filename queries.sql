Access to psql: sudo -u postgres psql
Access for local user: psql -U <username>
Access for local user to concrete DB: psql -d <db_name> -U <username>

Shell commands:
    \q - exit
    \l - databases list
    \d - tables list
    \d+ <table_name> - table description
    \c <database> - connect to database

CREATE ROLE shop LOGIN CREATEDB PASSWORD 'shop';
CREATE DATABASE shop WITH OWNER=shop ENCODING='UTF8';

CREATE TABLE "category" (
    category_id SERIAL PRIMARY KEY NOT NULL,
    category_title VARCHAR(100) NOT NULL
);

INSERT INTO "category" (category_title) VALUES ('smartphones'), ('tablets'), ('PC');

CREATE TABLE "item" (
    item_id SERIAL PRIMARY KEY NOT NULL,
    item_title VARCHAR(100) NOT NULL,
    item_price DECIMAL(8, 2) NOT NULL,
    category_id INTEGER NOT NULL
);

INSERT INTO "item" (item_title, item_price, category_id) VALUES
('iPhone', 999.99, 1),
('Samsung Galaxy', 799.99, 1),
('iPad', 1999.99, 2),
('Lenovo', 199.99, 2),
('MacBook Pro', 4999.99, 3),
('Sony', 999.99, 3);

SELECT * FROM "item";
SELECT item_title, item_price FROM "item";
SELECT item_title, item_price FROM "item" WHERE category_id = 1;
SELECT item_title, item_price FROM "item" WHERE category_id = 1 AND item_price > 800;
SELECT item_title, item_price FROM "item" ORDER BY item_price ASC;
SELECT item_title, item_price FROM "item" ORDER BY item_price DESC;
SELECT item_title, item_price FROM "item" ORDER BY item_price LIMIT 3 OFFSET 2;

SELECT * FROM "item" JOIN "category" ON "item".category_id = "category".category_id;

SELECT
    "item".item_id,
    "category".category_id,
    "category".category_title,
    "item".item_title,
    "item".item_price
FROM "item" JOIN "category" ON "item".category_id = "category".category_id;

SELECT
    i.item_id,
    c.category_id,
    c.category_title,
    i.item_title,
    i.item_price
FROM "item" AS i JOIN "category" AS c ON i.category_id = c.category_id;

SELECT * FROM "item" NATURAL JOIN "category";

INSERT INTO "category" (category_title) VALUES ('TV');

INSERT INTO "item" (item_title, item_price, category_id) VALUES
('Ariston', 999.99, 5);

SELECT * FROM "item" FULL OUTER JOIN "category" ON "item".category_id = "category".category_id;
SELECT * FROM "item" LEFT JOIN "category" ON "item".category_id = "category".category_id;
SELECT * FROM "item" RIGHT JOIN "category" ON "item".category_id = "category".category_id;

UPDATE "item" SET category_id = 3 WHERE item_id = 7;

DELETE FROM "item" WHERE item_id = 7;

INSERT INTO "item" (item_title, item_price, category_id) VALUES
('Ariston', 999.99, 3);

-- 1. Создать базу данных shop.
-- 2. Создать юзера shop и дать ему полный доступ к БД shop.
-- 4. Создать таблицу для хранения категорий (хранить название).
-- 5. Добавить несколько категорий.
-- 6. Создать таблицу для хранения товаров (название, категория, цена).
-- 7. Внести несколько товаров по цене 1.00
-- 8. Обновить цену первого товара — 3.50
-- 9. Увеличить цену всех товаров на 10%.
-- 10. Удалить товар № 2.
-- 11. Выбрать все товары с сортировкой по названию.
-- 12. Выбрать все товары с сортировкой по убыванию цены.
-- 13. Выбрать 3 самых дорогих товара.
-- 14. Выбрать 3 самых дешевых товара.
-- 15. Выбрать вторую тройку самых дорогих товаров (с 4 по 6).
-- 16. Выбрать наименование самого дорогого товара.
-- 17. Выбрать наименование самого дешевого товара.
-- 18. Выбрать количество всех товаров.
-- 19. Выбрать среднюю цену всех товаров.
