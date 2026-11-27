.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

--SELECT * FROM stations;
--SELECT * FROM members;
--SELECT * FROM bikes;
--SELECT * FROM trips;

SELECT * FROM stations
WHERE capacity > 16;

SELECT * FROM stations
WHERE capacity = 16;
