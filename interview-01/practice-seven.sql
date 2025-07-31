select partner, count(DISCTINCT(user)) as total_clicks, count(DISTINCT(booked_at)) as total_bookings,
    total_bookings / total_clicks as coversion_rate
from clicks c
join bookings b on c.user_id = b.user_id
group by partner




select partner, destination, search_count
from (
    select 
        partner,
        destination,
        COUNT(*) as search_count,

)
where searched_at >= '7-1-2025' and searched_at < '8-1-2025'
group by partner, destination
order by search_count desc
limit 3



with returning_users as (
    select *, count(user_id) as returning_times
    from trip_searches 
    where count(user_id) > 1
    group by user_id
)

SELECT 
    partner, 
    COUNT(DISTINCT(user_id)) as total_user, 
    COUNT(DISCTINCT(user_id)) /  as returning_users
    COUNT(DISTINCT(user_id)) / 

from trip_searches
HAVING COUNT(DISTINCT(user_id)) > 1
group by partner