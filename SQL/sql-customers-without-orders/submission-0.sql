-- Write your query below
select name from customers where name not in (select name from customers as c join orders as o on c.id=o.customer_id) 
