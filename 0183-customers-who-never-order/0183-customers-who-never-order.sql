# Write your MySQL query statement bel
Select name as customers from customers 
left join orders o 
on customers.id = o.customerId
where o.id is null