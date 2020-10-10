SELECT distinct(p.id), p.name
FROM places p, schedules s, place_reviews r
WHERE p.id = s.place_id and s.place_id = r.place_id
     and r.place_id in
        (select s1.place_id
         from schedules s1
         where DATE_FORMAT(s1.scheduled_at, '%Y-%m-%d') = "2019-01-06")
ORDER BY p.id
