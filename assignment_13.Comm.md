Welcome to the MySQL monitor.  Commands end with ; or \\g.

Your MySQL connection id is 8

Server version: 8.0.42 MySQL Community Server - GPL



Copyright (c) 2000, 2025, Oracle and/or its affiliates.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\\h' for help. Type '\\c' to clear the current input statement.



mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| clique\_bait        |

| d\_diner            |

| diner              |

| information\_schema |

| mysql              |

| performance\_schema |

| sakila             |

| sec                |

| sys                |

| world              |

+--------------------+

10 rows in set (0.08 sec)



mysql> use sec;

Database changed

mysql> show tables;

+---------------+

| Tables\_in\_sec |

+---------------+

| members       |

| menu          |

| sales         |

+---------------+

3 rows in set (0.02 sec)



mysql> use clique\_bait;

Database changed

mysql> show tables;

+-----------------------+

| Tables\_in\_clique\_bait |

+-----------------------+

| campaign\_identifier   |

| event\_identifier      |

| events                |

| page\_hierarchy        |

| users                 |

+-----------------------+

5 rows in set (0.00 sec)



mysql> SELECT COUNT(DISTINCT user\_id) AS total\_users

&nbsp;   -> FROM users;

+-------------+

| total\_users |

+-------------+

|          10 |

+-------------+

1 row in set (0.05 sec)



mysql> SELECT ROUND(COUNT(DISTINCT cookie\_id) \* 1.0 / COUNT(DISTINCT user\_id), 2) AS avg\_cookies\_per\_user

&nbsp;   -> FROM users;

+----------------------+

| avg\_cookies\_per\_user |

+----------------------+

|                 1.00 |

+----------------------+

1 row in set (0.01 sec)



mysql> SELECT event\_type, COUNT(\*) AS event\_count

&nbsp;   -> FROM events

&nbsp;   -> GROUP BY event\_type;

+------------+-------------+

| event\_type | event\_count |

+------------+-------------+

|          1 |           8 |

|          2 |           2 |

+------------+-------------+

2 rows in set (0.03 sec)



mysql> SELECT

&nbsp;   ->   ROUND(COUNT(DISTINCT CASE WHEN event\_type = 2 THEN visit\_id END) \* 100.0 / COUNT(DISTINCT visit\_id), 2) AS purchase\_visit\_percentage

&nbsp;   -> FROM events;

+---------------------------+

| purchase\_visit\_percentage |

+---------------------------+

|                     20.00 |

+---------------------------+

1 row in set (0.00 sec)



mysql> SELECT

&nbsp;   ->   ROUND(COUNT(DISTINCT CASE

&nbsp;   ->                         WHEN visit\_id IN (

&nbsp;   ->                           SELECT visit\_id

&nbsp;   ->                           FROM events

&nbsp;   ->                           WHERE page\_id = 9

&nbsp;   ->                         )

&nbsp;   ->                         AND visit\_id NOT IN (

&nbsp;   ->                           SELECT visit\_id

&nbsp;   ->                           FROM events

&nbsp;   ->                           WHERE event\_type = 2

&nbsp;   ->                         )

&nbsp;   ->                       THEN visit\_id END) \* 100.0 / COUNT(DISTINCT visit\_id), 2) AS checkout\_no\_purchase\_percentage

&nbsp;   -> FROM events;

+---------------------------------+

| checkout\_no\_purchase\_percentage |

+---------------------------------+

|                            0.00 |

+---------------------------------+

1 row in set (0.01 sec)



mysql> SELECT page\_id, COUNT(\*) AS views

&nbsp;   -> FROM events

&nbsp;   -> WHERE event\_type = 1

&nbsp;   -> GROUP BY page\_id

&nbsp;   -> ORDER BY views DESC

&nbsp;   -> LIMIT 3;

+---------+-------+

| page\_id | views |

+---------+-------+

|       1 |     2 |

|       5 |     1 |

|       2 |     1 |

+---------+-------+

3 rows in set (0.00 sec)



mysql> SELECT page\_id, COUNT(\*) AS purchase\_count

&nbsp;   -> FROM events

&nbsp;   -> WHERE event\_type = 2

&nbsp;   -> GROUP BY page\_id

&nbsp;   -> ORDER BY purchase\_count DESC

&nbsp;   -> LIMIT 3;

+---------+----------------+

| page\_id | purchase\_count |

+---------+----------------+

|       6 |              1 |

|       3 |              1 |

+---------+----------------+

2 rows in set (0.00 sec)

