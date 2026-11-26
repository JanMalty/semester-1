.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- TASK 2(a)
INSERT INTO customers (customer_id, name, email)
VALUES (1, 'John', 'john@example.com');


-- TASK 2(b)
INSERT INTO customers (customer_id, name, email)
VALUES (9001, 'Test Customer B', NULL);


-- TASK 2(c)
INSERT INTO orders (order_id, customer_id, restaurant_id, driver_id)
VALUES (9002, 1, 1, 99999);


-- TASK 2(d)
INSERT INTO reviews (review_id, order_id, rating, comment)
VALUES (9003, 1, 7, 'Test review');


-- TASK 2(e)
INSERT INTO customers (customer_id, name, email)
VALUES (9004, 'Test Customer E1', 'duplicate@example.com');

INSERT INTO customers (customer_id, name, email)
VALUES (9005, 'Test Customer E2', 'duplicate@example.com');

