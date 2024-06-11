select name, ISNULL(sum(distance), 0) as travelled_distance from users 
left join rides 
on users.id = rides.user_id
group by users.id, name
order by sum(distance) desc, name asc;