# Write your MySQL query statement below
SELECT email As Email FROM Person Group by email Having count(*) > 1;