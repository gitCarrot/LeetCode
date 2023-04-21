# Write your MySQL query statement below
SELECT class From courses
GROUP BY class
Having Count(student) >=5;