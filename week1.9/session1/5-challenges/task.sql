.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- Bronze 1: List every column for every driver
SELECT * FROM drivers;

-- Bronze 2: List the name and price of every dish sold by Bangkok Garden (restaurant 3)
SELECT name, price
FROM menu_items
WHERE restaurant_id = 3;

-- Bronze 3: List the names of all Indian restaurants
SELECT name
FROM restaurants
WHERE cuisine = 'Indian';

-- Bronze 4: How many customers does Leeds Eats have?
SELECT COUNT(*) FROM customers;
